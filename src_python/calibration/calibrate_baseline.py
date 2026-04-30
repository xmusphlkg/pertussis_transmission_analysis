from __future__ import annotations

from copy import deepcopy

import numpy as np
from scipy.optimize import minimize

from src_python.calibration.likelihood import squared_error_loss
from src_python.simulation.common import make_config, run_prepared_config
from src_python.utils.io import project_path, read_table, write_dataframe


def objective(log_params: np.ndarray) -> float:
    beta_s, initial_exposed_per_100k = np.exp(log_params)
    config = make_config(vaccine_scenario="symptom_protective", resistance_scenario="moderate")
    config = deepcopy(config)
    config["transmission"]["beta_S"] = float(beta_s)
    config["initial_conditions"]["initial_exposed_per_100k"] = float(initial_exposed_per_100k)
    _, summary = run_prepared_config(
        config,
        analysis="calibration",
        scenario="candidate",
        vaccine_scenario="symptom_protective",
        resistance_scenario="moderate",
    )
    targets = read_table(project_path("data/processed/calibration_targets.csv"))
    infant_target = float(targets.loc[targets["target"].eq("infant_reported_case_fraction"), "value"].iloc[0])
    annual_target = float(targets.loc[targets["target"].eq("annual_reported_cases_per_100k"), "value"].iloc[0])
    total_reported = float(summary["total_reported_cases"].iloc[0])
    infant_reported_proxy = float(summary["total_infant_cases"].iloc[0] / max(summary["total_symptomatic_cases"].iloc[0], 1e-9))
    annual_per_100k = total_reported / (3.0 * 1000.4)
    return squared_error_loss(
        np.array([infant_target, annual_target]),
        np.array([infant_reported_proxy, annual_per_100k]),
    )


def main() -> None:
    start = np.log(np.array([0.055, 2.5]))
    result = minimize(objective, start, method="Nelder-Mead", options={"maxiter": 20})
    output = {
        "beta_S": float(np.exp(result.x[0])),
        "initial_exposed_per_100k": float(np.exp(result.x[1])),
        "objective": float(result.fun),
        "success": bool(result.success),
    }
    write_dataframe(__import__("pandas").DataFrame([output]), project_path("outputs/tables/calibration_placeholder.csv"))


if __name__ == "__main__":
    main()
