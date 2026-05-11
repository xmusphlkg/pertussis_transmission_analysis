from __future__ import annotations

import argparse
from typing import Any

import numpy as np

from src_python.simulation.common import load_configs, make_config, run_scenario_list


def _grid_values(settings: dict[str, Any], key: str, default: list[float]) -> list[float]:
    values = settings.get(key, default)
    return [float(value) for value in values]


def main(n_jobs: int | None = None):
    configs = load_configs()
    grid_settings = configs["baseline"].get("fitness_grid", {})
    resistance_name = configs["baseline"].get("baseline_resistance_scenario", "country_timeline")
    fitness_values = _grid_values(
        grid_settings,
        "fitness_R_values",
        [0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25],
    )
    ve_inf_values = _grid_values(grid_settings, "VE_inf_values", [0.08, 0.25, 0.40, 0.60, 0.75])

    scenarios = []
    for country in configs["countries"]:
        for fitness_r in fitness_values:
            for ve_inf in ve_inf_values:
                scenario = f"fitness_{fitness_r:.2f}_VEinf_{ve_inf:.2f}"
                config = make_config(
                    vaccine_scenario="symptom_protective",
                    resistance_scenario=resistance_name,
                    country_profile=country,
                    vaccine_overrides={"VE_inf": float(ve_inf)},
                    resistance_overrides={"fitness_R": float(fitness_r)},
                )
                scenarios.append(
                    {
                        "config": config,
                        "analysis": "fitness_resistance_grid",
                        "scenario": scenario,
                        "vaccine_scenario": "symptom_protective",
                        "resistance_scenario": resistance_name,
                        "metadata": {
                            "country": country,
                            "grid_fitness_R": float(fitness_r),
                            "grid_VE_inf": float(ve_inf),
                        },
                    }
                )

    reference_fitness = min(fitness_values, key=lambda value: abs(value - 0.70))
    reference_ve_inf = min(ve_inf_values, key=lambda value: abs(value - 0.08))
    reference = f"fitness_{reference_fitness:.2f}_VEinf_{reference_ve_inf:.2f}"
    return run_scenario_list(
        scenarios,
        stem="fitness_resistance_grid",
        reference_scenario=reference,
        n_jobs=n_jobs,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run continuous resistant-fitness and VE_inf stress grid.")
    parser.add_argument("--n-jobs", type=int, default=None)
    args = parser.parse_args()
    main(n_jobs=args.n_jobs)
