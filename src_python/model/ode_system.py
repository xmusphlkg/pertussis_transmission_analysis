from __future__ import annotations

import numpy as np

from src_python.model.compartments import (
    COMPARTMENTS,
    STRAINS,
    VACCINE_ORIGINS,
    StateIndex,
    compartment_name,
    exposed_name,
    infectious_name,
    susceptible_name,
    treated_name,
)
from src_python.model.force_of_infection import compute_force_of_infection
from src_python.model.parameters import PreparedParameters
from src_python.model.treatment import treated_recovery_rate
from src_python.model.vaccination import (
    default_routine_target_origin_distribution,
    origin_recovery_rate_multiplier,
    origin_symptomatic_probability,
    origin_relative_effect,
    origin_is_vaccine_dose,
    vaccine_susceptibility,
)

# Import Numba kernels if available
try:
    from src_python.model.ode_kernel_numba import (
        apply_aging,
        apply_wpp_nudging,
        apply_resistance_anchor,
        get_index_cache,
        NUMBA_AVAILABLE,
    )
except ImportError:
    NUMBA_AVAILABLE = False


def rhs(t: float, y: np.ndarray, params: PreparedParameters, index: StateIndex) -> np.ndarray:
    state = np.maximum(index.reshape(y), 0.0)
    comp = {name: state[:, i] for i, name in enumerate(COMPARTMENTS)}
    dy = np.zeros_like(state)

    foi = compute_force_of_infection(t, state.reshape(index.size), params, index)
    lambda_s = foi["lambda_S"]
    lambda_r = foi["lambda_R"]

    ve_dur = float(params.vaccine.get("VE_dur", 0.0))
    waned_relative_effect = float(params.immunity_model.get("waned_relative_effect", 0.35))
    maternal_relative_effect = float(params.immunity_model.get("maternal_relative_effect", 0.75))
    dose1_relative_effect = float(params.immunity_model.get("dose1_relative_effect", 0.45))
    dose2_relative_effect = float(params.immunity_model.get("dose2_relative_effect", 0.75))

    # Use pre-computed per-origin arrays from params (avoids ~64 function calls per rhs)
    use_cache = params.origin_relative_effects.size > 0
    if use_cache:
        susceptibility_arr = params.origin_susceptibility   # shape (n_origins,)
        sym_prob_arr = params.origin_symptomatic_prob       # shape (n_origins, n_age)
        recovery_mult_arr = params.origin_recovery_mult     # shape (n_origins,)
    else:
        # Fallback: compute on the fly (legacy path, should not be reached)
        from src_python.model.vaccination import (
            origin_relative_effect, vaccine_susceptibility,
            origin_symptomatic_probability, origin_recovery_rate_multiplier,
        )
        ve_sus = float(params.vaccine.get("VE_sus", 0.0))
        ve_sym = float(params.vaccine.get("VE_sym", 0.0))

    sigma = float(params.rates["latent"])
    base_gamma_sym = float(params.rates["recovery_symptomatic"])
    base_gamma_asym = float(params.rates["recovery_asymptomatic"])
    gamma_treated_s = treated_recovery_rate(base_gamma_sym, params.treatment, "S")
    gamma_treated_r = treated_recovery_rate(base_gamma_sym, params.treatment, "R")
    waning_vaccine = float(params.rates["waning_vaccine"])
    waning_vaccine_waned = float(params.rates.get("waning_vaccine_waned", waning_vaccine))
    waning_maternal = float(params.rates.get("waning_maternal", 0.0))
    waning_natural = float(params.rates["waning_natural"])
    tr_sym = float(params.treatment["treatment_rate_symptomatic"])
    tr_asym = float(params.treatment["treatment_rate_asymptomatic"])

    c = {name: COMPARTMENTS.index(name) for name in COMPARTMENTS}

    infection_from_origin = {strain: {} for strain in STRAINS}
    for oi, origin in enumerate(VACCINE_ORIGINS):
        if use_cache:
            sus_mult = float(susceptibility_arr[oi])
        else:
            relative_effect = origin_relative_effect(
                origin,
                waned_relative_effect=waned_relative_effect,
                maternal_relative_effect=maternal_relative_effect,
                dose1_relative_effect=dose1_relative_effect,
                dose2_relative_effect=dose2_relative_effect,
            )
            sus_mult = vaccine_susceptibility(ve_sus, relative_effect=relative_effect)
        sus_comp = comp[susceptible_name(origin)]
        infection_from_origin["S"][origin] = lambda_s * sus_mult * sus_comp
        infection_from_origin["R"][origin] = lambda_r * sus_mult * sus_comp

    for origin in VACCINE_ORIGINS:
        compartment = susceptible_name(origin)
        dy[:, c[compartment]] -= infection_from_origin["S"][origin] + infection_from_origin["R"][origin]

    dy[:, c["S"]] += waning_natural * comp["R_natural"]
    dy[:, c["M_protected"]] -= waning_maternal * comp["M_protected"]
    dy[:, c["S"]] += waning_maternal * comp["M_protected"]
    for recent, waned in (
        ("V_dose1_recent", "V_dose1_waned"),
        ("V_dose2_recent", "V_dose2_waned"),
        ("V_recent", "V_waned"),
    ):
        dy[:, c[recent]] -= waning_vaccine * comp[recent]
        dy[:, c[waned]] += waning_vaccine * comp[recent]
        dy[:, c[waned]] -= waning_vaccine_waned * comp[waned]
        dy[:, c["S"]] += waning_vaccine_waned * comp[waned]

    recovered = np.zeros(index.n_age, dtype=float)
    for strain in STRAINS:
        gamma_treated_base = gamma_treated_s if strain == "S" else gamma_treated_r
        for oi, origin in enumerate(VACCINE_ORIGINS):
            exposed = exposed_name(strain, origin)
            i_sym = infectious_name(strain, "sym", origin)
            i_asym = infectious_name(strain, "asym", origin)
            treated = treated_name(strain, origin)
            progression = sigma * comp[exposed]

            if use_cache:
                p_sym = sym_prob_arr[oi]           # shape (n_age,)
                recovery_multiplier = float(recovery_mult_arr[oi])
            else:
                p_sym = origin_symptomatic_probability(
                    params.symptom_probability, ve_sym, origin,
                    waned_relative_effect=waned_relative_effect,
                    maternal_relative_effect=maternal_relative_effect,
                    dose1_relative_effect=dose1_relative_effect,
                    dose2_relative_effect=dose2_relative_effect,
                )
                recovery_multiplier = origin_recovery_rate_multiplier(
                    ve_dur, origin,
                    waned_relative_effect=waned_relative_effect,
                    maternal_relative_effect=maternal_relative_effect,
                    dose1_relative_effect=dose1_relative_effect,
                    dose2_relative_effect=dose2_relative_effect,
                )

            gamma_sym = base_gamma_sym * recovery_multiplier
            gamma_asym = base_gamma_asym * recovery_multiplier
            gamma_treated = gamma_treated_base * recovery_multiplier

            dy[:, c[exposed]] = infection_from_origin[strain][origin] - progression
            dy[:, c[i_sym]] = p_sym * progression - tr_sym * comp[i_sym] - gamma_sym * comp[i_sym]
            dy[:, c[i_asym]] = (1.0 - p_sym) * progression - tr_asym * comp[i_asym] - gamma_asym * comp[i_asym]
            dy[:, c[treated]] = tr_sym * comp[i_sym] + tr_asym * comp[i_asym] - gamma_treated * comp[treated]
            recovered += gamma_sym * comp[i_sym] + gamma_asym * comp[i_asym] + gamma_treated * comp[treated]

    dy[:, c["R_natural"]] = recovered - waning_natural * comp["R_natural"]

    _add_routine_vaccination(dy, state, params, c)
    _add_importation(dy, comp, params, c)
    if params.resistance.get("anchor_during_dynamics", False):
        _add_resistance_prevalence_anchor(dy, state, params, c)
    _add_demographic_turnover(dy, state, params, index, c, t=float(t))

    return index.flatten(dy)


