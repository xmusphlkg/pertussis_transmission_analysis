# Pertussis Vaccine and Macrolide Resistance Model

This repository implements an age-structured deterministic transmission model of pertussis to evaluate how imperfect vaccine transmission-blocking effects and macrolide resistance jointly influence pertussis control. The model is implemented in Python. Simulation outputs are exported in tidy CSV and parquet formats and visualized in R.

Main analyses:

1. Vaccine mechanism scenarios
2. Macrolide resistance scenarios
3. Vaccine transmission-blocking by resistance prevalence heatmap
4. Intervention strategy comparison
5. Global sensitivity analysis
6. Reporting-rate sensitivity analysis
7. Multi-country profile analysis

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

The default model runs for 30 simulated analysis years after a 60-year burn-in, with weekly output. Long-run dynamics include demographic turnover, routine vaccination maintenance, low-level importation, country-specific annual seasonality, country-specific contact matrices, and a weak multi-year phase-locking term used to represent observed 3-5 year pertussis recurrence. Treat the multi-year term as a calibration/sensitivity device, not as proof of a causal oscillator.

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
config/              Central settings plus generated scenario/profile YAML files
data/                Local raw external extracts and processed model inputs
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

This is a mechanistic modelling and scenario-analysis project, not a definitive country calibration. Manuscript claims should use cautious language such as "under plausible assumptions" and "in scenario analyses."

Model settings are centralized in `config/model_settings.yaml`, including source notes for the major parameter blocks. Country profiles use WPP population denominators, local PertussisIncidence surveillance extracts, vaccine coverage/schedule metadata, and Prem/contactdata contact matrices aggregated to the five model age groups.
