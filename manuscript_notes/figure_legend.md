# Figure Logic and Legends

## Manuscript Logic

The revised figure sequence is designed to move from context to mechanism to decision-relevant results.

1. Establish international and regional pertussis context, then show why the ten country profiles were selected and that calibration reproduces observed data.
2. Test how vaccine mechanism (especially transmission blocking) changes infant burden, total infections and infection-source composition.
3. Show how macrolide resistance and vaccine transmission-blocking interact across a fitness × VE_inf grid.
4. Translate the mechanism results into intervention scenario projections grouped by interpretability with uncertainty quantification.
5. Move input data, source provenance, calibration checks, model architecture, temporal diagnostics, reporting assumptions, resistance hindcast plausibility checks and sensitivity analysis to JAMA-style eFigures.

All panels are labelled A-F in the figure files. Descriptive panel titles, roles and explanatory details are kept here in the legend. Each main figure carries one dominant claim (stated explicitly below each figure heading).

**Posterior-validity elements:** Figure 1D and Figure 4D incorporate conditional beta-grid intervals only when the beta-grid validity checks pass. If validity is not achieved, these panels fall back to deterministic point estimates (Fig 1D) or a resistance-benefit scatter (Fig 4D). Figure 4B cell annotations use approximate horizon-scaled conditional 95% intervals around deterministic intervention comparisons, followed by "lower to upper" interval wording; these are not full intervention posterior credible intervals or full structural-uncertainty intervals. Cross-country summary intervals in other deterministic scenario panels are empirical 2.5th-97.5th percentile ranges across country profiles, with 25th-75th percentile intervals shown as the thicker inner band where space permits.

## Main Figure 1. Global context, country selection and baseline heterogeneity

File: `outputs/figures/figure_1_baseline_heterogeneity.pdf/png`

**Claim:** The 10 country profiles span sufficient heterogeneity in demography, immunization programmes, reported incidence and resistance starting points, and the calibrated model reproduces observed reported-case levels.

**A. WHO regional reported incidence context.** Reported pertussis incidence is shown for the global total and the five WHO regions represented in the ten-country set, with the remaining WHO regions shown as a grey background context. The selected country profiles come from the Western Pacific, South-East Asia, European, Americas and African regions, so this panel establishes the wider surveillance backdrop rather than claiming global representativeness.

**B. Country selection basis.** The panel summarizes the profile dimensions that motivated the ten-country set: WHO region, population size, observed mean reported incidence, starting resistant fraction and routine programme signature. This is intended to make the country choice reproducible and explicit rather than implicit.

**C. Model-data reported incidence anchor.** Observed mean annual reported incidence is compared with modelled annual reported incidence for each country profile. Points are coloured by the resistant infection fraction at the start of the saved analysis period. The dashed line indicates equality between observed and modelled reported incidence; countries with accepted calibration artifacts are based on calibrated configurations, while the remaining country runs should still be interpreted as scenario analyses rather than definitive inference.

**D. Baseline burden metrics.** Annualized modelled incidence of all infections, reported cases and infant cases is shown by country on a log scale, with conditional beta-grid posterior predictive intervals that include transmission-rate uncertainty plus horizon-scaled stochastic observation/process dispersion. Countries are ordered by modelled infant case incidence.

**Panel roles:** A = context/motivation; B = methodological bridge (country selection justification); C = calibration check; D = anchor panel (core baseline result).

**Note:** Resistance trajectory and epidemic recurrence diagnostics are shown in eFigure 4 (baseline temporal dynamics) and eFigure 6 (resistance dynamics).

## Main Figure 2. Vaccine mechanism scenarios

File: `outputs/figures/figure_2_vaccine_mechanisms.pdf/png`

**Claim:** Stronger vaccine transmission-blocking effects (VE_inf) produce progressively larger reductions in both infant cases and total infections, and the mechanism differences are visible in infection-source decomposition.

**A. Vaccine scenario parameter matrix.** The five vaccine profiles (no vaccine, symptom-protective aP, infection-blocking, transmission-blocking, upper-bound high-transmission-blocking) are shown as a tile plot of VE_sus, VE_sym, VE_inf and VE_dur values. This panel defines the scenarios for the reader.

**B. Infant case burden by vaccine scenario.** Annualized infant case incidence is shown across countries for each vaccine scenario, with country-level points, cross-country median, 50% interval and 95% interval on a log scale.

