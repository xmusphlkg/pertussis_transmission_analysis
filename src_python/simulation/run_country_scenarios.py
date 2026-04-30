from __future__ import annotations

from src_python.simulation.common import apply_country_profile, load_configs, make_config, run_scenario_list


def main():
    configs = load_configs()
    scenarios = []
    for country in configs["countries"]:
        config = apply_country_profile(
            make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate"),
            country,
        )
        scenarios.append(
            {
                "config": config,
                "analysis": "country_profiles",
                "scenario": country,
                "vaccine_scenario": "symptom_protective",
                "resistance_scenario": "moderate",
                "metadata": {"country": country},
            }
        )
    return run_scenario_list(scenarios, stem="country_scenarios", reference_scenario="China")


if __name__ == "__main__":
    main()
