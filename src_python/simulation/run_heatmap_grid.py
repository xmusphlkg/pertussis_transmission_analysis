from __future__ import annotations

import numpy as np

from src_python.simulation.common import (
    make_config,
    run_scenario_list,
)


def main():
    ve_inf_values = np.round(np.linspace(0.0, 0.9, 10), 2)
    resistance_values = np.round(np.linspace(0.0, 1.0, 11), 2)
    scenarios = []

    for ve_inf in ve_inf_values:
        for resistance in resistance_values:
            scenario = f"VEinf_{ve_inf:.2f}_res_{resistance:.2f}"
            config = make_config(
                vaccine_scenario="symptom_protective",
                resistance_scenario="moderate",
                vaccine_overrides={"VE_inf": float(ve_inf)},
                resistance_overrides={"initial_resistance_prevalence": float(resistance)},
            )
            scenarios.append(
                {
                    "config": config,
                    "analysis": "veinf_resistance_grid",
                    "scenario": scenario,
                    "vaccine_scenario": "symptom_protective",
                    "resistance_scenario": "custom_grid",
                    "metadata": {"grid_VE_inf": float(ve_inf), "grid_resistance_prevalence": float(resistance)},
                }
            )
    return run_scenario_list(
        scenarios,
        stem="veinf_resistance_grid",
        reference_scenario="VEinf_0.00_res_0.00",
    )


if __name__ == "__main__":
    main()