**C. Infection-source decomposition.** Median infection shares by maternal, dose-1, dose-2, dose-3-plus and waned source histories are shown as stacked bars for each vaccine scenario, illustrating how stronger vaccine profiles shift the origin composition of infections.

**D. Total infection burden by vaccine scenario.** Annualized all-infection incidence is shown across countries for each vaccine scenario, with country-level points, cross-country median, 50% interval and 95% interval on a log scale.

**Panel roles:** A = methodological bridge (scenario definition); B = anchor panel (core evidence); C = mechanistic explanation; D = trade-off/translational consequence.

**Note:** Country-specific outcome breakdowns and representative trajectories are shown in eFigure 5 (vaccine mechanism deep dive).

## Main Figure 3. Macrolide resistance and vaccine transmission blocking

File: `outputs/figures/figure_3_resistance_interaction.pdf/png`

**Claim:** Macrolide resistance can approach high resistant fractions under neutral or above-neutral fitness assumptions, but this behavior is conditional on fitness, importation, treatment and PEP assumptions; stronger vaccine transmission-blocking (VE_inf) reduces projected infant burden across these resistance assumptions.

**A. Resistant-fraction dynamics.** Resistant infection fraction trajectories are shown over the first 5 simulated years for all 10 study countries under their country-specific resistance timeline. Starting points (circles) reflect empirical initial resistance prevalence; countries with high baseline resistance (China, Japan) begin near saturation, while those with low initial prevalence (Australia, Brazil, United Kingdom) show transition dynamics under the baseline assumptions.

**B. Fitness-dependent resistant-fraction dynamics.** Median resistant fraction across all countries is shown for seven resistant-strain fitness values (f_R = 0.85-1.15), with 50% and 95% cross-country intervals. Fitness-cost assumptions dampen projected resistant-strain expansion, while neutral or above-neutral fitness accelerates convergence to high resistant fractions in many profiles.

**C. Burden across resistance scenarios.** Annualized infant case incidence is shown for each country across low, moderate, high and very high initial resistance scenarios. Connected lines highlight country-specific sensitivity to starting resistance prevalence. This panel establishes that resistance prevalence matters for infant burden before the heatmaps show how VE_inf interacts with it.

**D. Resistance equilibrium heatmap.** Median end-period resistant fraction across all countries is shown over the grid of resistant-strain fitness (f_R) and vaccine reduction in infectiousness (VE_inf). The annotated representative grid point shows the median and 95% cross-country interval.

**E. Infant disease burden heatmap.** Median annualized infant case incidence (log10 scale) across countries over the same fitness-VE_inf grid. The annotated representative grid point shows the median and 95% cross-country interval. Higher VE_inf substantially reduces projected infant burden across resistance-fitness assumptions. This is the anchor panel.

**F. Transmission-blocking benefit by country.** Relative infant-case reduction when VE_inf is increased from 5% to 55%, shown for each country at three fitness levels (cost, neutral, advantage). Lollipop segments highlight that the projected benefit of stronger transmission-blocking scenarios varies across fitness assumptions and epidemiological settings.

**Panel roles:** A = case illustration (country-specific dynamics); B = plausibility check under new regime (fitness sensitivity); C = claim-supporting evidence (resistance-burden link); D = benchmark comparison (resistance equilibrium); E = anchor panel (core interaction result); F = translational consequence (country-specific benefit).

**Note:** Extended resistance dynamics are shown in eFigure 6. Resistance hindcast plausibility checks against observed trajectories in China, Japan and Australia are shown in eFigure 8.

## Main Figure 4. Scenario projections by intervention category

File: `outputs/figures/figure_4_intervention_prioritisation.pdf/png`

**Claim:** Projected infant burden differs across intervention categories because vaccine transmission-blocking assumptions and resistance-aware treatment assumptions alter distinct model pathways; scenarios are grouped by interpretability rather than presented as mutually substitutable policy options.

**A. Infant case burden by intervention and country.** Annualized infant case incidence is shown for current practice and each intervention. Current practice is the status quo baseline comparator and is grouped with current-program modifications, including higher child coverage and adolescent boosting; other scenarios are grouped as implementation-dependent proxy or management scenarios and hypothetical product-target or stress-test profiles. Individual country points are jittered around the strategy axis; black diamonds show cross-country medians with 50% and empirical 95% intervals.

