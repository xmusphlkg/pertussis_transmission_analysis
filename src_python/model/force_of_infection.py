from __future__ import annotations

import numpy as np

from src_python.model.compartments import COMPARTMENTS, StateIndex
from src_python.model.parameters import PreparedParameters
from src_python.model.treatment import treated_infectiousness_relative
from src_python.model.vaccination import infectiousness_multiplier, vaccinated_infection_share


def _seasonal_multiplier(t: float, params: PreparedParameters) -> float:
    amplitude = float(params.transmission.get("seasonal_amplitude", 0.0))
    phase = float(params.transmission.get("seasonal_phase", 0.0))
    annual = 1.0 + amplitude * np.cos(2.0 * np.pi * (t - phase) / 365.0)

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
    vaccine_origin = vaccinated_infection_share(comp["S"], comp["V"], ve_sus)
    vax_inf_multiplier = infectiousness_multiplier(vaccine_origin, ve_inf)

    rel_asym = float(params.transmission["relative_infectiousness_asymptomatic"])
    rel_treated_s = treated_infectiousness_relative(params.treatment, "S")
    rel_treated_r = treated_infectiousness_relative(params.treatment, "R")

    pressure_sensitive = (
        vax_inf_multiplier * (comp["I_S_sym"] + rel_asym * comp["I_S_asym"])
        + rel_treated_s * comp["T_S"]
    ) / population
    pressure_resistant = (
        vax_inf_multiplier * (comp["I_R_sym"] + rel_asym * comp["I_R_asym"])
        + rel_treated_r * comp["T_R"]
    ) / population

    beta_s = float(params.transmission["beta_S"]) * _seasonal_multiplier(t, params)
    beta_r = beta_s * float(params.transmission.get("fitness_R", 1.0))
    lambda_s_base = beta_s * params.contact_matrix.dot(pressure_sensitive)
    lambda_r_base = beta_r * params.contact_matrix.dot(pressure_resistant)

    pep_coverage = 0.0
    lambda_s = lambda_s_base.copy()
    lambda_r = lambda_r_base.copy()
    if apply_pep:
        detected_symptomatic_prevalence = float(
            np.sum((comp["I_S_sym"] + comp["I_R_sym"]) * params.reporting_rate_at(t)) / np.sum(population)
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
        "vaccine_origin_share": np.clip(vaccine_origin, 0.0, 1.0),
        "pep_coverage": pep_coverage,
    }
