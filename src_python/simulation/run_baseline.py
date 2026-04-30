from __future__ import annotations

from src_python.simulation.common import make_config, run_prepared_config, write_outputs


def main() -> None:
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    timeseries, summary = run_prepared_config(
        config,
        analysis="baseline",
        scenario="baseline",
        vaccine_scenario="symptom_protective",
        resistance_scenario="moderate",
    )
    write_outputs(timeseries, summary, "baseline_timeseries")


if __name__ == "__main__":
    main()
