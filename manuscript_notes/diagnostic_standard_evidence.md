# Pertussis Diagnostic Standard Timeline

This note documents the curated diagnostic-standard dataset:

- `data/raw/pertussis_diagnostic_standards_timeline.csv`
- `data/raw/pertussis_diagnostic_standards_sources.csv`

## Rationale

Reported pertussis counts are not only a function of transmission. They also depend on:

- case definitions;
- whether reporting is clinical, epidemiologically linked, or laboratory confirmed;
- availability of culture, PCR, LAMP, oral-fluid testing, and pertussis-toxin serology;
- test timing relative to cough onset;
- outbreak-specific testing intensity and clinician awareness.

These changes can create step changes or sharp waves in notifications that are not directly comparable across time. This is especially relevant for recent high-count countries in the Bayesian calibration, where the likelihood can otherwise force transmission, vaccine-effect, or resistance-fitness parameters to explain observation-system discontinuities.

## Encoding

The timeline file encodes one row per country-period diagnostic regime. The columns
`relative_detection_prior_mean`, `relative_detection_prior_lower`, and
`relative_detection_prior_upper` are literature-informed observation-layer priors.
They are not deterministic corrections to the observed case counts.

Interpretation:

- `1.0` means the period is treated as the within-country reference observation regime.
- Values below `1.0` indicate likely lower ascertainment than the reference regime.
- Values above `1.0` indicate enhanced detection, broadened case definition, or outbreak-driven testing.
- Wide bounds indicate weak or indirect evidence.

The most important model use is a time-varying reporting or diagnostic multiplier in the observation model:

```text
expected_reported_cases(t) =
    model_symptomatic_cases(t)
    * age_reporting_rate
    * country_reporting_multiplier
    * diagnostic_regime_multiplier(t)
```

For MCMC, the multiplier should usually be fixed at the row mean for a sensitivity run or sampled with a strong prior within the encoded lower/upper bounds. It should not be left completely free because it is confounded with `beta_S`, `reporting_multiplier`, and vaccine-effect parameters.

## High-Priority Regime Breaks

- China: late-March 2024 enhanced active PCR screening during the resurgence.
- Japan: 2018 shift from pediatric sentinel reporting to all-facility notification with laboratory diagnosis as a rule.
- United Kingdom: July/November 2001 introduction of national serology/PCR supplementation.
- United States: 2020 CSTE case-definition update, estimated to increase reported cases by roughly 10 percent.
- Australia: post-2007 PCR-dominant notification era.
- Thailand: 2023-2024 Narathiwat outbreak case definition used cough >=1 week rather than the national cough >=2 week definition.

## Modelling Caution

The dataset should enter the likelihood only as an observation-process term. It should not alter the biological state variables. For countries where the current calibration window falls entirely inside one diagnostic regime, the multiplier is absorbed by the country reporting multiplier and has little effect. For countries crossing a regime break or outbreak-specific enhanced testing, it can materially reduce artificial posterior sharpness and multimodality.
