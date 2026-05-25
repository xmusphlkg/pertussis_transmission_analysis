from __future__ import annotations

import argparse
import os

from src_python.simulation.common import write_manuscript_tables
from src_python.simulation.run_age_pattern_sensitivity import main as run_age_pattern_sensitivity
from src_python.simulation.run_bayesian_uncertainty import main as run_bayesian_uncertainty
from src_python.simulation.run_baseline import main as run_baseline
from src_python.simulation.run_country_scenarios import main as run_countries
from src_python.simulation.run_fitness_grid import main as run_fitness_grid
from src_python.simulation.run_heatmap_grid import main as run_heatmap
from src_python.simulation.run_immunity_sensitivity import main as run_immunity
from src_python.simulation.run_intervention_scenarios import main as run_interventions
from src_python.simulation.run_reporting_scenarios import main as run_reporting
from src_python.simulation.run_resistance_fitness_sensitivity import main as run_resistance_fitness
from src_python.simulation.run_resistance_hindcast import main as run_hindcast
from src_python.simulation.run_resistance_mechanism_decomposition import main as run_resistance_mechanism
from src_python.simulation.run_resistance_scenarios import main as run_resistance
from src_python.simulation.run_routine_timeliness_sensitivity import main as run_routine_timeliness
from src_python.simulation.run_sensitivity import main as run_sensitivity
from src_python.simulation.run_vaccine_scenarios import main as run_vaccines


BAYESIAN_FIXED_PARAMETERS = (
    "reporting_multiplier",
    "VE_sus",
    "VE_inf",
    "relative_infectiousness_asymptomatic",
    "fitness_R",
)


def main(n_jobs: int | None = None, include_bayesian: bool = False) -> None:
    if n_jobs is not None:
        os.environ["PERTUSSIS_N_JOBS"] = str(n_jobs)

    run_baseline()
    run_vaccines()
    run_resistance()
    run_reporting()
    run_countries()
    run_heatmap()
    run_fitness_grid(n_jobs=n_jobs)
    run_interventions()
    run_age_pattern_sensitivity()
    run_routine_timeliness(n_jobs=n_jobs)
    run_sensitivity()
    run_immunity()
    run_resistance_fitness(n_jobs=n_jobs)
    run_resistance_mechanism(n_jobs=n_jobs)
    run_hindcast()
    if include_bayesian:
        run_bayesian_uncertainty(
            n_jobs=n_jobs,
            solver_mode="calibration",
            sampler="beta_grid",
            proposal_scale=1.0,
            warmup=0,
            draws=250,
            fix_durations=True,
            fixed_parameters=BAYESIAN_FIXED_PARAMETERS,
            grid_points=81,
            grid_log_beta_half_width=0.08,
            grid_max_points=321,
            grid_max_refinements=5,
            grid_smoothing="auto",
        )
    write_manuscript_tables()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the full pertussis simulation suite.")
    parser.add_argument(
        "--n-jobs",
        type=int,
        default=None,
        help="Optional parallel worker cap for all scenario stages.",
    )
    parser.add_argument(
        "--include-bayesian",
        action="store_true",
        help="Also run the beta-grid Bayesian uncertainty target with pre-specified checks.",
    )
    args = parser.parse_args()
    main(n_jobs=args.n_jobs, include_bayesian=args.include_bayesian)
