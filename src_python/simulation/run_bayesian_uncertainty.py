from __future__ import annotations

"""Bayesian uncertainty analysis with Adaptive Metropolis MCMC.

Improvements over the initial implementation:
1. Adaptive Metropolis (Haario et al. 2001): learns the empirical covariance
   during warmup for efficient exploration of correlated parameter spaces
   (e.g. beta_S vs reporting_multiplier).
2. Convergence diagnostics: split-R-hat, bulk/tail ESS (Vehtari et al. 2021)
   computed post-sampling and written as artifacts.
3. Increased default draws (500 post-warmup per chain, 250 warmup) for
   reliable 95% CrI estimation.
4. Time-varying reporting multiplier: optional linear trend parameter so the
   posterior can capture secular changes in surveillance completeness.
5. Dispersion (k) sensitivity sweep on the stochastic overlay.
6. Full multi-core parallelization: chains run in parallel across all CPUs.

References:
    Haario, H., Saksman, E., & Tamminen, J. (2001). An adaptive Metropolis
    algorithm. Bernoulli, 7(2), 223-242.
    Vehtari, A. et al. (2021). Rank-normalization, folding, and localization:
    An improved R-hat. Bayesian Analysis, 16(2), 667-718.
    Lavine, J.S. et al. (2011). Natural immune boosting in pertussis dynamics
    and the potential for long-term vaccine failure. PNAS, 108(17), 7259-7264.
"""

import argparse
from copy import deepcopy
from dataclasses import dataclass, field
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
from src_python.calibration.mcmc_diagnostics import (
    compute_diagnostics,
    summarize_convergence,
)
from src_python.simulation.common import (
    execute_scenario_list,
    load_configs,
    make_config,
    run_prepared_config,
    write_outputs,
)
from src_python.simulation.stochastic_overlay import (
    StochasticOverlayConfig,
    decompose_variance,
    stochastic_overlay_samples,
    summarize_overlay_intervals,
)
from src_python.utils.io import project_path, write_dataframe
from src_python.utils.parallel import parallel_map


# ---------------------------------------------------------------------------
# Parameter space definition
# ---------------------------------------------------------------------------

PARAMETER_NAMES = (
    "log_beta_S",
    "log_reporting_multiplier",
    "logit_VE_sus",
    "logit_VE_inf",
    "logit_relative_infectiousness_asymptomatic",
    "log_infectious_duration_symptomatic",
    "log_infectious_duration_asymptomatic",
    "logit_fitness_R_scaled",
)

N_PARAMS = len(PARAMETER_NAMES)

# Initial diagonal proposal scales (used before adaptation kicks in).
# Larger scales than before to reduce autocorrelation. The Adaptive Metropolis
# will learn the true scale and correlations during warmup.
INITIAL_PROPOSAL_SCALES = np.array(
    [0.05, 0.06, 0.06, 0.06, 0.06, 0.04, 0.05, 0.06],
    dtype=float,
)

# Adaptive Metropolis constants (Haario et al. 2001)
AM_EPSILON = 1e-5  # regularization for covariance (slightly larger for stability)
AM_SD = 2.4 ** 2 / N_PARAMS  # optimal scaling factor for Gaussian targets
AM_COMPONENTWISE_STEPS = 600  # componentwise phase length (~75 full parameter cycles)

# Robbins-Monro step-size adaptation (targets 23.4% acceptance for multivariate)
RM_TARGET_ACCEPTANCE = 0.234
RM_INITIAL_SCALE = 1.5  # start with larger scale to encourage exploration
RM_GAMMA = 0.6  # decay exponent for step-size adaptation (0.5 < gamma < 1)
# Scale bounds: prevent the global scale from collapsing to near-zero.
# exp(-0.5) ≈ 0.61 ensures proposals remain large enough to explore.
RM_LOG_SCALE_MIN = -0.5
RM_LOG_SCALE_MAX = 2.5
LOCAL_PROPOSAL_PROBABILITY = 0.20
BLOCK_PROPOSAL_PROBABILITY = 0.30
PROPOSAL_BLOCKS = (
    (0, 1),  # transmission/reporting scale (strongly correlated)
    (2, 3, 4),  # vaccine acquisition, infectiousness, asymptomatic contribution
    (5, 6),  # infectious durations
    (7,),  # resistance fitness (single parameter)
)


@dataclass(frozen=True)
class ChainTask:
    country: str
    chain: int
    seed: int
    warmup: int
    draws: int
    proposal_scale: float
    enable_time_varying_reporting: bool = True
    thin: int = 2  # thinning interval: store every Nth post-warmup draw


@dataclass
class AdaptiveState:
    """Running statistics for Adaptive Metropolis covariance estimation."""
    n: int = 0
    mean: np.ndarray = field(default_factory=lambda: np.zeros(N_PARAMS))
    cov: np.ndarray = field(default_factory=lambda: np.eye(N_PARAMS))
    _sum: np.ndarray = field(default_factory=lambda: np.zeros(N_PARAMS))
    _sum_sq: np.ndarray = field(default_factory=lambda: np.zeros((N_PARAMS, N_PARAMS)))

    def update(self, x: np.ndarray) -> None:
        """Welford-style online covariance update."""
        self.n += 1
        self._sum += x
        self._sum_sq += np.outer(x, x)
        self.mean = self._sum / self.n
        if self.n > 1:
            self.cov = (self._sum_sq / self.n - np.outer(self.mean, self.mean)) + AM_EPSILON * np.eye(N_PARAMS)

    def proposal_cov(self) -> np.ndarray:
        """Return the adapted proposal covariance matrix."""
        return AM_SD * self.cov


