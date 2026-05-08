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

- The default simulation horizon is 30 years after a 60-year burn-in, with weekly output.
- Annual seasonality remains enabled through a cosine multiplier.
- A configurable 4-year multi-year transmission multiplier is included for diagnostic sensitivity and calibration. It should be treated as phenomenological unless supported by calibration.
- Fixed-population demographic turnover moves people through age groups while keeping the configured WPP age vector as the no-disease fixed point; the oldest group outflow is recycled into newborn susceptible/vaccinated entry states.
- Routine vaccination maintenance relaxes vaccinated counts toward age-specific coverage targets.
- Low-level importation keeps the deterministic system from becoming unrealistically extinct after the initial seed.
- Resistant prevalence is rebalanced once after burn-in for scenario initialization. Continuous strain re-anchoring during the analysis period is disabled by default and reserved for sensitivity cases.
- Exposed, infectious, and treated states retain their maternal/dose-history infection source so vaccine symptom, infectiousness, and duration effects act on the correct source history.

## Country Profiles

`config/country_profiles.yaml` provides generated profiles for Australia, China, United Kingdom, Japan, New Zealand, Sweden, Singapore, and the United States. These profiles combine measured extracts, derived aggregates, and explicit assumptions; country-specific absolute incidence should be interpreted as uncalibrated scenario analysis unless a calibration run is reported.

The eight-country set is purposive rather than exhaustive. It spans Western Pacific, European and Americas WHO regions; a wide range of observed reported incidence and population size; contrasting routine pertussis programme signatures; and both measured and conservative low starting resistance anchors. The new Figure 1A-B panels are meant to make that selection logic visible instead of leaving it implicit.

Accepted calibration artifacts are written under `outputs/calibrations/` and are preferred automatically by the scenario runners when present. If a country has no accepted calibration artifact, its outputs should still be treated as exploratory scenario analysis rather than as fitted inference.

## Reporting Evidence

The current age-specific reporting gradient is still an assumption layer rather than a country-calibrated observation model. I added a compact literature scan in [`manuscript_notes/reporting_evidence_summary.md`](/home/lkg/pertussis_transmission_analysis/manuscript_notes/reporting_evidence_summary.md) that separates direct quantitative anchors from qualitative evidence gaps. The strongest public anchors I found are in England/Wales, Sweden, Ontario, and a few US studies; for Australia, China, New Zealand, Japan, and Singapore the evidence I found is mostly indirect or qualitative.

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

The model now maps simulation days to real calendar dates. Output rows include `calendar_date`, `calendar_year`, and `calendar_day_of_year`; annual calibration targets split modelled reporting intervals across calendar-year boundaries rather than using arbitrary simulated year bins. Country calibration overrides `calendar.analysis_start_date` to January 1 of the first retained surveillance year so observed and modelled annual reports are aligned on the same calendar axis.

Maternal protection and vaccine dose history are now represented by explicit susceptible-origin states instead of a single protected proxy: `M_protected`, dose-1 recent/waned, dose-2 recent/waned, and dose-3-plus recent/waned. Infection, treatment, symptom, infectiousness, and duration flows retain those origins, allowing maternal and partial-dose histories to carry distinct effects and waning rates.

The full eight-country calibration run completed with accepted artifacts for Australia, China, United Kingdom, Japan, New Zealand, Sweden, Singapore, and the United States. Accepted calibrated YAML files are available under `outputs/calibrations/`, and the scenario runners automatically load them when the runtime configuration hash matches.

Remaining limitations after this update:

- Explicit dose-history states are still deterministic population compartments, not individual vaccination cohorts with stochastic event histories.
- Calendar alignment fixes annual target matching, but it does not itself infer reporting shocks, surveillance interruptions, or policy changes within a year.
- The staged country calibration targets recent reported annual incidence and should be treated as a pragmatic fit, not a full posterior uncertainty analysis.
