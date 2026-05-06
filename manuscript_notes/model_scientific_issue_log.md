# Model Scientific Issue Log

This log tracks the model-design issues found in the line-by-line review and
the decision taken for each item. It is intended to keep the manuscript aligned
with the code actually used for analysis.

## Fixed in code

1. ODE symptomatic and asymptomatic incident outcomes now use exposed-to-clinical
   progression flows, not infection-at-susceptible-entry flows.
2. The ODE observation layer now has an explicit care/testing/reporting cascade
   helper. Existing age-group `reporting_rate` values remain the final reporting
   probability when no split components are supplied.
3. Intervention scenarios now burn in under the matched current-practice baseline
   and apply intervention parameters at analysis start.
4. Initial infection seeding now normalizes the seed age distribution and caps
   seeded infections by available susceptible/vaccinated source pools.
5. Imported infections now conserve population by capping exposure introductions
   to the actual source pools removed.
6. Infant annualized incidence now uses infant population time at risk rather
   than total population.
7. Calibration objective alignment no longer collapses model output to a mean
   when observed and simulated series lengths differ.
8. `config_overrides` now has final precedence after country profile and
   resistance-timeline application.
9. Parameter preparation now rejects invalid probabilities, negative populations,
   negative transition/transmission values, invalid treatment/PEP inputs, invalid
   initialization/importation weights, and failed contact reciprocity correction
   tolerances instead of silently clipping core inputs.
10. Dynamic PEP activation now uses the same final observation probability as
    reported cases, including any explicit care/testing/reporting cascade.
11. Explicit seed age distributions now normalize only over specified age groups;
    unspecified groups receive zero seed weight unless no distribution is supplied.
12. Vaccine-waning sensitivity samples now preserve the configured ratio between
    recent and waned vaccine-duration stages.
13. The reference complex/network model now estimates snapshot incidence from
    exposed progression over each observation interval instead of differencing
    active `I + A` prevalence.
14. The reference model's bundled observation data paths now resolve relative to
    the companion network tree when run from the parent repo.

## Explicit assumptions or remaining manuscript cautions

1. Country resistance-timeline scenarios may use a 2025 current-evidence anchor
   while some other denominators remain tied to the 2023 analysis inputs. Any
   manuscript text must label this as a current-evidence resistance scenario,
   not a pure 2023 surveillance baseline.
2. Burn-in resistance rebalancing is an initialization device for the analysis
   start state. It should not be described as a mechanistic strain-emergence
   process.
3. Routine vaccination remains a coverage-relaxation approximation over tracked
   vaccine states. The ODE does not explicitly track booster histories for
   naturally immune individuals.
4. Sensitivity analysis uses the explicitly configured baseline country and
   records it in outputs. Multi-country sensitivity requires a declared
   scenario expansion.
5. The companion network scaffold is not the runtime model for the primary ODE
   outputs. Manuscript claims must not mix network mechanisms into ODE results.
6. Network demography changes node states but not edges over long horizons.
7. Network maternal immunization is a newborn/youngest-age proxy, not a mechanistic
   pregnancy-to-infant antibody-transfer model.
8. Network strain outputs are post-simulation projections, not mechanistic
   co-circulating strain competition.
9. Serology and hospitalization target tables are not supported by the complex
   calibration objective unless the objective is extended.
10. Network-layer contact clustering may exceed target contact-matrix cells before
    residual matching; contact-matrix preservation must be checked before using
    clustered network outputs as primary evidence.
11. The reference model still requires a real local `epydemix-data` checkout
    for country contact matrices. Do not silently replace this with a synthetic
    contact matrix for manuscript analyses.

## Verification notes

1. Main ODE tests: `python -m pytest -q tests` passes.
2. Syntax checks: `python -m compileall -q src_python tests` passes.
3. Targeted reference-model tests for smoke, observation, burden, and complex
   objectives pass.
4. The full companion-network test suite is not clean in this checkout because
   the local `epydemix-data` contact-data checkout is absent; this is tracked as
   a data-fixture/completeness risk, not as evidence that the primary ODE outputs
   are valid.
