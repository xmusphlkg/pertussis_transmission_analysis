from __future__ import annotations

import numpy as np

from src_python.model.compartments import StateIndex
from src_python.model.contact_matrix import balance_reciprocity, reciprocity_error
from src_python.model.outputs import active_resistant_fraction, initial_state, solve_model
from src_python.model.parameters import PreparedParameters
from src_python.calibration.calibrate_baseline import apply_calibration_vector, initial_calibration_vector
from src_python.simulation.common import make_config, run_prepared_config
from src_python.utils.validation import validate_timeseries


def _baseline_params() -> PreparedParameters:
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
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


def test_timeseries_has_valid_epidemiological_columns():
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    timeseries, _ = run_prepared_config(
        config,
        analysis="test",
        scenario="baseline",
        vaccine_scenario="symptom_protective",
        resistance_scenario="moderate",
    )
    validate_timeseries(timeseries)


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
