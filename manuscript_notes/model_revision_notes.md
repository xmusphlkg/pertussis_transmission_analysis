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

- The default simulation horizon is 20 years with weekly output.
- Annual seasonality remains enabled through a cosine multiplier.
- A configurable 4-year multi-year transmission multiplier is included for diagnostic sensitivity and calibration. It should be treated as phenomenological unless supported by calibration.
- Fixed-population demographic turnover moves people through age groups and recycles the oldest group into newborn susceptible/vaccinated entry states.
- Routine vaccination maintenance relaxes vaccinated counts toward age-specific coverage targets.
- Low-level importation keeps the deterministic system from becoming unrealistically extinct after the initial seed.

## Country Profiles

`config/country_profiles.yaml` provides synthetic placeholder profiles for China, United States, Thailand, and Denmark. These should be replaced with real country-specific population, birth-rate, vaccination, and contact-matrix inputs before drawing country-specific conclusions.
