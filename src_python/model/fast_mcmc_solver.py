"""Fully Numba-compiled RK4 solver for MCMC likelihood evaluation.

This module provides a ~20-50x speedup over the Python RHS + scipy RK45 path
by compiling the ENTIRE ODE right-hand side and RK4 integrator into native
machine code via Numba. All parameters are packed into flat numpy arrays
before the integration loop, eliminating Python dict lookups, object attribute
access, and interpreter overhead.

Architecture:
    1. `pack_params()` — converts a PreparedParameters object into a flat
       `PackedParams` namedtuple of numpy arrays (called ONCE per MCMC step).
    2. `rhs_numba()` — the full ODE RHS as a single @njit function.
    3. `solve_mcmc_fast()` — fixed-step RK4 that calls rhs_numba in a tight
       loop, returning only the coarse time-series needed for likelihood.

Performance target:
    - Python RHS: ~1.8ms/call × 2000 calls = 3.6s per ODE solve
    - Numba RHS: ~0.05ms/call × 2000 calls = 0.1s per ODE solve (dt=2 days)
    - Total per MCMC step: 0.1-0.3s (vs 5.4s before) → 30-50x speedup
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
from numba import njit, types
from numba.typed import Dict as NumbaDict

from src_python.model.compartments import (
    COMPARTMENTS,
    STRAINS,
    VACCINE_ORIGINS,
    StateIndex,
    compartment_index,
    exposed_name,
    infectious_name,
    susceptible_name,
    treated_name,
)
from src_python.model.parameters import PreparedParameters
from src_python.model.treatment import treated_recovery_rate


# ---------------------------------------------------------------------------
# Compartment index constants (computed once at module load)
# ---------------------------------------------------------------------------

N_AGE = 8  # Will be validated at runtime
N_COMP = len(COMPARTMENTS)
N_ORIGINS = len(VACCINE_ORIGINS)
N_STATE = N_AGE * N_COMP

# Pre-compute all compartment indices as module-level constants
_S_IDX = compartment_index("S")
_M_IDX = compartment_index("M_protected")
_R_NAT_IDX = compartment_index("R_natural")

# Vaccine waning pairs: (recent, waned)
_V_PAIRS = [
    (compartment_index("V_dose1_recent"), compartment_index("V_dose1_waned")),
    (compartment_index("V_dose2_recent"), compartment_index("V_dose2_waned")),
    (compartment_index("V_recent"), compartment_index("V_waned")),
]
_V_RECENT_INDICES = np.array([p[0] for p in _V_PAIRS], dtype=np.int64)
_V_WANED_INDICES = np.array([p[1] for p in _V_PAIRS], dtype=np.int64)

# Per-origin compartment indices
_SUS_INDICES = np.array([compartment_index(susceptible_name(o)) for o in VACCINE_ORIGINS], dtype=np.int64)
_EXP_S_INDICES = np.array([compartment_index(exposed_name("S", o)) for o in VACCINE_ORIGINS], dtype=np.int64)
_EXP_R_INDICES = np.array([compartment_index(exposed_name("R", o)) for o in VACCINE_ORIGINS], dtype=np.int64)
_INF_S_SYM_INDICES = np.array([compartment_index(infectious_name("S", "sym", o)) for o in VACCINE_ORIGINS], dtype=np.int64)
_INF_S_ASYM_INDICES = np.array([compartment_index(infectious_name("S", "asym", o)) for o in VACCINE_ORIGINS], dtype=np.int64)
_INF_R_SYM_INDICES = np.array([compartment_index(infectious_name("R", "sym", o)) for o in VACCINE_ORIGINS], dtype=np.int64)
_INF_R_ASYM_INDICES = np.array([compartment_index(infectious_name("R", "asym", o)) for o in VACCINE_ORIGINS], dtype=np.int64)
_TREATED_S_INDICES = np.array([compartment_index(treated_name("S", o)) for o in VACCINE_ORIGINS], dtype=np.int64)
_TREATED_R_INDICES = np.array([compartment_index(treated_name("R", o)) for o in VACCINE_ORIGINS], dtype=np.int64)


# ---------------------------------------------------------------------------
# Packed parameter structure (flat arrays for Numba)
# ---------------------------------------------------------------------------

@dataclass
class PackedParams:
    """All ODE parameters packed into flat numpy arrays for Numba consumption."""
    # Dimensions
    n_age: int
    n_comp: int
    n_origins: int

    # Contact matrix (n_age, n_age)
    contact_matrix: np.ndarray

    # Transmission
    beta_S: float
    beta_R: float  # beta_S * fitness_R
    relative_infectiousness_asymptomatic: float
    treated_infectiousness_relative_S: float
    treated_infectiousness_relative_R: float

    # Rates
    sigma: float  # 1/latent_duration
    gamma_sym: float  # 1/infectious_duration_symptomatic
    gamma_asym: float  # 1/infectious_duration_asymptomatic
    gamma_treated_S: float
    gamma_treated_R: float
    waning_vaccine: float
    waning_vaccine_waned: float
    waning_maternal: float
    waning_natural: float

    # Treatment (age-specific)
    tr_sym_by_age: np.ndarray  # (n_age,)
    tr_asym_by_age: np.ndarray  # (n_age,)

    # Per-origin arrays
    susceptibility: np.ndarray  # (n_origins,)
    infectiousness: np.ndarray  # (n_origins,)
    symptomatic_prob: np.ndarray  # (n_origins, n_age)
    recovery_mult: np.ndarray  # (n_origins,)

    # Demography
    aging_rates: np.ndarray  # (n_age,)
    maternal_exit_mask: np.ndarray  # (n_age,) bool

    # Importation
    importation_rate_per_day: np.ndarray  # (n_age,) imported cases/day
    importation_resistant_fraction: float

    # Resistance anchor
    resistance_anchor_rate: float  # per day
    resistance_anchor_target: float

    # Routine vaccination
    rv_rate: float  # relaxation rate per day
    rv_max_flow: float  # max daily flow fraction from S
    vaccine_target_frac: np.ndarray  # (n_age, n_origins) target fractions

    # Birth entry
    birth_fracs: np.ndarray  # (n_comp,) fraction of births to each compartment

    # Index arrays (pre-computed)
    sus_indices: np.ndarray
    exp_S_indices: np.ndarray
    exp_R_indices: np.ndarray
    inf_S_sym_indices: np.ndarray
    inf_S_asym_indices: np.ndarray
    inf_R_sym_indices: np.ndarray
    inf_R_asym_indices: np.ndarray
    treated_S_indices: np.ndarray
    treated_R_indices: np.ndarray
    v_recent_indices: np.ndarray
    v_waned_indices: np.ndarray
    s_idx: int
    m_idx: int
    r_nat_idx: int


def pack_params(params: PreparedParameters) -> PackedParams:
    """Convert PreparedParameters into flat arrays for Numba.

    Called once per MCMC step (cheap relative to ODE solve).
    """
    n_age = len(params.age_groups)
    assert n_age == N_AGE, f"Expected {N_AGE} age groups, got {n_age}"

    # Transmission rates
    beta_S = float(params.transmission["beta_S"])
    fitness_R = float(params.transmission.get("fitness_R", 1.0))
    beta_R = beta_S * fitness_R
    rel_inf_asym = float(params.transmission["relative_infectiousness_asymptomatic"])
    treated_inf_S = float(params.treatment.get("treated_infectiousness_relative", 0.5))
    treated_inf_R = float(params.treatment.get("treated_infectiousness_relative_R", treated_inf_S))

    # Core rates
    sigma = float(params.rates["latent"])
    gamma_sym = float(params.rates["recovery_symptomatic"])
    gamma_asym = float(params.rates["recovery_asymptomatic"])
    gamma_treated_S = treated_recovery_rate(gamma_sym, params.treatment, "S")
    gamma_treated_R = treated_recovery_rate(gamma_sym, params.treatment, "R")
    waning_vaccine = float(params.rates["waning_vaccine"])
    waning_vaccine_waned = float(params.rates.get("waning_vaccine_waned", waning_vaccine))
    waning_maternal = float(params.rates.get("waning_maternal", 0.0))
    waning_natural = float(params.rates["waning_natural"])

    # Treatment rates (age-specific via diagnosis_probability)
    tr_sym_base = float(params.treatment["treatment_rate_symptomatic"])
    tr_asym_base = float(params.treatment["treatment_rate_asymptomatic"])
    diagnosis_prob = params.diagnosis_probability
    age_treatment_scale = diagnosis_prob / max(float(diagnosis_prob.max()), 1e-6)
    tr_sym_by_age = (tr_sym_base * age_treatment_scale).astype(np.float64)
    tr_asym_by_age = (tr_asym_base * age_treatment_scale).astype(np.float64)

    # Demography aging rates
    config = params.demography
    duration_by_age = config.get("age_bin_durations_years", {})
    durations = np.array(
        [float(duration_by_age.get(age, 1.0)) for age in params.age_groups], dtype=np.float64
    )
    if config.get("fixed_population_profile", True) and not params.wpp_trajectory_active():
        reference_age = str(config.get("fixed_population_reference_age_group", params.age_groups[0]))
        reference_idx = params.age_groups.index(reference_age) if reference_age in params.age_groups else 0
        target_pop = np.maximum(params.population, 1e-12)
        reference_flow = target_pop[reference_idx] / (durations[reference_idx] * 365.0)
        aging_rates = reference_flow / target_pop
    else:
        aging_rates = 1.0 / (durations * 365.0)

    # Maternal exit mask
    maternal_proxy = config.get("maternal_protection_proxy", {})
    maternal_exit_groups = (
        set(maternal_proxy.get("exit_age_groups", [])) if maternal_proxy.get("enabled", False) else set()
    )
    maternal_exit_mask = np.array(
        [age in maternal_exit_groups for age in params.age_groups], dtype=np.bool_
    )


    # Importation
    imp_config = params.importation
    if imp_config.get("enabled", False):
        rate_per_100k_year = float(imp_config.get("rate_per_100k_per_year", 0.0))
        age_dist = np.array(
            [float(imp_config.get("age_distribution", {}).get(age, 1.0 / n_age)) for age in params.age_groups],
            dtype=np.float64,
        )
        age_dist = age_dist / max(age_dist.sum(), 1e-12)
        total_imported = params.total_population * rate_per_100k_year / 100_000.0 / 365.0
        importation_rate = total_imported * age_dist
        imp_res_frac = float(imp_config.get("resistant_fraction",
                                            params.initial.get("initial_resistance_prevalence", 0.0)))
    else:
        importation_rate = np.zeros(n_age, dtype=np.float64)
        imp_res_frac = 0.0

    # Resistance anchor
    res_config = params.resistance
    if res_config.get("anchor_during_dynamics", False):
        anchor_rate = float(res_config.get("prevalence_anchor_rate_per_year", 0.0)) / 365.0
        anchor_target = float(np.clip(
            res_config.get("target_prevalence_at_analysis_start",
                           params.initial.get("initial_resistance_prevalence", 0.0)),
            0.0, 1.0,
        ))
    else:
        anchor_rate = 0.0
        anchor_target = 0.0

    # Routine vaccination: pre-compute target fractions per (age, origin)
    # vaccine_target_frac[ai, oi] = fraction of population that should be in sus_indices[oi]
    from src_python.model.vaccination import default_routine_target_origin_distribution, origin_is_vaccine_dose
    rv_config = params.routine_vaccination
    rv_enabled = rv_config.get("enabled", False)
    rv_rate = float(rv_config.get("target_relaxation_rate_per_year", 0.0)) / 365.0 if rv_enabled else 0.0
    rv_max_flow = float(rv_config.get("max_daily_flow_fraction", 0.01)) if rv_enabled else 0.0

    vaccine_target_frac = np.zeros((n_age, N_ORIGINS), dtype=np.float64)
    if rv_enabled and rv_rate > 0.0:
        for ai, age in enumerate(params.age_groups):
            configured = rv_config.get("target_origin_distribution_by_age", {})
            if age in configured:
                dist = {str(o): float(s) for o, s in configured[age].items()}
            else:
                dist = default_routine_target_origin_distribution(age)
            # Filter to vaccine dose origins only
            vaccine_dist = {o: max(0.0, s) for o, s in dist.items() if origin_is_vaccine_dose(o)}
            total_share = sum(vaccine_dist.values())
            if total_share <= 0.0:
                continue
            coverage = params.vaccine_coverage[ai]
            for oi, origin in enumerate(VACCINE_ORIGINS):
                if origin in vaccine_dist:
                    vaccine_target_frac[ai, oi] = coverage * vaccine_dist[origin] / total_share

    # Birth entry fractions (which compartments newborns enter)
    birth_entry_config = config.get("birth_entry", params.demography.get("birth_entry", {"S": 1.0}))
    birth_fracs = np.zeros(N_COMP, dtype=np.float64)
    total_weight = sum(max(0.0, float(w)) for w in birth_entry_config.values())
    if total_weight > 0:
        from src_python.model.compartments import compartment_name
        for comp_name, weight in birth_entry_config.items():
            resolved = compartment_name(comp_name)
            cidx = compartment_index(resolved)
            birth_fracs[cidx] = max(0.0, float(weight)) / total_weight
    else:
        birth_fracs[_S_IDX] = 1.0

    return PackedParams(
        n_age=n_age,
        n_comp=N_COMP,
        n_origins=N_ORIGINS,
        contact_matrix=params.contact_matrix.astype(np.float64).copy(),
        beta_S=beta_S,
        beta_R=beta_R,
        relative_infectiousness_asymptomatic=rel_inf_asym,
        treated_infectiousness_relative_S=treated_inf_S,
        treated_infectiousness_relative_R=treated_inf_R,
        sigma=sigma,
        gamma_sym=gamma_sym,
        gamma_asym=gamma_asym,
        gamma_treated_S=gamma_treated_S,
        gamma_treated_R=gamma_treated_R,
        waning_vaccine=waning_vaccine,
        waning_vaccine_waned=waning_vaccine_waned,
        waning_maternal=waning_maternal,
        waning_natural=waning_natural,
        tr_sym_by_age=tr_sym_by_age,
        tr_asym_by_age=tr_asym_by_age,
        susceptibility=params.origin_susceptibility.astype(np.float64).copy(),
        infectiousness=params.origin_infectiousness.astype(np.float64).copy(),
        symptomatic_prob=params.origin_symptomatic_prob.astype(np.float64).copy(),
        recovery_mult=params.origin_recovery_mult.astype(np.float64).copy(),
        aging_rates=aging_rates.astype(np.float64),
        maternal_exit_mask=maternal_exit_mask,
        importation_rate_per_day=importation_rate.astype(np.float64),
        importation_resistant_fraction=imp_res_frac,
        resistance_anchor_rate=anchor_rate,
        resistance_anchor_target=anchor_target,
        rv_rate=rv_rate,
        rv_max_flow=rv_max_flow,
        vaccine_target_frac=vaccine_target_frac,
        birth_fracs=birth_fracs,
        sus_indices=_SUS_INDICES,
        exp_S_indices=_EXP_S_INDICES,
        exp_R_indices=_EXP_R_INDICES,
        inf_S_sym_indices=_INF_S_SYM_INDICES,
        inf_S_asym_indices=_INF_S_ASYM_INDICES,
        inf_R_sym_indices=_INF_R_SYM_INDICES,
        inf_R_asym_indices=_INF_R_ASYM_INDICES,
        treated_S_indices=_TREATED_S_INDICES,
        treated_R_indices=_TREATED_R_INDICES,
        v_recent_indices=_V_RECENT_INDICES,
        v_waned_indices=_V_WANED_INDICES,
        s_idx=_S_IDX,
        m_idx=_M_IDX,
        r_nat_idx=_R_NAT_IDX,
    )


# ---------------------------------------------------------------------------
# Fully compiled RHS (single @njit function — no Python callbacks)
# ---------------------------------------------------------------------------

@njit(cache=True, fastmath=True)
def _rhs_compiled(
    state_flat: np.ndarray,
    # Dimensions
    n_age: int,
    n_comp: int,
    n_origins: int,
    # Contact & transmission
    contact_matrix: np.ndarray,
    beta_S: float,
    beta_R: float,
    rel_inf_asym: float,
    treated_inf_S: float,
    treated_inf_R: float,
    # Rates
    sigma: float,
    gamma_sym: float,
    gamma_asym: float,
    gamma_treated_S: float,
    gamma_treated_R: float,
    waning_vaccine: float,
    waning_vaccine_waned: float,
    waning_maternal: float,
    waning_natural: float,
    # Treatment (age-specific)
    tr_sym_by_age: np.ndarray,
    tr_asym_by_age: np.ndarray,
    # Per-origin
    susceptibility: np.ndarray,
    infectiousness: np.ndarray,
    symptomatic_prob: np.ndarray,
    recovery_mult: np.ndarray,
    # Demography
    aging_rates: np.ndarray,
    maternal_exit_mask: np.ndarray,
    # Routine vaccination
    rv_rate: float,
    rv_max_flow: float,
    vaccine_target_frac: np.ndarray,
    # Birth entry
    birth_fracs: np.ndarray,
    # Importation
    importation_rate: np.ndarray,
    imp_res_frac: float,
    # Resistance anchor
    anchor_rate: float,
    anchor_target: float,
    # Index arrays
    sus_indices: np.ndarray,
    exp_S_indices: np.ndarray,
    exp_R_indices: np.ndarray,
    inf_S_sym_indices: np.ndarray,
    inf_S_asym_indices: np.ndarray,
    inf_R_sym_indices: np.ndarray,
    inf_R_asym_indices: np.ndarray,
    treated_S_indices: np.ndarray,
    treated_R_indices: np.ndarray,
    v_recent_indices: np.ndarray,
    v_waned_indices: np.ndarray,
    s_idx: int,
    m_idx: int,
    r_nat_idx: int,
) -> np.ndarray:
    """Complete ODE RHS compiled to native code. No Python callbacks."""
    # Reshape flat state to (n_age, n_comp)
    state = np.maximum(state_flat.reshape((n_age, n_comp)), 0.0)
    dy = np.zeros((n_age, n_comp))


    # --- 1. Force of infection ---
    # Compute infectious pressure per age group
    population = np.zeros(n_age)
    for ai in range(n_age):
        for ci in range(n_comp):
            population[ai] += state[ai, ci]
        population[ai] = max(population[ai], 1.0)

    pressure_S = np.zeros(n_age)
    pressure_R = np.zeros(n_age)
    for ai in range(n_age):
        for oi in range(n_origins):
            inf_mult = infectiousness[oi]
            i_S_sym = state[ai, inf_S_sym_indices[oi]]
            i_S_asym = state[ai, inf_S_asym_indices[oi]]
            t_S = state[ai, treated_S_indices[oi]]
            pressure_S[ai] += inf_mult * (
                i_S_sym + rel_inf_asym * i_S_asym + treated_inf_S * t_S
            )
            i_R_sym = state[ai, inf_R_sym_indices[oi]]
            i_R_asym = state[ai, inf_R_asym_indices[oi]]
            t_R = state[ai, treated_R_indices[oi]]
            pressure_R[ai] += inf_mult * (
                i_R_sym + rel_inf_asym * i_R_asym + treated_inf_R * t_R
            )
        pressure_S[ai] /= population[ai]
        pressure_R[ai] /= population[ai]

    # FOI = beta * contact_matrix @ pressure
    lambda_S = np.zeros(n_age)
    lambda_R = np.zeros(n_age)
    for ai in range(n_age):
        for aj in range(n_age):
            lambda_S[ai] += contact_matrix[ai, aj] * pressure_S[aj]
            lambda_R[ai] += contact_matrix[ai, aj] * pressure_R[aj]
        lambda_S[ai] *= beta_S
        lambda_R[ai] *= beta_R


    # --- 2. Infection, progression, treatment, recovery ---
    for ai in range(n_age):
        recovered_total = 0.0
        tr_sym = tr_sym_by_age[ai]
        tr_asym = tr_asym_by_age[ai]

        for oi in range(n_origins):
            sus_mult = susceptibility[oi]
            sus = state[ai, sus_indices[oi]]

            # New infections
            new_inf_S = lambda_S[ai] * sus_mult * sus
            new_inf_R = lambda_R[ai] * sus_mult * sus
            dy[ai, sus_indices[oi]] -= new_inf_S + new_inf_R

            # Exposed → progression
            e_S = state[ai, exp_S_indices[oi]]
            e_R = state[ai, exp_R_indices[oi]]
            prog_S = sigma * e_S
            prog_R = sigma * e_R
            dy[ai, exp_S_indices[oi]] += new_inf_S - prog_S
            dy[ai, exp_R_indices[oi]] += new_inf_R - prog_R

            # Symptomatic/asymptomatic split
            p_sym = symptomatic_prob[oi, ai]
            rec_mult = recovery_mult[oi]
            g_sym = gamma_sym * rec_mult
            g_asym = gamma_asym * rec_mult
            g_tr_S = gamma_treated_S * rec_mult
            g_tr_R = gamma_treated_R * rec_mult

            # Infectious S
            i_S_sym = state[ai, inf_S_sym_indices[oi]]
            i_S_asym = state[ai, inf_S_asym_indices[oi]]
            dy[ai, inf_S_sym_indices[oi]] += p_sym * prog_S - tr_sym * i_S_sym - g_sym * i_S_sym
            dy[ai, inf_S_asym_indices[oi]] += (1.0 - p_sym) * prog_S - tr_asym * i_S_asym - g_asym * i_S_asym

            # Infectious R
            i_R_sym = state[ai, inf_R_sym_indices[oi]]
            i_R_asym = state[ai, inf_R_asym_indices[oi]]
            dy[ai, inf_R_sym_indices[oi]] += p_sym * prog_R - tr_sym * i_R_sym - g_sym * i_R_sym
            dy[ai, inf_R_asym_indices[oi]] += (1.0 - p_sym) * prog_R - tr_asym * i_R_asym - g_asym * i_R_asym

            # Treated
            t_S = state[ai, treated_S_indices[oi]]
            t_R = state[ai, treated_R_indices[oi]]
            dy[ai, treated_S_indices[oi]] += tr_sym * i_S_sym + tr_asym * i_S_asym - g_tr_S * t_S
            dy[ai, treated_R_indices[oi]] += tr_sym * i_R_sym + tr_asym * i_R_asym - g_tr_R * t_R

            # Recovery flows
            recovered_total += (
                g_sym * i_S_sym + g_asym * i_S_asym + g_tr_S * t_S
                + g_sym * i_R_sym + g_asym * i_R_asym + g_tr_R * t_R
            )

        # R_natural
        dy[ai, r_nat_idx] += recovered_total - waning_natural * state[ai, r_nat_idx]
        dy[ai, s_idx] += waning_natural * state[ai, r_nat_idx]


    # --- 3. Immunity waning ---
    for ai in range(n_age):
        # Maternal
        dy[ai, m_idx] -= waning_maternal * state[ai, m_idx]
        dy[ai, s_idx] += waning_maternal * state[ai, m_idx]
        # Vaccine waning: recent → waned → S
        for vi in range(v_recent_indices.shape[0]):
            recent_idx = v_recent_indices[vi]
            waned_idx = v_waned_indices[vi]
            dy[ai, recent_idx] -= waning_vaccine * state[ai, recent_idx]
            dy[ai, waned_idx] += waning_vaccine * state[ai, recent_idx]
            dy[ai, waned_idx] -= waning_vaccine_waned * state[ai, waned_idx]
            dy[ai, s_idx] += waning_vaccine_waned * state[ai, waned_idx]

    # --- 4. Demography (aging) ---
    for ai in range(n_age - 1):
        rate = aging_rates[ai]
        for ci in range(n_comp):
            flow = rate * state[ai, ci]
            dy[ai, ci] -= flow
            if maternal_exit_mask[ai] and ci == m_idx:
                dy[ai + 1, s_idx] += flow
            else:
                dy[ai + 1, ci] += flow
    # Oldest exits
    rate_last = aging_rates[n_age - 1]
    total_exit = 0.0
    for ci in range(n_comp):
        flow = rate_last * state[n_age - 1, ci]
        dy[n_age - 1, ci] -= flow
        total_exit += flow
    # Births enter youngest group according to birth_fracs
    for ci in range(n_comp):
        dy[0, ci] += total_exit * birth_fracs[ci]

    # --- 5. Routine vaccination (relaxation toward target coverage) ---
    if rv_rate > 0.0:
        for ai in range(n_age):
            # Total deficit across all vaccine origins
            total_deficit = 0.0
            for oi in range(n_origins):
                target = vaccine_target_frac[ai, oi] * population[ai]
                current = state[ai, sus_indices[oi]]
                deficit = target - current
                if deficit > 0.0:
                    total_deficit += deficit
            if total_deficit <= 0.0:
                continue
            s_available = state[ai, s_idx]
            total_flow = rv_rate * total_deficit
            max_allowed = rv_max_flow * s_available
            if total_flow > max_allowed:
                total_flow = max_allowed
            if total_flow <= 0.0:
                continue
            dy[ai, s_idx] -= total_flow
            for oi in range(n_origins):
                target = vaccine_target_frac[ai, oi] * population[ai]
                current = state[ai, sus_indices[oi]]
                deficit = target - current
                if deficit > 0.0:
                    dy[ai, sus_indices[oi]] += total_flow * deficit / total_deficit

    # --- 6. Importation ---
    for ai in range(n_age):
        imp = importation_rate[ai]
        if imp <= 0.0:
            continue
        # Distribute across susceptible origins proportionally
        total_sus = 0.0
        for oi in range(n_origins):
            total_sus += state[ai, sus_indices[oi]]
        if total_sus < 1e-12:
            continue
        for oi in range(n_origins):
            share = state[ai, sus_indices[oi]] / total_sus
            from_origin = imp * share
            from_origin = min(from_origin, state[ai, sus_indices[oi]])
            dy[ai, sus_indices[oi]] -= from_origin
            dy[ai, exp_R_indices[oi]] += from_origin * imp_res_frac
            dy[ai, exp_S_indices[oi]] += from_origin * (1.0 - imp_res_frac)


    # --- 6. Resistance prevalence anchor ---
    if anchor_rate > 0.0:
        for oi in range(n_origins):
            # Exposed
            for ai in range(n_age):
                s_val = state[ai, exp_S_indices[oi]]
                r_val = state[ai, exp_R_indices[oi]]
                total = s_val + r_val
                desired_r = anchor_target * total
                flow = anchor_rate * (desired_r - r_val)
                dy[ai, exp_S_indices[oi]] -= flow
                dy[ai, exp_R_indices[oi]] += flow
            # Infectious sym
            for ai in range(n_age):
                s_val = state[ai, inf_S_sym_indices[oi]]
                r_val = state[ai, inf_R_sym_indices[oi]]
                total = s_val + r_val
                desired_r = anchor_target * total
                flow = anchor_rate * (desired_r - r_val)
                dy[ai, inf_S_sym_indices[oi]] -= flow
                dy[ai, inf_R_sym_indices[oi]] += flow
            # Infectious asym
            for ai in range(n_age):
                s_val = state[ai, inf_S_asym_indices[oi]]
                r_val = state[ai, inf_R_asym_indices[oi]]
                total = s_val + r_val
                desired_r = anchor_target * total
                flow = anchor_rate * (desired_r - r_val)
                dy[ai, inf_S_asym_indices[oi]] -= flow
                dy[ai, inf_R_asym_indices[oi]] += flow
            # Treated
            for ai in range(n_age):
                s_val = state[ai, treated_S_indices[oi]]
                r_val = state[ai, treated_R_indices[oi]]
                total = s_val + r_val
                desired_r = anchor_target * total
                flow = anchor_rate * (desired_r - r_val)
                dy[ai, treated_S_indices[oi]] -= flow
                dy[ai, treated_R_indices[oi]] += flow

    return dy.ravel()


# ---------------------------------------------------------------------------
# Compiled RK4 integrator (entire solve in native code)
# ---------------------------------------------------------------------------

@njit(cache=True, fastmath=True)
def _rk4_integrate(
    y0: np.ndarray,
    t_start: float,
    t_end: float,
    dt: float,
    t_eval: np.ndarray,
    # All params passed individually (Numba can't handle dataclasses)
    n_age: int, n_comp: int, n_origins: int,
    contact_matrix: np.ndarray,
    beta_S: float, beta_R: float,
    rel_inf_asym: float, treated_inf_S: float, treated_inf_R: float,
    sigma: float, gamma_sym: float, gamma_asym: float,
    gamma_treated_S: float, gamma_treated_R: float,
    waning_vaccine: float, waning_vaccine_waned: float,
    waning_maternal: float, waning_natural: float,
    tr_sym_by_age: np.ndarray, tr_asym_by_age: np.ndarray,
    susceptibility: np.ndarray, infectiousness: np.ndarray,
    symptomatic_prob: np.ndarray, recovery_mult: np.ndarray,
    aging_rates: np.ndarray, maternal_exit_mask: np.ndarray,
    rv_rate: float, rv_max_flow: float, vaccine_target_frac: np.ndarray,
    birth_fracs: np.ndarray,
    importation_rate: np.ndarray, imp_res_frac: float,
    anchor_rate: float, anchor_target: float,
    sus_indices: np.ndarray, exp_S_indices: np.ndarray, exp_R_indices: np.ndarray,
    inf_S_sym_indices: np.ndarray, inf_S_asym_indices: np.ndarray,
    inf_R_sym_indices: np.ndarray, inf_R_asym_indices: np.ndarray,
    treated_S_indices: np.ndarray, treated_R_indices: np.ndarray,
    v_recent_indices: np.ndarray, v_waned_indices: np.ndarray,
    s_idx: int, m_idx: int, r_nat_idx: int,
) -> np.ndarray:
    """Fixed-step RK4 integration, fully compiled. Returns states at t_eval."""
    n_steps = max(1, int(np.ceil((t_end - t_start) / dt)))
    actual_dt = (t_end - t_start) / n_steps
    n_state = n_age * n_comp
    n_eval = len(t_eval)

    y = y0.copy()
    t = t_start
    output = np.zeros((n_eval, n_state))
    eval_idx = 0

    # Common args tuple for rhs calls
    def call_rhs(y_in):
        return _rhs_compiled(
            y_in, n_age, n_comp, n_origins,
            contact_matrix, beta_S, beta_R, rel_inf_asym, treated_inf_S, treated_inf_R,
            sigma, gamma_sym, gamma_asym, gamma_treated_S, gamma_treated_R,
            waning_vaccine, waning_vaccine_waned, waning_maternal, waning_natural,
            tr_sym_by_age, tr_asym_by_age,
            susceptibility, infectiousness, symptomatic_prob, recovery_mult,
            aging_rates, maternal_exit_mask,
            rv_rate, rv_max_flow, vaccine_target_frac, birth_fracs,
            importation_rate, imp_res_frac, anchor_rate, anchor_target,
            sus_indices, exp_S_indices, exp_R_indices,
            inf_S_sym_indices, inf_S_asym_indices,
            inf_R_sym_indices, inf_R_asym_indices,
            treated_S_indices, treated_R_indices,
            v_recent_indices, v_waned_indices, s_idx, m_idx, r_nat_idx,
        )

    for step in range(n_steps):
        k1 = call_rhs(y)
        k2 = call_rhs(y + 0.5 * actual_dt * k1)
        k3 = call_rhs(y + 0.5 * actual_dt * k2)
        k4 = call_rhs(y + actual_dt * k3)
        y = y + (actual_dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        # Clamp negatives
        for i in range(n_state):
            if y[i] < 0.0:
                y[i] = 0.0
        t += actual_dt

        # Check if we should record this time point
        while eval_idx < n_eval and t >= t_eval[eval_idx] - 0.5 * actual_dt:
            output[eval_idx, :] = y
            eval_idx += 1

    # Fill any remaining eval points with final state
    while eval_idx < n_eval:
        output[eval_idx, :] = y
        eval_idx += 1

    return output


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def solve_mcmc_fast(
    params: PreparedParameters,
    index: StateIndex,
    y0: np.ndarray,
    t_start: float,
    t_end: float,
    dt: float = 2.0,
    t_eval: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Fast MCMC ODE solve using fully compiled Numba RK4.

    Parameters
    ----------
    params : PreparedParameters
    index : StateIndex
    y0 : initial state vector (flat)
    t_start, t_end : integration bounds
    dt : fixed step size in days (default 2.0 for MCMC)
    t_eval : output times (if None, only final state)

    Returns
    -------
    t_out : 1-D array of output times
    y_out : 2-D array (n_states, n_times) — same layout as solve_ivp
    """
    pp = pack_params(params)

    if t_eval is None:
        t_eval = np.array([t_end], dtype=np.float64)
    else:
        t_eval = np.asarray(t_eval, dtype=np.float64)

    output = _rk4_integrate(
        y0.astype(np.float64),
        float(t_start), float(t_end), float(dt),
        t_eval,
        pp.n_age, pp.n_comp, pp.n_origins,
        pp.contact_matrix, pp.beta_S, pp.beta_R,
        pp.relative_infectiousness_asymptomatic,
        pp.treated_infectiousness_relative_S, pp.treated_infectiousness_relative_R,
        pp.sigma, pp.gamma_sym, pp.gamma_asym,
        pp.gamma_treated_S, pp.gamma_treated_R,
        pp.waning_vaccine, pp.waning_vaccine_waned,
        pp.waning_maternal, pp.waning_natural,
        pp.tr_sym_by_age, pp.tr_asym_by_age,
        pp.susceptibility, pp.infectiousness,
        pp.symptomatic_prob, pp.recovery_mult,
        pp.aging_rates, pp.maternal_exit_mask,
        pp.rv_rate, pp.rv_max_flow, pp.vaccine_target_frac,
        pp.birth_fracs,
        pp.importation_rate_per_day, pp.importation_resistant_fraction,
        pp.resistance_anchor_rate, pp.resistance_anchor_target,
        pp.sus_indices, pp.exp_S_indices, pp.exp_R_indices,
        pp.inf_S_sym_indices, pp.inf_S_asym_indices,
        pp.inf_R_sym_indices, pp.inf_R_asym_indices,
        pp.treated_S_indices, pp.treated_R_indices,
        pp.v_recent_indices, pp.v_waned_indices,
        pp.s_idx, pp.m_idx, pp.r_nat_idx,
    )

    # Return in solve_ivp format: (n_states, n_times)
    return t_eval, output.T


