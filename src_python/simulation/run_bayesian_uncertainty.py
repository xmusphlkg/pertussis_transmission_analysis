from __future__ import annotations

import argparse
from copy import deepcopy
from dataclasses import dataclass
from math import isfinite
from typing import Any

import numpy as np
import pandas as pd
from scipy.special import gammaln

from src_python.calibration.calibrate_baseline import (
    align_annual_case_series,
    calibration_runtime_config,
    observed_annual_case_frame,
    predicted_case_frame,
    retain_recent_observed_window,
    reporting_rate_prior_penalty,
)
from src_python.calibration.likelihood import negative_binomial_nll
from src_python.simulation.common import (
    execute_scenario_list,
    load_configs,
    make_config,
    run_prepared_config,
    write_outputs,
)
from src_python.utils.io import project_path, read_table, write_dataframe
from src_python.utils.parallel import parallel_map


PARAMETER_NAMES = (
    "log_beta_S",
    "log_reporting_multiplier",
    "logit_VE_sus",
    "logit_VE_inf",
    "logit_VE_dur",
    "logit_relative_infectiousness_asymptomatic",
    "log_infectious_duration_symptomatic",
    "log_infectious_duration_asymptomatic",
    "logit_fitness_R_scaled",
    "logit_resistance_prevalence",
)

PROPOSAL_SCALES = np.array([0.12, 0.18, 0.28, 0.28, 0.30, 0.25, 0.10, 0.12, 0.25, 0.24], dtype=float)


@dataclass(frozen=True)
class ChainTask:
    country: str
    chain: int
    seed: int
    warmup: int
    draws: int
    proposal_scale: float


def _logit(value: float) -> float:
    value = float(np.clip(value, 1e-9, 1.0 - 1e-9))
    return float(np.log(value / (1.0 - value)))


def _inv_logit(value: float) -> float:
    if value >= 0:
        z = np.exp(-value)
        return float(1.0 / (1.0 + z))
    z = np.exp(value)
    return float(z / (1.0 + z))


def _beta_ab(mean: float, sd: float) -> tuple[float, float]:
    mean = float(np.clip(mean, 1e-6, 1.0 - 1e-6))
    sd = max(float(sd), 1e-6)
    variance = min(sd**2, mean * (1.0 - mean) * 0.95)
    common = mean * (1.0 - mean) / variance - 1.0
    return max(mean * common, 1e-3), max((1.0 - mean) * common, 1e-3)


def _beta_logpdf(value: float, mean: float, sd: float) -> float:
    if not 0.0 < value < 1.0:
        return -np.inf
    alpha, beta = _beta_ab(mean, sd)
    return float(
        (alpha - 1.0) * np.log(value)
        + (beta - 1.0) * np.log1p(-value)
        + gammaln(alpha + beta)
        - gammaln(alpha)
        - gammaln(beta)
    )


def _normal_logpdf(value: float, mean: float, sd: float) -> float:
    sd = max(float(sd), 1e-9)
    z = (float(value) - float(mean)) / sd
    return float(-0.5 * z * z - np.log(sd) - 0.5 * np.log(2.0 * np.pi))


def _scaled_logit_to_value(x: float, lower: float, upper: float) -> float:
    s = _inv_logit(x)
    return float(lower + (upper - lower) * s)


def _value_to_scaled_logit(value: float, lower: float, upper: float) -> float:
    scaled = (float(value) - lower) / max(upper - lower, 1e-12)
    return _logit(float(np.clip(scaled, 1e-9, 1.0 - 1e-9)))


def _log_jacobian_logit(x: float) -> float:
    s = _inv_logit(x)
    return float(np.log(max(s, 1e-12)) + np.log(max(1.0 - s, 1e-12)))


def _log_jacobian_scaled_logit(x: float, lower: float, upper: float) -> float:
    return float(np.log(max(upper - lower, 1e-12)) + _log_jacobian_logit(x))


def _country_observed(country: str) -> pd.DataFrame:
    configs = load_configs()
    observed = observed_annual_case_frame(country)
    recent_years = int(configs["baseline"].get("calibration", {}).get("recent_years", 0))
    return retain_recent_observed_window(observed, recent_years)


