from __future__ import annotations

import argparse
from copy import deepcopy
from typing import Any

import numpy as np
import pandas as pd
from scipy.optimize import minimize

from src_python.calibration.likelihood import negative_binomial_nll
from src_python.simulation.common import load_configs, make_config, run_prepared_config
from src_python.utils.io import project_path, write_dataframe


def _logit(x: float) -> float:
    x = float(np.clip(x, 1e-6, 1.0 - 1e-6))
    return float(np.log(x / (1.0 - x)))


def _inv_logit(x: float) -> float:
    return float(1.0 / (1.0 + np.exp(-x)))


def apply_calibration_vector(config: dict[str, Any], vector: np.ndarray) -> dict[str, Any]:
    beta_s = float(np.exp(vector[0]))
    reporting_multiplier = float(np.exp(vector[1]))
    seasonal_amplitude = float(0.35 * _inv_logit(vector[2]))
    importation_rate = float(np.exp(vector[3]))
    importation_fraction = float(_inv_logit(vector[4]))

    out = deepcopy(config)
    out["transmission"]["beta_S"] = beta_s
    out["transmission"]["seasonal_amplitude"] = seasonal_amplitude
    out["reporting_multiplier"] = reporting_multiplier
    out["importation"]["rate_per_100k_per_year"] = importation_rate
    out["resistance"]["importation_fraction"] = importation_fraction
    out["importation"]["resistant_fraction"] = importation_fraction
    return out


def initial_calibration_vector(config: dict[str, Any]) -> np.ndarray:
    return np.array(
        [
            np.log(float(config["transmission"]["beta_S"])),
            np.log(float(config["reporting_multiplier"])),
            _logit(float(config["transmission"]["seasonal_amplitude"]) / 0.35),
            np.log(float(config["importation"]["rate_per_100k_per_year"])),
            _logit(float(config["importation"]["resistant_fraction"])),
        ],
        dtype=float,
    )


def annual_reported_cases(timeseries: pd.DataFrame, *, analysis_year: int | None = None) -> pd.DataFrame:
    out = timeseries.copy()
    out["simulation_year"] = np.floor((out["time"] - float(out["time"].min())) / 365.0).astype(int)
    annual = out.groupby("simulation_year", as_index=False).agg(reported_cases=("reported_cases", "sum"))
    if analysis_year is not None and not annual.empty:
        first_calendar_year = int(analysis_year) - int(annual["simulation_year"].max())
        annual["year"] = first_calendar_year + annual["simulation_year"].astype(int)
    return annual


def observed_annual_cases_table(country: str) -> pd.DataFrame:
    who_path = project_path("data/processed/who_pertussis_reported_cases.csv")
    if who_path.exists():
        who = pd.read_csv(who_path)
        who_country = who.loc[who["config_key"].eq(country)].copy()
        if not who_country.empty:
            who_country["reported_cases"] = pd.to_numeric(who_country["reported_cases"], errors="coerce")
            observed = who_country.dropna(subset=["reported_cases"]).sort_values("year")
            if not observed.empty:
                return observed[["year", "reported_cases"]].assign(year=lambda df: df["year"].astype(int))

    path = project_path("data/processed/pertussis_incidence_timeseries.csv")
    observed = pd.read_csv(path)
    observed = observed.loc[observed["config_key"].eq(country)].copy()
    if observed.empty:
        raise ValueError(f"No processed observed pertussis time series found for {country}.")
    observed["Cases"] = pd.to_numeric(observed["Cases"], errors="coerce").fillna(0.0)
    annual = observed.groupby("Year", as_index=False)["Cases"].sum()
    return annual.rename(columns={"Year": "year", "Cases": "reported_cases"}).assign(
        year=lambda df: df["year"].astype(int)
    )


def observed_annual_cases(country: str) -> np.ndarray:
    return observed_annual_cases_table(country)["reported_cases"].to_numpy(dtype=float)


