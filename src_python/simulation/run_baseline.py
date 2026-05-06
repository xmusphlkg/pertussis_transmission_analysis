from __future__ import annotations

from src_python.simulation.common import load_configs, make_config, run_prepared_config, write_outputs


def main() -> None:
    configs = load_configs()
    country = configs["baseline"]["baseline_country_profile"]
    vaccine_name = configs["baseline"]["baseline_vaccine_scenario"]
    resistance_name = configs["baseline"]["baseline_resistance_scenario"]
    config = make_config(
        vaccine_scenario=vaccine_name,
        resistance_scenario=resistance_name,
        country_profile=country,
    )
    timeseries, summary = run_prepared_config(
        config,
        analysis="baseline",
        scenario="baseline",
        vaccine_scenario=vaccine_name,
        resistance_scenario=resistance_name,
        metadata={"country": country},
    )
    write_outputs(timeseries, summary, "baseline_timeseries")


if __name__ == "__main__":
    main()
