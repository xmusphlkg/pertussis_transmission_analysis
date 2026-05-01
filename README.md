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
python -m src_python.data.build_who_inputs
python -m src_python.simulation.run_all
```

Independent scenario simulations run in parallel across available CPU cores by default. To limit parallelism:

```bash
PERTUSSIS_N_JOBS=32 python -m src_python.simulation.run_all
```

The default model runs for 30 simulated analysis years after a 60-year burn-in, with weekly output. Long-run dynamics include demographic turnover, routine vaccination maintenance, low-level importation, country-specific annual seasonality, and country-specific contact matrices. A weak multi-year phase-locking term can be enabled for countries where surveillance supports 3-5 year recurrence, but the baseline amplitude is zero and the term should be treated as a calibration/sensitivity device, not as proof of a causal oscillator.

Resistance scenarios now target the resistant fraction at the start of the saved analysis period. The burn-in first establishes total pertussis dynamics, then strain-specific exposed, infectious, and treated states are rebalanced to the scenario target before analysis output begins. This avoids interpreting long burn-in strain fixation as the intended low/moderate/high resistance scenario.

The default baseline resistance scenario is `country_timeline`, which reads `data/raw/country_resistance_timeline.csv` and uses `config/data_sources.yaml::analysis_year` to interpolate or select the nearest country-specific resistance anchor. That anchor is written into `resistance.target_prevalence_at_analysis_start`, `resistance.importation_fraction`, `importation.resistant_fraction`, and `initial_conditions.initial_resistance_prevalence`. Rows labelled as `measured_*` use surveillance or isolate-study estimates; rows labelled as `*_model_anchor` are explicit low/imported modelling anchors for settings where public country-specific fractions were not found. The older `data/raw/resistance_data.csv` file is retained only as a deprecated planning placeholder and is not used as global resistance evidence.

The vaccine state is split into recent and waned vaccine-derived protection proxy states. The model still remains an age-structured ODE scenario model, but this prevents all vaccinated people from sharing one protection level throughout long simulations.

Run validation and tests:

```bash
python -m src_python.utils.validation
pytest
```

Run a country calibration pass:

```bash
python -m src_python.calibration.calibrate_baseline --country Australia
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
Rscript scripts_R/09_plot_calibration_diagnostics.R
```

## Repository Layout

```text
config/              Central settings plus generated scenario/profile YAML files
data/                Local raw external extracts and processed model inputs
src_python/model/    Deterministic ODE model implementation
src_python/simulation/ Scenario runners
src_python/calibration/ Country-level calibration and posterior predictive helpers
src_python/utils/    I/O and validation helpers
scripts_R/           Manuscript figure scripts
outputs/             Generated simulations, summaries, figures, tables
manuscript_notes/    Generated parameter and scenario tables
tests/               Unit tests
```

## Important Interpretation Note

This is a mechanistic modelling and scenario-analysis project, not a definitive country calibration. Manuscript claims should use cautious language such as "under plausible assumptions" and "in scenario analyses."

Model settings are centralized in `config/model_settings.yaml`, including source notes for the major parameter blocks. Country profiles use WPP population denominators, local PertussisIncidence surveillance extracts, WHO/JRF annual reported case and schedule extracts, vaccine coverage/schedule metadata, and Prem/contactdata contact matrices aggregated to the five model age groups.
