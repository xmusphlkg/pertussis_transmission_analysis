from __future__ import annotations

import numpy as np
import pandas as pd

from src_python.model.compartments import StateIndex
from src_python.model.outputs import initial_state, solve_model
from src_python.model.parameters import PreparedParameters
from src_python.simulation.common import make_config, run_prepared_config
from src_python.utils.io import project_path, read_table


EXPECTED_TIMESERIES_COLUMNS = {
    "time",
    "age_group",
    "strain",
    "scenario",
    "symptomatic_cases",
    "asymptomatic_infections",
    "total_infections",
    "reported_cases",
    "infant_cases",
    "infant_infections",
    "resistant_fraction",
    "treated_cases",
    "PEP_averted_cases",
    "effective_reproduction_proxy",
    "cumulative_cases",
    "cumulative_infections",
}


def validate_timeseries(df: pd.DataFrame) -> None:
    missing = EXPECTED_TIMESERIES_COLUMNS.difference(df.columns)
    if missing:
        raise AssertionError(f"Missing expected output columns: {sorted(missing)}")
    numeric = df.select_dtypes(include=["number"])
    if not np.isfinite(numeric.to_numpy()).all():
        raise AssertionError("Timeseries contains NaN or infinite values.")

    nonnegative_cols = [
        "symptomatic_cases",
        "asymptomatic_infections",
        "total_infections",
        "reported_cases",
        "infant_cases",
        "infant_infections",
        "treated_cases",
        "PEP_averted_cases",
        "cumulative_cases",
        "cumulative_infections",
    ]
    min_value = float(df[nonnegative_cols].min().min())
    if min_value < -1e-8:
        raise AssertionError(f"Negative model output detected: {min_value}")
    if (df["reported_cases"] - df["symptomatic_cases"] > 1e-8).any():
        raise AssertionError("Reported cases exceed symptomatic infections.")
    if not df["resistant_fraction"].between(-1e-8, 1.0 + 1e-8).all():
        raise AssertionError("Resistant fraction is outside [0, 1].")


def validate_population_conservation() -> None:
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    params = PreparedParameters.from_config(
        config,
        analysis="validation",
        scenario="population_conservation",
        vaccine_scenario="symptom_protective",
        resistance_scenario="moderate",
    )
    index = StateIndex(params.age_groups)
    y0 = initial_state(params, index)
    solution = solve_model(params, index)
    if not solution.success:
        raise AssertionError(solution.message)
    totals = solution.y.reshape(index.n_age, index.n_compartments, -1).sum(axis=(0, 1))
    expected = float(index.reshape(y0).sum())
    max_abs_error = float(np.max(np.abs(totals - expected)))
    tolerance = max(1e-4, expected * 1e-8)
    if max_abs_error > tolerance:
        raise AssertionError(f"Population is not conserved; max error={max_abs_error}")
    if solution.y.min() < -1e-5:
        raise AssertionError(f"Negative compartment value detected: {solution.y.min()}")


def validate_baseline_outputs() -> None:
    path = project_path("outputs/simulations/baseline_timeseries.parquet")
    try:
        df = read_table(path)
    except FileNotFoundError:
        df, _ = run_prepared_config(
            make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate"),
            analysis="baseline",
            scenario="baseline",
            vaccine_scenario="symptom_protective",
            resistance_scenario="moderate",
        )
    validate_timeseries(df)


def main() -> None:
    validate_population_conservation()
    validate_baseline_outputs()
    print("Validation checks passed.")


if __name__ == "__main__":
    main()
