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
    treated_name,
)
from src_python.model.force_of_infection import compute_force_of_infection
from src_python.model.parameters import PreparedParameters
from src_python.model.treatment import treated_recovery_rate
from src_python.model.vaccination import (
    origin_recovery_rate_multiplier,
    origin_symptomatic_probability,
    vaccine_susceptibility,
)


def rhs(t: float, y: np.ndarray, params: PreparedParameters, index: StateIndex) -> np.ndarray:
    state = np.maximum(index.reshape(y), 0.0)
    comp = {name: state[:, i] for i, name in enumerate(COMPARTMENTS)}
    dy = np.zeros_like(state)

    foi = compute_force_of_infection(t, state.reshape(index.size), params, index)
    lambda_s = foi["lambda_S"]
    lambda_r = foi["lambda_R"]

    ve_sus = float(params.vaccine["VE_sus"])
    ve_dur = float(params.vaccine["VE_dur"])
    waned_relative_effect = float(params.immunity_model["waned_relative_effect"])
    ve_sym = float(params.vaccine["VE_sym"])

    sigma = float(params.rates["latent"])
    base_gamma_sym = float(params.rates["recovery_symptomatic"])
    base_gamma_asym = float(params.rates["recovery_asymptomatic"])
    gamma_treated_s = treated_recovery_rate(base_gamma_sym, params.treatment, "S")
    gamma_treated_r = treated_recovery_rate(base_gamma_sym, params.treatment, "R")
    waning_vaccine = float(params.rates["waning_vaccine"])
    waning_vaccine_waned = float(params.rates["waning_vaccine_waned"])
    waning_natural = float(params.rates["waning_natural"])
    tr_sym = float(params.treatment["treatment_rate_symptomatic"])
    tr_asym = float(params.treatment["treatment_rate_asymptomatic"])

    c = {name: COMPARTMENTS.index(name) for name in COMPARTMENTS}
    infection_from_origin = {
        "S": {
            "unvaccinated": lambda_s * comp["S"],
            "recent": lambda_s * vaccine_susceptibility(ve_sus) * comp["V_recent"],
            "waned": lambda_s
            * vaccine_susceptibility(ve_sus, relative_effect=waned_relative_effect)
            * comp["V_waned"],
        },
        "R": {
            "unvaccinated": lambda_r * comp["S"],
            "recent": lambda_r * vaccine_susceptibility(ve_sus) * comp["V_recent"],
            "waned": lambda_r
            * vaccine_susceptibility(ve_sus, relative_effect=waned_relative_effect)
            * comp["V_waned"],
        },
    }

    dy[:, c["S"]] = (
        -infection_from_origin["S"]["unvaccinated"]
        - infection_from_origin["R"]["unvaccinated"]
        + waning_vaccine_waned * comp["V_waned"]
        + waning_natural * comp["R_natural"]
    )
    dy[:, c["V_recent"]] = (
        -infection_from_origin["S"]["recent"]
        - infection_from_origin["R"]["recent"]
        - waning_vaccine * comp["V_recent"]
    )
    dy[:, c["V_waned"]] = (
        -infection_from_origin["S"]["waned"]
        - infection_from_origin["R"]["waned"]
        + waning_vaccine * comp["V_recent"]
        - waning_vaccine_waned * comp["V_waned"]
    )

    recovered = np.zeros(index.n_age, dtype=float)
    for strain in STRAINS:
        gamma_treated_base = gamma_treated_s if strain == "S" else gamma_treated_r
        for origin in VACCINE_ORIGINS:
            exposed = exposed_name(strain, origin)
            i_sym = infectious_name(strain, "sym", origin)
            i_asym = infectious_name(strain, "asym", origin)
            treated = treated_name(strain, origin)
            progression = sigma * comp[exposed]
            p_sym = origin_symptomatic_probability(
                params.symptom_probability,
                ve_sym,
                origin,
                waned_relative_effect=waned_relative_effect,
            )
            recovery_multiplier = origin_recovery_rate_multiplier(
                ve_dur,
                origin,
                waned_relative_effect=waned_relative_effect,
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
    if bool(params.resistance["anchor_during_dynamics"]):
        _add_resistance_prevalence_anchor(dy, state, params, c)
    _add_demographic_turnover(dy, state, params, index, c)

    return index.flatten(dy)


def _add_routine_vaccination(
    dy: np.ndarray,
    state: np.ndarray,
    params: PreparedParameters,
    c: dict[str, int],
) -> None:
    config = params.routine_vaccination
    if not bool(config["enabled"]):
        return
    rate = float(config["target_relaxation_rate_per_year"]) / 365.0
    if rate <= 0.0:
        return

    current_population = np.maximum(state.sum(axis=1), 0.0)
    target_vaccinated = current_population * params.vaccine_coverage
    current_vaccinated = state[:, c["V_recent"]] + state[:, c["V_waned"]]
    deficit = np.maximum(target_vaccinated - current_vaccinated, 0.0)
    flow = np.minimum(rate * deficit, state[:, c["S"]])
    dy[:, c["S"]] -= flow
    dy[:, c["V_recent"]] += flow


def _add_importation(
    dy: np.ndarray,
    comp: dict[str, np.ndarray],
    params: PreparedParameters,
    c: dict[str, int],
) -> None:
    config = params.importation
    if not bool(config["enabled"]):
        return
    rate_per_100k_year = float(config["rate_per_100k_per_year"])
    if rate_per_100k_year <= 0.0:
        return

    age_distribution = np.array(
        [float(config["age_distribution"][age]) for age in params.age_groups],
        dtype=float,
    )
    total_share = float(age_distribution.sum())
    if total_share <= 0.0:
        raise ValueError("Importation age distribution must have positive total weight.")
    else:
        age_distribution = age_distribution / total_share

    total_imported = params.total_population * rate_per_100k_year / 100_000.0 / 365.0
    imported = total_imported * age_distribution
    resistant_fraction = float(config["resistant_fraction"])

    susceptible_pool = np.maximum(comp["S"] + comp["V_recent"] + comp["V_waned"], 1e-12)
    from_s_share = np.divide(comp["S"], susceptible_pool, out=np.ones_like(comp["S"]), where=susceptible_pool > 0)
    from_recent_share = np.divide(comp["V_recent"], susceptible_pool, out=np.zeros_like(comp["S"]), where=susceptible_pool > 0)
    from_waned_share = np.divide(comp["V_waned"], susceptible_pool, out=np.zeros_like(comp["S"]), where=susceptible_pool > 0)
    from_s = np.minimum(imported * from_s_share, comp["S"])
    from_recent = np.minimum(imported * from_recent_share, comp["V_recent"])
    from_waned = np.minimum(imported * from_waned_share, comp["V_waned"])

    dy[:, c["S"]] -= from_s
    dy[:, c["V_recent"]] -= from_recent
    dy[:, c["V_waned"]] -= from_waned
    imported_by_origin = {
        "unvaccinated": from_s,
        "recent": from_recent,
        "waned": from_waned,
    }
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
    rate = float(config["prevalence_anchor_rate_per_year"]) / 365.0
    if rate <= 0.0:
        return
    target = float(
        np.clip(
            config["target_prevalence_at_analysis_start"],
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
) -> None:
    config = params.demography
    if not bool(config["enabled"]):
        return

    duration_by_age = config["age_bin_durations_years"]
    durations = np.array(
        [float(duration_by_age[age]) for age in params.age_groups],
        dtype=float,
    )
    if np.any(durations <= 0.0):
        raise ValueError("All demography age-bin durations must be > 0.")
    if bool(config["fixed_population_profile"]):
        reference_age = str(config["fixed_population_reference_age_group"])
        if reference_age not in params.age_groups:
            raise ValueError(f"Unknown fixed population reference age group: {reference_age}")
        reference_idx = params.age_groups.index(reference_age)
        target_population = np.maximum(params.population, 1e-12)
        reference_flow = target_population[reference_idx] / (durations[reference_idx] * 365.0)
        aging_rates = reference_flow / target_population
    else:
        aging_rates = 1.0 / (durations * 365.0)

    for age_idx in range(index.n_age - 1):
        flow = aging_rates[age_idx] * state[age_idx, :]
        dy[age_idx, :] -= flow
        dy[age_idx + 1, :] += flow

    oldest_flow = aging_rates[-1] * state[-1, :]
    dy[-1, :] -= oldest_flow
    total_births = float(oldest_flow.sum())

    birth_entry = config["birth_entry"]
    total_weight = float(sum(max(0.0, float(weight)) for weight in birth_entry.values()))
    if total_weight <= 0.0:
        raise ValueError("Demography birth-entry weights must have positive total weight.")
    for compartment, weight in birth_entry.items():
        resolved = compartment_name(compartment)
        if resolved not in c:
            raise ValueError(f"Unknown demography birth-entry compartment: {compartment}")
        dy[0, c[resolved]] += total_births * max(0.0, float(weight)) / total_weight
