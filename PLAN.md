
# Project Plan for Codex Agent

## Project Title

**Impact of Imperfect Transmission-Blocking Vaccination and Macrolide Resistance on Pertussis Control: An Age-Structured Transmission Dynamic Modelling Study**

---

## 1. Scientific Rationale

Pertussis remains difficult to control even in populations with high vaccine coverage. A key mechanism is that acellular pertussis vaccines may protect against clinical disease more effectively than they prevent colonization, infection, or onward transmission. Experimental baboon studies showed that acellular pertussis vaccination protected against symptoms but did not fully prevent colonization or transmission. ([美国国家科学院院刊][1])

At the same time, macrolides remain central to pertussis treatment and post-exposure prophylaxis, but antibiotic choice may depend on resistance patterns. CDC guidance supports macrolides for treatment and PEP, while noting that resistance patterns may affect antibiotic selection. ([疾病控制与预防中心][2])

Macrolide-resistant *Bordetella pertussis* has become a major concern in China. A Shanghai genomic surveillance study using isolates from 2018–2024 reported that macrolide resistance increased from ≤50% before 2020 to nearly 100% afterward, with resistant isolates carrying the 23S rRNA A2047G mutation. ([PMC][3])

Therefore, this project will use a transmission dynamic model to evaluate how two mechanisms interact:

1. Vaccines that reduce symptoms but incompletely block infection or transmission.
2. Macrolide resistance that reduces the effectiveness of treatment and post-exposure prophylaxis.

---

## 2. Main Research Question

**How do imperfect transmission-blocking vaccination and macrolide resistance jointly affect pertussis transmission, hidden infections, infant cases, and the effectiveness of control strategies?**

---

## 3. Specific Objectives

### Objective 1

Quantify how different vaccine mechanisms affect the relationship between reported symptomatic cases and total infections.

### Objective 2

Evaluate how increasing macrolide resistance alters transmission, outbreak duration, infant infections, and the benefit of treatment or post-exposure prophylaxis.

### Objective 3

Assess the interaction between vaccine transmission-blocking ability and macrolide resistance.

### Objective 4

Compare intervention strategies, including booster vaccination, maternal immunization, resistance-guided treatment, and next-generation transmission-blocking vaccine scenarios.

---

## 4. Overall Computational Strategy

Use:

* **Python** for model implementation, simulation, calibration, uncertainty analysis, and exporting tidy outputs.
* **R** for figure generation and manuscript-ready visualization.
* Data exchange between Python and R using `.csv` or `.parquet`.

Recommended workflow:

```text
Python:
    define model
    load parameters
    run baseline calibration
    run scenario simulations
    run sensitivity analysis
    export results

R:
    load exported results
    create figures
    save publication-ready plots
```

Do not duplicate model logic in R. R should only read Python-generated outputs and visualize them.

---

# 5. Model Design

## 5.1 Population Structure

Use an age-structured model with five age groups:

| Age group   | Label          | Rationale                                                        |
| ----------- | -------------- | ---------------------------------------------------------------- |
| 0–2 months  | `infant_0_2m`  | Highest severe disease risk; before or around first vaccine dose |
| 3–11 months | `infant_3_11m` | Partially vaccinated infants                                     |
| 1–6 years   | `child_1_6y`   | Early childhood transmission and vaccine protection period       |
| 7–17 years  | `school_7_17y` | School-age and adolescent transmission reservoir                 |
| ≥18 years   | `adult_18plus` | Parents, caregivers, adult reservoir                             |

Use an age-specific contact matrix. Synthetic contact matrices such as those from Prem et al. can be used for China or as a starting point if local matrices are unavailable. These contact matrices are commonly used in age-structured infectious disease models. ([PLOS][4])

---

## 5.2 Infection States

For each age group, include the following states:

```text
S       susceptible
V       vaccinated / partially protected
E_S     exposed to macrolide-sensitive strain
E_R     exposed to macrolide-resistant strain
I_S_sym symptomatic infection, sensitive strain
I_S_asym asymptomatic or mild infection, sensitive strain
I_R_sym symptomatic infection, resistant strain
I_R_asym asymptomatic or mild infection, resistant strain
T_S     treated infection, sensitive strain
T_R     treated infection, resistant strain
R       recovered / temporarily immune
```

The model should allow waning immunity from both vaccination and natural infection.

---

## 5.3 Strain Structure

Include two bacterial strain categories:

