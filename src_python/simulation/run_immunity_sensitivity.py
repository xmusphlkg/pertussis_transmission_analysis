"""Immunity structure sensitivity analysis.

Compares the current waning-only immunity model against alternative structures:
1. Baseline (waning-only): S → E → I → R → S with exponential waning
2. Long natural immunity: 15-year post-infection protection
3. Short vaccine immunity: 3-year vaccine waning (faster than baseline 5y)
4. SIRWS-like boosting proxy: Very long natural immunity + faster vaccine waning

This addresses the concern (Wearing & Rohani 2009; Lavine et al. 2011) that
pertussis models are sensitive to immunity structure assumptions, particularly
whether natural boosting maintains population immunity.

Since the model does not have an explicit SIRWS boosting state, we approximate
the effect by varying waning durations to bracket the plausible range.

Usage:
    python -m src_python.simulation.run_immunity_sensitivity
"""
from __future__ import annotations

from copy import deepcopy

from src_python.simulation.common import load_configs, make_config, run_scenario_list


IMMUNITY_STRUCTURES = {
    "baseline_waning_only": {
        "description": "Current model: 9-year natural immunity, 5-year vaccine protection.",
        "overrides": {},
    },
    "long_natural_immunity": {
        "description": "Extended natural immunity (15 years) simulating strong natural boosting.",
        "overrides": {
            "natural_history": {
                "recovered_immunity_duration": 5475.0,  # 15 years
            },
        },
    },
    "short_vaccine_immunity": {
        "description": "Faster vaccine waning (3 years) representing rapid aP decline.",
        "overrides": {
            "natural_history": {
                "vaccine_protection_duration": 1095.0,  # 3 years
            },
        },
    },
    "sirws_proxy_boosting": {
        "description": (
            "SIRWS-like proxy: very long natural immunity (20y) + short vaccine (3y). "
            "Approximates a model where natural infection provides durable protection "
            "maintained by subclinical re-exposure, while vaccine immunity wanes quickly."
        ),
        "overrides": {
            "natural_history": {
                "recovered_immunity_duration": 7300.0,  # 20 years
                "vaccine_protection_duration": 1095.0,  # 3 years
            },
        },
    },
}


def main():
    configs = load_configs()
    resistance_name = configs["baseline"].get("baseline_resistance_scenario", "country_timeline")
    scenarios = []

    for country in configs["countries"]:
        for name, spec in IMMUNITY_STRUCTURES.items():
            config = make_config(
                vaccine_scenario="symptom_protective",
                resistance_scenario=resistance_name,
                country_profile=country,
            )
            # Apply immunity structure overrides
            overrides = spec.get("overrides", {})
            if "natural_history" in overrides:
                for key, value in overrides["natural_history"].items():
                    config["natural_history"][key] = value

            scenarios.append(
                {
                    "config": config,
                    "analysis": "immunity_structure_sensitivity",
                    "scenario": name,
                    "vaccine_scenario": "symptom_protective",
                    "resistance_scenario": resistance_name,
                    "metadata": {
                        "country": country,
                        "immunity_structure": name,
                        "description": spec["description"],
                    },
                }
            )

    return run_scenario_list(
        scenarios,
        stem="immunity_sensitivity",
        reference_scenario="baseline_waning_only",
    )


if __name__ == "__main__":
    main()