def _add_routine_vaccination(
    dy: np.ndarray,
    state: np.ndarray,
    params: PreparedParameters,
    c: dict[str, int],
) -> None:
    config = params.routine_vaccination
    if not config.get("enabled", False):
        return
    rate = float(config.get("target_relaxation_rate_per_year", 0.0)) / 365.0
    if rate <= 0.0:
        return

    current_population = np.maximum(state.sum(axis=1), 0.0)
    for age_idx, age in enumerate(params.age_groups):
        target_distribution = _routine_target_distribution(params, age)
        target_distribution = {
            origin: share for origin, share in target_distribution.items() if origin_is_vaccine_dose(origin)
        }
        total_share = float(sum(max(0.0, share) for share in target_distribution.values()))
        if total_share <= 0.0:
            continue

        deficits = {}
        for origin, share in target_distribution.items():
            desired = current_population[age_idx] * params.vaccine_coverage[age_idx] * max(0.0, share) / total_share
            current = state[age_idx, c[susceptible_name(origin)]]
            deficits[origin] = max(0.0, float(desired - current))
        total_deficit = float(sum(deficits.values()))
        if total_deficit <= 0.0:
            continue
        total_flow = min(rate * total_deficit, state[age_idx, c["S"]])
        dy[age_idx, c["S"]] -= total_flow
        for origin, deficit in deficits.items():
            dy[age_idx, c[susceptible_name(origin)]] += total_flow * deficit / total_deficit