| Strain     | Meaning                            |
| ---------- | ---------------------------------- |
| `S_strain` | Macrolide-sensitive *B. pertussis* |
| `R_strain` | Macrolide-resistant *B. pertussis* |

Let the transmission rate of the resistant strain be:

```text
beta_R = beta_S * fitness_R
```

Default:

```text
fitness_R = 1.0
```

Then explore sensitivity values such as:

```text
fitness_R = 0.8, 1.0, 1.1, 1.25
```

This avoids assuming that resistance automatically increases biological transmissibility.

---

# 6. Vaccine Mechanism

The model should not use a single vaccine efficacy parameter. Instead, split vaccine effects into four components:

| Parameter | Meaning                                                         |
| --------- | --------------------------------------------------------------- |
| `VE_sus`  | Reduction in susceptibility to infection                        |
| `VE_sym`  | Reduction in probability of symptomatic disease after infection |
| `VE_inf`  | Reduction in infectiousness if infected                         |
| `VE_dur`  | Reduction in infectious duration                                |

This is the main conceptual innovation of the project.

## 6.1 Vaccine Scenarios

Implement the following vaccine mechanism scenarios:

| Scenario                | Description                               | Expected pattern                                      |
| ----------------------- | ----------------------------------------- | ----------------------------------------------------- |
| `no_vaccine`            | No vaccine protection                     | Highest disease and infection burden                  |
| `symptom_protective`    | High `VE_sym`, low `VE_sus`, low `VE_inf` | Fewer reported cases but hidden transmission persists |
| `infection_blocking`    | High `VE_sus`                             | Fewer infections and fewer cases                      |
| `transmission_blocking` | High `VE_inf` and/or high `VE_dur`        | Reduced onward transmission                           |
| `next_generation`       | High `VE_sus`, `VE_sym`, and `VE_inf`     | Strongest control                                     |

Initial example values:

```yaml
no_vaccine:
  VE_sus: 0.00
  VE_sym: 0.00
  VE_inf: 0.00
  VE_dur: 0.00

symptom_protective:
  VE_sus: 0.20
  VE_sym: 0.85
  VE_inf: 0.10
  VE_dur: 0.00

infection_blocking:
  VE_sus: 0.75
  VE_sym: 0.85
  VE_inf: 0.20
  VE_dur: 0.10

transmission_blocking:
  VE_sus: 0.30
  VE_sym: 0.85
  VE_inf: 0.70
  VE_dur: 0.30

next_generation:
  VE_sus: 0.80
  VE_sym: 0.90
  VE_inf: 0.75
  VE_dur: 0.40
```

These values are placeholders. The code should allow easy replacement through configuration files.

---

# 7. Antibiotic Treatment and PEP Module

## 7.1 Treatment Effects

Implement treatment as a reduction in infectious duration and/or infectiousness.

For macrolide-sensitive infection:

```text
treatment_effect_sensitive = high
```

For macrolide-resistant infection:

```text
treatment_effect_resistant = low
```

Example defaults:

```yaml
treatment:
  treatment_rate_symptomatic: 0.50
  treatment_rate_asymptomatic: 0.05

  sensitive:
    infectious_duration_reduction: 0.60
    infectiousness_reduction: 0.50

  resistant:
    infectious_duration_reduction: 0.10
    infectiousness_reduction: 0.05
```

## 7.2 Post-Exposure Prophylaxis

CDC supports PEP for household contacts of pertussis cases within 21 days of cough onset, and household secondary attack rates may remain high even among vaccinated contacts. ([疾病控制与预防中心][5])

Model PEP as a reduction in susceptibility among recently exposed household or close-contact individuals.

Because this model is age-structured rather than explicitly household-based, approximate PEP as a reduction in force of infection among target age groups after symptomatic case detection.

Example:

```yaml
PEP:
  coverage_household_contacts: 0.30
  effectiveness_sensitive: 0.70
  effectiveness_resistant: 0.10
```

---

# 8. Force of Infection

For age group `a`, define the force of infection from both sensitive and resistant strains.

Conceptual form:

```text
lambda_a = sum_b C_ab * [
    beta_S * infectious_pressure_sensitive_b
    +
    beta_R * infectious_pressure_resistant_b
]
```

Where:

```text
infectious_pressure_sensitive_b =
    (I_S_sym_b
     + rel_inf_asym * I_S_asym_b
     + rel_inf_treated_sensitive * T_S_b) / N_b
```

