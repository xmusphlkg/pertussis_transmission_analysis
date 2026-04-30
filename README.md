# Pertussis Vaccine and Macrolide Resistance Model

This repository implements an age-structured deterministic transmission model of pertussis to evaluate how imperfect vaccine transmission-blocking effects and macrolide resistance jointly influence pertussis control. The model is implemented in Python. Simulation outputs are exported in tidy CSV and parquet formats and visualized in R.

Main analyses:

1. Vaccine mechanism scenarios
2. Macrolide resistance scenarios
3. Vaccine transmission-blocking by resistance prevalence heatmap
4. Intervention strategy comparison
5. Global sensitivity analysis
6. Reporting-rate sensitivity analysis
7. Country profile sensitivity analysis

## Quick Start

Create the recommended conda environment:

```bash
conda create -y -n pertussis_model -c conda-forge python=3.11 numpy pandas scipy pyyaml pydantic tqdm joblib matplotlib pyarrow pytest
conda activate pertussis_model
```

Run all Python analyses:

```bash
python -m src_python.simulation.run_all
```

Independent scenario simulations run in parallel across available CPU cores by default. To limit parallelism:

```bash
PERTUSSIS_N_JOBS=32 python -m src_python.simulation.run_all
```

The default model now runs for 20 simulated years with weekly output. Long-run dynamics include demographic turnover, routine vaccination maintenance, low-level importation, annual seasonality, and a configurable 4-year multi-year forcing term. Treat the multi-year term as a calibration/sensitivity device unless supported by fitted data.

Run validation and tests:

```bash
python -m src_python.utils.validation
pytest
```

Generate figures with R:

```bash
Rscript scripts_R/00_setup.R
Rscript scripts_R/01_plot_model_structure.R
Rscript scripts_R/02_plot_vaccine_scenarios.R
Rscript scripts_R/03_plot_resistance_scenarios.R
Rscript scripts_R/04_plot_heatmaps.R
Rscript scripts_R/05_plot_intervention_comparison.R
Rscript scripts_R/06_plot_sensitivity.R
Rscript scripts_R/07_plot_reporting_scenarios.R
Rscript scripts_R/08_plot_country_scenarios.R
```

## Repository Layout

```text
config/              YAML scenario and parameter files
data/                Synthetic placeholder data and processed inputs
src_python/model/    Deterministic ODE model implementation
src_python/simulation/ Scenario runners
src_python/calibration/ Light-touch calibration placeholders
src_python/utils/    I/O and validation helpers
scripts_R/           Manuscript figure scripts
outputs/             Generated simulations, summaries, figures, tables
manuscript_notes/    Generated parameter and scenario tables
tests/               Unit tests
```

## Important Interpretation Note

This is a mechanistic modelling and scenario-analysis scaffold. Default parameter values are plausible placeholders designed for reproducible computation, not definitive epidemiological estimates. Manuscript claims should use cautious language such as "under plausible assumptions" and "in scenario analyses."

Country profiles in `config/country_profiles.yaml` are synthetic placeholders. Replace them with real population, birth-rate, vaccine-history, and contact-matrix inputs before making country-specific claims.