**B. Country x strategy heatmap.** Within-country relative infant-case reduction versus current practice is shown for each country-strategy combination. Cell annotations show the point estimate followed by the conditional 95% interval using "lower to upper" interval wording, derived from the same negative-binomial stochastic overlay used for annualized burden displays. These intervals are not full posterior intervention uncertainty. This avoids comparing absolute burden levels across countries with different baseline incidence and shows within-country scenario contrasts.

**C. Median intervention burden across outcomes.** Median annualized incidence across countries is shown for infant cases, reported cases and all infections, with 50% and empirical 95% intervals, using the same scenario grouping as panel A.

**D. Conditional beta-grid intervals or resistance-benefit relationship.** When beta-grid checks pass: conditional beta-grid intervals for baseline infant case incidence are shown by country, with calibrated point estimates overlaid as crosses. If checks are not achieved: the benefit of resistance-guided treatment for infant cases is plotted against starting resistant fraction, with a descriptive fitted line showing that higher starting resistance is associated with greater benefit from resistance-guided treatment.

**Panel roles:** A = anchor panel (category-specific burden); B = benchmark comparison (country heterogeneity); C = multi-outcome consistency check; D = conditional uncertainty quantification or translational consequence (resistance-benefit relationship).

**Note:** Maternal-household composite proxy decomposition (direct antibody, adult boosting, cocooning components), intervention lever definitions and country-specific outcome reductions are shown in eFigure 7 (intervention extended outcomes).

## eFigure 1. Country profile inputs and resistance evidence

File: `outputs/appendix/extended_data_figure_1_country_inputs.pdf/png`

**A. Vaccine programme coverage.** Available DTP1, DTP3 and pregnancy Tdap coverage values used in the country profiles.

**B. Routine schedule timing.** Age at first and last routine pertussis-containing vaccine dose. Point size denotes routine dose count; fill denotes whether a maternal programme is included.

**C. Aggregated contact intensity.** Total contacts per day by source age group after aggregation to the eight model age groups.

**D. Macrolide-resistance evidence timeline.** Country-specific resistance anchors and measured isolate fractions are plotted by evidence year with reported uncertainty intervals where available.

## eFigure 2. Surveillance, calibration and reporting diagnostics

File: `outputs/appendix/extended_data_figure_2_diagnostics_sensitivity.pdf/png`

**A. Observed surveillance time series.** Annual reported incidence time series used for country-profile input derivation, shown by country code.

**B. Calibration diagnostic.** For available calibration output, the grey line shows observed reported-case intervals and the orange line/shaded band shows the calibrated model mean and approximate predictive interval.

**C. Reporting-rate sensitivity.** Median annualized all-infection, reported-case and infant-case incidence across countries under reporting-rate assumptions, with 50% and 95% cross-country intervals.

**D. Fitted reporting probabilities by age.** Age-specific reporting probabilities retained in the accepted calibration artifacts are shown by country.

## eFigure 3. Model structure and vaccine-effect weights

File: `outputs/appendix/extended_data_figure_3_model_structure.pdf/png`

**A. Mechanistic model-design schematic.** Four formula-based diagrams summarize the state space, transmission kernel, within-age natural history, and immunity/vaccine-mechanism parameterization. The full ODE repeats a 74-state within-age template across 8 age strata, with strain-specific force of infection, origin-specific vaccine effects, SIRWS waning/boosting, and PEP represented as a force-of-infection modifier rather than as a separate compartment.

**B. Origin-specific effect weights.** Maternal, partial-dose, recent and waned vaccine histories carry different relative vaccine-effect weights.

## eFigure 4. Baseline temporal dynamics

File: `outputs/appendix/extended_data_figure_4_baseline_dynamics.pdf/png`

**A. All-infection incidence.** Baseline infection incidence is shown over the saved analysis period when detailed trajectories are available; otherwise the annualized summary endpoint is shown by country.

**B. Infant case incidence.** Baseline infant case incidence is shown over time when detailed trajectories are available; otherwise the annualized summary endpoint is shown by country.

**C. Resistant fraction dynamics.** The resistant infection fraction is shown through the saved analysis period when detailed trajectories are available; otherwise start-to-end resistant fraction endpoints are shown.

**D. Infection contribution.** The share of all infections attributable to each age group and strain is summarized over the analysis period when detailed trajectories are available; otherwise source-history shares are shown from the summary outputs.

## eFigure 5. Vaccine mechanism deep dive

File: `outputs/appendix/extended_data_figure_5_vaccine_deep_dive.pdf/png`

