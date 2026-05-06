from __future__ import annotations

import numpy as np
import pytest

from src_python.model.compartments import COMPARTMENTS, VACCINE_ORIGINS, StateIndex, exposed_name, infectious_name
from src_python.model.contact_matrix import balance_reciprocity, reciprocity_error
from src_python.model.force_of_infection import compute_force_of_infection
from src_python.model.ode_system import rhs
from src_python.model.outputs import (
    _daily_metrics,
    _normalized_age_distribution,
    active_resistant_fraction,
    initial_state,
    solve_model,
    summarize_timeseries,
)
from src_python.model.parameters import PreparedParameters
from src_python.calibration.calibrate_baseline import (
    align_annual_reported_cases,
    apply_calibration_vector,
    initial_calibration_vector,
)
from src_python.simulation.common import make_config, make_intervention_config, run_prepared_config, validate_run_metadata
from src_python.utils.io import load_yaml, project_path
from src_python.utils.validation import validate_timeseries


def _baseline_params() -> PreparedParameters:
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    config["simulation"]["burn_in_years"] = 2
    config["simulation"]["end_time"] = 365
    return PreparedParameters.from_config(
        config,
        analysis="test",
        scenario="baseline",
        vaccine_scenario="symptom_protective",
        resistance_scenario="moderate",
    )


def test_initial_population_matches_config():
    params = _baseline_params()
    index = StateIndex(params.age_groups)
    y0 = initial_state(params, index)
    age_totals = index.reshape(y0).sum(axis=1)
    assert np.allclose(age_totals, params.population)


def test_solution_population_conserved_and_nonnegative():
    params = _baseline_params()
    index = StateIndex(params.age_groups)
    y0 = initial_state(params, index)
    solution = solve_model(params, index)
    assert solution.success
    totals = solution.y.reshape(index.n_age, index.n_compartments, -1).sum(axis=(0, 1))
    expected = float(index.reshape(y0).sum())
    assert np.max(np.abs(totals - expected)) < params.total_population * 1e-8
    assert solution.y.min() > -1e-5


def test_demography_keeps_config_age_population_as_fixed_point():
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate", country_profile="China")
    config["simulation"]["burn_in_years"] = 3
    config["simulation"]["end_time"] = 28
    config["transmission"]["beta_S"] = 0.0
    config["importation"]["enabled"] = False
    config["initial_conditions"]["initial_exposed_per_100k"] = 0.0
    config["initial_conditions"]["initial_infectious_per_100k"] = 0.0
    params = PreparedParameters.from_config(
        config,
        analysis="test",
        scenario="age_fixed_point",
    )
    index = StateIndex(params.age_groups)
    solution = solve_model(params, index)
    age_totals = solution.y[:, 0].reshape(index.n_age, index.n_compartments).sum(axis=1)
    assert np.allclose(age_totals, params.population, rtol=1e-4, atol=1e-2)


def test_timeseries_has_valid_epidemiological_columns():
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    config["simulation"]["burn_in_years"] = 1
    config["simulation"]["end_time"] = 56
    timeseries, _ = run_prepared_config(
        config,
        analysis="test",
        scenario="baseline",
        vaccine_scenario="symptom_protective",
        resistance_scenario="moderate",
    )
    validate_timeseries(timeseries)
    first = timeseries.loc[np.isclose(timeseries["time"], timeseries["time"].min())]
    assert first["cumulative_cases"].max() == 0.0
    assert first["total_infections"].max() == 0.0


def test_vaccine_source_compartments_track_recent_and_waned_breakthroughs():
    params = _baseline_params()
    index = StateIndex(params.age_groups)
    y0 = initial_state(params, index)
    state = index.reshape(y0)
    c = {name: COMPARTMENTS.index(name) for name in COMPARTMENTS}
    source_seeded = [
        float(state[:, c[exposed_name("S", origin)]].sum() + state[:, c[infectious_name("S", "sym", origin)]].sum())
        for origin in VACCINE_ORIGINS
    ]
    assert source_seeded[1] > 0.0
    assert source_seeded[2] > 0.0


