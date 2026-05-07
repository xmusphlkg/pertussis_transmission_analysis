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
- Exposed, infectious, and treated states retain their unvaccinated/recent/waned infection source so vaccine symptom, infectiousness, and duration effects act on the correct source history.

## Country Profiles

`config/country_profiles.yaml` provides generated profiles for Australia, China, United Kingdom, Japan, New Zealand, Sweden, Singapore, and the United States. These profiles combine measured extracts, derived aggregates, and explicit assumptions; country-specific absolute incidence should be interpreted as uncalibrated scenario analysis unless a calibration run is reported.

## Reporting Evidence

The current age-specific reporting gradient is still an assumption layer rather than a country-calibrated observation model. I added a compact literature scan in [`manuscript_notes/reporting_evidence_summary.md`](/home/mpi/pertussis_transmission/manuscript_notes/reporting_evidence_summary.md) that separates direct quantitative anchors from qualitative evidence gaps. The strongest public anchors I found are in England/Wales, Sweden, Ontario, and a few US studies; for Australia, China, New Zealand, Japan, and Singapore the evidence I found is mostly indirect or qualitative.

Those ranges are now encoded as country-specific `reporting_rate_prior` bands in the generated country profiles, while the existing `reporting_rate` values remain the point assumptions used by the current deterministic model.

The country calibration objective now adds a soft penalty from those prior bands so the fitted reporting multiplier stays plausible without forcing a hard age-specific hierarchy into the parameterization.