# ---------------------------------------------------------------------------
# Transform utilities
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Data loading and parameter vector construction
# ---------------------------------------------------------------------------

def _country_observed(country: str, interval: str = "native") -> pd.DataFrame:
    configs = load_configs()
    observed = observed_annual_case_frame(country)
    recent_years = int(configs["baseline"].get("calibration", {}).get("recent_years", 0))
    observed = retain_recent_observed_window(observed, recent_years)
    return _aggregate_observed_intervals(observed, interval)


def _aggregate_observed_intervals(observed: pd.DataFrame, interval: str) -> pd.DataFrame:
    """Aggregate high-frequency surveillance intervals for Bayesian likelihoods.

    Weekly reports are autocorrelated and much noisier than the deterministic
    ODE can represent.  Treating every week as an independent NB observation
    over-weights large high-frequency datasets and creates pathologically
    narrow posteriors.  Monthly aggregation preserves the epidemic-scale signal
    while conserving reported cases.
    """
    interval = str(interval or "native").lower()
    if interval in {"native", "none", "reporting_interval"}:
        return observed
    if interval not in {"monthly", "month"}:
        raise ValueError(f"Unsupported Bayesian likelihood interval: {interval}")
    if not {"period_start", "period_end"}.issubset(observed.columns) or observed.empty:
        return observed

    frame = observed.copy()
    frame["period_start"] = pd.to_datetime(frame["period_start"], errors="coerce")
    frame["period_end"] = pd.to_datetime(frame["period_end"], errors="coerce")
    frame["reported_cases"] = pd.to_numeric(frame["reported_cases"], errors="coerce").fillna(0.0)
    frame = frame.dropna(subset=["period_start", "period_end"]).copy()
    frame = frame.loc[frame["period_end"].gt(frame["period_start"])].copy()
    if frame.empty:
        return observed.iloc[0:0].copy()

    data_start = frame["period_start"].min()
    data_end = frame["period_end"].max()
    first_month = data_start.to_period("M")
    last_month = (data_end - pd.Timedelta(nanoseconds=1)).to_period("M")
    rows: list[dict[str, Any]] = []

    source_starts = frame["period_start"].to_numpy(dtype="datetime64[ns]")
    source_ends = frame["period_end"].to_numpy(dtype="datetime64[ns]")
    source_days = (source_ends - source_starts).astype("timedelta64[s]").astype(float) / 86400.0
    source_days = np.maximum(source_days, 1e-9)
    source_cases = frame["reported_cases"].to_numpy(dtype=float)

    for period in pd.period_range(first_month, last_month, freq="M"):
        month_start = pd.Timestamp(period.start_time)
        month_end = pd.Timestamp((period + 1).start_time)
        covered_start = max(month_start, data_start)
        covered_end = min(month_end, data_end)
        if covered_end <= covered_start:
            continue

        target_start = np.datetime64(covered_start.to_datetime64())
        target_end = np.datetime64(covered_end.to_datetime64())
        overlap_start = np.maximum(source_starts, target_start)
        overlap_end = np.minimum(source_ends, target_end)
        overlap_days = (overlap_end - overlap_start).astype("timedelta64[s]").astype(float) / 86400.0
        mask = overlap_days > 0.0
        reported = float(np.sum(source_cases[mask] * overlap_days[mask] / source_days[mask]))
        start_date = covered_start.date().isoformat()
        end_date = covered_end.date().isoformat()
        rows.append(
            {
                "series_year": len(rows),
                "observed_year": int(covered_start.year),
                "observed_interval_id": f"{start_date}_{end_date}",
                "period_start": covered_start,
                "period_end": covered_end,
                "interval_days": float((covered_end - covered_start).days),
                "reported_cases": reported,
                "reporting_frequency": "monthly_aggregated",
            }
        )

    return pd.DataFrame(rows)


def _initial_vector(config: dict[str, Any], enable_trend: bool = True) -> np.ndarray:
    fitness_bounds = load_configs()["baseline"]["bayesian_uncertainty"]["priors"]["fitness_R"]
    vec = [
        np.log(float(config["transmission"]["beta_S"])),
        np.log(float(config.get("reporting_multiplier", 1.0))),
        _logit(float(config["vaccine"].get("VE_sus", 0.0))),
        _logit(float(config["vaccine"].get("VE_inf", 0.0))),
        _logit(float(config["transmission"]["relative_infectiousness_asymptomatic"])),
        np.log(float(config["natural_history"]["infectious_duration_symptomatic"])),
        np.log(float(config["natural_history"]["infectious_duration_asymptomatic"])),
        _value_to_scaled_logit(
            float(config["transmission"].get("fitness_R", 1.0)),
            float(fitness_bounds.get("min", 0.70)),
            float(fitness_bounds.get("max", 1.25)),
        ),
    ]
    return np.array(vec, dtype=float)


