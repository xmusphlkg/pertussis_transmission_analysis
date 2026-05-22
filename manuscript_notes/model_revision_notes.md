# Model Revision Notes

## Why the First MVP Curve Was Not Epidemiologically Plausible

The first deterministic ODE scaffold behaved like a single seeded outbreak because it had no demographic renewal and only a short three-year horizon. Pertussis is usually analyzed as a recurrent infection with annual seasonality layered on top of multi-year epidemic cycles. Those 3-5 year cycles can emerge from susceptible replenishment, waning immunity, vaccination history, contact structure, and observation changes; they should not be forced into the model as the only explanation.

## Changes Introduced From the Companion `pertussis_epidemic_model`

The local companion project emphasizes:

- Age-specific contact structure as a first-class input.
- Demographic turnover through births and aging for multi-year simulations.
- Age- and country-specific observation/reporting probabilities.
- Pertussis-oriented time scales: about 8 days latent period and about 21 days symptomatic infectious period.
- Lower relative infectiousness for asymptomatic infection than the first MVP default.
- Externalized country/scenario profiles rather than hard-coded assumptions.

This project now carries those ideas into the deterministic ODE version while keeping the vaccine/resistance scenario logic.

## Current Long-Run Assumptions

- The default simulation horizon is 26 years (2025–2050) after a 15-year burn-in, with weekly output.
- Annual seasonality remains enabled through a cosine multiplier.
- A configurable 4-year multi-year transmission multiplier is included for diagnostic sensitivity and calibration. It should be treated as phenomenological unless supported by calibration.
- Fixed-population demographic turnover moves people through age groups while keeping the configured WPP age vector as the no-disease fixed point; the oldest group outflow is recycled into newborn susceptible/vaccinated entry states.
- Routine vaccination maintenance relaxes vaccinated counts toward age-specific coverage targets.
- Low-level importation keeps the deterministic system from becoming unrealistically extinct after the initial seed.
- Resistant prevalence is rebalanced once after burn-in for scenario initialization. Continuous strain re-anchoring during the analysis period is disabled by default and reserved for sensitivity cases.
- Exposed, infectious, and treated states retain their maternal/dose-history infection source so vaccine symptom, infectiousness, and duration effects act on the correct source history.

## Country Profiles

`config/country_profiles.yaml` provides generated profiles for Australia, Brazil, China, United Kingdom, Japan, New Zealand, Sweden, Thailand, and the United States. These profiles combine measured extracts, derived aggregates, and explicit assumptions; country-specific absolute incidence should be interpreted as uncalibrated scenario analysis unless a calibration run is reported.

The nine-country set is purposive rather than exhaustive. It spans Western Pacific, South-East Asian, European and Americas WHO regions; a wide range of observed reported incidence and population size; contrasting routine pertussis programme signatures; and both measured and conservative low starting resistance anchors. The new Figure 1A-B panels are meant to make that selection logic visible instead of leaving it implicit.

Accepted calibration artifacts are written under `outputs/calibrations/` and are preferred automatically by the scenario runners when present. If a country has no accepted calibration artifact, its outputs should still be treated as exploratory scenario analysis rather than as fitted inference.

## Reporting Evidence

The current age-specific reporting gradient is still an assumption layer rather than a country-calibrated observation model. I added a compact literature scan in [`manuscript_notes/reporting_evidence_summary.md`](/home/lkg/pertussis_transmission_analysis/manuscript_notes/reporting_evidence_summary.md) that separates direct quantitative anchors from qualitative evidence gaps. The strongest public anchors I found are in England/Wales, Sweden, Ontario, and a few US studies; for Australia, Brazil, China, New Zealand, Japan, and Thailand the evidence I found is mostly indirect or qualitative.

Those ranges are now encoded as country-specific `reporting_rate_prior` bands in the generated country profiles, while the existing `reporting_rate` values remain the point assumptions used by the current deterministic model.

The country calibration objective now adds a soft penalty from those prior bands so the fitted reporting multiplier stays plausible without forcing a hard age-specific hierarchy into the parameterization.

## WHO Immunization Modelling Guidance Audit, 2026-05-08

I reviewed the implementation against WHO's 2025 *Guidance for using modelling for immunization decision-making*. The most important corrections were:

- Reporting-rate sensitivity is now treated as an observation-model perturbation only. PEP activation uses a separate `pep_detection_rate`, so changing reporting completeness no longer changes true transmission unless an explicit detection or intervention scenario is added.
- Maternal protection is now treated as a short-lived infant proxy. Birth-entry `V` flows are converted back to susceptible when infants leave `infant_0_2m`, preventing maternal antibodies from being carried forward as multi-year vaccine-derived immunity.
- Infant summary incidence now uses the infant population denominator rather than total population, and summaries expose `infant_population`.
- Adult vaccine-derived protection proxies were made more conservative. Maternal vaccination coverage no longer drives a large protected fraction across the whole 18+ population.
- Probability inputs for coverage, symptom probability, vaccine effects and PEP detection are now rejected if outside `[0, 1]` instead of being silently clipped.

Remaining limitations should be explicit in interpretation:

