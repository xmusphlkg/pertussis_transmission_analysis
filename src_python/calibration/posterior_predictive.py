from __future__ import annotations

import pandas as pd

from src_python.simulation.common import make_config, run_prepared_config
from src_python.utils.io import project_path, write_dataframe


def main() -> None:
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    frames = []
    for beta_scale in [0.9, 1.0, 1.1]:
        candidate = dict(config)
        candidate["transmission"] = dict(config["transmission"])
        candidate["transmission"]["beta_S"] = config["transmission"]["beta_S"] * beta_scale
        ts, _ = run_prepared_config(
            candidate,
            analysis="posterior_predictive_placeholder",
            scenario=f"beta_scale_{beta_scale:.1f}",
            vaccine_scenario="symptom_protective",
            resistance_scenario="moderate",
        )
        frames.append(ts)
    write_dataframe(pd.concat(frames, ignore_index=True), project_path("outputs/simulations/posterior_predictive_placeholder.parquet"))


if __name__ == "__main__":
    main()