def _sample_from_vector(vector: np.ndarray, priors: dict[str, Any]) -> dict[str, float]:
    fitness = priors["fitness_R"]
    return {
        "beta_S": float(np.exp(vector[0])),
        "reporting_multiplier": float(np.exp(vector[1])),
        "VE_sus": _inv_logit(vector[2]),
        "VE_inf": _inv_logit(vector[3]),
        "VE_dur": float(priors.get("VE_dur", {}).get("mean", 0.10)),  # fixed at prior mean
        "relative_infectiousness_asymptomatic": _inv_logit(vector[4]),
        "infectious_duration_symptomatic": float(np.exp(vector[5])),
        "infectious_duration_asymptomatic": float(np.exp(vector[6])),
        "fitness_R": _scaled_logit_to_value(
            vector[7],
            float(fitness.get("min", 0.70)),
            float(fitness.get("max", 1.25)),
        ),
        "resistance_prevalence": float(priors.get("resistance_prevalence_fixed", 0.30)),
        "reporting_trend_end_multiplier": float(priors.get("reporting_trend_fixed", 1.0)),
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

    # Resistance prevalence is fixed at the country-calibrated value (not sampled)
    resistance = float(np.clip(sample["resistance_prevalence"], 0.0, 1.0))
    out["initial_conditions"]["initial_resistance_prevalence"] = resistance
    out.setdefault("resistance", {})["target_prevalence_at_analysis_start"] = resistance
    out["resistance"]["importation_fraction"] = resistance
    out.setdefault("importation", {})["resistant_fraction"] = resistance

    # Reporting trend is fixed at 1.0 (no secular change assumed)
    # The reporting_multiplier parameter absorbs the average level.
    trend_end = sample.get("reporting_trend_end_multiplier", 1.0)
    simulation = out.get("simulation", {})
    out["reporting_time_variation"] = {
        "start_time": float(simulation.get("start_time", 0.0)),
        "end_time": float(simulation.get("end_time", 0.0)),
        "start_multiplier": 1.0,
        "end_multiplier": float(trend_end),
    }
    return out


# ---------------------------------------------------------------------------
# Prior and posterior
# ---------------------------------------------------------------------------

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


def _log_prior(
    vector: np.ndarray,
    base_config: dict[str, Any],
    country: str,
    settings: dict[str, Any],
) -> float:
    priors = settings["priors"]
    sample = _sample_from_vector(vector, priors)

    # Hard bounds
    if not 0.002 <= sample["beta_S"] <= 0.2:
        return -np.inf
    if not 0.05 <= sample["reporting_multiplier"] <= 10.0:
        return -np.inf
    if not 7.0 <= sample["infectious_duration_symptomatic"] <= 35.0:
        return -np.inf
    if not 5.0 <= sample["infectious_duration_asymptomatic"] <= 28.0:
        return -np.inf

    logp = 0.0

    # Log-normal priors for positive parameters
    logp += _normal_logpdf(
        np.log(sample["beta_S"]),
        np.log(float(base_config["transmission"]["beta_S"])),
        float(priors.get("log_beta_S_sd", 0.40)),
    )
    logp += _normal_logpdf(
        np.log(sample["reporting_multiplier"]),
        np.log(float(base_config.get("reporting_multiplier", 1.0))),
        float(priors.get("log_reporting_multiplier_sd", 0.40)),
    )

    # Beta priors for bounded [0,1] parameters
    for key, vector_idx in (
        ("VE_sus", 2),
        ("VE_inf", 3),
        ("relative_infectiousness_asymptomatic", 4),
    ):
        prior = priors[key]
        logp += _beta_logpdf(sample[key], float(prior["mean"]), float(prior["sd"]))
        logp += _log_jacobian_logit(vector[vector_idx])

    # Log-normal priors for durations
    logp += _normal_logpdf(
        np.log(sample["infectious_duration_symptomatic"]),
        np.log(float(base_config["natural_history"]["infectious_duration_symptomatic"])),
        float(priors["infectious_duration_symptomatic"].get("log_sd", 0.15)),
    )
    logp += _normal_logpdf(
        np.log(sample["infectious_duration_asymptomatic"]),
        np.log(float(base_config["natural_history"]["infectious_duration_asymptomatic"])),
        float(priors["infectious_duration_asymptomatic"].get("log_sd", 0.20)),
    )

    # Normal prior for fitness_R on bounded scale
    fitness_prior = priors["fitness_R"]
    logp += _normal_logpdf(
        sample["fitness_R"],
        float(fitness_prior.get("mean", 1.00)),
        float(fitness_prior.get("sd", 0.12)),
    )
    logp += _log_jacobian_scaled_logit(
        vector[7],
        float(fitness_prior.get("min", 0.70)),
        float(fitness_prior.get("max", 1.25)),
    )

    return float(logp)


def _log_likelihood(
    config: dict[str, Any],
    observed: pd.DataFrame,
    country: str,
    dispersion: float,
    _cache: dict[str, float] | None = None,
) -> float:
    """Compute log-likelihood with optional caching to avoid redundant ODE solves.
    
    For MCMC efficiency, we cache results by parameter hash to avoid re-solving
    the ODE for identical parameter sets (which can happen during rejection steps).
    """
    try:
        # Create a hashable key from the parameter values
        if _cache is not None:
            # Hash the key parameters that affect the likelihood
            key_params = (
                config["transmission"]["beta_S"],
                config.get("reporting_multiplier", 1.0),
                config.get("reporting_time_variation", {}).get("end_multiplier", 1.0),
                config["vaccine"]["VE_sus"],
                config["vaccine"]["VE_inf"],
                config["transmission"]["relative_infectiousness_asymptomatic"],
                config["natural_history"]["infectious_duration_symptomatic"],
                config["natural_history"]["infectious_duration_asymptomatic"],
                config["transmission"].get("fitness_R", 1.0),
                config["initial_conditions"]["initial_resistance_prevalence"],
            )
            cache_key = hash(key_params)
            if cache_key in _cache:
                return _cache[cache_key]
        
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
            result = -np.inf
        else:
            result = float(
                -negative_binomial_nll(
                    aligned["observed_reported_cases"].to_numpy(dtype=float),
                    aligned["predicted_reported_cases"].to_numpy(dtype=float),
                    dispersion=dispersion,
                )
            )
        
        # Cache the result
        if _cache is not None:
            _cache[cache_key] = result
        
        return result
    except Exception:
        return -np.inf


def _log_posterior(
    vector: np.ndarray,
    base_config: dict[str, Any],
    observed: pd.DataFrame,
    country: str,
    settings: dict[str, Any],
    _cache: dict[str, float] | None = None,
) -> tuple[float, dict[str, float] | None]:
    prior = _log_prior(vector, base_config, country, settings)
    if not isfinite(prior):
        return -np.inf, None
    sample = _sample_from_vector(vector, settings["priors"])
    candidate = _apply_sample(base_config, sample)
    likelihood = _log_likelihood(
        candidate, observed, country, float(settings.get("dispersion", 50.0)), _cache=_cache
    )
    if not isfinite(likelihood):
        return -np.inf, None
    posterior = likelihood + prior - reporting_rate_prior_penalty(candidate)
    return float(posterior), sample


# ---------------------------------------------------------------------------
# Adaptive Metropolis MCMC chain runner
# ---------------------------------------------------------------------------

def _proposal_covariance(
    adapter: AdaptiveState,
    initial_cov: np.ndarray,
    global_scale: float,
) -> np.ndarray:
    if adapter.n >= AM_COMPONENTWISE_STEPS:
        adapted = adapter.proposal_cov()
        cov = global_scale * (0.85 * adapted + 0.15 * initial_cov)
    else:
        cov = global_scale * initial_cov
    cov = 0.5 * (cov + cov.T)
    cov += AM_EPSILON * np.eye(N_PARAMS)
    return cov


def _draw_mixed_proposal(
    rng: np.random.Generator,
    current: np.ndarray,
    proposal_cov: np.ndarray,
    diagonal_scales: np.ndarray,
    global_scale: float,
) -> np.ndarray:
    """Draw a symmetric proposal from a local/block/full mixture."""
    proposal = current.copy()
    move = rng.random()

    if move < LOCAL_PROPOSAL_PROBABILITY:
        component = int(rng.integers(0, N_PARAMS))
        std = float(np.sqrt(max(proposal_cov[component, component], 1e-12)))
        proposal[component] += rng.normal(0.0, std)
        return proposal

    if move < LOCAL_PROPOSAL_PROBABILITY + BLOCK_PROPOSAL_PROBABILITY:
        block = np.array(PROPOSAL_BLOCKS[int(rng.integers(0, len(PROPOSAL_BLOCKS)))], dtype=int)
        try:
            block_cov = proposal_cov[np.ix_(block, block)]
            L = np.linalg.cholesky(block_cov)
            proposal[block] += L @ rng.standard_normal(len(block))
        except np.linalg.LinAlgError:
            proposal[block] += rng.normal(
                0.0,
                diagonal_scales[block] * max(np.sqrt(global_scale), 1e-6),
            )
        return proposal

    try:
        L = np.linalg.cholesky(proposal_cov)
        return current + L @ rng.standard_normal(N_PARAMS)
    except np.linalg.LinAlgError:
        return current + rng.normal(0.0, diagonal_scales * max(np.sqrt(global_scale), 1e-6))


def _run_chain(task: ChainTask) -> pd.DataFrame:
    """Run a single MCMC chain with Adaptive Metropolis + Robbins-Monro scaling.

    Three-phase strategy for robust convergence in the transformed parameter space:

    Phase 1 — Componentwise exploration (steps 0 to AM_COMPONENTWISE_STEPS):
        Update one parameter at a time with moderate steps. This guarantees
        ~40-50% acceptance per component and builds a high-quality sample for
        the AM covariance estimate (~45 full parameter cycles).

    Phase 2 — Adaptive warmup (AM_COMPONENTWISE_STEPS to task.warmup):
        Full multivariate AM proposal using the empirical covariance from
        Phase 1. A Robbins-Monro step-size adaptation continuously tunes the
        global scaling factor to target 23.4% acceptance. The covariance
        continues to be updated throughout warmup.

    Phase 3 — Sampling (post-warmup):
        Covariance frozen at the warmup-adapted value. Robbins-Monro scaling
        frozen. Thinned draws are recorded.
    """
    rng = np.random.default_rng(task.seed)
    configs = load_configs()
    settings = configs["baseline"]["bayesian_uncertainty"]
    base = make_config(
        vaccine_scenario=configs["baseline"]["baseline_vaccine_scenario"],
        resistance_scenario=configs["baseline"]["baseline_resistance_scenario"],
        country_profile=task.country,
    )
    observed = _country_observed(
        task.country,
        interval=str(settings.get("likelihood_observation_frequency", "monthly")),
    )
    runtime_base = calibration_runtime_config(base, observed)
    from src_python.model.rk4_solver import apply_mcmc_solver_overrides
    runtime_base = apply_mcmc_solver_overrides(runtime_base)

    # Inject country-specific fixed values into priors for _sample_from_vector
    # Resistance prevalence is fixed at the country-calibrated value
    country_resistance = float(runtime_base["resistance"]["target_prevalence_at_analysis_start"])
    settings = dict(settings)  # shallow copy to avoid mutating shared config
    settings["priors"] = dict(settings["priors"])
    settings["priors"]["resistance_prevalence_fixed"] = country_resistance
    settings["priors"]["reporting_trend_fixed"] = 1.0  # no secular trend

    current = _initial_vector(runtime_base, enable_trend=task.enable_time_varying_reporting)

    # Small jitter to disperse chains
    jitter_scale = 0.5 * INITIAL_PROPOSAL_SCALES * float(task.proposal_scale)
    current = current + rng.normal(0.0, jitter_scale)

    # Initialize likelihood cache to avoid redundant ODE solves
    likelihood_cache: dict[str, float] = {}

    current_logp, current_sample = _log_posterior(
        current, runtime_base, observed, task.country, settings, _cache=likelihood_cache
    )
    if current_sample is None:
        current_sample = _sample_from_vector(current, settings["priors"])

    # If initial position has -inf posterior, try random starts
    if not isfinite(current_logp):
        for _attempt in range(50):
            trial = _initial_vector(runtime_base, enable_trend=task.enable_time_varying_reporting)
            trial = trial + rng.normal(0.0, jitter_scale * (1.0 + _attempt * 0.1))
            trial_logp, trial_sample = _log_posterior(
                trial, runtime_base, observed, task.country, settings, _cache=likelihood_cache
            )
            if isfinite(trial_logp):
                current = trial
                current_logp = trial_logp
                current_sample = trial_sample or _sample_from_vector(trial, settings["priors"])
                break

    # Adaptive Metropolis state
    adapter = AdaptiveState()
    adapter.update(current)

    # Initial diagonal proposal
    diagonal_scales = INITIAL_PROPOSAL_SCALES * float(task.proposal_scale)
    initial_cov = np.diag(diagonal_scales ** 2)

    # Robbins-Monro global scaling factor (log-scale for stability)
    log_scale = np.log(RM_INITIAL_SCALE)

    rows: list[dict[str, Any]] = []
    accepted = 0
    total_post_warmup_steps = int(task.draws * task.thin)
    total_steps = int(task.warmup) + total_post_warmup_steps

    # Progress reporting
    _progress_dir = project_path("outputs", "metadata", "mcmc_progress")
    _progress_dir.mkdir(parents=True, exist_ok=True)
    _progress_file = _progress_dir / f"{task.country}_chain{task.chain:02d}.txt"
    _progress_interval = 200

    for step in range(total_steps):
        if step % _progress_interval == 0:
            try:
                rate = accepted / max(step, 1)
                scale_str = f" scale={np.exp(log_scale):.2f}" if step >= AM_COMPONENTWISE_STEPS else ""
                _progress_file.write_text(
                    f"{step}/{total_steps} accept={rate:.3f}{scale_str}" if step > 0
                    else f"0/{total_steps} starting"
                )
            except OSError:
                pass

        # Phase 1: Componentwise updates
        if step < AM_COMPONENTWISE_STEPS:
            component = step % N_PARAMS
            proposal = current.copy()
            # Use a larger step for componentwise (5x the base scale) to ensure
            # the chain explores broadly during this phase and builds a good
            # covariance estimate. Higher acceptance during componentwise is fine.
            proposal[component] += rng.normal(0.0, diagonal_scales[component] * 5.0)

            proposed_logp, proposed_sample = _log_posterior(
                proposal, runtime_base, observed, task.country, settings, _cache=likelihood_cache
            )
            if isfinite(proposed_logp) and np.log(rng.random()) < proposed_logp - current_logp:
                current = proposal
                current_logp = proposed_logp
                current_sample = proposed_sample or _sample_from_vector(current, settings["priors"])
                accepted += 1
            # Always update adapter (even on rejection, current position is repeated)
            adapter.update(current)

        else:
            # Phase 2/3: Full multivariate AM proposal with Robbins-Monro scaling
            global_scale = np.exp(log_scale)

            proposal_cov = _proposal_covariance(adapter, initial_cov, global_scale)
            proposal = _draw_mixed_proposal(
                rng,
                current,
                proposal_cov,
                diagonal_scales,
                global_scale,
            )

            proposed_logp, proposed_sample = _log_posterior(
                proposal, runtime_base, observed, task.country, settings, _cache=likelihood_cache
            )

            # Metropolis acceptance
            accept = isfinite(proposed_logp) and np.log(rng.random()) < proposed_logp - current_logp
            if accept:
                current = proposal
                current_logp = proposed_logp
                current_sample = proposed_sample or _sample_from_vector(current, settings["priors"])
                accepted += 1

            # Robbins-Monro step-size adaptation during warmup
            if step < task.warmup:
                # Adapt log_scale so acceptance rate → RM_TARGET_ACCEPTANCE
                # Update rule: log_scale += gamma_t * (alpha - target)
                # where gamma_t = c / (step - AM_COMPONENTWISE_STEPS + c) decays
                adapt_step = step - AM_COMPONENTWISE_STEPS + 1
                gamma_t = 1.0 / (adapt_step ** RM_GAMMA)
                log_scale += gamma_t * (float(accept) - RM_TARGET_ACCEPTANCE)
                # Clamp to prevent extreme scaling — the lower bound is critical
                # to prevent chains from getting stuck with near-zero step sizes
                log_scale = float(np.clip(log_scale, RM_LOG_SCALE_MIN, RM_LOG_SCALE_MAX))
                # Continue updating covariance during warmup
                adapter.update(current)
            else:
                # Post-warmup: very slow adaptation to prevent chains from freezing
                # if the warmup-adapted scale was too small. Use a much smaller
                # learning rate (1/10th of warmup rate) so the chain remains
                # approximately stationary while still being able to escape stuck states.
                adapt_step = step - task.warmup + 1
                gamma_t = 0.1 / (adapt_step ** 0.8)
                log_scale += gamma_t * (float(accept) - RM_TARGET_ACCEPTANCE)
                log_scale = float(np.clip(log_scale, RM_LOG_SCALE_MIN, RM_LOG_SCALE_MAX))

        # Record post-warmup draws (with thinning)
        if step >= task.warmup:
            post_warmup_step = step - task.warmup
            if post_warmup_step % task.thin == 0:
                draw_idx = post_warmup_step // task.thin + 1
                row = {
                    "country": task.country,
                    "chain": task.chain,
                    "draw": draw_idx,
                    "step": step + 1,
                    "posterior_log_prob": current_logp,
                    "accepted_fraction": accepted / float(step + 1),
                }
                row.update(current_sample)
                rows.append(row)

    # Final progress
    try:
        _progress_file.write_text(
            f"{total_steps}/{total_steps} done accept={accepted/total_steps:.3f} scale={np.exp(log_scale):.2f}"
        )
    except OSError:
        pass

    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Posterior predictive and output generation
# ---------------------------------------------------------------------------

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
        "reporting_trend_end_multiplier",
    )