def _initial_vector(config: dict[str, Any]) -> np.ndarray:
    fitness_bounds = load_configs()["baseline"]["bayesian_uncertainty"]["priors"]["fitness_R"]
    return np.array(
        [
            np.log(float(config["transmission"]["beta_S"])),
            np.log(float(config.get("reporting_multiplier", 1.0))),
            _logit(float(config["vaccine"].get("VE_sus", 0.0))),
            _logit(float(config["vaccine"].get("VE_inf", 0.0))),
            _logit(float(config["vaccine"].get("VE_dur", 0.0))),
            _logit(float(config["transmission"]["relative_infectiousness_asymptomatic"])),
            np.log(float(config["natural_history"]["infectious_duration_symptomatic"])),
            np.log(float(config["natural_history"]["infectious_duration_asymptomatic"])),
            _value_to_scaled_logit(
                float(config["transmission"].get("fitness_R", 1.0)),
                float(fitness_bounds.get("min", 0.70)),
                float(fitness_bounds.get("max", 1.25)),
            ),
            _logit(float(config["resistance"]["target_prevalence_at_analysis_start"])),
        ],
        dtype=float,
    )


def _sample_from_vector(vector: np.ndarray, priors: dict[str, Any]) -> dict[str, float]:
    fitness = priors["fitness_R"]
    return {
        "beta_S": float(np.exp(vector[0])),
        "reporting_multiplier": float(np.exp(vector[1])),
        "VE_sus": _inv_logit(vector[2]),
        "VE_inf": _inv_logit(vector[3]),
        "VE_dur": _inv_logit(vector[4]),
        "relative_infectiousness_asymptomatic": _inv_logit(vector[5]),
        "infectious_duration_symptomatic": float(np.exp(vector[6])),
        "infectious_duration_asymptomatic": float(np.exp(vector[7])),
        "fitness_R": _scaled_logit_to_value(
            vector[8],
            float(fitness.get("min", 0.70)),
            float(fitness.get("max", 1.25)),
        ),
        "resistance_prevalence": _inv_logit(vector[9]),
    }


def _apply_sample(config: dict[str, Any], sample: dict[str, float]) -> dict[str, Any]:
    out = deepcopy(config)
    out["transmission"]["beta_S"] = sample["beta_S"]
    out["reporting_multiplier"] = sample["reporting_multiplier"]
    out["vaccine"]["VE_sus"] = sample["VE_sus"]
    out["vaccine"]["VE_inf"] = sample["VE_inf"]
    out["vaccine"]["VE_dur"] = sample["VE_dur"]
    out["transmission"]["relative_infectiousness_asymptomatic"] = sample[
        "relative_infectiousness_asymptomatic"
    ]
    out["natural_history"]["infectious_duration_symptomatic"] = sample[
        "infectious_duration_symptomatic"
    ]
    out["natural_history"]["infectious_duration_asymptomatic"] = sample[
        "infectious_duration_asymptomatic"
    ]
    out["transmission"]["fitness_R"] = sample["fitness_R"]

    resistance = float(np.clip(sample["resistance_prevalence"], 0.0, 1.0))
    out["initial_conditions"]["initial_resistance_prevalence"] = resistance
    out.setdefault("resistance", {})["target_prevalence_at_analysis_start"] = resistance
    out["resistance"]["importation_fraction"] = resistance
    out.setdefault("importation", {})["resistant_fraction"] = resistance
    return out


def _resistance_prior(country: str, target: float, settings: dict[str, Any]) -> tuple[float, float]:
    path = project_path("data", "raw", "country_resistance_timeline.csv")
    floor_sd = float(settings["priors"].get("resistance_prevalence", {}).get("floor_sd", 0.03))
    if not path.exists():
        return float(np.clip(target, 1e-6, 1.0 - 1e-6)), max(floor_sd, 0.05)
    timeline = pd.read_csv(path)
    rows = timeline.loc[timeline["country"].astype(str).eq(country)].copy()
    if rows.empty:
        return float(np.clip(target, 1e-6, 1.0 - 1e-6)), max(floor_sd, 0.05)
    rows["year"] = pd.to_numeric(rows["year"], errors="coerce")
    rows = rows.sort_values("year").dropna(subset=["year"])
    row = rows.iloc[-1]
    lower = pd.to_numeric(pd.Series([row.get("lower", np.nan)]), errors="coerce").iloc[0]
    upper = pd.to_numeric(pd.Series([row.get("upper", np.nan)]), errors="coerce").iloc[0]
    if np.isfinite(lower) and np.isfinite(upper) and upper > lower:
        sd = max(float(upper - lower) / 3.92, floor_sd)
    else:
        sample_size = pd.to_numeric(pd.Series([row.get("sample_size", np.nan)]), errors="coerce").iloc[0]
        if np.isfinite(sample_size) and sample_size > 0:
            sd = np.sqrt(max(target * (1.0 - target), 1e-6) / float(sample_size))
            sd = max(float(sd), floor_sd)
        else:
            sd = max(floor_sd, 0.05)
    return float(np.clip(target, 1e-6, 1.0 - 1e-6)), float(sd)