- The deterministic model does not represent stochastic outbreak fadeout or parameter posterior uncertainty; scenario rankings should be read with sensitivity outputs.
- Country profiles combine measured, derived and assumption-based inputs; uncalibrated country outputs remain exploratory until accepted calibration artifacts are available.

## Calendar-Time and Explicit Dose-History Update, 2026-05-08

The model now maps simulation days to real calendar dates. Output rows include `calendar_date`, `calendar_year`, and `calendar_day_of_year`; calibration targets split modelled reporting intervals across observed surveillance intervals rather than using arbitrary simulated year bins. Country calibration overrides `calendar.analysis_start_date` to the first retained surveillance interval so observed and modelled reports are aligned on the same calendar axis.

Maternal protection and vaccine dose history are now represented by explicit susceptible-origin states instead of a single protected proxy: `M_protected`, dose-1 recent/waned, dose-2 recent/waned, and dose-3-plus recent/waned. Infection, treatment, symptom, infectiousness, and duration flows retain those origins, allowing maternal and partial-dose histories to carry distinct effects and waning rates.

The country-set and incidence-source update regenerated the calibration summary for the nine-country set. Accepted calibrated YAML files are available for countries passing the absolute-fit screen, while rejected rows remain explicit in `outputs/tables/calibration_all_countries.csv` for auditability.

Remaining limitations after this update:

- Explicit dose-history states are still deterministic population compartments, not individual vaccination cohorts with stochastic event histories.
- Calendar alignment fixes reporting-interval target matching, but it does not itself infer reporting shocks, surveillance interruptions, or policy changes within a year.
- The staged country calibration targets recent reported intervals and should be treated as a pragmatic fit, not a full posterior uncertainty analysis.


## Bayesian Uncertainty Analysis Upgrade, revised 2026-05-19

The Bayesian uncertainty module was substantially upgraded to address the concern (Lavine et al. 2011) that long-term pertussis projections are sensitive to parameter uncertainty and that a deterministic model without proper uncertainty quantification cannot support credible interval claims.

### Changes

1. **Validated beta-grid posterior path**: The production uncertainty analysis now fixes weakly identifiable nuisance parameters (`reporting_multiplier`, `VE_sus`, `VE_inf`, `relative_infectiousness_asymptomatic`, infectious durations, and `fitness_R`) at calibrated, literature-informed, or pre-specified baseline values and integrates the identifiable transmission parameter `beta_S` by deterministic log-grid quadrature. This is the canonical path for the reported conditional posterior predictive intervals.

2. **Grid validity diagnostics**: Results are accepted only if each country's beta grid has both edges at least 20 log-posterior units below the mode, at least 10 effective grid points, and no single grid point carrying more than 20% posterior mass. The canonical run passed in all 10 countries.

3. **Historical MCMC retained for diagnosis**: Adaptive Metropolis, componentwise Metropolis, and slice samplers remain available for pilot comparisons, but the previous high-dimensional MCMC path is not used for the primary interval estimates because beta/reporting/VE coupling made it unstable in country-level calibration.

4. **Auditable posterior artifacts**: The canonical outputs include `bayesian_posterior_samples`, `bayesian_uncertainty_summary`, `bayesian_uncertainty_intervals_summary`, `bayesian_stochastic_overlay_intervals_summary`, `bayesian_k_sensitivity_sweep`, and `bayesian_beta_grid_quality`, plus per-country raw/smoothed grid files under `outputs/metadata/beta_grid_bayesian_uncertainty/`.

5. **Dispersion k-sensitivity sweep**: The stochastic overlay now runs at k ∈ {5, 10, 20, 30, 50} to demonstrate how the combined predictive-interval width varies with the aggregate dispersion assumption. This makes the k=10 default auditable rather than opaque.

6. **Analysis start date moved to 2025-01-01**: Allows short-term out-of-sample validation against 2025 surveillance data before the forward projection period, increasing reader confidence in the model's near-term performance.

7. **Full multi-core parallelization**: Grid evaluations and posterior predictive scenarios run in parallel across available CPUs via joblib/loky, with BLAS thread limits set to prevent over-subscription.

### Remaining limitations

- The primary CrI are conditional on fixed nuisance parameters rather than a full joint posterior over reporting, vaccine effects, duration, asymptomatic infectiousness, and resistance fitness.
- Model structural uncertainty (e.g., exponential vs step-function waning, age-varying asymptomatic infectiousness) is not formally included in the posterior and should be discussed as a limitation in interpretation.
- The sensitivity analyses are therefore part of the uncertainty argument, not optional decoration: reporting-rate, vaccine-mechanism, global sensitivity, and resistance-fitness results should be interpreted alongside the beta-grid CrI.


## Resistance Fitness Assumption Revision, 2026-05-12

### Problem

The previous model assumed `fitness_R = 0.70` (30% fitness cost) for all macrolide-resistant B. pertussis scenarios. This caused resistant strain prevalence to decline toward zero in long-term projections, which is contradicted by observed epidemiology:

- China: MRBP rose from 36% (2016) to >99% (2024) in 8 years
- Japan: 83-88% MRBP by 2024-2025
- Australia: 4.3% in 2024 with genomic evidence of MT28 importation
- Global MT28-ptxP3 clone spreading across continents without apparent fitness barrier

A 30% fitness cost is mathematically inconsistent with fixation on this timescale under any plausible treatment pressure.

### Changes

1. **Baseline fitness_R changed from 0.70 to 1.00** (fitness-neutral). This is the most parsimonious assumption given the observed rapid fixation dynamics.

2. **Bayesian prior for fitness_R recentered**: mean 0.95 → 1.00, SD 0.18 → 0.12. The tighter SD reflects the stronger epidemiological constraint from observed fixation dynamics.

3. **New resistance scenarios added**:
   - `country_timeline_fitness_cost` (fitness_R = 0.85): retained as optimistic bound
   - `country_timeline_fitness_advantage` (fitness_R = 1.10): motivated by co-selection with virulence/vaccine-escape alleles (ptxP3, prn-negative)
   - `high_fitness_advantage` (fitness_R = 1.15): worst-case scenario

4. **Fitness grid extended**: finer resolution around 1.0 (added 0.98, 1.02) to better characterize the sensitivity near the neutral point.

5. **Dedicated fitness sensitivity runner** (`run_resistance_fitness_sensitivity.py`): produces country-specific projections at 7 fitness values with relative impact quantification.

6. **Literature evidence summary** written to `manuscript_notes/resistance_fitness_evidence.md`.

### Justification

The A2047G 23S rRNA mutation:
- Shows no demonstrated in vitro growth penalty in B. pertussis
- Co-occurs with virulence-enhancing alleles (ptxP3, prn-negative, fim3-2) in dominant MRBP clones
- Has reached near-fixation in China and high prevalence in Japan on timescales inconsistent with fitness_R < 0.90

The fitness-neutral default is conservative in the sense that it does not assume a fitness advantage, while being consistent with the epidemiological data. The sensitivity analysis explicitly explores both fitness costs and advantages.

### Remaining limitations

- The model treats fitness as a single scalar multiplying the transmission rate. In reality, fitness is context-dependent (varies with treatment pressure, vaccine coverage, and host immunity landscape).
- Compensatory mutations that restore fitness after initial resistance acquisition are not explicitly modeled.
- The co-selection of resistance with vaccine-escape alleles (prn-negative) means the effective fitness in aP-vaccinated populations may differ from the intrinsic fitness measured in vitro.


## Age Group Restructuring: 5 → 8 Groups, 2026-05-12

### Motivation

The previous 5-group structure had two major limitations:
- `adult_18plus` (62-year span) conflated young adults (18-39, primary infant transmission source) with elderly (65+, different contact patterns and clinical presentation)
- `school_7_17y` (11-year span) conflated primary school children (recently boosted) with adolescents (vaccine protection substantially waned)

### New 8-Group Structure

| Group | Age Range | Duration | Epidemiological Rationale |
|-------|-----------|----------|--------------------------|
| `infant_0_2m` | 0-2 months | 0.17 yr | Maternal protection period |
| `infant_3_11m` | 3-11 months | 0.75 yr | Primary immunization series |
| `child_1_4y` | 1-4 years | 4 yr | Post-primary series, aligns with Prem [0,5) |
| `child_5_9y` | 5-9 years | 5 yr | School entry, aligns with Prem [5,10) |
| `adolescent_10_17y` | 10-17 years | 8 yr | Booster waning period |
| `young_adult_18_39y` | 18-39 years | 22 yr | Reproductive age, infant contact source |
| `middle_adult_40_64y` | 40-64 years | 25 yr | Working age, lowest reporting |
| `elderly_65plus` | 65+ years | 15 yr | Retirement, different clinical presentation |

### Key Design Decisions

1. **Alignment with Prem contact matrix bins**: The child groups (1-4, 5-9) align cleanly with the 5-year Prem bins, enabling direct aggregation without interpolation.

2. **Adult split at 40 and 65**: The 18-39 group captures the parenting age range (primary household contact with infants). The 40-64 group has the lowest reporting rates. The 65+ group has distinct clinical presentation and healthcare-seeking behavior.

3. **State space**: 8 ages × 73 compartments = 584 state variables (vs 365 previously). ODE solve time increases ~60% but remains under 20 seconds per country.

### Files Modified

- `config/model_settings.yaml`: age_groups, contact_matrix, demography, reporting scenarios
- `config/country_profiles.yaml`: fully regenerated for all 10 countries
- `src_python/data/build_country_inputs.py`: aggregation logic, reporting priors
- `src_python/model/vaccination.py`: origin distributions per age group
- `src_python/simulation/run_reporting_age_sensitivity.py`: reporting bounds
- `tests/test_model.py`: age group references

### Consequences

- All previous calibration artifacts are invalidated and must be regenerated.
- Country-specific contact matrices are now 8×8, aggregated from Prem 16-group data with population-weighted reciprocity correction.
- WPP demographic trajectories are re-aggregated to the new 8-group structure.
- The reporting rate sensitivity analysis now has 8 independent parameters instead of 5, providing finer resolution on which age groups' reporting uncertainty matters most.