def align_annual_reported_cases(
    predicted: pd.DataFrame,
    observed: pd.DataFrame,
) -> tuple[np.ndarray, np.ndarray]:
    if "year" not in predicted.columns:
        raise ValueError("Predicted annual cases must include a calendar 'year' column.")
    predicted_aligned = predicted[["year", "reported_cases"]].rename(columns={"reported_cases": "predicted"})
    observed_aligned = observed[["year", "reported_cases"]].rename(columns={"reported_cases": "observed"})
    merged = predicted_aligned.merge(observed_aligned, on="year", how="inner").sort_values("year")
    if merged.empty:
        raise ValueError("No overlapping calendar years between simulated and observed calibration series.")
    return (
        merged["observed"].to_numpy(dtype=float),
        merged["predicted"].to_numpy(dtype=float),
    )


def calibration_objective(vector: np.ndarray, base_config: dict[str, Any], country: str, dispersion: float) -> float:
    config = apply_calibration_vector(base_config, vector)
    timeseries, _ = run_prepared_config(
        config,
        analysis="calibration",
        scenario="candidate",
        vaccine_scenario=base_config["baseline_vaccine_scenario"],
        resistance_scenario=base_config["baseline_resistance_scenario"],
        metadata={"country": country},
    )
    analysis_year = int(base_config["metadata"]["analysis_year"])
    predicted_annual = annual_reported_cases(timeseries, analysis_year=analysis_year)
    observed_annual = observed_annual_cases_table(country)
    observed, predicted = align_annual_reported_cases(predicted_annual, observed_annual)
    return negative_binomial_nll(observed, predicted, dispersion=dispersion)


def calibrate_country(country: str, *, maxiter: int | None = None) -> tuple[dict[str, Any], pd.DataFrame]:
    configs = load_configs()
    calibration = configs["baseline"]["calibration"]
    dispersion = float(calibration["dispersion"])
    config = make_config(
        vaccine_scenario=configs["baseline"]["baseline_vaccine_scenario"],
        resistance_scenario=configs["baseline"]["baseline_resistance_scenario"],
        country_profile=country,
    )
    candidate_start = initial_calibration_vector(config)
    result = minimize(
        lambda x: calibration_objective(x, config, country, dispersion),
        candidate_start,
        method="Nelder-Mead",
        options={"maxiter": int(maxiter or calibration["maxiter"]), "xatol": 0.03, "fatol": 0.5},
    )
    calibrated = apply_calibration_vector(config, result.x)
    timeseries, summary = run_prepared_config(
        calibrated,
        analysis="calibration",
        scenario=f"{country}_calibrated",
        vaccine_scenario=configs["baseline"]["baseline_vaccine_scenario"],
        resistance_scenario=configs["baseline"]["baseline_resistance_scenario"],
        metadata={"country": country},
    )
    analysis_year = int(config["metadata"]["analysis_year"])
    annual = annual_reported_cases(timeseries, analysis_year=analysis_year)
    predicted_mean = float(annual["reported_cases"].mean())
    predicted_sd = float(max(annual["reported_cases"].std(ddof=0), np.sqrt(max(predicted_mean, 1.0))))
    reporting_by_age = ";".join(
        f"{record['label']}={min(1.0, float(record['reporting_rate']) * float(calibrated['reporting_multiplier'])):.4f}"
        for record in calibrated["age_groups"]
    )
    summary["fit_score"] = float(result.fun)
    summary["calibrated_beta"] = float(calibrated["transmission"]["beta_S"])
    summary["reporting_multiplier_by_age"] = reporting_by_age
    summary["posterior_interval_low"] = max(0.0, predicted_mean - 1.96 * predicted_sd)
    summary["posterior_interval_high"] = predicted_mean + 1.96 * predicted_sd
    summary["calibration_success"] = bool(result.success)
    summary["calibration_message"] = str(result.message)
    return calibrated, summary


def main() -> None:
    configs = load_configs()
    calibration_country = configs["baseline"]["calibration"]["calibration_country_profile"]
    parser = argparse.ArgumentParser(description="Calibrate country-level pertussis model parameters.")
    parser.add_argument("--country", default=calibration_country)
    parser.add_argument("--maxiter", type=int, default=None)
    args = parser.parse_args()

    _, summary = calibrate_country(args.country, maxiter=args.maxiter)
    write_dataframe(summary, project_path(f"outputs/tables/calibration_{args.country}.csv"))


if __name__ == "__main__":
    main()