def _log_prior(vector: np.ndarray, base_config: dict[str, Any], country: str, settings: dict[str, Any]) -> float:
    priors = settings["priors"]
    sample = _sample_from_vector(vector, priors)
    if not 0.002 <= sample["beta_S"] <= 0.2:
        return -np.inf
    if not 0.05 <= sample["reporting_multiplier"] <= 20.0:
        return -np.inf
    if not 7.0 <= sample["infectious_duration_symptomatic"] <= 35.0:
        return -np.inf
    if not 5.0 <= sample["infectious_duration_asymptomatic"] <= 28.0:
        return -np.inf

    logp = 0.0
    logp += _normal_logpdf(
        np.log(sample["beta_S"]),
        np.log(float(base_config["transmission"]["beta_S"])),
        float(priors.get("log_beta_S_sd", 0.50)),
    )
    logp += _normal_logpdf(
        np.log(sample["reporting_multiplier"]),
        np.log(float(base_config.get("reporting_multiplier", 1.0))),
        float(priors.get("log_reporting_multiplier_sd", 0.70)),
    )

    for key, vector_idx in (
        ("VE_sus", 2),
        ("VE_inf", 3),
        ("VE_dur", 4),
        ("relative_infectiousness_asymptomatic", 5),
    ):
        prior = priors[key]
        logp += _beta_logpdf(sample[key], float(prior["mean"]), float(prior["sd"]))
        logp += _log_jacobian_logit(vector[vector_idx])

    logp += _normal_logpdf(
        np.log(sample["infectious_duration_symptomatic"]),
        np.log(float(base_config["natural_history"]["infectious_duration_symptomatic"])),
        float(priors["infectious_duration_symptomatic"].get("log_sd", 0.20)),
    )
    logp += _normal_logpdf(
        np.log(sample["infectious_duration_asymptomatic"]),
        np.log(float(base_config["natural_history"]["infectious_duration_asymptomatic"])),
        float(priors["infectious_duration_asymptomatic"].get("log_sd", 0.25)),
    )

    fitness_prior = priors["fitness_R"]
    logp += _normal_logpdf(
        sample["fitness_R"],
        float(fitness_prior.get("mean", 0.95)),
        float(fitness_prior.get("sd", 0.18)),
    )
    logp += _log_jacobian_scaled_logit(
        vector[8],
        float(fitness_prior.get("min", 0.70)),
        float(fitness_prior.get("max", 1.25)),
    )

    target = float(base_config["resistance"]["target_prevalence_at_analysis_start"])
    resistance_mean, resistance_sd = _resistance_prior(country, target, settings)
    logp += _normal_logpdf(sample["resistance_prevalence"], resistance_mean, resistance_sd)
    logp += _log_jacobian_logit(vector[9])
    return float(logp)


def _log_likelihood(config: dict[str, Any], observed: pd.DataFrame, country: str, dispersion: float) -> float:
    try:
        timeseries, _ = run_prepared_config(
            config,
            analysis="bayesian_calibration",
            scenario="candidate",
            vaccine_scenario=config["baseline_vaccine_scenario"],
            resistance_scenario=config["baseline_resistance_scenario"],
            metadata={"country": country},
        )
        predicted = predicted_case_frame(timeseries, observed)
        aligned = align_annual_case_series(predicted, observed)
        if len(aligned) < 3:
            return -np.inf
        return float(
            -negative_binomial_nll(
                aligned["observed_reported_cases"].to_numpy(dtype=float),
                aligned["predicted_reported_cases"].to_numpy(dtype=float),
                dispersion=dispersion,
            )
        )
    except Exception:
        return -np.inf


