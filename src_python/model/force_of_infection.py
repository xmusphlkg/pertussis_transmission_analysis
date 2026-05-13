from __future__ import annotations

import numpy as np

from src_python.model.compartments import (
    COMPARTMENTS,
    STRAINS,
    VACCINE_ORIGINS,
    StateIndex,
    infectious_name,
    susceptible_name,
    treated_name,
)
from src_python.model.parameters import PreparedParameters
from src_python.model.treatment import treated_infectiousness_relative
from src_python.model.vaccination import origin_infectiousness_multiplier, origin_relative_effect, vaccine_susceptibility

# Import Numba-accelerated kernel if available
try:
    from src_python.model.ode_kernel_numba import (
        compute_infectious_pressure,
        get_index_cache,
        NUMBA_AVAILABLE,
    )
except ImportError:
    NUMBA_AVAILABLE = False


def _seasonal_multiplier(t: float, params: PreparedParameters) -> float:
    amplitude = float(params.transmission.get("seasonal_amplitude", 0.0))
    phase = float(params.transmission.get("seasonal_phase", 0.0))
    seasonal_day = params.calendar_day_of_year_at(t)
    annual = 1.0 + amplitude * np.cos(2.0 * np.pi * (seasonal_day - phase) / 365.0)

    multi_amp = float(params.transmission.get("multi_year_amplitude", 0.0))
    multi_period_days = 365.0 * float(params.transmission.get("multi_year_period_years", 4.0))
    multi_phase = float(params.transmission.get("multi_year_phase", 0.0))
    if multi_period_days <= 0.0:
        multi_year = 1.0
    else:
        multi_year = 1.0 + multi_amp * np.cos(2.0 * np.pi * (t - multi_phase) / multi_period_days)

    return float(max(0.0, annual * multi_year))


