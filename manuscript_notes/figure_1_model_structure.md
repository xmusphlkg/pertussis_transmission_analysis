# Figure 1 Model Structure and Implementation Notes

This note documents the model structure represented in Figure 1 and links each
visual element to the current implementation. The active manuscript model in
this repository is the deterministic age-structured ODE model under
`src_python/model/`; a separate network-model scaffold and burden-calibration
utility set is maintained alongside it for future extensions, but it is not
read by the deterministic ODE simulation runners.

## 1. Model Scope

The model represents pertussis transmission in an age-stratified population and
is designed for scenario analysis of vaccine mechanism, macrolide resistance,
treatment, post-exposure prophylaxis (PEP), reporting, and country profiles. The
state vector is deterministic and continuous. It is solved with `scipy`'s
`solve_ivp` using the solver explicitly configured in
`config/model_settings.yaml` (`LSODA` in the current analysis).

Core implementation files:

- `src_python/model/compartments.py`: state names and age-by-compartment index.
- `src_python/model/ode_system.py`: right-hand side of the ODE system.
- `src_python/model/force_of_infection.py`: age-specific and strain-specific
  force of infection.
- `src_python/model/vaccination.py`: vaccine mechanism helpers.
- `src_python/model/treatment.py`: treatment effects for sensitive and resistant
  infection.
- `src_python/model/outputs.py`: initialization, burn-in, solver call, and
  derived output metrics.
- `src_python/model/parameters.py`: conversion of YAML configuration into a
  `PreparedParameters` object.
- `src_python/simulation/common.py`: scenario construction and batch execution.

## 2. Age Structure

The active ODE model uses five declared age strata:

| Code label | Interpretation |
|---|---|
| `infant_0_2m` | infants aged 0-2 months |
| `infant_3_11m` | infants aged 3-11 months |
| `child_1_6y` | children aged 1-6 years |
| `school_7_17y` | school-aged children/adolescents aged 7-17 years |
| `adult_18plus` | adults aged 18 years and older |

Age-specific population, vaccine coverage, symptom probability, reporting
probability, and contact rates are loaded from `config/model_settings.yaml` and
country overrides in `config/country_profiles.yaml`. Country profiles are
generated from WPP population denominators, WHO/WUENIC-like vaccine metadata,
reported pertussis surveillance extracts, and epydemix-data contact matrices
aggregated to the five model age groups.

## 3. Compartmental State Space

For each age group `a`, the ODE state contains 28 compartments:

| Compartment | Meaning |
|---|---|
| `S` | unvaccinated or fully susceptible |
| `V` | vaccinated/protected proxy state |
| `E_{S/R}_{unvaccinated/recent/waned}` | exposed to sensitive or resistant pertussis, retaining infection source |
| `I_{S/R}_{sym/asym}_{unvaccinated/recent/waned}` | symptomatic or asymptomatic infectious infection, retaining strain and source |
| `T_{S/R}_{unvaccinated/recent/waned}` | treated infection, retaining strain and source |
| `R` | recovered/post-infection immunity |

The current state dimension is therefore `5 age groups x 28 compartments = 140`
ODE states. This state list is defined in `src_python/model/compartments.py` as
`COMPARTMENTS`.

## 4. Transmission and Force of Infection

Transmission is calculated separately for sensitive (`S`) and resistant (`R`)
pertussis. For recipient age group `a`, the sensitive force of infection is:

```text
lambda_S,a(t) = beta_S * m(t) * sum_b C[a,b] * pressure_S,b(t)
```

The resistant force of infection is:

```text
lambda_R,a(t) = beta_S * fitness_R * m(t) * sum_b C[a,b] * pressure_R,b(t)
```

where `C[a,b]` is the age-contact matrix, `beta_S` is the baseline sensitive
transmission rate, and `fitness_R` is the resistant-strain transmissibility
modifier.

The time multiplier `m(t)` is implemented as an annual seasonal term multiplied
by a weak multi-year phase-locking term:

```text
m(t) = [1 + seasonal_amplitude * cos(2*pi*(t - seasonal_phase)/365)]
       *
       [1 + multi_year_amplitude * cos(2*pi*(t - multi_year_phase)/
        (365 * multi_year_period_years))]
```

The strain-specific infectious pressure in each source age group includes
symptomatic infection, reduced infectiousness from asymptomatic infection,
reduced infectiousness from treatment, and reduced onward infectiousness for
breakthrough infections of vaccinated origin. In implementation this is handled
in `compute_force_of_infection(...)`.

PEP is implemented as a dynamic reduction in both strain-specific forces of
infection. The activation signal is detected symptomatic prevalence:

```text
activation = detected_symptomatic_prevalence /
             (detected_symptomatic_prevalence + activation_prevalence)
pep_coverage = coverage_household_contacts * activation
```

The resulting `pep_coverage` reduces `lambda_S` and `lambda_R` according to
strain-specific PEP effectiveness.

## 5. Infection Progression

New infections arise from `S`, `V_recent`, and `V_waned`:

```text
new_unvaccinated_sensitive = lambda_S * S
new_recent_sensitive = lambda_S * (1 - VE_sus) * V_recent
new_waned_sensitive = lambda_S * (1 - waned_relative_effect * VE_sus) * V_waned
```

The exposed states progress at rate `sigma = 1 / latent_duration`. Progression
is split into symptomatic and asymptomatic infection using age-specific baseline
symptom probability and the retained infection source:

```text
p_sym_source = p_sym_unvaccinated * (1 - VE_sym * source_relative_effect)
```