def _log_posterior(
    vector: np.ndarray,
    base_config: dict[str, Any],
    observed: pd.DataFrame,
    country: str,
    settings: dict[str, Any],
) -> tuple[float, dict[str, float] | None]:
    prior = _log_prior(vector, base_config, country, settings)
    if not isfinite(prior):
        return -np.inf, None
    sample = _sample_from_vector(vector, settings["priors"])
    candidate = _apply_sample(base_config, sample)
    likelihood = _log_likelihood(candidate, observed, country, float(settings.get("dispersion", 50.0)))
    if not isfinite(likelihood):
        return -np.inf, None
    posterior = likelihood + prior - reporting_rate_prior_penalty(candidate)
    return float(posterior), sample


def _run_chain(task: ChainTask) -> pd.DataFrame:
    rng = np.random.default_rng(task.seed)
    configs = load_configs()
    settings = configs["baseline"]["bayesian_uncertainty"]
    base = make_config(
        vaccine_scenario=configs["baseline"]["baseline_vaccine_scenario"],
        resistance_scenario=configs["baseline"]["baseline_resistance_scenario"],
        country_profile=task.country,
    )
    observed = _country_observed(task.country)
    runtime_base = calibration_runtime_config(base, observed)
    current = _initial_vector(runtime_base)
    current_logp, current_sample = _log_posterior(current, runtime_base, observed, task.country, settings)
    if current_sample is None:
        current_sample = _sample_from_vector(current, settings["priors"])

    rows: list[dict[str, Any]] = []
    accepted = 0
    total_steps = int(task.warmup + task.draws)
    proposal_scales = PROPOSAL_SCALES * float(task.proposal_scale)
    for step in range(total_steps):
        proposal = current + rng.normal(0.0, proposal_scales)
        proposed_logp, proposed_sample = _log_posterior(proposal, runtime_base, observed, task.country, settings)
        if isfinite(proposed_logp) and np.log(rng.random()) < proposed_logp - current_logp:
            current = proposal
            current_logp = proposed_logp
            current_sample = proposed_sample or _sample_from_vector(current, settings["priors"])
            accepted += 1
        if step >= task.warmup:
            row = {
                "country": task.country,
                "chain": task.chain,
                "draw": step - task.warmup + 1,
                "step": step + 1,
                "posterior_log_prob": current_logp,
                "accepted_fraction": accepted / float(step + 1),
            }
            row.update(current_sample)
            rows.append(row)
    return pd.DataFrame(rows)


def _posterior_predictive_scenarios(samples: pd.DataFrame, draws_per_country: int) -> list[dict[str, Any]]:
    configs = load_configs()
    scenarios = []
    rng = np.random.default_rng(int(configs["baseline"]["bayesian_uncertainty"].get("random_seed", 20260510)) + 917)
    for country, group in samples.groupby("country", sort=False):
        group = group.reset_index(drop=True)
        if len(group) > draws_per_country:
            selected = group.iloc[np.sort(rng.choice(len(group), draws_per_country, replace=False))].copy()
        else:
            selected = group.copy()
        for draw_idx, row in enumerate(selected.itertuples(index=False), start=1):
            sample = {name: float(getattr(row, name)) for name in _sample_columns()}
            config = make_config(
                vaccine_scenario=configs["baseline"]["baseline_vaccine_scenario"],
                resistance_scenario=configs["baseline"]["baseline_resistance_scenario"],
                country_profile=country,
            )
            config = _apply_sample(config, sample)
            metadata = {
                "country": country,
                "posterior_draw": draw_idx,
                "posterior_chain": int(getattr(row, "chain")),
                "posterior_log_prob": float(getattr(row, "posterior_log_prob")),
                **{f"posterior_{key}": value for key, value in sample.items()},
            }
            scenarios.append(
                {
                    "config": config,
                    "analysis": "bayesian_uncertainty",
                    "scenario": f"{country}_draw_{draw_idx:03d}",
                    "vaccine_scenario": configs["baseline"]["baseline_vaccine_scenario"],
                    "resistance_scenario": configs["baseline"]["baseline_resistance_scenario"],
                    "metadata": metadata,
                }
            )
    return scenarios


