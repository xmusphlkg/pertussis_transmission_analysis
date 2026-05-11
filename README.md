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
python -m src_python.calibration.run_all
python -m src_python.simulation.run_all
```

Independent scenario simulations run in parallel across available CPU cores by default. To limit parallelism:

```bash
PERTUSSIS_N_JOBS=32 python -m src_python.simulation.run_all
```

You can also set the worker cap explicitly on the new CLI:

```bash
python -m src_python.simulation.run_all --n-jobs 32
```

The default model runs for 30 calendar-mapped analysis years after a 60-year burn-in, with weekly output. Simulation time is stored as days since `calendar.analysis_start_date`, and outputs include `calendar_date`/`calendar_year`; calibration overrides the analysis start date to the first observed surveillance year and splits modelled reporting intervals across calendar-year boundaries so model and observed annual cases align by real calendar year. Long-run dynamics include demographic turnover, routine vaccination maintenance, low-level importation, country-specific annual seasonality, and country-specific contact matrices. A weak multi-year phase-locking term can be enabled for countries where surveillance supports 3-5 year recurrence, but the baseline amplitude is zero and the term should be treated as a calibration/sensitivity device, not as proof of a causal oscillator.

Resistance scenarios now target the resistant fraction at the start of the saved analysis period. The burn-in first establishes total pertussis dynamics, then strain-specific exposed, infectious, and treated states are rebalanced to the scenario target before analysis output begins. This avoids interpreting long burn-in strain fixation as the intended low/moderate/high resistance scenario.

The default baseline resistance scenario is `country_timeline`, which reads `data/raw/country_resistance_timeline.csv` and uses `config/model_settings.yaml::runtime.data_sources.resistance_anchor_year` to select country-specific resistance anchors. Future evidence is disallowed unless a scenario explicitly opts into it. The selected anchor is written into `resistance.target_prevalence_at_analysis_start`, `resistance.importation_fraction`, `importation.resistant_fraction`, and `initial_conditions.initial_resistance_prevalence`. The raw timeline mixes measured surveillance/isolate rows with conservative low anchors where public numeric estimates were not found, and it includes a `sample_size` column when the source reports a denominator.

The epidemiologic baseline uses the harmonized surveillance intervals in `data/raw/external/Pertussis Incidence Report.xlsx` with `incidence_cutoff_policy: all_records`, so incidence-derived seasonality, reported-incidence summaries, and calibration can use all available complete or partial reporting intervals. Resistance anchoring intentionally uses 2025 evidence.

Maternal protection and dose history are represented as explicit susceptible-origin states: `M_protected`, dose-1 recent/waned, dose-2 recent/waned, and dose-3-plus recent/waned. Exposed, infectious, and treated infections retain that source history, so `VE_sym`, `VE_inf`, and `VE_dur` act on the infection source rather than on a point-in-time aggregate proxy.

Generated outputs now include `outputs/metadata/*_run_metadata.json` with a configuration hash, git state, dependency versions, and row counts. Validation refuses to silently read outputs that do not match the current runtime configuration.

Run validation and tests:

```bash
python -m src_python.utils.validation
pytest
```

Run a country calibration pass:

```bash
python -m src_python.calibration.calibrate_baseline --country Australia
```

Run the full country calibration set in parallel:

```bash
python -m src_python.calibration.run_all --n-jobs 4
```

Generate figures with R:

```bash
Rscript scripts_R/00_setup.R
Rscript scripts_R/10_plot_nature_figure_set.R
```

You can also run individual figure scripts directly:

```bash
Rscript scripts_R/11_plot_nature_figure_1_baseline_heterogeneity.R
Rscript scripts_R/12_plot_nature_figure_2_vaccine_mechanisms.R
Rscript scripts_R/13_plot_nature_figure_3_resistance_interaction.R
Rscript scripts_R/14_plot_nature_figure_4_intervention_prioritisation.R
Rscript scripts_R/15_plot_nature_extended_data_1_country_inputs.R
Rscript scripts_R/16_plot_nature_extended_data_2_diagnostics_sensitivity.R
Rscript scripts_R/17_plot_nature_extended_data_3_data_provenance.R
Rscript scripts_R/18_plot_nature_extended_data_4_calibration_diagnostics.R
Rscript scripts_R/19_plot_nature_extended_data_5_model_architecture.R
Rscript scripts_R/20_plot_nature_extended_data_6_baseline_dynamics.R
Rscript scripts_R/21_plot_nature_extended_data_7_vaccine_deep_dive.R
Rscript scripts_R/22_plot_nature_extended_data_8_resistance_dynamics.R
Rscript scripts_R/23_plot_nature_extended_data_9_full_grid.R
Rscript scripts_R/24_plot_nature_extended_data_10_intervention_extended.R
Rscript scripts_R/25_plot_nature_extended_data_11_model_structure.R
Rscript scripts_R/26_plot_nature_extended_data_12_contact_matrix_reconstruction.R
```

Main figures are written to `outputs/figures/` and Extended Data figures are written to `outputs/appendix/`.
The figure legend and panel-by-panel notes live in `manuscript_notes/figure_legend.md`.

## Repository Layout

```text
config/              Central settings plus generated scenario/profile YAML files
data/                Local raw external extracts and processed model inputs
src_python/model/    Deterministic ODE model implementation
src_python/simulation/ Scenario runners
src_python/calibration/ Country-level calibration helpers
src_python/utils/    I/O and validation helpers
scripts_R/           Manuscript figure scripts
outputs/             Generated simulations, summaries, figures, tables
manuscript_notes/    Generated parameter and scenario tables
tests/               Unit tests
```

## Important Interpretation Note

This is a mechanistic modelling project with optional country-level calibration artifacts. Scenario runners automatically prefer accepted calibration outputs in `outputs/calibrations/` when they exist; otherwise the outputs remain exploratory scenario analyses. Manuscript claims should use cautious language such as "under plausible assumptions" and distinguish calibrated from exploratory results.

Model settings are centralized in `config/model_settings.yaml`, including source notes for the major parameter blocks. The legacy YAML files in `config/` are generated mirrors of the runtime blocks and are checked in tests. Country profiles use WPP population denominators, local PertussisIncidence surveillance extracts, WHO/JRF annual reported case and schedule extracts, vaccine coverage/schedule metadata, and Prem/contactdata contact matrices aggregated to the five model age groups.
