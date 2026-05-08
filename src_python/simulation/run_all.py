from __future__ import annotations

import argparse
import os

from src_python.simulation.common import write_manuscript_tables
from src_python.simulation.run_baseline import main as run_baseline
from src_python.simulation.run_country_scenarios import main as run_countries
from src_python.simulation.run_heatmap_grid import main as run_heatmap
from src_python.simulation.run_intervention_scenarios import main as run_interventions
from src_python.simulation.run_reporting_scenarios import main as run_reporting
from src_python.simulation.run_resistance_scenarios import main as run_resistance
from src_python.simulation.run_sensitivity import main as run_sensitivity
from src_python.simulation.run_vaccine_scenarios import main as run_vaccines


def main(n_jobs: int | None = None) -> None:
    if n_jobs is not None:
        os.environ["PERTUSSIS_N_JOBS"] = str(n_jobs)

    run_baseline()
    run_vaccines()
    run_resistance()
    run_reporting()
    run_countries()
    run_heatmap()
    run_interventions()
    run_sensitivity()
    write_manuscript_tables()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the full pertussis simulation suite.")
    parser.add_argument(
        "--n-jobs",
        type=int,
        default=None,
        help="Optional parallel worker cap for all scenario stages.",
    )
    args = parser.parse_args()
    main(n_jobs=args.n_jobs)