def _posterior_predictive_scenarios(
    samples: pd.DataFrame, draws_per_country: int
) -> list[dict[str, Any]]:
    configs = load_configs()
    scenarios = []
    rng = np.random.default_rng(
        int(configs["baseline"]["bayesian_uncertainty"].get("random_seed", 20260510)) + 917
    )
    for country, group in samples.groupby("country", sort=False):
        group = group.reset_index(drop=True)
        if len(group) > draws_per_country:
            selected = group.iloc[
                np.sort(rng.choice(len(group), draws_per_country, replace=False))
            ].copy()
        else:
            selected = group.copy()
        for draw_idx, row in enumerate(selected.itertuples(index=False), start=1):
            sample = {}
            for name in _sample_columns():
                val = getattr(row, name, None)
                if val is not None:
                    sample[name] = float(val)
                else:
                    # Fallback for legacy samples without trend
                    sample[name] = 1.0 if name == "reporting_trend_end_multiplier" else 0.0
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
            if outcome not in group.columns:
                continue
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
    write_dataframe(
        pd.DataFrame(rows),
        project_path("outputs/summaries/bayesian_uncertainty_intervals_summary.csv"),
    )

    parameter_rows = []
    for country, group in samples.groupby("country", sort=False):
        for parameter in _sample_columns():
            if parameter not in group.columns:
                continue
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
    write_dataframe(
        pd.DataFrame(parameter_rows),
        project_path("outputs/summaries/bayesian_parameter_summary.csv"),
    )