def _add_importation(
    dy: np.ndarray,
    comp: dict[str, np.ndarray],
    params: PreparedParameters,
    c: dict[str, int],
) -> None:
    config = params.importation
    if not config.get("enabled", False):
        return
    rate_per_100k_year = float(config.get("rate_per_100k_per_year", 0.0))
    if rate_per_100k_year <= 0.0:
        return

    age_distribution = np.array(
        [float(config.get("age_distribution", {}).get(age, 1.0 / len(params.age_groups))) for age in params.age_groups],
        dtype=float,
    )
    total_share = float(age_distribution.sum())
    if total_share <= 0.0:
        age_distribution = np.repeat(1.0 / len(params.age_groups), len(params.age_groups))
    else:
        age_distribution = age_distribution / total_share

    total_imported = params.total_population * rate_per_100k_year / 100_000.0 / 365.0
    imported = total_imported * age_distribution
    resistant_fraction = float(config.get("resistant_fraction", params.initial.get("initial_resistance_prevalence", 0.0)))

    susceptible_pool = np.maximum(
        sum(comp[susceptible_name(origin)] for origin in VACCINE_ORIGINS),
        1e-12,
    )
    imported_by_origin = {}
    for origin in VACCINE_ORIGINS:
        compartment = susceptible_name(origin)
        share = np.divide(
            comp[compartment],
            susceptible_pool,
            out=np.zeros_like(comp[compartment]),
            where=susceptible_pool > 0,
        )
        from_origin = imported * share
        dy[:, c[compartment]] -= np.minimum(from_origin, comp[compartment])
        imported_by_origin[origin] = from_origin
    for origin, imported_origin in imported_by_origin.items():
        dy[:, c[exposed_name("R", origin)]] += imported_origin * resistant_fraction
        dy[:, c[exposed_name("S", origin)]] += imported_origin * (1.0 - resistant_fraction)


def _add_resistance_prevalence_anchor(
    dy: np.ndarray,
    state: np.ndarray,
    params: PreparedParameters,
    c: dict[str, int],
) -> None:
    config = params.resistance
    rate = float(config.get("prevalence_anchor_rate_per_year", 0.0)) / 365.0
    if rate <= 0.0:
        return
    target = float(
        np.clip(
            config.get(
                "target_prevalence_at_analysis_start",
                params.initial.get("initial_resistance_prevalence", 0.0),
            ),
            0.0,
            1.0,
        )
    )
    for origin in VACCINE_ORIGINS:
        for sensitive, resistant in (
            (exposed_name("S", origin), exposed_name("R", origin)),
            (infectious_name("S", "sym", origin), infectious_name("R", "sym", origin)),
            (infectious_name("S", "asym", origin), infectious_name("R", "asym", origin)),
            (treated_name("S", origin), treated_name("R", origin)),
        ):
            total = state[:, c[sensitive]] + state[:, c[resistant]]
            desired_resistant = target * total
            flow_to_resistant = rate * (desired_resistant - state[:, c[resistant]])
            dy[:, c[sensitive]] -= flow_to_resistant
            dy[:, c[resistant]] += flow_to_resistant