**A. Country-specific outcome reductions.** Relative reductions in infant cases, reported cases, all infections and resistant infections are shown for each vaccine scenario and country.

**B. Infection-source histories.** Median infection shares by maternal, dose-1, dose-2, dose-3-plus and waned source histories are summarized across countries, with annotated 95% cross-country intervals.

**C. Representative vaccine trajectories.** Infant case trajectories are shown for Australia and China under the vaccine mechanism scenarios when detailed trajectories are available; otherwise annualized scenario endpoints are shown.

## eFigure 6. Resistance dynamics

File: `outputs/appendix/extended_data_figure_6_resistance_dynamics.pdf/png`

**A. Resistant infection burden.** Annualized resistant infection incidence is shown by country and resistance scenario.

**B. Treatment and PEP event burden.** Median treated-case and PEP-averted event rates are summarized across resistance scenarios, with 50% and 95% cross-country intervals.

**C. Sensitive and resistant strain trajectories.** Country-timeline infection trajectories are shown by strain for Australia and China when detailed trajectories are available; otherwise annualized strain-specific endpoints are shown.

## eFigure 7. Intervention strategy extended outcomes

File: `outputs/appendix/extended_data_figure_7_intervention_extended.pdf/png`

**A. Intervention lever matrix.** Each intervention strategy is mapped to the higher-child-coverage, adolescent-booster, maternal-household composite proxy, resistance-guided-treatment, upper-bound-vaccine, and transmission-blocking-vaccine levers it modifies.

**B. Country-specific outcome reductions.** Relative reductions in infant cases, reported cases, all infections and resistant infections are shown by strategy and country.

**C. Maternal-household composite proxy decomposition.** Infant-case reductions are shown separately for the three mechanistic components of the modeled proxy: direct antibody protection (passive transfer to neonates), adult boosting (reduced reproductive-age adult susceptibility and infectiousness), and cocooning (reduced household contact intensity). The full composite proxy is shown for comparison, with 50% and 95% cross-country intervals.

## eFigure 8. Resistance Hindcast Plausibility Checks

File: `outputs/appendix/extended_data_figure_8_resistance_hindcast.pdf/png`

**Claim:** The model's resistance dynamics module is broadly compatible with observed macrolide-resistance trajectories in countries with multi-time-point surveillance data, supporting plausibility checks for the resistance projections used in the main analysis.

**A. China hindcast (2016–2024).** Modelled resistant fraction trajectories are initialized from the 2016 resistance anchor (Fu et al. 2024: 36%) and shown for six fitness values (f_R = 0.85–1.10) against observed resistance prevalence data points in 2022 (Fu et al. 2024: 97.2%) and 2024 (Cai et al. 2025: 99.7%). The neutral-fitness scenario (f_R = 1.0) is highlighted. Observed data points are shown with reported uncertainty intervals where available.

**B. Japan hindcast (2024–2025).** Modelled resistant fraction trajectories are initialized from the 2024 high-prevalence anchor and compared with the observed 2025 resistance estimate. The short hindcast window reflects limited multi-time-point data availability.

**C. Australia hindcast (2024–2026).** Modelled resistant fraction trajectories are initialized from and compared with the genomic epidemiology estimate (4.3% in 2024, Fong et al. 2026). Australia's low starting prevalence tests whether the model maintains low resistance when fitness is neutral and importation pressure is limited.

**D. Hindcast scoring summary.** Mean absolute error between modelled and observed resistant fractions is shown for each country and fitness value. The best-fitting fitness value is highlighted for each country. This panel summarizes which fitness assumptions are most consistent with observed resistance trajectories.

**Panel roles:** A-C = observed-data plausibility checks (country-specific hindcast); D = benchmark comparison (fitness scoring).

**Note:** The hindcast uses country-specific saved horizons with the same 15-year burn-in as the main analysis and the six-value fitness grid present in `outputs/tables/resistance_hindcast_results.csv`. Results are generated by `python -m src_python.simulation.run_resistance_hindcast` and scored outputs are in `outputs/tables/resistance_hindcast_scores.csv`.

## Output and Style Notes

Figures are exported as editable vector PDF and 300 dpi PNG. The plotting style uses a consistent sans-serif font, 8.5 pt bold panel labels, restrained line widths and colour-blind-aware palettes. Main and supplementary figures use upper-case A-F panel labels to keep the manuscript convention consistent.
