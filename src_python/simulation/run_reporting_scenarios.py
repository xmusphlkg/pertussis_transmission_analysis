from __future__ import annotations

from copy import deepcopy

from src_python.simulation.common import load_configs, make_config, run_scenario_list
from src_python.utils.io import deep_update


def _apply_reporting_scenario(config: dict, scenario_def: dict) -> dict:
    out = deepcopy(config)
    out["reporting_multiplier"] = float(scenario_def.get("multiplier", 1.0))

    age_multipliers = scenario_def.get("age_multipliers", {})
    if age_multipliers:
        for record in out["age_groups"]:
            multiplier = float(age_multipliers.get(record["label"], 1.0))
            record["reporting_rate"] = min(1.0, max(0.0, float(record["reporting_rate"]) * multiplier))

    time_variation = scenario_def.get("time_variation")
    if time_variation:
        out["reporting_time_variation"] = deep_update(
            {
                "start_time": out["simulation"]["start_time"],
                "end_time": out["simulation"]["end_time"],
                "start_multiplier": 1.0,
                "end_multiplier": 1.0,
            },
            time_variation,
        )
    return out


def main():
    configs = load_configs()
    scenarios = []
    for name, scenario_def in configs["baseline"]["reporting_rate_sensitivity"].items():
        config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
        config = _apply_reporting_scenario(config, scenario_def)
        scenarios.append(
            {
                "config": config,
                "analysis": "reporting_rate_sensitivity",
                "scenario": name,
                "vaccine_scenario": "symptom_protective",
                "resistance_scenario": "moderate",
                "metadata": {"reporting_scenario": name},
            }
        )
    return run_scenario_list(scenarios, stem="reporting_scenarios", reference_scenario="medium")


if __name__ == "__main__":
    main()
