# Parameter Source Audit, 2026-05-22

Purpose: check whether each reported parameter value is directly supported by
literature/data, calibrated from project data, or should be labelled as a
literature-informed modeling assumption or scenario setting.

## Classification Key

- Direct data/source: value is read from a named data source or closely matches
  an external clinical/surveillance source.
- Calibrated: value is estimated from the project's calibration data, not taken
  directly from literature.
- Literature-informed assumption: literature supports the direction/range, but
  the exact numeric model value is a decomposition or implementation choice.
- Scenario/stress test: value is deliberately hypothetical or used for
  sensitivity analysis.

## Baseline Parameters

| Parameter | Value | Audit classification | Verdict/action |
|---|---:|---|---|
| `simulation.end_time` | 9495 days | Scenario/design | 26-year calendar horizon (2025-01-01 to 2050-12-31); not a literature parameter. Fixed stale "30 years" wording. |
| `simulation.burn_in_years` | 15 years | Scenario/design | Numerical initialization choice to reduce dependence on initial conditions. |
| `transmission.beta_S` | 0.01 placeholder | Calibrated | Shared-config placeholder only; country beta values are calibrated to reported incidence and listed separately. |
| `transmission.relative_infectiousness_asymptomatic` | 0.35 | Literature-informed assumption | aP/WHO evidence supports residual infection/transmission, but not this exact ratio; keep sensitivity label. |
| `transmission.multi_year_period_years` | 4 years | Literature/data-informed diagnostic | Pertussis cycles and local surveillance peaks support 3-5-year diagnostics; exact fallback is a model setting. |
| `transmission.multi_year_amplitude` | 0 | Scenario/design | Weak phase-locking disabled by default; not a literature estimate. |
| `natural_history.latent_duration` | 8 days | Direct clinical anchor | Within CDC 7-10 day common incubation range. |
| `natural_history.infectious_duration_symptomatic` | 21 days | Direct clinical anchor | Matches CDC infectiousness through about the third week after paroxysm onset. |
| `natural_history.infectious_duration_asymptomatic` | 14 days | Literature-informed assumption | Shorter mild/asymptomatic infectious window; no direct routine-surveillance estimate. |
| `natural_history.recovered_immunity_duration` | 3285 days | Literature-informed anchor | 9 years lies within CDC 4-20 year infection-acquired immunity range and pertussis cycle-model constraints. |
| `natural_history.vaccine_protection_duration` | 1825 days | Literature-informed anchor | Supported by aP waning literature showing substantial decline within roughly 3-7 years. |
| `treatment.treatment_rate_symptomatic` | 0.025/day | Implementation assumption | CDC supports early treatment but does not define this daily transition rate. |
| `PEP.coverage_household_contacts` | 0.30 | Implementation assumption | CDC supports household/high-risk PEP but does not define this model coverage ceiling. |

## Scenario Parameters

| Component | Values | Audit classification | Verdict/action |
|---|---|---|---|
| Vaccine profile `no_vaccine` | all VE components 0 | Counterfactual | Correctly a counterfactual, no citation needed beyond scenario definition. |
| Vaccine profile `symptom_protective` | VE_sym 0.85; VE_sus/VE_inf/VE_dur decomposed | Literature-informed mechanism scenario | Disease protection is supported; component decomposition is a model assumption. Wording revised. |
| Vaccine profiles `infection_blocking`, `transmission_blocking`, `next_generation` | higher VE_sus/VE_inf/VE_dur | Scenario/stress test | These are product-target or mechanism scenarios, not empirical current-product estimates. Wording revised. |
| Resistance `country_timeline` prevalence anchors | country-specific timeline CSV | Direct surveillance/literature data | Anchor values have source rows; `fitness_R=1.0` remains an epidemiologically motivated assumption. |
| Fixed resistance levels | 0.05, 0.30, 0.70, 0.95 | Scenario/stress test | Deliberate low-to-very-high contrasts; should not be presented as country estimates. |
| Resistance fitness scenarios/grid | 0.70-1.25 | Scenario/stress test | Literature supports concern about rapid MRBP expansion, but relative fitness is not directly measured. Wording revised. |
| Resistant treatment/PEP effect | 0.1 | Implementation/scenario assumption | Direction supported by macrolide resistance; exact residual effect is scenario-based. |
| Reporting scenarios | 0.5, 1.0, 1.5 and age/time variants | Scenario/sensitivity | Under-reporting literature supports uncertainty; exact multipliers are sensitivity assumptions. |
| Intervention coverage updates | strategy-specific | Scenario/implementation assumption | Current coverage inputs are data-derived where available; future improved coverage is scenario design. |
| Maternal immunization VE_sym | 0.92 | Literature-supported anchor | Consistent with high infant/hospitalization protection in maternal Tdap studies. |
| Maternal VE_sus and cocooning/contact reduction | 0.55 and 0.30 | Literature-informed decomposition | Studies support overall infant protection; decomposition into infection blocking and contact reduction is model-specific. |

## Bayesian Prior/Nuisance Parameters

| Parameter | Prior | Audit classification | Verdict/action |
|---|---|---|---|
| `log_beta_S` | Normal around calibrated beta | Calibrated/prior | Correct: uncertainty around calibrated transmission rate. |
| `log_reporting_multiplier` | Normal around calibrated multiplier | Calibrated/prior | Correct: reporting uncertainty, not direct literature. |
| `VE_sus`, `VE_inf`, `VE_dur` | beta priors/fixed mean | Literature-informed decomposition | Exact components not directly identifiable; wording revised. |
| `relative_infectiousness_asymptomatic` | beta prior | Literature-informed assumption | Exact ratio not directly measured; wording revised. |
| `infectious_duration_symptomatic` | log-normal | Clinical anchor + nuisance prior | Added interpretation. |
| `infectious_duration_asymptomatic` | log-normal | Literature-informed assumption | Added interpretation. |
| `fitness_R` | beta prior centered at 1.0 | Epidemiologically motivated assumption | Not a measured relative-fitness parameter; wording revised. |
| `resistance_prevalence` | fixed country timeline | Direct data where available | Correct as fixed evidence anchor; must distinguish from fitness assumption. |

## Overall Conclusion

The parameter set is defensible if the manuscript distinguishes four
provenance classes. The most important correction was wording: several
parameters have literature support for their direction or plausible range, but
not for the exact number. The files now label those as calibrated,
literature-informed, implementation, or scenario assumptions rather than
implying every value is directly copied from a paper.