def _sample_columns() -> tuple[str, ...]:
    return (
        "beta_S",
        "reporting_multiplier",
        "VE_sus",
        "VE_inf",
        "VE_dur",
        "relative_infectiousness_asymptomatic",
        "infectious_duration_symptomatic",
        "infectious_duration_asymptomatic",
        "fitness_R",
        "resistance_prevalence",
    )


def _write_interval_summaries(summary: pd.DataFrame, samples: pd.DataFrame) -> None:
    outcome_cols = [
        "annualized_infant_cases_per_100k",
        "annualized_infections_per_100k",
        "annualized_reported_cases_per_100k",
        "annualized_infant_infections_per_100k",
        "resistant_fraction",
        "resistant_fraction_end",
        "resistant_infections",
    ]
    rows = []
    for country, group in summary.groupby("country", sort=False):
        for outcome in outcome_cols:
            values = pd.to_numeric(group[outcome], errors="coerce").dropna().to_numpy(dtype=float)
            if len(values) == 0:
                continue
            low, median, high = np.percentile(values, [2.5, 50.0, 97.5])
            rows.append(
                {
                    "country": country,
                    "outcome": outcome,
                    "posterior_median": float(median),
                    "credible_interval_low": float(low),
                    "credible_interval_high": float(high),
                    "posterior_draws": int(len(values)),
                }
            )
    write_dataframe(pd.DataFrame(rows), project_path("outputs/summaries/bayesian_uncertainty_intervals_summary.csv"))

    parameter_rows = []
    for country, group in samples.groupby("country", sort=False):
        for parameter in _sample_columns():
            values = pd.to_numeric(group[parameter], errors="coerce").dropna().to_numpy(dtype=float)
            if len(values) == 0:
                continue
            low, median, high = np.percentile(values, [2.5, 50.0, 97.5])
            parameter_rows.append(
                {
                    "country": country,
                    "parameter": parameter,
                    "posterior_median": float(median),
                    "credible_interval_low": float(low),
                    "credible_interval_high": float(high),
                    "posterior_draws": int(len(values)),
                }
            )
    write_dataframe(pd.DataFrame(parameter_rows), project_path("outputs/summaries/bayesian_parameter_summary.csv"))


def main(n_jobs: int | None = None, draws: int | None = None, warmup: int | None = None):
    configs = load_configs()
    settings = configs["baseline"]["bayesian_uncertainty"]
    n_chains = int(settings.get("n_chains", 4))
    chain_draws = int(draws or settings.get("draws", 16))
    chain_warmup = int(warmup or settings.get("warmup", 8))
    base_seed = int(settings.get("random_seed", 20260510))
    proposal_scale = float(settings.get("proposal_scale", 1.0))
    tasks = [
        ChainTask(
            country=country,
            chain=chain,
            seed=base_seed + country_idx * 1000 + chain * 137,
            warmup=chain_warmup,
            draws=chain_draws,
            proposal_scale=proposal_scale,
        )
        for country_idx, country in enumerate(configs["countries"])
        for chain in range(1, n_chains + 1)
    ]

    sample_frames = parallel_map(_run_chain, tasks, desc="bayesian_chains", n_jobs=n_jobs)
    samples = pd.concat(sample_frames, ignore_index=True)
    write_dataframe(samples, project_path("outputs/simulations/bayesian_posterior_samples.csv"))

    pp_draws = int(settings.get("posterior_predictive_draws_per_country", 20))
    scenarios = _posterior_predictive_scenarios(samples, pp_draws)
    timeseries, summary = execute_scenario_list(scenarios, stem="bayesian_uncertainty", n_jobs=n_jobs)
    write_outputs(timeseries, summary, "bayesian_uncertainty")
    _write_interval_summaries(summary, samples)
    return timeseries, summary, samples


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Bayesian uncertainty analysis for pertussis scenarios.")
    parser.add_argument("--n-jobs", type=int, default=None)
    parser.add_argument("--draws", type=int, default=None)
    parser.add_argument("--warmup", type=int, default=None)
    args = parser.parse_args()
    main(n_jobs=args.n_jobs, draws=args.draws, warmup=args.warmup)