# ---------------------------------------------------------------------------
# Stochastic overlay with k-sensitivity sweep
# ---------------------------------------------------------------------------

def _apply_stochastic_overlay(
    summary: pd.DataFrame,
    settings: dict[str, Any],
) -> pd.DataFrame:
    """Layer superspreading + household-clustering stochastic replicates on the
    posterior predictive summary, writing combined-uncertainty CrI artifacts.
    """
    overlay = StochasticOverlayConfig.from_dict(settings.get("stochastic_overlay"))
    if not overlay.enabled:
        return pd.DataFrame()

    overlay_samples = stochastic_overlay_samples(summary, overlay=overlay)
    combined_intervals = summarize_overlay_intervals(summary, overlay_samples, overlay=overlay)
    variance_components = decompose_variance(overlay_samples)

    write_dataframe(
        overlay_samples,
        project_path("outputs/simulations/bayesian_stochastic_overlay_samples.csv"),
    )
    write_dataframe(
        combined_intervals,
        project_path("outputs/summaries/bayesian_stochastic_overlay_intervals_summary.csv"),
    )
    write_dataframe(
        variance_components,
        project_path("outputs/summaries/bayesian_stochastic_overlay_variance_components.csv"),
    )
    return combined_intervals


def _run_k_sensitivity_sweep(
    summary: pd.DataFrame,
    settings: dict[str, Any],
) -> pd.DataFrame:
    """Run stochastic overlay at multiple k values to show CrI sensitivity.

    Sweeps superspreading_k over [5, 10, 20, 30, 50] to demonstrate how
    the choice of aggregate dispersion affects the combined credible interval
    width. This addresses the concern that k=10 vs k=50 is an assumption.
    """
    k_values = settings.get("stochastic_overlay", {}).get(
        "k_sensitivity_values", [5.0, 10.0, 20.0, 30.0, 50.0]
    )
    base_overlay_dict = settings.get("stochastic_overlay", {})
    all_rows: list[dict[str, Any]] = []

    for k_val in k_values:
        sweep_dict = dict(base_overlay_dict)
        sweep_dict["superspreading_k"] = float(k_val)
        # Use fewer replicates for the sweep to keep runtime manageable
        sweep_dict["replicates_per_draw"] = min(
            int(base_overlay_dict.get("replicates_per_draw", 200)), 100
        )
        overlay = StochasticOverlayConfig.from_dict(sweep_dict)
        overlay_samples = stochastic_overlay_samples(summary, overlay=overlay)
        intervals = summarize_overlay_intervals(summary, overlay_samples, overlay=overlay)
        intervals["superspreading_k_sweep"] = float(k_val)
        all_rows.append(intervals)

    if all_rows:
        k_sensitivity = pd.concat(all_rows, ignore_index=True)
        write_dataframe(
            k_sensitivity,
            project_path("outputs/summaries/bayesian_k_sensitivity_sweep.csv"),
        )
        return k_sensitivity
    return pd.DataFrame()