```text
infectious_pressure_resistant_b =
    (I_R_sym_b
     + rel_inf_asym * I_R_asym_b
     + rel_inf_treated_resistant * T_R_b) / N_b
```

Vaccinated individuals experience reduced susceptibility:

```text
lambda_vaccinated_a = lambda_a * (1 - VE_sus)
```

Infected vaccinated individuals may have:

```text
lower probability of symptoms
lower infectiousness
shorter duration of infection
```

depending on the vaccine scenario.

---

# 9. Model Outputs

For each simulation, export the following outcomes by time, age group, strain, and scenario:

```text
symptomatic_cases
asymptomatic_infections
total_infections
reported_cases
infant_cases
infant_infections
resistant_fraction
treated_cases
PEP_averted_cases
effective_reproduction_proxy
cumulative_cases
cumulative_infections
```

Also calculate summary outcomes:

```text
total_symptomatic_cases
total_infections
total_infant_cases
total_infant_infections
peak_incidence
time_to_peak
outbreak_duration
proportion_asymptomatic
case_to_infection_ratio
relative_reduction_vs_baseline
```

---

# 10. Reporting Rate Handling

Do not try to estimate the true reporting rate as a primary goal.

Instead, implement reporting as a scenario parameter:

```yaml
reporting_rate:
  infant_0_2m: 0.60
  infant_3_11m: 0.50
  child_1_6y: 0.25
  school_7_17y: 0.10
  adult_18plus: 0.05
```

Then run sensitivity analyses:

```text
high reporting
medium reporting
low reporting
age-biased reporting
time-varying reporting
```

The key manuscript claim should be based on **relative strategy rankings**, not absolute infection burden.

---

# 11. Scenario Analyses

## Analysis 1: Vaccine Mechanism and Hidden Transmission

Compare:

```text
no_vaccine
symptom_protective
infection_blocking
transmission_blocking
next_generation
```

Primary outputs:

```text
reported_cases
total_infections
case_to_infection_ratio
asymptomatic_fraction
infant_infections
```

Expected figure:

```text
Line plots of reported cases vs total infections over time.
Bar plot of cumulative reported cases and cumulative total infections.
```

---

## Analysis 2: Macrolide Resistance Scenarios

Run resistance prevalence scenarios:

```yaml
resistance_prevalence:
  low: 0.05
  moderate: 0.30
  high: 0.70
  very_high: 0.95
```

Primary outputs:

```text
total_infections
infant_cases
outbreak_duration
treated_cases
resistant_fraction_over_time
```

Expected figure:

```text
Line plot of resistant fraction over time.
Bar plot of infant cases by resistance scenario.
```

---

## Analysis 3: Vaccine Transmission Blocking × Resistance Interaction

Run a two-dimensional grid:

```text
VE_inf from 0.0 to 0.9
resistance_prevalence from 0.0 to 1.0
```

For each grid point, calculate:

```text
cumulative_infant_cases
cumulative_total_infections
case_to_infection_ratio
R_effective_proxy
```

Expected figure:

```text
Heatmap:
    x-axis = VE_inf
    y-axis = resistance prevalence
    color = cumulative infant cases or total infections
```

This should be one of the main figures.

---

## Analysis 4: Intervention Strategy Comparison

Compare these strategies:

| Strategy                      | Description                                                              |
| ----------------------------- | ------------------------------------------------------------------------ |
| `current`                     | Current vaccination + standard macrolide treatment                       |
| `higher_child_coverage`       | Increased routine childhood vaccine coverage                             |
| `adolescent_booster`          | Additional booster for 7–17 years                                        |
| `maternal_immunization`       | Direct infant protection through maternal vaccination                    |
| `resistance_guided_treatment` | Resistance testing plus alternative treatment                            |
| `next_generation_vaccine`     | Improved transmission-blocking vaccine                                   |
| `combined_strategy`           | Maternal immunization + adolescent booster + resistance-guided treatment |

Primary outputs:

```text
relative_reduction_in_infant_cases
relative_reduction_in_total_infections
relative_reduction_in_reported_cases
relative_reduction_in_resistant_infections
```

Expected figure:

```text
Ranked bar chart or dot-whisker plot showing relative reduction by strategy.
```

---

## Analysis 5: Global Sensitivity Analysis

Use Latin hypercube sampling or Sobol sensitivity analysis.

Key uncertain parameters:

```text
VE_sus
VE_sym
VE_inf
VE_dur
waning_rate_vaccine
waning_rate_natural
relative_infectiousness_asymptomatic
duration_asymptomatic
treatment_rate_symptomatic
PEP_coverage
PEP_effectiveness_resistant
fitness_R
reporting_rate_by_age
```