def _add_demographic_turnover(
    dy: np.ndarray,
    state: np.ndarray,
    params: PreparedParameters,
    index: StateIndex,
    c: dict[str, int],
    t: float = 0.0,
) -> None:
    config = params.demography
    if not config.get("enabled", False):
        return

    duration_by_age = config.get("age_bin_durations_years", {})
    durations = np.array(
        [float(duration_by_age.get(age, 1.0)) for age in params.age_groups],
        dtype=float,
    )
    if np.any(durations <= 0.0):
        raise ValueError("All demography age-bin durations must be > 0.")

    maternal_proxy = config.get("maternal_protection_proxy", {})
    maternal_exit_groups = (
        set(maternal_proxy.get("exit_age_groups", [])) if maternal_proxy.get("enabled", False) else set()
    )

    wpp_active = params.wpp_trajectory_active()
    if wpp_active:
        _apply_wpp_demography(dy, state, params, index, c, t, durations, maternal_exit_groups)
    else:
        _apply_fixed_profile_demography(dy, state, params, index, c, durations, maternal_exit_groups)


def _apply_fixed_profile_demography(
    dy: np.ndarray,
    state: np.ndarray,
    params: PreparedParameters,
    index: StateIndex,
    c: dict[str, int],
    durations: np.ndarray,
    maternal_exit_groups: set[str],
) -> None:
    config = params.demography
    if config.get("fixed_population_profile", True):
        reference_age = str(config.get("fixed_population_reference_age_group", params.age_groups[0]))
        reference_idx = params.age_groups.index(reference_age) if reference_age in params.age_groups else 0
        target_population = np.maximum(params.population, 1e-12)
        reference_flow = target_population[reference_idx] / (durations[reference_idx] * 365.0)
        aging_rates = reference_flow / target_population
    else:
        aging_rates = 1.0 / (durations * 365.0)

    for age_idx in range(index.n_age - 1):
        flow = aging_rates[age_idx] * state[age_idx, :]
        flow_to_next = flow.copy()
        if params.age_groups[age_idx] in maternal_exit_groups:
            flow_to_next[c["S"]] += flow_to_next[c["M_protected"]]
            flow_to_next[c["M_protected"]] = 0.0
        dy[age_idx, :] -= flow
        dy[age_idx + 1, :] += flow_to_next

    oldest_flow = aging_rates[-1] * state[-1, :]
    dy[-1, :] -= oldest_flow
    total_births = float(oldest_flow.sum())

    birth_entry = config.get("birth_entry", {"S": 1.0})
    total_weight = float(sum(max(0.0, float(weight)) for weight in birth_entry.values()))
    if total_weight <= 0.0:
        dy[0, c["S"]] += total_births
        return
    for compartment, weight in birth_entry.items():
        resolved = compartment_name(compartment)
        if resolved not in c:
            raise ValueError(f"Unknown demography birth-entry compartment: {compartment}")
        dy[0, c[resolved]] += total_births * max(0.0, float(weight)) / total_weight


