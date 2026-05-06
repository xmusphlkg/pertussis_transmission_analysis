from __future__ import annotations

from copy import deepcopy

import numpy as np
import pandas as pd
from scipy.stats import qmc

from src_python.simulation.common import execute_scenario_list, load_configs, make_config, write_outputs
from src_python.utils.io import set_by_dotted_path


def _apply_sample(config: dict, sample: dict[str, float]) -> dict:
    out = deepcopy(config)
    for path, value in sample.items():
        if path == "reporting_multiplier":
            out["reporting_multiplier"] = value
        elif path == "rates.waning_vaccine":
            previous_recent = float(out["natural_history"]["vaccine_protection_duration"])
            previous_waned = float(out["immunity_model"]["waned_vaccine_duration"])
            waned_ratio = previous_waned / previous_recent if previous_recent > 0.0 else 1.0
            duration = 1.0 / max(value, 1e-12)
            out["natural_history"]["vaccine_protection_duration"] = duration
            out["immunity_model"]["waned_vaccine_duration"] = duration * waned_ratio
        elif path == "rates.waning_natural":
            duration = 1.0 / max(value, 1e-12)
            out["natural_history"]["recovered_immunity_duration"] = duration
        else:
            set_by_dotted_path(out, path, value)
    return out


def main():
    configs = load_configs()
    sensitivity = configs["sensitivity"]
    names = list(sensitivity["parameters"].keys())
    specs = [sensitivity["parameters"][name] for name in names]
    lower = np.array([spec["min"] for spec in specs], dtype=float)
    upper = np.array([spec["max"] for spec in specs], dtype=float)
    sample_size = int(sensitivity["sample_size"])
    seed = int(sensitivity["random_seed"])

    sampler = qmc.LatinHypercube(d=len(names), seed=seed)
    sample_matrix = qmc.scale(sampler.random(sample_size), lower, upper)

    scenarios = []
    vaccine_name = configs["baseline"]["baseline_vaccine_scenario"]
    resistance_name = configs["baseline"]["baseline_resistance_scenario"]
    country = configs["baseline"]["baseline_country_profile"]
    base_config = make_config(
        vaccine_scenario=vaccine_name,
        resistance_scenario=resistance_name,
        country_profile=country,
    )
    for run_idx, row in enumerate(sample_matrix, start=1):
        sampled_values = {specs[i]["path"]: float(row[i]) for i in range(len(names))}
        config = _apply_sample(base_config, sampled_values)
        metadata = {names[i]: float(row[i]) for i in range(len(names))}
        metadata["country"] = country
        scenario = f"lhs_{run_idx:03d}"
        scenarios.append(
            {
                "config": config,
                "analysis": "sensitivity",
                "scenario": scenario,
                "vaccine_scenario": "sampled",
                "resistance_scenario": resistance_name,
                "metadata": metadata,
            }
        )

    timeseries, summary = execute_scenario_list(scenarios, stem="sensitivity_lhs")
    _add_tornado_metrics(summary, names)
    write_outputs(timeseries, summary, "sensitivity_runs")
    return timeseries, summary


def _add_tornado_metrics(summary: pd.DataFrame, parameter_names: list[str]) -> None:
    outcome = summary["total_infant_cases"].to_numpy(dtype=float)
    for name in parameter_names:
        x = summary[name].to_numpy(dtype=float)
        if np.std(x) == 0 or np.std(outcome) == 0:
            summary[f"corr_{name}_infant_cases"] = 0.0
        else:
            summary[f"corr_{name}_infant_cases"] = float(np.corrcoef(x, outcome)[0, 1])


if __name__ == "__main__":
    main()
