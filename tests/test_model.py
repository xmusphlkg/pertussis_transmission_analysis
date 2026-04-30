from __future__ import annotations

import numpy as np

from src_python.model.compartments import StateIndex
from src_python.model.outputs import initial_state, solve_model
from src_python.model.parameters import PreparedParameters
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