Primary outputs for sensitivity:

```text
infant_cases
total_infections
case_to_infection_ratio
resistant_fraction
strategy_ranking
```

Expected figure:

```text
Tornado plot or Sobol index plot.
```

---

# 12. Suggested Repository Structure

```text
pertussis_vaccine_resistance_model/
│
├── README.md
├── requirements.txt
├── renv.lock or install_R_packages.R
│
├── config/
│   ├── baseline_parameters.yaml
│   ├── vaccine_scenarios.yaml
│   ├── resistance_scenarios.yaml
│   ├── intervention_scenarios.yaml
│   └── sensitivity_parameters.yaml
│
├── data/
│   ├── raw/
│   │   ├── age_population.csv
│   │   ├── contact_matrix_china.csv
│   │   ├── observed_cases_by_age.csv
│   │   └── resistance_data.csv
│   │
│   └── processed/
│       ├── population_age_groups.csv
│       ├── contact_matrix_5groups.csv
│       └── calibration_targets.csv
│
├── src_python/
│   ├── model/
│   │   ├── compartments.py
│   │   ├── parameters.py
│   │   ├── ode_system.py
│   │   ├── force_of_infection.py
│   │   ├── vaccination.py
│   │   ├── treatment.py
│   │   └── outputs.py
│   │
│   ├── simulation/
│   │   ├── run_baseline.py
│   │   ├── run_vaccine_scenarios.py
│   │   ├── run_resistance_scenarios.py
│   │   ├── run_intervention_scenarios.py
│   │   ├── run_heatmap_grid.py
│   │   └── run_sensitivity.py
│   │
│   ├── calibration/
│   │   ├── likelihood.py
│   │   ├── calibrate_baseline.py
│   │   └── posterior_predictive.py
│   │
│   └── utils/
│       ├── io.py
│       ├── validation.py
│       └── plotting_preview.py
│
├── scripts_R/
│   ├── 00_setup.R
│   ├── 01_plot_model_structure.R
│   ├── 02_plot_vaccine_scenarios.R
│   ├── 03_plot_resistance_scenarios.R
│   ├── 04_plot_heatmaps.R
│   ├── 05_plot_intervention_comparison.R
│   └── 06_plot_sensitivity.R
│
├── outputs/
│   ├── simulations/
│   ├── summaries/
│   ├── figures/
│   └── tables/
│
└── manuscript_notes/
    ├── parameter_table.csv
    ├── scenario_table.csv
    └── methods_equations.md
```

---

# 13. Python Implementation Requirements

## Required Python packages

Use:

```text
numpy
pandas
scipy
pyyaml
pydantic
tqdm
joblib
SALib
matplotlib
pyarrow
```

Optional:

```text
numba
pymc
emcee
arviz
```

Use `scipy.integrate.solve_ivp` for the deterministic ODE model.

Recommended solver:

```python
solve_ivp(method="LSODA")
```

or:

```python
solve_ivp(method="BDF")
```

because pertussis models with waning immunity and age structure may become stiff.

---

## Python Deliverables

The Codex agent should produce:

```text
1. A working deterministic age-structured ODE model.
2. YAML-driven parameter input.
3. Scenario runner scripts.
4. Simulation output files in tidy format.
5. Calibration placeholder or simple calibration routine.
6. Sensitivity analysis script.
7. Unit tests for population conservation and non-negative states.
8. CSV/parquet outputs for R visualization.
```

---

# 14. R Visualization Requirements

## Required R packages

Use:

```r
tidyverse
data.table
ggplot2
patchwork
scales
viridis
cowplot
readr
arrow
yaml
```

Optional:

```r
ggrepel
ggpubr
sf
```

## R Deliverables

The R scripts should produce these manuscript-ready figures:

```text
Figure 1. Model structure diagram
Figure 2. Reported cases vs total infections under vaccine mechanism scenarios
Figure 3. Impact of macrolide resistance on infections, infant cases, and outbreak duration
Figure 4. Heatmap of vaccine transmission-blocking effect × resistance prevalence
Figure 5. Intervention strategy comparison
Figure 6. Sensitivity analysis tornado or Sobol plot
```

All figures should be saved as:

