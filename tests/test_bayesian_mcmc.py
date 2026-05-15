from __future__ import annotations

import numpy as np

from src_python.model.parameters import PreparedParameters
from src_python.simulation.common import load_configs, make_config
from src_python.simulation.run_bayesian_uncertainty import (
    _aggregate_observed_intervals,
    _apply_sample,
    _country_observed,
)


def test_monthly_bayesian_observation_aggregation_conserves_cases():
    native = _country_observed("United_States", interval="native")
    monthly = _aggregate_observed_intervals(native, "monthly")

    assert len(monthly) < len(native)
    assert np.isclose(monthly["reported_cases"].sum(), native["reported_cases"].sum())
    assert monthly["period_end"].gt(monthly["period_start"]).all()
    assert monthly["reporting_frequency"].eq("monthly_aggregated").all()


def test_time_varying_reporting_sample_is_wired_into_model_parameters():
    config = make_config(country_profile="Australia")
    config["simulation"]["start_time"] = 0.0
    config["simulation"]["end_time"] = 365.0
    sample = {
        "beta_S": float(config["transmission"]["beta_S"]),
        "reporting_multiplier": 0.5,
        "VE_sus": 0.25,
        "VE_inf": 0.25,
        "VE_dur": 0.10,
        "relative_infectiousness_asymptomatic": 0.45,
        "infectious_duration_symptomatic": 21.0,
        "infectious_duration_asymptomatic": 14.0,
        "fitness_R": 1.0,
        "resistance_prevalence": 0.05,
        "reporting_trend_end_multiplier": 1.2,
    }

    updated = _apply_sample(config, sample)
    params = PreparedParameters.from_config(
        updated,
        analysis="test",
        scenario="reporting_trend",
    )

    assert updated["reporting_time_variation"]["end_multiplier"] == 1.2
    assert np.allclose(params.reporting_rate_at(0.0), params.reporting_rate)
    assert np.allclose(params.reporting_rate_at(365.0), params.reporting_rate * 1.2)


def test_calibration_artifact_overlay_keeps_bayesian_start_calibrated():
    config = make_config(country_profile="Australia")
    baseline_beta = float(load_configs()["baseline"]["transmission"]["beta_S"])

    assert bool(config["metadata"]["calibration_loaded"])
    assert float(config["transmission"]["beta_S"]) != baseline_beta

