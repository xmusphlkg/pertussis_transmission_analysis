from __future__ import annotations

from src_python.simulation.common import load_configs, make_config, run_prepared_config, write_outputs


def main() -> None:
    configs = load_configs()
    country = configs["baseline"].get("baseline_country_profile", "China")
    config = make_config(
        vaccine_scenario="symptom_protective",
        resistance_scenario="moderate",
        country_profile=country,
    )
    timeseries, summary = run_prepared_config(
        config,
        analysis="baseline",
        scenario="baseline",
        vaccine_scenario="symptom_protective",
        resistance_scenario="moderate",
        metadata={"country": country},
    )
    write_outputs(timeseries, summary, "baseline_timeseries")


if __name__ == "__main__":
    main()