```text
outputs/figures/figure_1_model_structure.pdf
outputs/figures/figure_2_vaccine_scenarios.pdf
outputs/figures/figure_3_resistance_scenarios.pdf
outputs/figures/figure_4_heatmap.pdf
outputs/figures/figure_5_interventions.pdf
outputs/figures/figure_6_sensitivity.pdf
```

Also save `.png` versions for quick review.

---

# 15. Calibration Strategy

Use a light-touch calibration first.

The model should initially be calibrated to match broad observed patterns, not exact true incidence.

Calibration targets:

```text
age distribution of reported cases
annual or monthly reported case trend
approximate infant case proportion
approximate resistant strain prevalence, if available
```

Recommended calibrated parameters:

```text
beta_S
initial_exposed
initial_resistant_fraction
reporting_rate_multiplier
seasonality_amplitude
waning_rate_vaccine
```

Do not attempt to identify all parameters simultaneously.

Use either:

```text
least squares / maximum likelihood
```

or a simple Bayesian calibration if time allows.

Suggested likelihood:

```text
Negative binomial likelihood for reported cases by age and time.
```

The negative binomial model is preferable because pertussis surveillance data are usually overdispersed.

---

# 16. Minimum Viable Product

The first version should not be overly complex.

## MVP requirements

The Codex agent should first implement:

```text
1. Five age groups.
2. Two strains: sensitive and resistant.
3. Symptomatic and asymptomatic infection states.
4. Vaccinated and susceptible compartments.
5. Waning vaccine protection.
6. Treatment effect that differs by strain.
7. Four vaccine scenarios.
8. Four resistance scenarios.
9. One heatmap analysis.
10. R figures for the main results.
```

Do not implement household-level transmission in the MVP.

Do not implement stochastic individual-based simulation in the MVP.

Do not implement cost-effectiveness in the MVP.

---

# 17. Validation Checks

The code should automatically check:

```text
population remains non-negative
total population is conserved, except births/deaths if implemented
no compartment contains NaN or infinite values
scenario outputs have expected columns
reported cases never exceed symptomatic infections after applying reporting rates
resistant fraction remains between 0 and 1
```

Create a small test script:

```text
src_python/utils/validation.py
```

and run it after every major simulation.

---

# 18. Suggested Execution Order for Codex Agent

## Step 1: Build repository skeleton

Create folders, config files, and minimal README.

## Step 2: Implement parameter loading

Read all parameters from YAML.

## Step 3: Implement model state indexing

Create a clean state index system for:

```text
age group × compartment
```

## Step 4: Implement ODE system

Implement:

```text
force of infection
vaccination protection
symptomatic vs asymptomatic split
sensitive vs resistant strain infection
treatment transition
recovery
waning immunity
```

## Step 5: Run baseline simulation

Export:

```text
outputs/simulations/baseline_timeseries.parquet
outputs/summaries/baseline_summary.csv
```

## Step 6: Run vaccine mechanism scenarios

Export:

```text
outputs/simulations/vaccine_scenarios.parquet
outputs/summaries/vaccine_scenarios_summary.csv
```

## Step 7: Run resistance scenarios

Export:

```text
outputs/simulations/resistance_scenarios.parquet
outputs/summaries/resistance_scenarios_summary.csv
```

## Step 8: Run interaction heatmap

Export:

```text
outputs/simulations/veinf_resistance_grid.parquet
outputs/summaries/veinf_resistance_grid_summary.csv
```

## Step 9: Run intervention comparison

Export:

```text
outputs/simulations/intervention_scenarios.parquet
outputs/summaries/intervention_scenarios_summary.csv
```

## Step 10: Run R visualization

Generate all figures into:

```text
outputs/figures/
```

---

# 19. Main Manuscript Claims to Test

The model should be designed to test whether the following claims are supported:

1. A symptom-protective vaccine can substantially reduce reported disease while allowing hidden transmission to persist.
2. Macrolide resistance reduces the population-level benefit of treatment and post-exposure prophylaxis.
3. The combination of weak transmission blocking and high resistance produces the highest risk of persistent transmission.
4. Strategies that directly protect infants or reduce transmission from older age groups may outperform strategies that only increase routine childhood vaccine coverage.
5. A next-generation vaccine with stronger transmission-blocking activity could have larger population-level effects than a vaccine that mainly reduces symptoms.

---

# 20. Key Output Tables

Generate these tables:

## Table 1. Parameter table

Columns:

```text
parameter
description
baseline_value
range
unit
source_or_assumption
used_in_sensitivity_analysis
```

## Table 2. Vaccine scenario definitions

