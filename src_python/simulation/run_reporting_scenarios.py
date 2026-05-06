from __future__ import annotations

from copy import deepcopy

from src_python.simulation.common import load_configs, make_config, run_scenario_list


def _apply_reporting_scenario(config: dict, scenario_def: dict) -> dict:
    out = deepcopy(config)
    out["reporting_multiplier"] = float(scenario_def["multiplier"])

    age_multipliers = scenario_def["age_multipliers"] or {}
    if age_multipliers:
        for record in out["age_groups"]:
            if record["label"] not in age_multipliers:
                raise ValueError(f"Reporting scenario is missing age multiplier for {record['label']}.")
            multiplier = float(age_multipliers[record["label"]])
            record["reporting_rate"] = min(1.0, max(0.0, float(record["reporting_rate"]) * multiplier))

    time_variation = scenario_def["time_variation"]
    if time_variation:
        required = {"start_time", "end_time", "start_multiplier", "end_multiplier"}
        missing = required.difference(time_variation)
        if missing:
            raise ValueError(f"Reporting time_variation is missing fields: {sorted(missing)}")
        out["reporting_time_variation"] = dict(time_variation)
    return out


def main():
    configs = load_configs()
    vaccine_name = configs["baseline"]["baseline_vaccine_scenario"]
    resistance_name = configs["baseline"]["baseline_resistance_scenario"]
    scenarios = []
    for country in configs["countries"]:
        for name, scenario_def in configs["baseline"]["reporting_rate_sensitivity"].items():
            config = make_config(
                vaccine_scenario=vaccine_name,
                resistance_scenario=resistance_name,
                country_profile=country,
            )
            config = _apply_reporting_scenario(config, scenario_def)
            scenarios.append(
                {
                    "config": config,
                    "analysis": "reporting_rate_sensitivity",
                    "scenario": name,
                    "vaccine_scenario": vaccine_name,
                    "resistance_scenario": resistance_name,
                    "metadata": {"reporting_scenario": name, "country": country},
                }
            )
    return run_scenario_list(scenarios, stem="reporting_scenarios", reference_scenario="medium")


if __name__ == "__main__":
    main()
