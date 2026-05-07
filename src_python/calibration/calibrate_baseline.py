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
    out.setdefault("resistance", {})["importation_fraction"] = importation_fraction
    out["importation"]["resistant_fraction"] = importation_fraction
    return out


def initial_calibration_vector(config: dict[str, Any]) -> np.ndarray:
    return np.array(
        [
            np.log(float(config["transmission"]["beta_S"])),
            np.log(float(config.get("reporting_multiplier", 1.0))),
            _logit(float(config["transmission"].get("seasonal_amplitude", 0.0)) / 0.35),
            np.log(float(config.get("importation", {}).get("rate_per_100k_per_year", 0.2))),
            _logit(float(config.get("importation", {}).get("resistant_fraction", 0.3))),
        ],
        dtype=float,
    )


def reporting_rate_prior_penalty(config: dict[str, Any]) -> float:
    prior = config.get("reporting_rate_prior", {})
    if prior.get("method") != "literature_range":
        return 0.0

    age_bands = prior.get("age_groups", {})
    weight = float(prior.get("weight", 1.0))
    multiplier = float(config.get("reporting_multiplier", 1.0))

    penalty = 0.0
    for record in config.get("age_groups", []):
        label = record.get("label", "")
        band = age_bands.get(label)
        if not band:
            continue

        base_rate = float(record.get("reporting_rate", 0.0))
        target_rate = float(np.clip(base_rate * multiplier, 0.0, 1.0))
        lower = float(band.get("lower", base_rate))
        upper = float(band.get("upper", base_rate))

        if target_rate <= base_rate:
            scale = max(base_rate - lower, 1e-6)
        else:
            scale = max(upper - base_rate, 1e-6)

        standardized = (target_rate - base_rate) / scale
        penalty += standardized**2

    return float(weight * penalty)


def annual_reported_cases(timeseries: pd.DataFrame) -> pd.DataFrame:
    out = timeseries.copy()
    out["simulation_year"] = np.floor((out["time"] - float(out["time"].min())) / 365.0).astype(int)
    return out.groupby("simulation_year", as_index=False).agg(reported_cases=("reported_cases", "sum"))


def observed_annual_cases(country: str) -> np.ndarray:
    configs = load_configs()
    surveillance_year = int(configs["data_sources"].get("surveillance_year", configs["data_sources"].get("analysis_year", 2023)))
    who_path = project_path("data/processed/who_pertussis_reported_cases.csv")
    if who_path.exists():
        who = pd.read_csv(who_path)
        who_country = who.loc[who["config_key"].eq(country)].copy()
        if not who_country.empty:
            who_country["reported_cases"] = pd.to_numeric(who_country["reported_cases"], errors="coerce")
            observed = who_country.loc[who_country["year"].le(surveillance_year)].dropna(subset=["reported_cases"]).sort_values("year")
            if not observed.empty:
                return observed["reported_cases"].to_numpy(dtype=float)

    path = project_path("data/processed/pertussis_incidence_timeseries.csv")
    observed = pd.read_csv(path)
    observed = observed.loc[observed["config_key"].eq(country) & observed["Year"].le(surveillance_year)].copy()
    if observed.empty:
        incidence = configs["countries"][country].get("observed_incidence", {})
        population = float(configs["countries"][country]["total_population"])
        mean_incidence = float(incidence.get("observed_mean_annual_reported_incidence_per_100k", 0.0))
        return np.array([mean_incidence * population / 100_000.0], dtype=float)
    observed["Cases"] = pd.to_numeric(observed["Cases"], errors="coerce").fillna(0.0)
    return observed.groupby("Year")["Cases"].sum().to_numpy(dtype=float)


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
    predicted = annual_reported_cases(timeseries)["reported_cases"].to_numpy(dtype=float)
    observed = observed_annual_cases(country)
    if predicted.size != observed.size:
        predicted = np.repeat(float(np.mean(predicted)), observed.size)
    return negative_binomial_nll(observed, predicted, dispersion=dispersion) + reporting_rate_prior_penalty(config)


def calibrate_country(country: str, *, maxiter: int | None = None) -> tuple[dict[str, Any], pd.DataFrame]:
    configs = load_configs()
    calibration = configs["baseline"].get("calibration", {})
    dispersion = float(calibration.get("dispersion", 50.0))
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
        options={"maxiter": int(maxiter or calibration.get("maxiter", 30)), "xatol": 0.03, "fatol": 0.5},
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
    annual = annual_reported_cases(timeseries)
    predicted_mean = float(annual["reported_cases"].mean())
    predicted_sd = float(max(annual["reported_cases"].std(ddof=0), np.sqrt(max(predicted_mean, 1.0))))
    observed = observed_annual_cases(country)
    predicted = annual["reported_cases"].to_numpy(dtype=float)
    if predicted.size != observed.size:
        predicted = np.repeat(float(np.mean(predicted)), observed.size)
    data_fit_score = float(negative_binomial_nll(observed, predicted, dispersion=dispersion))
    reporting_by_age = ";".join(
        f"{record['label']}={min(1.0, float(record.get('reporting_rate', 0.0)) * float(calibrated.get('reporting_multiplier', 1.0))):.4f}"
        for record in calibrated["age_groups"]
    )
    reporting_prior = calibrated.get("reporting_rate_prior", {})
    reporting_prior_groups = reporting_prior.get("age_groups", {})
    reporting_prior_by_age = ";".join(
        f"{record['label']}={float(record.get('reporting_rate', 0.0)):.4f}["
        f"{float(reporting_prior_groups.get(record['label'], {}).get('lower', np.nan)):.4f},"
        f"{float(reporting_prior_groups.get(record['label'], {}).get('upper', np.nan)):.4f}]"
        for record in calibrated["age_groups"]
    )
    summary["data_fit_score"] = data_fit_score
    summary["reporting_rate_prior_penalty"] = float(reporting_rate_prior_penalty(calibrated))
    summary["fit_score"] = float(result.fun)
    summary["calibrated_beta"] = float(calibrated["transmission"]["beta_S"])
    summary["reporting_multiplier_by_age"] = reporting_by_age
    summary["reporting_rate_prior_by_age"] = reporting_prior_by_age
    summary["reporting_rate_prior_method"] = str(reporting_prior.get("method", ""))
    summary["reporting_rate_prior_evidence_class"] = str(reporting_prior.get("evidence_class", ""))
    summary["posterior_interval_low"] = max(0.0, predicted_mean - 1.96 * predicted_sd)
    summary["posterior_interval_high"] = predicted_mean + 1.96 * predicted_sd
    summary["calibration_success"] = bool(result.success)
    summary["calibration_message"] = str(result.message)
    return calibrated, summary


def main() -> None:
    configs = load_configs()
    default_country = configs["baseline"].get("calibration", {}).get(
        "default_country_profile",
        configs["baseline"].get("baseline_country_profile", "Australia"),
    )
    parser = argparse.ArgumentParser(description="Calibrate country-level pertussis model parameters.")
    parser.add_argument("--country", default=default_country)
    parser.add_argument("--maxiter", type=int, default=None)
    args = parser.parse_args()

    _, summary = calibrate_country(args.country, maxiter=args.maxiter)
    write_dataframe(summary, project_path(f"outputs/tables/calibration_{args.country}.csv"))


if __name__ == "__main__":
    main()