def test_seed_distribution_must_explicitly_cover_all_age_groups():
    with pytest.raises(ValueError, match="missing age groups"):
        _normalized_age_distribution({"child_1_6y": 2.0}, ("infant_0_2m", "child_1_6y", "adult_18plus"))
    with pytest.raises(ValueError, match="missing age groups"):
        _normalized_age_distribution({}, ("a", "b"))
    shares = _normalized_age_distribution(
        {"infant_0_2m": 0.0, "child_1_6y": 2.0, "adult_18plus": 0.0},
        ("infant_0_2m", "child_1_6y", "adult_18plus"),
    )
    assert shares.tolist() == [0.0, 1.0, 0.0]


def test_symptomatic_cases_are_counted_at_exposed_progression():
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    config["transmission"]["beta_S"] = 0.0
    config["transmission"]["beta_R"] = 0.0
    config["importation"]["enabled"] = False
    config["demography"]["enabled"] = False
    for record in config["age_groups"]:
        record["symptom_probability"] = 1.0
        record["reporting_rate"] = 1.0
    params = PreparedParameters.from_config(config, analysis="test", scenario="progression_cases")
    index = StateIndex(params.age_groups)
    state = np.zeros((index.n_age, index.n_compartments), dtype=float)
    c = {name: COMPARTMENTS.index(name) for name in COMPARTMENTS}
    state[0, c["S"]] = params.population[0] - 80.0
    state[0, c[exposed_name("S", "unvaccinated")]] = 80.0
    rows = _daily_metrics(0.0, index.flatten(state), params, index)
    first_age_sensitive = [
        row for row in rows if row["age_group"] == params.age_groups[0] and row["strain"] == "sensitive"
    ][0]
    assert np.isclose(first_age_sensitive["total_infection_rate_per_day"], 0.0)
    assert np.isclose(first_age_sensitive["symptomatic_case_rate_per_day"], 80.0 * params.rates["latent"])


def test_pep_activation_uses_full_observation_cascade():
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    config["PEP"]["coverage_household_contacts"] = 1.0
    config["PEP"]["activation_prevalence"] = 0.01
    config["observation_model"]["components"] = {
        "care_seeking_probability": 0.5,
        "testing_probability": 0.5,
        "test_reporting_probability": 0.5,
    }
    for record in config["age_groups"]:
        record["reporting_rate"] = 1.0
    params = PreparedParameters.from_config(config, analysis="test", scenario="pep_observation")
    index = StateIndex(params.age_groups)
    state = np.zeros((index.n_age, index.n_compartments), dtype=float)
    c = {name: COMPARTMENTS.index(name) for name in COMPARTMENTS}
    state[:, c["S"]] = params.population
    state[0, c["S"]] -= 100.0
    state[0, c[infectious_name("S", "sym", "unvaccinated")]] = 100.0
    foi = compute_force_of_infection(0.0, index.flatten(state), params, index)
    detected_prevalence = 100.0 * 0.125 / params.total_population
    expected_activation = detected_prevalence / (detected_prevalence + config["PEP"]["activation_prevalence"])
    assert np.isclose(float(foi["pep_coverage"]), expected_activation)


def test_importation_is_capped_by_available_source_pools():
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    config["transmission"]["beta_S"] = 0.0
    config["transmission"]["beta_R"] = 0.0
    config["demography"]["enabled"] = False
    config["routine_vaccination"]["enabled"] = False
    config.setdefault("rates", {})["waning_natural"] = 0.0
    config["importation"]["enabled"] = True
    config["importation"]["rate_per_100k_per_year"] = 1e9
    params = PreparedParameters.from_config(config, analysis="test", scenario="capped_importation")
    index = StateIndex(params.age_groups)
    state = np.zeros((index.n_age, index.n_compartments), dtype=float)
    c = {name: COMPARTMENTS.index(name) for name in COMPARTMENTS}
    state[:, c["R_natural"]] = params.population
    dy = rhs(0.0, index.flatten(state), params, index)
    assert np.isclose(float(dy.sum()), 0.0)
    assert np.allclose(dy.reshape(index.n_age, index.n_compartments)[:, c["R_natural"]], 0.0)


def test_burn_in_rebalances_resistance_to_analysis_start_target():
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="low", country_profile="Australia")
    config["simulation"]["burn_in_years"] = 2
    config["simulation"]["end_time"] = 28
    params = PreparedParameters.from_config(
        config,
        analysis="test",
        scenario="resistance_rebalance",
        vaccine_scenario="symptom_protective",
        resistance_scenario="low",
    )
    index = StateIndex(params.age_groups)
    solution = solve_model(params, index)
    assert solution.success
    assert np.isclose(active_resistant_fraction(solution.y[:, 0], index), 0.05, atol=1e-8)


