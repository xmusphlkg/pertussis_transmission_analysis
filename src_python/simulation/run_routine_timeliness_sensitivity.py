from __future__ import annotations

import argparse
from copy import deepcopy
from typing import Any

import numpy as np
import pandas as pd

from src_python.simulation.common import (
    load_configs,
    make_intervention_config,
    run_scenario_list,
)
from src_python.utils.io import project_path, write_dataframe


TIMELINESS_RATE_PER_YEAR = 6.0
TIMELINESS_MAX_DAILY_FLOW_FRACTION = 0.03

TIMELINESS_TARGET_DISTRIBUTION = {
    "infant_3_11m": {"dose1_recent": 0.10, "dose2_recent": 0.30, "recent": 0.60},
    "child_1_4y": {"recent": 0.80, "waned": 0.20},
    "child_5_9y": {"recent": 0.65, "waned": 0.35},
}

SCENARIO_DEFINITIONS = (
    (
        "current",
        "current",
        False,
        "Current practice with country-profile routine coverage and default age-bin vaccine-origin timing.",
    ),
    (
        "coverage_floor_only",
        "higher_child_coverage",
        False,
        "Coverage-floor-only scenario used in the main intervention comparison.",
    ),
    (
        "timeliness_only",
        "current",
        True,
        "Current coverage with faster routine-vaccination relaxation and earlier infant/child vaccine-origin targets.",
    ),
    (
        "coverage_floor_plus_timeliness",
        "higher_child_coverage",
        True,
        "Coverage floor plus faster routine-vaccination relaxation and earlier infant/child vaccine-origin targets.",
    ),
)


def _set_summary_runtime(config: dict[str, Any]) -> dict[str, Any]:
    out = deepcopy(config)
    out["simulation"]["output_time_step"] = 30.0
    out["simulation"]["rtol"] = max(float(out["simulation"].get("rtol", 1e-5)), 1e-4)
    out["simulation"]["atol"] = max(float(out["simulation"].get("atol", 1e-7)), 1e-6)
    return out


def _apply_timeliness(config: dict[str, Any]) -> dict[str, Any]:
    out = deepcopy(config)
    routine = out.setdefault("routine_vaccination", {})
    routine["target_relaxation_rate_per_year"] = max(
        float(routine.get("target_relaxation_rate_per_year", 0.0)),
        TIMELINESS_RATE_PER_YEAR,
    )
    routine["max_daily_flow_fraction"] = max(
        float(routine.get("max_daily_flow_fraction", 0.0)),
        TIMELINESS_MAX_DAILY_FLOW_FRACTION,
    )
    target_by_age = deepcopy(routine.get("target_origin_distribution_by_age", {}))
    for age_group, distribution in TIMELINESS_TARGET_DISTRIBUTION.items():
        target_by_age[age_group] = deepcopy(distribution)
    routine["target_origin_distribution_by_age"] = target_by_age
    return out


def _build_scenarios(configs: dict[str, Any]) -> list[dict[str, Any]]:
    scenarios: list[dict[str, Any]] = []
    resistance_name = configs["baseline"].get("baseline_resistance_scenario", "country_timeline")
    for country in configs["countries"]:
        for scenario_name, intervention_name, apply_timeliness, note in SCENARIO_DEFINITIONS:
            config, vaccine_name = make_intervention_config(intervention_name, country_profile=country)
            if apply_timeliness:
                config = _apply_timeliness(config)
            config = _set_summary_runtime(config)
            scenarios.append(
                {
                    "config": config,
                    "analysis": "routine_timeliness_sensitivity",
                    "scenario": scenario_name,
                    "vaccine_scenario": vaccine_name,
                    "resistance_scenario": resistance_name,
                    "intervention": intervention_name,
                    "metadata": {
                        "country": country,
                        "strategy": scenario_name,
                        "coverage_floor_applied": intervention_name == "higher_child_coverage",
                        "timeliness_applied": bool(apply_timeliness),
                        "timeliness_rate_per_year": TIMELINESS_RATE_PER_YEAR if apply_timeliness else np.nan,
                        "timeliness_max_daily_flow_fraction": (
                            TIMELINESS_MAX_DAILY_FLOW_FRACTION if apply_timeliness else np.nan
                        ),
                        "implementation_note": note,
                    },
                }
            )
    return scenarios