Symptomatic and asymptomatic infections recover at different rates. Vaccinated
origin can shorten infectious duration through the `VE_dur` mechanism, applied
to the retained infection source.

## 6. Vaccine Mechanisms

The model separates four vaccine mechanisms:

| Parameter | Implemented effect |
|---|---|
| `VE_sus` | reduces susceptibility of `V` before entry into `E_S` or `E_R` |
| `VE_sym` | reduces probability that a breakthrough infection is symptomatic |
| `VE_inf` | reduces onward infectiousness among infections of vaccinated origin |
| `VE_dur` | shortens infectious duration for infections of vaccinated origin |

Routine vaccination is represented by relaxation toward age-specific target
coverage across `V_recent + V_waned`:

```text
target_vaccinated_a = population_a(t) * vaccine_coverage_a
flow_S_to_V_recent = min(rate * max(target_vaccinated_a - V_recent_a - V_waned_a, 0), S_a)
```

If a vaccine scenario sets all `VE_*` values to zero, `make_config(...)` also
sets vaccine coverage and vaccinated birth entry to zero.

## 7. Treatment, Resistance, and PEP

Symptomatic and asymptomatic infectious compartments move into treated
compartments at rates configured under `treatment_rate_symptomatic` and
`treatment_rate_asymptomatic`. Treatment effects differ by strain:

- Sensitive treated infections (`T_S`) have a larger reduction in infectious
  duration and infectiousness.
- Resistant treated infections (`T_R`) retain more infectiousness and have a
  smaller duration reduction.

The resistant-strain scenario layer sets:

- `initial_conditions.initial_resistance_prevalence`
- `resistance.target_prevalence_at_analysis_start`
- `resistance.importation_fraction`
- `transmission.fitness_R`

After burn-in, active exposed/infectious/treated states are rebalanced once to
the scenario target. Continuous re-anchoring during the analysis period is off
in the declared baseline.

The PEP layer is resistance-aware through separate `effectiveness_sensitive` and
`effectiveness_resistant` values.

## 8. Demography, Importation, and Burn-in

Long-run recurrence is supported by three implementation choices:

1. Fixed-population demographic turnover ages individuals through the age bins
   while keeping the configured WPP age vector as the no-disease fixed point;
   the oldest-bin outflow is recycled into newborn entry states.
2. Low-level importation continuously seeds exposed infections and prevents the
   deterministic system from unrealistically going extinct after the initial
   seed.
3. The solver runs a pre-analysis burn-in (`burn_in_years = 60`)
   before saving the 30-year analysis horizon.

The ODE solver stores weekly output (`output_time_step = 7`) while
integrating the continuous system with configured tolerances.

## 9. Initialization and Outputs

`initial_state(...)` initializes each age group by splitting population between
`S` and `V` according to vaccine coverage, then seeds exposed and infectious
individuals according to:

- `initial_exposed_per_100k`
- `initial_infectious_per_100k`
- `initial_resistance_prevalence`
- `seed_age_distribution`

`compute_timeseries(...)` converts model states into daily/weekly output rows by
age group and strain. Derived outputs include:

- symptomatic cases
- asymptomatic infections
- total infections
- reported cases
- infant cases and infant infections
- treated cases
- PEP-averted cases
- resistant fraction among infections
- cumulative infections, cases, and reported cases

`summarize_timeseries(...)` then creates scenario-level summaries such as total
infections, annualized incidence, peak incidence, epidemic peak intervals,
resistant fraction, and relative reductions against a reference scenario.

## 10. Scenario Construction

`src_python/simulation/common.py` centralizes scenario construction:

- Vaccine scenarios modify the four `VE_*` parameters.
- Resistance scenarios modify resistance prevalence and resistant fitness.
- Intervention scenarios can modify vaccine coverage, vaccine mechanisms,
  treatment, and PEP.
- Country profiles provide active population, coverage, reporting,
  contact matrix, and transmission seasonality values.
- Reporting scenarios can apply global, age-biased, or time-varying reporting
  multipliers.

Outputs are written under `outputs/simulations/`, `outputs/summaries/`, and
`outputs/figures/`. Each simulation stem also receives
`outputs/metadata/{stem}_run_metadata.json`, which records the configuration
hash, git state, dependency versions, and row counts used for stale-output
checks.

## 11. Relationship to Companion Burden Files

A separate network model and burden-oriented observation scaffold contains the
current burden files:

- burden multipliers
- serology targets
- hospitalizations by age

Those files are loaded by the companion model's `Script/data_pipeline.py` and
can be flattened into a calibration target table. In the companion fitter,
`burden_multipliers` can already enter the objective as log-scale penalties,
whereas serology and hospitalization targets are ingested but not yet mapped
into the objective. The deterministic ODE model in `src_python/` does not
currently consume these burden files. Figure 1 therefore shows the deterministic
ODE pathway as the active analysis model and notes burden inputs as future or
companion calibration extensions, not as active ODE calibration data.

## 12. Figure 1 Panel Mapping

Figure 1 is organized as follows:

- Panel A: age-replicated two-strain ODE compartments and transitions.
- Panel B: contact-matrix mixing and strain-specific force-of-infection
  calculation.
- Panel C: vaccine, treatment, resistance, and PEP mechanism points.
- Panel D: implementation workflow from YAML/data inputs to solver outputs and
  manuscript figures.

The figure is generated by `scripts_R/01_plot_model_structure.R` and saved as:

- `outputs/figures/figure_1_model_structure.pdf`
- `outputs/figures/figure_1_model_structure.png`