def test_country_resistance_timeline_sets_country_specific_anchor():
    china = make_config(
        vaccine_scenario="symptom_protective",
        resistance_scenario="country_timeline",
        country_profile="China",
    )
    united_states = make_config(
        vaccine_scenario="symptom_protective",
        resistance_scenario="country_timeline",
        country_profile="United_States",
    )

    assert china["resistance"]["target_prevalence_at_analysis_start"] > 0.90
    assert united_states["resistance"]["target_prevalence_at_analysis_start"] <= 0.05
    assert china["importation"]["resistant_fraction"] == china["resistance"]["importation_fraction"]
    assert united_states["importation"]["resistant_fraction"] == united_states["resistance"]["importation_fraction"]
    assert china["resistance"]["prevalence_anchor_rate_per_year"] == 2.0
    assert not china["resistance"].get("anchor_during_dynamics", False)
    assert china["metadata"]["resistance_timeline_anchor_year"] == 2025
    assert not china["metadata"]["resistance_timeline_allows_future_evidence"]


def test_generic_resistance_scenario_is_not_replaced_by_country_timeline():
    config = make_config(
        vaccine_scenario="symptom_protective",
        resistance_scenario="moderate",
        country_profile="China",
    )
    assert np.isclose(config["resistance"]["target_prevalence_at_analysis_start"], 0.30)


def test_explicit_resistance_override_takes_precedence_over_country_timeline():
    config = make_config(
        vaccine_scenario="symptom_protective",
        resistance_scenario="country_timeline",
        country_profile="China",
        resistance_overrides={
            "target_prevalence_at_analysis_start": 0.40,
            "initial_resistance_prevalence": 0.40,
            "importation_fraction": 0.40,
        },
    )
    assert np.isclose(config["resistance"]["target_prevalence_at_analysis_start"], 0.40)
    assert np.isclose(config["importation"]["resistant_fraction"], 0.40)


def test_equal_strain_effects_do_not_drive_resistance_fixation():
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate", country_profile="Australia")
    config["simulation"]["burn_in_years"] = 1
    config["simulation"]["end_time"] = 365
    config["treatment"]["resistant"] = dict(config["treatment"]["sensitive"])
    config["PEP"]["effectiveness_resistant"] = config["PEP"]["effectiveness_sensitive"]
    config["transmission"]["fitness_R"] = 1.0
    config["importation"]["resistant_fraction"] = 0.30
    config["resistance"]["importation_fraction"] = 0.30
    _, summary = run_prepared_config(
        config,
        analysis="test",
        scenario="neutral_resistance",
        vaccine_scenario="symptom_protective",
        resistance_scenario="moderate",
    )
    assert float(summary["resistant_fraction_end"].iloc[0]) < 0.90
    assert np.isclose(float(summary["resistant_fraction_start"].iloc[0]), 0.30, atol=0.05)


def test_intervention_config_burns_in_under_current_practice_baseline():
    config, _ = make_intervention_config("higher_child_coverage", country_profile="China")
    assert "burn_in_config" in config
    intervention_coverage = {
        record["label"]: float(record["vaccine_coverage"])
        for record in config["age_groups"]
    }
    burn_in_coverage = {
        record["label"]: float(record["vaccine_coverage"])
        for record in config["burn_in_config"]["age_groups"]
    }
    assert intervention_coverage["child_1_6y"] > burn_in_coverage["child_1_6y"]
    assert config["metadata"]["burn_in_parameterization"] == "current_practice_baseline"


def test_contact_matrix_reciprocity_correction_balances_population_flows():
    matrix = np.array([[4.0, 8.0], [1.0, 3.0]])
    population = np.array([100.0, 1000.0])
    corrected = balance_reciprocity(matrix, population)
    assert reciprocity_error(matrix, population) > 0.0
    assert reciprocity_error(corrected, population) < 1e-12


def test_calibration_vector_updates_declared_parameters():
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate", country_profile="Australia")
    vector = initial_calibration_vector(config)
    vector[0] = np.log(0.041)
    vector[1] = np.log(1.25)
    updated = apply_calibration_vector(config, vector)
    assert np.isclose(updated["transmission"]["beta_S"], 0.041)
    assert np.isclose(updated["reporting_multiplier"], 1.25)
    assert updated["importation"]["resistant_fraction"] == updated["resistance"]["importation_fraction"]


