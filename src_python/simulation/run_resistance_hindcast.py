"""Resistance hindcast validation.

For countries with multiple time-point resistance observations (China, Japan,
Australia), this module initializes the model at an earlier resistance prevalence
and simulates forward to check whether the model can reproduce the observed
trajectory under plausible fitness/importation/treatment assumptions.

This addresses the concern that near-fixation in the model may be a structural
artifact rather than a mechanistically supported outcome.

Usage:
    python -m src_python.simulation.run_resistance_hindcast
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import date, datetime

import numpy as np
import pandas as pd

from src_python.simulation.common import (
    load_configs,
    make_config,
    run_prepared_config,
    write_outputs,
    execute_scenario_list,
    add_relative_reductions,
)
from src_python.utils.io import project_path, write_dataframe


# Countries with at least 2 time-point resistance observations
HINDCAST_COUNTRIES = {
    "China": {
        "init_year": 2016,
        "init_resistance": 0.364,
        "observations": [
            {"year": 2022, "fraction": 0.972, "lower": 0.94, "upper": 0.99},
            {"year": 2024, "fraction": 0.997, "lower": 0.986, "upper": 1.0},
        ],
        "hindcast_years": 9,  # 2016 -> 2025
    },
    "Japan": {
        "init_year": 2024,
        "init_resistance": 0.875,
        "observations": [
            {"year": 2025, "fraction": 0.827, "lower": 0.697, "upper": 0.918},
        ],
        "hindcast_years": 2,  # 2024 -> 2026
    },
    "Australia": {
        "init_year": 2024,
        "init_resistance": 0.043,
        "observations": [
            # Only one time point available; use as endpoint check
            {"year": 2024, "fraction": 0.043, "lower": 0.019, "upper": 0.082},
        ],
        "hindcast_years": 3,  # Short forward projection to check stability
    },
}

# Fitness values to sweep for each country
FITNESS_VALUES = [0.85, 0.90, 0.95, 1.00, 1.05, 1.10]


def _make_hindcast_config(
    country: str,
    init_resistance: float,
    hindcast_years: int,
    fitness_R: float,
    init_year: int,
) -> dict:
    """Build a config for hindcast validation with shortened horizon."""
    config = make_config(
        vaccine_scenario="symptom_protective",
        resistance_scenario="moderate",
        country_profile=country,
        load_calibration=True,
        config_overrides={
            "resistance": {
                "target_prevalence_at_analysis_start": init_resistance,
                "importation_fraction": init_resistance,
                "rebalance_after_burn_in": True,
                "prevalence_anchor_rate_per_year": 2.0,
                "anchor_during_dynamics": False,
            },
            "importation": {
                "resistant_fraction": init_resistance,
            },
            "initial_conditions": {
                "initial_resistance_prevalence": init_resistance,
            },
            "transmission": {
                "fitness_R": fitness_R,
            },
            "simulation": {
                "end_time": hindcast_years * 365,
                "burn_in_years": 10,
                "output_time_step": 30,
            },
            "calendar": {
                "enabled": True,
                "analysis_start_date": f"{init_year}-01-01",
                "analysis_end_date": f"{init_year + hindcast_years}-12-31",
            },
        },
    )
    return config


def run_country_hindcast(country: str) -> pd.DataFrame:
    """Run hindcast for a single country across fitness values."""
    spec = HINDCAST_COUNTRIES[country]
    results = []

    for fitness_R in FITNESS_VALUES:
        config = _make_hindcast_config(
            country=country,
            init_resistance=spec["init_resistance"],
            hindcast_years=spec["hindcast_years"],
            fitness_R=fitness_R,
            init_year=spec["init_year"],
        )

        ts, summary = run_prepared_config(
            config,
            analysis="resistance_hindcast",
            scenario=f"fitness_{fitness_R:.2f}",
            vaccine_scenario="symptom_protective",
            resistance_scenario="hindcast",
        )

        # Extract end-of-year resistant fractions from timeseries
        if "calendar_year" in ts.columns and "resistant_fraction" in ts.columns:
            annual = (
                ts.groupby("calendar_year")["resistant_fraction"]
                .mean()
                .reset_index()
            )
        elif "time" in ts.columns and "resistant_fraction" in ts.columns:
            ts = ts.copy()
            ts["sim_year"] = spec["init_year"] + ts["time"] / 365.0
            annual = (
                ts.assign(calendar_year=ts["sim_year"].astype(int))
                .groupby("calendar_year")["resistant_fraction"]
                .mean()
                .reset_index()
            )
        else:
            annual = pd.DataFrame(columns=["calendar_year", "resistant_fraction"])

        for _, row in annual.iterrows():
            results.append({
                "country": country,
                "fitness_R": fitness_R,
                "calendar_year": int(row["calendar_year"]),
                "model_resistant_fraction": float(row["resistant_fraction"]),
                "init_year": spec["init_year"],
                "init_resistance": spec["init_resistance"],
            })

    df = pd.DataFrame(results)

    # Add observed data points for comparison
    obs_rows = []
    for obs in spec["observations"]:
        obs_rows.append({
            "country": country,
            "year": obs["year"],
            "observed_fraction": obs["fraction"],
            "observed_lower": obs["lower"],
            "observed_upper": obs["upper"],
        })
    obs_df = pd.DataFrame(obs_rows)

    # Merge observed onto model results
    if not df.empty and not obs_df.empty:
        df = df.merge(
            obs_df.rename(columns={"year": "calendar_year"}),
            on=["country", "calendar_year"],
            how="left",
        )

    return df


def _score_hindcast(df: pd.DataFrame) -> pd.DataFrame:
    """Score each fitness scenario by how well it matches observations."""
    scored = df.dropna(subset=["observed_fraction"]).copy()
    if scored.empty:
        return pd.DataFrame()

    scored["absolute_error"] = (
        scored["model_resistant_fraction"] - scored["observed_fraction"]
    ).abs()
    scored["within_ci"] = (
        (scored["model_resistant_fraction"] >= scored["observed_lower"])
        & (scored["model_resistant_fraction"] <= scored["observed_upper"])
    )

    summary = (
        scored.groupby(["country", "fitness_R"])
        .agg(
            mean_absolute_error=("absolute_error", "mean"),
            max_absolute_error=("absolute_error", "max"),
            observations_within_ci=("within_ci", "sum"),
            total_observations=("within_ci", "count"),
        )
        .reset_index()
    )
    summary["fraction_within_ci"] = (
        summary["observations_within_ci"] / summary["total_observations"]
    )
    return summary.sort_values(["country", "mean_absolute_error"])


def main() -> None:
    parser = argparse.ArgumentParser(description="Run resistance hindcast validation.")
    parser.add_argument(
        "--countries",
        nargs="*",
        default=None,
        help="Subset of countries to hindcast (default: all available).",
    )
    args = parser.parse_args()

    countries = args.countries or list(HINDCAST_COUNTRIES.keys())
    countries = [c for c in countries if c in HINDCAST_COUNTRIES]

    all_results = []
    for country in countries:
        print(f"Running resistance hindcast for {country}...")
        df = run_country_hindcast(country)
        all_results.append(df)

    if all_results:
        combined = pd.concat(all_results, ignore_index=True)
        output_path = project_path("outputs/tables/resistance_hindcast_results.csv")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        write_dataframe(combined, output_path)

        # Score and write summary
        scores = _score_hindcast(combined)
        if not scores.empty:
            score_path = project_path("outputs/tables/resistance_hindcast_scores.csv")
            write_dataframe(scores, score_path)
            print("\nHindcast scoring summary:")
            print(scores.to_string(index=False))

        # Write interpretation
        _write_interpretation(scores, combined)
    else:
        print("No hindcast results generated.")


def _write_interpretation(scores: pd.DataFrame, results: pd.DataFrame) -> None:
    """Write a brief interpretation of hindcast results."""
    lines = [
        "# Resistance Hindcast Validation Summary",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Purpose",
        "",
        "This validation checks whether the model's resistance dynamics can",
        "reproduce observed resistance trajectories when initialized at an",
        "earlier time point. If the model cannot match observations under any",
        "plausible fitness value, the near-fixation results should be reported",
        "as stress tests rather than predictions.",
        "",
        "## Results by Country",
        "",
    ]

    if not scores.empty:
        for country in scores["country"].unique():
            country_scores = scores[scores["country"] == country]
            best = country_scores.iloc[0]
            lines.append(f"### {country}")
            lines.append("")
            lines.append(f"- Best fitness_R: {best['fitness_R']:.2f}")
            lines.append(f"- Mean absolute error: {best['mean_absolute_error']:.4f}")
            lines.append(f"- Observations within CI: {int(best['observations_within_ci'])}/{int(best['total_observations'])}")
            lines.append("")

            if best["fraction_within_ci"] >= 0.5:
                lines.append(f"  → Model CAN reproduce observed trajectory at fitness_R={best['fitness_R']:.2f}")
            else:
                lines.append(f"  → Model CANNOT reproduce observed trajectory under tested fitness values.")
                lines.append(f"    Near-fixation results for {country} should be reported as STRESS TEST only.")
            lines.append("")
    else:
        lines.append("No scored observations available.")

    lines.extend([
        "## Interpretation for Manuscript",
        "",
        "Countries where the model reproduces the observed resistance trajectory",
        "can support calibrated resistance projections. Countries where it cannot",
        "should have their resistance results framed as 'under the neutral-fitness",
        "scenario' rather than as predictions.",
        "",
    ])

    output_path = project_path("outputs/tables/resistance_hindcast_interpretation.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