def _apply_wpp_demography(
    dy: np.ndarray,
    state: np.ndarray,
    params: PreparedParameters,
    index: StateIndex,
    c: dict[str, int],
    t: float,
    durations: np.ndarray,
    maternal_exit_groups: set[str],
) -> None:
    """Apply an age-structured demographic update driven by WPP annual data.

    Three flows contribute at each integrator step:
    1. Aging: each age group loses ``population / (duration_years * 365)`` per day
       to the next age group, proportional to its current compartment state.
    2. Births: age-0 WPP inflow (interpolated by calendar year) is added to the
       youngest age group and allocated across compartments via ``birth_entry``.
    3. Nudging: a gentle rescaling pulls the total age-group population toward
       the WPP target trajectory to absorb net migration and differential
       mortality that are not explicit in the ODE. The nudge is applied uniformly
       across compartments within each age group so disease state proportions
       are preserved.
    """
    demography = params.demography
    year = _current_calendar_year(params, t)

    target_population = np.maximum(params.wpp_population_at(year), 1e-12)
    births_per_day = float(params.wpp_daily_birth_rate_at(year))

    # 1. Aging with constant per-age width, preserving disease state proportions.
    aging_rates = 1.0 / (durations * 365.0)
    for age_idx in range(index.n_age - 1):
        flow = aging_rates[age_idx] * state[age_idx, :]
        flow_to_next = flow.copy()
        if params.age_groups[age_idx] in maternal_exit_groups:
            flow_to_next[c["S"]] += flow_to_next[c["M_protected"]]
            flow_to_next[c["M_protected"]] = 0.0
        dy[age_idx, :] -= flow
        dy[age_idx + 1, :] += flow_to_next
    # Oldest group: individuals exit out of the model through natural mortality
    # (proxied by the aging-out rate). We do not route them back as births; those
    # are supplied by WPP instead.
    dy[-1, :] -= aging_rates[-1] * state[-1, :]

    # 2. Births from WPP age-0 inflow.
    birth_entry = demography.get("birth_entry", {"S": 1.0})
    total_weight = float(sum(max(0.0, float(weight)) for weight in birth_entry.values()))
    if total_weight <= 0.0:
        dy[0, c["S"]] += births_per_day
    else:
        for compartment, weight in birth_entry.items():
            resolved = compartment_name(compartment)
            if resolved not in c:
                raise ValueError(f"Unknown demography birth-entry compartment: {compartment}")
            dy[0, c[resolved]] += births_per_day * max(0.0, float(weight)) / total_weight

    # 3. Nudging toward the WPP target population.
    nudge_rate_per_year = float(demography.get("wpp_nudge_rate_per_year", 1.0))
    if nudge_rate_per_year > 0.0:
        nudge_rate_per_day = nudge_rate_per_year / 365.0
        current_age_population = np.maximum(state.sum(axis=1), 1e-12)
        ratio = target_population / current_age_population
        # Apply a first-order correction toward target: dP/dt_nudge = k * (target - P)
        # distributed proportionally across compartments so disease mixing is not
        # altered by the demographic adjustment.
        for age_idx in range(index.n_age):
            correction = nudge_rate_per_day * (target_population[age_idx] - current_age_population[age_idx])
            if abs(correction) < 1e-12:
                continue
            if current_age_population[age_idx] > 0:
                share = state[age_idx, :] / current_age_population[age_idx]
            else:
                share = np.zeros_like(state[age_idx, :])
                share[c["S"]] = 1.0
            dy[age_idx, :] += correction * share


def _current_calendar_year(params: PreparedParameters, t: float) -> float:
    """Return fractional calendar year for a simulation time ``t`` in days."""
    if params.calendar_start_date is not None:
        start_time = float(params.raw["simulation"].get("start_time", 0.0))
        calendar_date = params.calendar_start_date
        # Days elapsed from the analysis start (can be negative during burn-in).
        delta_days = float(t) - start_time
        # Fractional year relative to Jan-1 of the start year.
        year_start = calendar_date.replace(month=1, day=1).toordinal()
        current_ordinal = calendar_date.toordinal() + delta_days
        year = calendar_date.year + (current_ordinal - year_start) / 365.25
        return float(year)
    # Without a calendar, assume t=0 is Jan-1 of analysis_start_year in trajectory.
    trajectory = params.demography.get("wpp_trajectory", {})
    start_year = int(trajectory.get("analysis_start_year", 2026))
    return float(start_year) + float(t) / 365.25


def _routine_target_distribution(params: PreparedParameters, age: str) -> dict[str, float]:
    configured = params.routine_vaccination.get("target_origin_distribution_by_age", {})
    if age in configured:
        return {str(origin): float(share) for origin, share in configured[age].items()}
    return default_routine_target_origin_distribution(age)
