from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from src_python.model.compartments import COMPARTMENTS, VACCINE_ORIGINS, StateIndex, exposed_name, infectious_name
from src_python.model.contact_matrix import balance_reciprocity, reciprocity_error
from src_python.model.outputs import active_resistant_fraction, initial_state, solve_model
from src_python.model.parameters import PreparedParameters
from src_python.calibration.calibrate_baseline import (
    apply_calibration_vector,
    initial_calibration_vector,
    observed_annual_cases,
    reporting_rate_prior_penalty,
)
from src_python.simulation.common import add_relative_reductions, load_configs, make_config, run_prepared_config, validate_run_metadata
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


def test_reporting_rate_prior_penalty_is_zero_at_baseline_and_positive_when_shifted():
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate", country_profile="Australia")
    assert np.isclose(reporting_rate_prior_penalty(config), 0.0)

    config["reporting_multiplier"] = 1.5
    assert reporting_rate_prior_penalty(config) > 0.0


def test_calibration_observed_cases_respects_surveillance_year():
    configs = load_configs()
    surveillance_year = int(configs["data_sources"]["surveillance_year"])
    who = pd.read_csv(project_path("data/processed/who_pertussis_reported_cases.csv"))
    expected_years = who.loc[(who["config_key"].eq("Australia")) & (who["year"].le(surveillance_year)), "year"].nunique()

    observed = observed_annual_cases("Australia")
    assert observed.shape[0] == expected_years


def test_country_profiles_carry_reporting_prior_bands_into_runtime_config():
    configs = load_configs()["countries"]
    australia_prior = configs["Australia"]["reporting_rate_prior"]
    sweden_prior = configs["Sweden"]["reporting_rate_prior"]

    assert australia_prior["method"] == "literature_range"
    assert sweden_prior["evidence_class"] == "direct_preschool_anchor"
    assert australia_prior["age_groups"]["infant_0_2m"]["lower"] < 0.60 < australia_prior["age_groups"]["infant_0_2m"]["upper"]
    assert sweden_prior["age_groups"]["child_1_6y"]["lower"] > australia_prior["age_groups"]["child_1_6y"]["lower"]

    runtime = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate", country_profile="Sweden")
    assert runtime["reporting_rate_prior"]["method"] == "literature_range"
    assert runtime["reporting_rate_prior"]["note"]


def test_missing_run_metadata_is_rejected():
    with pytest.raises(FileNotFoundError):
        validate_run_metadata("__missing_test_output__")


def test_relative_reductions_fall_back_to_global_reference_when_needed():
    summary = pd.DataFrame(
        {
            "country": ["Australia", "China"],
            "scenario": ["Australia", "China"],
            "total_infant_cases": [10.0, 20.0],
            "total_infections": [100.0, 200.0],
            "total_reported_cases": [5.0, 10.0],
            "resistant_infections": [0.0, 0.0],
        }
    )

    reduced = add_relative_reductions(summary, reference_scenario="China")

    australia = reduced.loc[reduced["country"].eq("Australia")].iloc[0]
    china = reduced.loc[reduced["country"].eq("China")].iloc[0]
    assert np.isclose(australia["relative_reduction_total_infections"], 0.5)
    assert np.isclose(china["relative_reduction_total_infections"], 0.0)
    assert np.isnan(australia["relative_reduction_resistant_infections"])


def test_relative_reductions_group_by_country_when_reference_exists_per_country():
    summary = pd.DataFrame(
        {
            "country": ["A", "A", "B", "B"],
            "scenario": ["current", "improved", "current", "improved"],
            "total_infant_cases": [10.0, 5.0, 20.0, 5.0],
            "total_infections": [100.0, 50.0, 200.0, 50.0],
            "total_reported_cases": [8.0, 4.0, 16.0, 4.0],
            "resistant_infections": [2.0, 1.0, 4.0, 1.0],
        }
    )

    reduced = add_relative_reductions(summary, reference_scenario="current")

    improved_a = reduced.loc[reduced["country"].eq("A") & reduced["scenario"].eq("improved")].iloc[0]
    improved_b = reduced.loc[reduced["country"].eq("B") & reduced["scenario"].eq("improved")].iloc[0]
    assert np.isclose(improved_a["relative_reduction_total_infections"], 0.5)
    assert np.isclose(improved_b["relative_reduction_total_infections"], 0.75)


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


def test_waning_durations_are_reported_as_sensitivity_parameters():
    table = pd.read_csv(project_path("manuscript_notes/parameter_table.csv")).set_index("parameter")
    for parameter in [
        "natural_history.recovered_immunity_duration",
        "natural_history.vaccine_protection_duration",
    ]:
        assert bool(table.loc[parameter, "used_in_sensitivity_analysis"])
        assert "reciprocal of" in str(table.loc[parameter, "range"])
