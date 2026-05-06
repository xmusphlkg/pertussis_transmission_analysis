from __future__ import annotations

import numpy as np

from src_python.model.compartments import COMPARTMENTS, STRAINS, VACCINE_ORIGINS, StateIndex, infectious_name, treated_name
from src_python.model.parameters import PreparedParameters
from src_python.model.treatment import treated_infectiousness_relative
from src_python.model.vaccination import origin_infectiousness_multiplier, vaccine_susceptibility


def _seasonal_multiplier(t: float, params: PreparedParameters) -> float:
    amplitude = float(params.transmission["seasonal_amplitude"])
    phase = float(params.transmission["seasonal_phase"])
    annual = 1.0 + amplitude * np.cos(2.0 * np.pi * (t - phase) / 365.0)

    multi_amp = float(params.transmission["multi_year_amplitude"])
    multi_period_days = 365.0 * float(params.transmission["multi_year_period_years"])
    multi_phase = float(params.transmission["multi_year_phase"])
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

    ve_sus = float(params.vaccine["VE_sus"])
    ve_inf = float(params.vaccine["VE_inf"])
    waned_relative_effect = float(params.immunity_model["waned_relative_effect"])

    rel_asym = float(params.transmission["relative_infectiousness_asymptomatic"])
    rel_treated_s = treated_infectiousness_relative(params.treatment, "S")
    rel_treated_r = treated_infectiousness_relative(params.treatment, "R")

    pressure_by_strain: dict[str, np.ndarray] = {}
    for strain in STRAINS:
        treated_relative = rel_treated_s if strain == "S" else rel_treated_r
        pressure = np.zeros(index.n_age, dtype=float)
        for origin in VACCINE_ORIGINS:
            origin_inf = origin_infectiousness_multiplier(
                ve_inf,
                origin,
                waned_relative_effect=waned_relative_effect,
            )
            pressure += origin_inf * (
                comp[infectious_name(strain, "sym", origin)]
                + rel_asym * comp[infectious_name(strain, "asym", origin)]
                + treated_relative * comp[treated_name(strain, origin)]
            )
        pressure_by_strain[strain] = pressure / population

    beta_s = float(params.transmission["beta_S"]) * _seasonal_multiplier(t, params)
    beta_r = beta_s * float(params.transmission["fitness_R"])
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
        observation_probability = params.observation_probabilities_at(t)["reported"]
        detected_symptomatic_prevalence = float(
            np.sum(symptomatic * observation_probability) / np.sum(population)
        )
        activation = detected_symptomatic_prevalence / (
            detected_symptomatic_prevalence + float(params.pep["activation_prevalence"])
        )
        pep_coverage = float(params.pep["coverage_household_contacts"]) * activation
        lambda_s *= 1.0 - pep_coverage * float(params.pep["effectiveness_sensitive"])
        lambda_r *= 1.0 - pep_coverage * float(params.pep["effectiveness_resistant"])

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
        ),
        "pep_coverage": pep_coverage,
    }


def _instant_vaccine_origin_share(
    comp: dict[str, np.ndarray],
    total_lambda: np.ndarray,
    ve_sus: float,
    *,
    waned_relative_effect: float,
) -> np.ndarray:
    from_s = total_lambda * comp["S"]
    from_recent = total_lambda * vaccine_susceptibility(ve_sus) * comp["V_recent"]
    from_waned = total_lambda * vaccine_susceptibility(ve_sus, relative_effect=waned_relative_effect) * comp["V_waned"]
    total = from_s + from_recent + from_waned
    return np.divide(
        from_recent + from_waned,
        total,
        out=np.zeros_like(total, dtype=float),
        where=total > 0,
    )
