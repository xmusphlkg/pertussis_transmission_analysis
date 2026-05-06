from __future__ import annotations

from src_python.simulation.common import load_configs, make_config, run_scenario_list


def main():
    configs = load_configs()
    vaccine_name = configs["baseline"]["baseline_vaccine_scenario"]
    resistance_name = configs["baseline"]["baseline_resistance_scenario"]
    scenarios = []
    for country in configs["countries"]:
        config = make_config(
            vaccine_scenario=vaccine_name,
            resistance_scenario=resistance_name,
            country_profile=country,
        )
        scenarios.append(
            {
                "config": config,
                "analysis": "country_profiles",
                "scenario": country,
                "vaccine_scenario": vaccine_name,
                "resistance_scenario": resistance_name,
                "metadata": {"country": country},
            }
        )
    return run_scenario_list(scenarios, stem="country_scenarios", reference_scenario="China")


if __name__ == "__main__":
    main()
