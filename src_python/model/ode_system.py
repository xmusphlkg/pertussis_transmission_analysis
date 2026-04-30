from __future__ import annotations

import numpy as np

from src_python.model.compartments import COMPARTMENTS, StateIndex
from src_python.model.force_of_infection import compute_force_of_infection
from src_python.model.parameters import PreparedParameters
from src_python.model.treatment import treated_recovery_rate
from src_python.model.vaccination import recovery_rate_multiplier, symptomatic_probability


def rhs(t: float, y: np.ndarray, params: PreparedParameters, index: StateIndex) -> np.ndarray:
    state = np.maximum(index.reshape(y), 0.0)
    comp = {name: state[:, i] for i, name in enumerate(COMPARTMENTS)}
    dy = np.zeros_like(state)

    foi = compute_force_of_infection(t, state.reshape(index.size), params, index)
    lambda_s = foi["lambda_S"]
    lambda_r = foi["lambda_R"]

    ve_sus = float(params.vaccine.get("VE_sus", 0.0))
    ve_sym = float(params.vaccine.get("VE_sym", 0.0))
    ve_dur = float(params.vaccine.get("VE_dur", 0.0))
    susceptibility_vaccinated = max(0.0, 1.0 - ve_sus)

    inf_s_from_s = lambda_s * comp["S"]
    inf_s_from_v = lambda_s * susceptibility_vaccinated * comp["V"]
    inf_r_from_s = lambda_r * comp["S"]
    inf_r_from_v = lambda_r * susceptibility_vaccinated * comp["V"]

    p_sym_s = symptomatic_probability(params.symptom_probability, inf_s_from_s, inf_s_from_v, ve_sym)
    p_sym_r = symptomatic_probability(params.symptom_probability, inf_r_from_s, inf_r_from_v, ve_sym)

    vaccine_origin = foi["vaccine_origin_share"]
    vax_recovery_multiplier = recovery_rate_multiplier(vaccine_origin, ve_dur)
    sigma = float(params.rates["latent"])
    gamma_sym = float(params.rates["recovery_symptomatic"]) * vax_recovery_multiplier
    gamma_asym = float(params.rates["recovery_asymptomatic"]) * vax_recovery_multiplier
    gamma_treated_s = treated_recovery_rate(float(params.rates["recovery_symptomatic"]), params.treatment, "S")
    gamma_treated_r = treated_recovery_rate(float(params.rates["recovery_symptomatic"]), params.treatment, "R")
    waning_vaccine = float(params.rates["waning_vaccine"])
    waning_natural = float(params.rates["waning_natural"])
    tr_sym = float(params.treatment["treatment_rate_symptomatic"])
    tr_asym = float(params.treatment["treatment_rate_asymptomatic"])

    new_s = inf_s_from_s + inf_s_from_v
    new_r = inf_r_from_s + inf_r_from_v
    prog_s = sigma * comp["E_S"]
    prog_r = sigma * comp["E_R"]

    c = {name: COMPARTMENTS.index(name) for name in COMPARTMENTS}
    dy[:, c["S"]] = -inf_s_from_s - inf_r_from_s + waning_vaccine * comp["V"] + waning_natural * comp["R"]
    dy[:, c["V"]] = -inf_s_from_v - inf_r_from_v - waning_vaccine * comp["V"]
    dy[:, c["E_S"]] = new_s - prog_s
    dy[:, c["E_R"]] = new_r - prog_r
    dy[:, c["I_S_sym"]] = p_sym_s * prog_s - tr_sym * comp["I_S_sym"] - gamma_sym * comp["I_S_sym"]
    dy[:, c["I_S_asym"]] = (1.0 - p_sym_s) * prog_s - tr_asym * comp["I_S_asym"] - gamma_asym * comp["I_S_asym"]
    dy[:, c["I_R_sym"]] = p_sym_r * prog_r - tr_sym * comp["I_R_sym"] - gamma_sym * comp["I_R_sym"]
    dy[:, c["I_R_asym"]] = (1.0 - p_sym_r) * prog_r - tr_asym * comp["I_R_asym"] - gamma_asym * comp["I_R_asym"]
    dy[:, c["T_S"]] = tr_sym * comp["I_S_sym"] + tr_asym * comp["I_S_asym"] - gamma_treated_s * comp["T_S"]
    dy[:, c["T_R"]] = tr_sym * comp["I_R_sym"] + tr_asym * comp["I_R_asym"] - gamma_treated_r * comp["T_R"]
    dy[:, c["R"]] = (
        gamma_sym * (comp["I_S_sym"] + comp["I_R_sym"])
        + gamma_asym * (comp["I_S_asym"] + comp["I_R_asym"])
        + gamma_treated_s * comp["T_S"]
        + gamma_treated_r * comp["T_R"]
        - waning_natural * comp["R"]
    )

    _add_routine_vaccination(dy, state, params, c)
    _add_importation(dy, comp, params, c)
    _add_demographic_turnover(dy, state, params, index, c)

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
    target_vaccinated = current_population * params.vaccine_coverage
    deficit = np.maximum(target_vaccinated - state[:, c["V"]], 0.0)
    flow = np.minimum(rate * deficit, state[:, c["S"]])
    dy[:, c["S"]] -= flow
    dy[:, c["V"]] += flow


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

    susceptible_pool = np.maximum(comp["S"] + comp["V"], 1e-12)
    from_s_share = np.divide(comp["S"], susceptible_pool, out=np.ones_like(comp["S"]), where=susceptible_pool > 0)
    from_s = imported * from_s_share
    from_v = imported - from_s

    dy[:, c["S"]] -= np.minimum(from_s, comp["S"])
    dy[:, c["V"]] -= np.minimum(from_v, comp["V"])
    dy[:, c["E_R"]] += imported * resistant_fraction
    dy[:, c["E_S"]] += imported * (1.0 - resistant_fraction)


def _add_demographic_turnover(
    dy: np.ndarray,
    state: np.ndarray,
    params: PreparedParameters,
    index: StateIndex,
    c: dict[str, int],
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
    aging_rates = 1.0 / (durations * 365.0)

    for age_idx in range(index.n_age - 1):
        flow = aging_rates[age_idx] * state[age_idx, :]
        dy[age_idx, :] -= flow
        dy[age_idx + 1, :] += flow

    oldest_flow = aging_rates[-1] * state[-1, :]
    dy[-1, :] -= oldest_flow
    total_births = float(oldest_flow.sum())

    birth_entry = config.get("birth_entry", {"S": 1.0})
    total_weight = float(sum(max(0.0, float(weight)) for weight in birth_entry.values()))
    if total_weight <= 0.0:
        dy[0, c["S"]] += total_births
        return
    for compartment, weight in birth_entry.items():
        if compartment not in c:
            raise ValueError(f"Unknown demography birth-entry compartment: {compartment}")
        dy[0, c[compartment]] += total_births * max(0.0, float(weight)) / total_weight