Columns:

```text
scenario
VE_sus
VE_sym
VE_inf
VE_dur
description
```

## Table 3. Resistance scenario definitions

Columns:

```text
scenario
initial_resistance_prevalence
fitness_R
treatment_effect_resistant
PEP_effectiveness_resistant
description
```

## Table 4. Intervention comparison

Columns:

```text
strategy
total_infections
reported_cases
infant_cases
resistant_infections
relative_reduction_infant_cases
relative_reduction_total_infections
```

---

# 21. Interpretation Rules

The final analysis should avoid overclaiming.

Use language such as:

```text
Under plausible assumptions...
In scenario analyses...
The model suggests...
Results were robust across reporting-rate assumptions...
```

Avoid language such as:

```text
This proves...
We estimated the true infection burden...
Resistance caused the outbreak...
```

The study should be framed as a **mechanistic modelling and scenario analysis**, not a definitive causal attribution study.

---

# 22. Suggested README Summary

The README should include:

```text
This repository implements an age-structured deterministic transmission model of pertussis to evaluate how imperfect vaccine transmission-blocking effects and macrolide resistance jointly influence pertussis control. The model is implemented in Python. Simulation outputs are exported in tidy format and visualized in R.

Main analyses:
1. Vaccine mechanism scenarios
2. Macrolide resistance scenarios
3. Vaccine transmission-blocking × resistance heatmap
4. Intervention strategy comparison
5. Sensitivity analysis
```

---

# 23. Short Prompt You Can Give to Codex Agent

```text
Build a Python + R modelling project for an age-structured pertussis transmission model.

Use Python for the deterministic ODE model, parameter handling, scenario simulations, calibration placeholder, sensitivity analysis, and exporting tidy results. Use R only for publication-quality visualization.

The scientific question is: how do imperfect transmission-blocking vaccination and macrolide resistance jointly affect pertussis transmission, hidden infections, infant cases, and intervention effectiveness?

Implement a five-age-group model:
0–2 months, 3–11 months, 1–6 years, 7–17 years, and ≥18 years.

Include susceptible, vaccinated, exposed, symptomatic infection, asymptomatic infection, treated infection, recovered states, with two strains: macrolide-sensitive and macrolide-resistant Bordetella pertussis.

Split vaccine effects into:
VE_sus, VE_sym, VE_inf, and VE_dur.

Implement vaccine scenarios:
no vaccine, symptom-protective vaccine, infection-blocking vaccine, transmission-blocking vaccine, and next-generation vaccine.

Implement resistance scenarios:
low, moderate, high, and very high macrolide resistance.

Implement treatment and post-exposure prophylaxis effects that are strong for sensitive strains but reduced for resistant strains.

Run four main analyses:
1. Vaccine mechanism scenarios.
2. Macrolide resistance scenarios.
3. Two-dimensional heatmap of VE_inf × resistance prevalence.
4. Intervention strategy comparison.

Export all results as tidy CSV or parquet files.

Create R scripts using ggplot2 to generate:
1. Model structure figure.
2. Reported cases vs total infections by vaccine scenario.
3. Macrolide resistance scenario comparison.
4. VE_inf × resistance heatmap.
5. Intervention strategy ranking.
6. Sensitivity analysis plot.

Use YAML config files for parameters and scenarios. Include validation checks for non-negative states, population conservation, no NaN values, and valid output ranges.
```

---

My recommendation is to start with the MVP version first: five age groups, deterministic ODEs, two strains, vaccine-mechanism scenarios, resistance scenarios, and one interaction heatmap. Once that runs cleanly, you can add calibration to Chinese age-specific pertussis surveillance data and local resistance data.

[1]: https://www.pnas.org/doi/pdf/10.1073/pnas.1314688110?utm_source=chatgpt.com "Acellular pertussis vaccines protect against disease but fail to ..."
[2]: https://www.cdc.gov/pertussis/hcp/clinical-care/index.html?utm_source=chatgpt.com "Treatment of Pertussis | Whooping Cough | CDC"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12710321/?utm_source=chatgpt.com "Genomic surveillance reveals global spread of macrolide-resistant ..."
[4]: https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1009098&utm_source=chatgpt.com "Projecting contact matrices in 177 geographical regions: An ... - PLOS"
[5]: https://www.cdc.gov/pertussis/php/postexposure-prophylaxis/index.html?utm_source=chatgpt.com "Postexposure Antimicrobial Prophylaxis | Whooping Cough | CDC"