def compute_force_of_infection(
    t: float,
    y: np.ndarray,
    params: PreparedParameters,
    index: StateIndex,
    *,
    apply_pep: bool = True,
) -> dict[str, np.ndarray | float]:
    state = np.maximum(index.reshape(y), 0.0)
    comp = {name: state[:, i] for i, name in enumerate(COMPARTMENTS)}
    population = np.maximum(state.sum(axis=1), 1.0)

    ve_sus = float(params.vaccine.get("VE_sus", 0.0))
    ve_inf = float(params.vaccine.get("VE_inf", 0.0))
    waned_relative_effect = float(params.immunity_model.get("waned_relative_effect", 0.35))
    maternal_relative_effect = float(params.immunity_model.get("maternal_relative_effect", 0.75))
    dose1_relative_effect = float(params.immunity_model.get("dose1_relative_effect", 0.45))
    dose2_relative_effect = float(params.immunity_model.get("dose2_relative_effect", 0.75))

    rel_asym = float(params.transmission["relative_infectiousness_asymptomatic"])
    rel_treated_s = treated_infectiousness_relative(params.treatment, "S")
    rel_treated_r = treated_infectiousness_relative(params.treatment, "R")

    # Use Numba-accelerated pressure computation if available
    if NUMBA_AVAILABLE:
        cache = get_index_cache()
        # Use pre-computed infectiousness multipliers from params if available
        if params.origin_infectiousness.size > 0:
            infectiousness_mult = params.origin_infectiousness
        else:
            infectiousness_mult = np.array(
                [origin_infectiousness_multiplier(
                    ve_inf, origin,
                    waned_relative_effect=waned_relative_effect,
                    maternal_relative_effect=maternal_relative_effect,
                    dose1_relative_effect=dose1_relative_effect,
                    dose2_relative_effect=dose2_relative_effect,
                ) for origin in VACCINE_ORIGINS],
                dtype=np.float64,
            )
        pressure_S, pressure_R = compute_infectious_pressure(
            state, index.n_age, index.n_compartments, cache.n_origins,
            cache.infectious_S_sym_indices, cache.infectious_S_asym_indices,
            cache.infectious_R_sym_indices, cache.infectious_R_asym_indices,
            cache.treated_S_indices, cache.treated_R_indices,
            infectiousness_mult, rel_asym, rel_treated_s, rel_treated_r,
        )
        pressure_by_strain = {"S": pressure_S, "R": pressure_R}
    else:
        pressure_by_strain: dict[str, np.ndarray] = {}
        for strain in STRAINS:
            treated_relative = rel_treated_s if strain == "S" else rel_treated_r
            pressure = np.zeros(index.n_age, dtype=float)
            for origin in VACCINE_ORIGINS:
                origin_inf = origin_infectiousness_multiplier(
                    ve_inf,
                    origin,
                    waned_relative_effect=waned_relative_effect,
                    maternal_relative_effect=maternal_relative_effect,
                    dose1_relative_effect=dose1_relative_effect,
                    dose2_relative_effect=dose2_relative_effect,
                )
                pressure += origin_inf * (
                    comp[infectious_name(strain, "sym", origin)]
                    + rel_asym * comp[infectious_name(strain, "asym", origin)]
                    + treated_relative * comp[treated_name(strain, origin)]
                )
            pressure_by_strain[strain] = pressure / population

    beta_s = float(params.transmission["beta_S"]) * _seasonal_multiplier(t, params)
    beta_r = beta_s * float(params.transmission.get("fitness_R", 1.0))
    lambda_s_base = beta_s * params.contact_matrix.dot(pressure_by_strain["S"])
    lambda_r_base = beta_r * params.contact_matrix.dot(pressure_by_strain["R"])

    pep_coverage = 0.0
    lambda_s = lambda_s_base.copy()
    lambda_r = lambda_r_base.copy()
    if apply_pep:
        symptomatic = sum(
            comp[infectious_name(strain, "sym", origin)]
            for strain in STRAINS
            for origin in VACCINE_ORIGINS
        )
        detected_symptomatic_prevalence = float(
            np.sum(symptomatic * params.pep_detection_rate_at(t)) / np.sum(population)
        )
        activation = detected_symptomatic_prevalence / (
            detected_symptomatic_prevalence + float(params.pep.get("activation_prevalence", 1e-5))
        )
        pep_coverage = float(params.pep.get("coverage_household_contacts", 0.0)) * activation
        lambda_s *= 1.0 - pep_coverage * float(params.pep.get("effectiveness_sensitive", 0.0))
        lambda_r *= 1.0 - pep_coverage * float(params.pep.get("effectiveness_resistant", 0.0))

    return {
        "lambda_S": np.clip(lambda_s, 0.0, None),
        "lambda_R": np.clip(lambda_r, 0.0, None),
        "lambda_S_base": np.clip(lambda_s_base, 0.0, None),
        "lambda_R_base": np.clip(lambda_r_base, 0.0, None),
        "vaccine_origin_share": _instant_vaccine_origin_share(
            comp,
            lambda_s + lambda_r,
            ve_sus,
            waned_relative_effect=waned_relative_effect,
            maternal_relative_effect=maternal_relative_effect,
            dose1_relative_effect=dose1_relative_effect,
            dose2_relative_effect=dose2_relative_effect,
            cached_rel_effects=params.origin_relative_effects if params.origin_relative_effects.size > 0 else None,
        ),
        "pep_coverage": pep_coverage,
    }


def _instant_vaccine_origin_share(
    comp: dict[str, np.ndarray],
    total_lambda: np.ndarray,
    ve_sus: float,
    *,
    waned_relative_effect: float,
    maternal_relative_effect: float,
    dose1_relative_effect: float,
    dose2_relative_effect: float,
    cached_rel_effects: np.ndarray | None = None,
) -> np.ndarray:
    total = np.zeros_like(total_lambda, dtype=float)
    protected_equivalent = np.zeros_like(total_lambda, dtype=float)
    for oi, origin in enumerate(VACCINE_ORIGINS):
        if cached_rel_effects is not None:
            relative_effect = float(cached_rel_effects[oi])
        else:
            relative_effect = origin_relative_effect(
                origin,
                waned_relative_effect=waned_relative_effect,
                maternal_relative_effect=maternal_relative_effect,
                dose1_relative_effect=dose1_relative_effect,
                dose2_relative_effect=dose2_relative_effect,
            )
        source = total_lambda * vaccine_susceptibility(ve_sus, relative_effect=relative_effect) * comp[
            susceptible_name(origin)
        ]
        total += source
        protected_equivalent += source * relative_effect
    return np.divide(
        protected_equivalent,
        total,
        out=np.zeros_like(total, dtype=float),
        where=total > 0,
    )