def _summarize(summary: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    data = summary.copy()
    data["strategy"] = data.get("strategy", data["scenario"])
    data["annualized_infant_cases_per_100k"] = pd.to_numeric(
        data["annualized_infant_cases_per_100k"],
        errors="coerce",
    )
    data["relative_reduction_infant_cases"] = pd.to_numeric(
        data["relative_reduction_infant_cases"],
        errors="coerce",
    )
    data["relative_reduction_total_infections"] = pd.to_numeric(
        data["relative_reduction_total_infections"],
        errors="coerce",
    )
    current_by_country = (
        data.loc[data["strategy"].eq("current"), ["country", "annualized_infant_cases_per_100k"]]
        .rename(columns={"annualized_infant_cases_per_100k": "current_infant_cases_per_100k"})
    )
    country = data.merge(current_by_country, on="country", how="left")
    country = country[
        [
            "country",
            "strategy",
            "current_infant_cases_per_100k",
            "annualized_infant_cases_per_100k",
            "relative_reduction_infant_cases",
            "relative_reduction_total_infections",
            "coverage_floor_applied",
            "timeliness_applied",
            "implementation_note",
        ]
    ].rename(columns={"annualized_infant_cases_per_100k": "scenario_infant_cases_per_100k"})

    rows: list[dict[str, Any]] = []
    for strategy, group in country.groupby("strategy", sort=False):
        reductions = pd.to_numeric(group["relative_reduction_infant_cases"], errors="coerce")
        infections = pd.to_numeric(group["relative_reduction_total_infections"], errors="coerce")
        scenario_cases = pd.to_numeric(group["scenario_infant_cases_per_100k"], errors="coerce")
        current_cases = pd.to_numeric(group["current_infant_cases_per_100k"], errors="coerce")
        first = group.iloc[0]
        rows.append(
            {
                "strategy": strategy,
                "coverage_floor_applied": bool(first.get("coverage_floor_applied", False)),
                "timeliness_applied": bool(first.get("timeliness_applied", False)),
                "median_current_infant_cases_per_100k": float(current_cases.median(skipna=True)),
                "median_scenario_infant_cases_per_100k": float(scenario_cases.median(skipna=True)),
                "median_relative_reduction_infant_cases": float(reductions.median(skipna=True)),
                "iqr_relative_reduction_infant_cases": (
                    f"{reductions.quantile(0.25):.4g} to {reductions.quantile(0.75):.4g}"
                ),
                "countries_with_positive_reduction": int((reductions > 0.0).sum()),
                "median_relative_reduction_total_infections": float(infections.median(skipna=True)),
                "countries": int(group["country"].nunique()),
                "implementation_note": first.get("implementation_note", ""),
            }
        )
    table = pd.DataFrame(rows)
    return table, country


def main(n_jobs: int | None = None) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    configs = load_configs()
    timeseries, summary = run_scenario_list(
        _build_scenarios(configs),
        stem="routine_timeliness_sensitivity",
        reference_scenario="current",
        n_jobs=n_jobs,
    )
    table, country = _summarize(summary)
    write_dataframe(table, project_path("outputs", "tables", "routine_timeliness_sensitivity.csv"))
    write_dataframe(country, project_path("outputs", "tables", "routine_timeliness_sensitivity_country.csv"))
    return timeseries, summary, table, country


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run routine coverage-floor and timeliness sensitivity scenarios.")
    parser.add_argument("--n-jobs", type=int, default=None)
    args = parser.parse_args()
    main(n_jobs=args.n_jobs)