def test_config_overrides_have_final_precedence_after_country_profile():
    config = make_config(
        vaccine_scenario="symptom_protective",
        resistance_scenario="moderate",
        country_profile="China",
        config_overrides={"country": "ManualOverride"},
    )
    assert config["country"] == "ManualOverride"


def test_invalid_probability_inputs_are_rejected():
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    config["age_groups"][0]["reporting_rate"] = 1.2
    with pytest.raises(ValueError, match="reporting rate"):
        PreparedParameters.from_config(config, analysis="test", scenario="bad_reporting")


def test_invalid_treatment_and_pep_inputs_are_rejected():
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    config["treatment"]["sensitive"]["infectiousness_reduction"] = 1.2
    with pytest.raises(ValueError, match="treatment reductions"):
        PreparedParameters.from_config(config, analysis="test", scenario="bad_treatment")

    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    config["PEP"]["activation_prevalence"] = 0.0
    with pytest.raises(ValueError, match="PEP activation prevalence"):
        PreparedParameters.from_config(config, analysis="test", scenario="bad_pep")


def test_calibration_alignment_uses_overlapping_years_without_mean_collapse():
    predicted = np.array([10.0, 20.0, 30.0])
    predicted_df = np.rec.fromarrays(([2021, 2022, 2023], predicted), names=("year", "reported_cases"))
    observed_df = np.rec.fromarrays(([2022, 2023, 2024], [200.0, 300.0, 400.0]), names=("year", "reported_cases"))
    observed, aligned_predicted = align_annual_reported_cases(
        pytest.importorskip("pandas").DataFrame.from_records(predicted_df),
        pytest.importorskip("pandas").DataFrame.from_records(observed_df),
    )
    assert observed.tolist() == [200.0, 300.0]
    assert aligned_predicted.tolist() == [20.0, 30.0]


def test_infant_annualized_incidence_uses_infant_population_denominator():
    pd = pytest.importorskip("pandas")
    rows = []
    for t in [0.0, 365.0]:
        for age, population in [
            ("infant_0_2m", 400.0),
            ("infant_3_11m", 600.0),
            ("adult_18plus", 9000.0),
        ]:
            for strain in ["sensitive", "resistant"]:
                infant_cases = 25.0 if t == 365.0 and age.startswith("infant") and strain == "sensitive" else 0.0
                rows.append(
                    {
                        "analysis": "test",
                        "scenario": "infant_denominator",
                        "vaccine_scenario": "",
                        "resistance_scenario": "",
                        "intervention": "",
                        "time": t,
                        "age_group": age,
                        "strain": strain,
                        "population": population,
                        "total_population": 10000.0,
                        "total_infections": 0.0,
                        "total_infection_rate_per_day": 0.0,
                        "symptomatic_cases": infant_cases,
                        "symptomatic_case_rate_per_day": 0.0,
                        "asymptomatic_infections": 0.0,
                        "reported_cases": infant_cases,
                        "reported_case_rate_per_day": 0.0,
                        "infant_cases": infant_cases,
                        "infant_infections": 0.0,
                        "treated_cases": 0.0,
                        "PEP_averted_cases": 0.0,
                    }
                )
    summary = summarize_timeseries(pd.DataFrame(rows))
    assert np.isclose(float(summary["infant_population"].iloc[0]), 1000.0)
    assert np.isclose(float(summary["annualized_infant_cases_per_100k"].iloc[0]), 5000.0)


def test_missing_run_metadata_is_rejected():
    with pytest.raises(FileNotFoundError):
        validate_run_metadata("__missing_test_output__")


def test_legacy_yaml_mirrors_runtime_config_source():
    runtime = load_yaml(project_path("config/model_settings.yaml"))["runtime"]
    mirrors = {
        "baseline_parameters.yaml": "baseline_parameters",
        "vaccine_scenarios.yaml": "vaccine_scenarios",
        "resistance_scenarios.yaml": "resistance_scenarios",
        "intervention_scenarios.yaml": "intervention_scenarios",
        "sensitivity_parameters.yaml": "sensitivity_parameters",
        "data_sources.yaml": "data_sources",
    }
    for filename, key in mirrors.items():
        assert load_yaml(project_path("config", filename)) == runtime[key]