def warmup_jit():
    """Trigger JIT compilation with dummy data. Call once at process start."""
    n_age = N_AGE
    n_comp = N_COMP
    n_state = n_age * n_comp
    y0 = np.ones(n_state, dtype=np.float64) * 100.0
    t_eval = np.array([1.0], dtype=np.float64)
    _rk4_integrate(
        y0, 0.0, 1.0, 1.0, t_eval,
        n_age, n_comp, N_ORIGINS,
        np.ones((n_age, n_age), dtype=np.float64),
        0.05, 0.05, 0.5, 0.5, 0.5,
        0.2, 0.05, 0.07, 0.1, 0.1,
        0.001, 0.001, 0.01, 0.001,
        np.ones(n_age, dtype=np.float64) * 0.05,
        np.ones(n_age, dtype=np.float64) * 0.01,
        np.ones(N_ORIGINS, dtype=np.float64),
        np.ones(N_ORIGINS, dtype=np.float64),
        np.ones((N_ORIGINS, n_age), dtype=np.float64) * 0.4,
        np.ones(N_ORIGINS, dtype=np.float64),
        np.ones(n_age, dtype=np.float64) * 0.001,
        np.zeros(n_age, dtype=np.bool_),
        0.005, 0.01, np.zeros((n_age, N_ORIGINS), dtype=np.float64),
        np.zeros(n_comp, dtype=np.float64),
        np.zeros(n_age, dtype=np.float64),
        0.0, 0.0, 0.0,
        _SUS_INDICES, _EXP_S_INDICES, _EXP_R_INDICES,
        _INF_S_SYM_INDICES, _INF_S_ASYM_INDICES,
        _INF_R_SYM_INDICES, _INF_R_ASYM_INDICES,
        _TREATED_S_INDICES, _TREATED_R_INDICES,
        _V_RECENT_INDICES, _V_WANED_INDICES,
        _S_IDX, _M_IDX, _R_NAT_IDX,
    )