# ---------------------------------------------------------------------------
# Convergence diagnostics
# ---------------------------------------------------------------------------

def _write_convergence_diagnostics(samples: pd.DataFrame) -> dict[str, Any]:
    """Compute and write MCMC convergence diagnostics (R-hat, ESS).

    Returns the convergence summary dict for inclusion in run metadata.
    """
    param_cols = [c for c in _sample_columns() if c in samples.columns]
    diagnostics = compute_diagnostics(
        samples,
        parameter_columns=tuple(param_cols),
        chain_column="chain",
        country_column="country",
    )
    write_dataframe(
        diagnostics,
        project_path("outputs/summaries/bayesian_convergence_diagnostics.csv"),
    )

    convergence_summary = summarize_convergence(diagnostics)

    # Write human-readable summary
    summary_path = project_path("outputs/summaries/bayesian_convergence_summary.txt")
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with summary_path.open("w", encoding="utf-8") as f:
        f.write("MCMC Convergence Summary\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"All parameters converged: {convergence_summary['all_converged']}\n")
        f.write(
            f"Parameters converged: {convergence_summary['n_parameters_converged']}"
            f" / {convergence_summary['n_parameters_total']}"
            f" ({convergence_summary.get('fraction_converged', 0):.1%})\n"
        )
        f.write(f"Worst R-hat (rank-normalized): {convergence_summary['worst_rhat']:.4f}\n")
        f.write(f"Minimum bulk ESS: {convergence_summary['min_bulk_ess']:.0f}\n")
        f.write(f"Minimum tail ESS: {convergence_summary['min_tail_ess']:.0f}\n")
        if convergence_summary["countries_with_issues"]:
            f.write(f"\nCountries with convergence issues: "
                    f"{', '.join(convergence_summary['countries_with_issues'])}\n")
        f.write("\n\nConvergence criteria:\n")
        f.write("  - R-hat (rank-normalized) < 1.05\n")
        f.write("  - Bulk ESS > 100\n")
        f.write("\nReference: Vehtari et al. (2021) Bayesian Analysis 16(2):667-718\n")

        # Per-country worst diagnostics
        f.write("\n\nPer-country worst diagnostics:\n")
        f.write("-" * 60 + "\n")
        for country in sorted(diagnostics["country"].unique()):
            country_diag = diagnostics.loc[diagnostics["country"].eq(country)]
            worst_rhat_row = country_diag.loc[country_diag["rhat_rank"].idxmax()]
            min_ess_row = country_diag.loc[country_diag["bulk_ess"].idxmin()]
            f.write(
                f"  {country}: worst R-hat={worst_rhat_row['rhat_rank']:.3f} "
                f"({worst_rhat_row['parameter']}), "
                f"min ESS={min_ess_row['bulk_ess']:.0f} "
                f"({min_ess_row['parameter']})\n"
            )

    return convergence_summary


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def _ensure_calibrated_country_starts(countries: list[str]) -> None:
    """Ensure Bayesian chains start from accepted country calibrations."""
    missing: list[str] = []
    configs = load_configs()
    vaccine = configs["baseline"]["baseline_vaccine_scenario"]
    resistance = configs["baseline"]["baseline_resistance_scenario"]
    for country in countries:
        config = make_config(
            vaccine_scenario=vaccine,
            resistance_scenario=resistance,
            country_profile=country,
        )
        if not bool(config.get("metadata", {}).get("calibration_loaded", False)):
            missing.append(country)

    if not missing:
        return

    from src_python.calibration.calibrate_baseline import calibrate_country

    for country in missing:
        calibrate_country(country)

    still_missing: list[str] = []
    for country in missing:
        config = make_config(
            vaccine_scenario=vaccine,
            resistance_scenario=resistance,
            country_profile=country,
        )
        if not bool(config.get("metadata", {}).get("calibration_loaded", False)):
            still_missing.append(country)

    if still_missing:
        raise RuntimeError(
            "Bayesian MCMC requires accepted country calibrations; missing after "
            f"auto-calibration: {', '.join(still_missing)}"
        )

def main(
    n_jobs: int | None = None,
    draws: int | None = None,
    warmup: int | None = None,
    skip_k_sensitivity: bool = False,
):
    """Run the full Bayesian uncertainty analysis pipeline.

    Steps:
    1. Run Adaptive Metropolis MCMC chains in parallel (all CPUs)
    2. Compute convergence diagnostics (R-hat, ESS)
    3. Generate posterior predictive simulations in parallel
    4. Compute credible intervals
    5. Apply stochastic overlay (superspreading + household clustering)
    6. Run k-sensitivity sweep
    7. Write all artifacts
    """
    configs = load_configs()
    settings = configs["baseline"]["bayesian_uncertainty"]
    n_chains = int(settings.get("n_chains", 4))
    chain_draws = int(draws or settings.get("draws", 2500))
    chain_warmup = int(warmup or settings.get("warmup", 1500))
    base_seed = int(settings.get("random_seed", 20260510))
    proposal_scale = float(settings.get("proposal_scale", 1.0))
    enable_trend = bool(settings.get("enable_time_varying_reporting", True))
    thin = int(settings.get("thin", 1))
    countries = list(configs["countries"])

    if bool(settings.get("require_calibrated_start", True)):
        _ensure_calibrated_country_starts(countries)

    # Build chain tasks: one per (country, chain) combination
    # All tasks run in parallel across available CPUs
    tasks = [
        ChainTask(
            country=country,
            chain=chain,
            seed=base_seed + country_idx * 1000 + chain * 137,
            warmup=chain_warmup,
            draws=chain_draws,
            proposal_scale=proposal_scale,
            enable_time_varying_reporting=enable_trend,
            thin=thin,
        )
        for country_idx, country in enumerate(countries)
        for chain in range(1, n_chains + 1)
    ]

    # Phase 1: MCMC sampling (parallelized across all chains)
    # Each chain is independent; run all (country × chain) tasks in parallel.
    # On high-core-count servers (e.g. 128-core EPYC), we can run all 40 chains
    # simultaneously. Memory per worker is ~200MB so 40 workers ≈ 8GB total.
    effective_n_jobs = n_jobs
    if effective_n_jobs is None or effective_n_jobs < 0:
        from src_python.utils.parallel import available_cpus
        cpus = available_cpus()
        # Use up to the number of tasks, leaving 4 CPUs free for system
        effective_n_jobs = min(len(tasks), max(1, cpus - 4))
    
    sample_frames = parallel_map(
        _run_chain, tasks, desc="bayesian_mcmc_chains", n_jobs=effective_n_jobs
    )
    samples = pd.concat(sample_frames, ignore_index=True)
    write_dataframe(
        samples, project_path("outputs/simulations/bayesian_posterior_samples.csv")
    )

    # Phase 2: Convergence diagnostics
    convergence_summary = _write_convergence_diagnostics(samples)
    if not convergence_summary["all_converged"]:
        import warnings
        warnings.warn(
            f"MCMC convergence issues detected: "
            f"{convergence_summary['n_parameters_converged']}"
            f"/{convergence_summary['n_parameters_total']} parameters converged. "
            f"Worst R-hat: {convergence_summary['worst_rhat']:.3f}. "
            f"Consider increasing warmup/draws.",
            stacklevel=2,
        )

    # Phase 3: Posterior predictive simulations (parallelized)
    pp_draws = int(settings.get("posterior_predictive_draws_per_country", 50))
    scenarios = _posterior_predictive_scenarios(samples, pp_draws)
    timeseries, summary = execute_scenario_list(
        scenarios, stem="bayesian_uncertainty", n_jobs=n_jobs
    )
    write_outputs(timeseries, summary, "bayesian_uncertainty")
    _write_interval_summaries(summary, samples)

    # Phase 4: Stochastic overlay
    _apply_stochastic_overlay(summary, settings)

    # Phase 5: k-sensitivity sweep (shows CrI sensitivity to dispersion choice)
    if not skip_k_sensitivity:
        _run_k_sensitivity_sweep(summary, settings)

    return timeseries, summary, samples


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run Bayesian uncertainty analysis with Adaptive Metropolis MCMC."
    )
    parser.add_argument("--n-jobs", type=int, default=None,
                        help="Number of parallel workers (-1 for all CPUs)")
    parser.add_argument("--draws", type=int, default=None,
                        help="Post-warmup draws per chain (default: 2500)")
    parser.add_argument("--warmup", type=int, default=None,
                        help="Warmup steps per chain (default: 1500)")
    parser.add_argument("--skip-k-sensitivity", action="store_true",
                        help="Skip the dispersion k sensitivity sweep")
    args = parser.parse_args()
    main(
        n_jobs=args.n_jobs,
        draws=args.draws,
        warmup=args.warmup,
        skip_k_sensitivity=args.skip_k_sensitivity,
    )
