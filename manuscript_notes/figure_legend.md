# Figure Logic and Legends

## Manuscript Logic

The revised figure sequence is designed to move from context to mechanism to decision-relevant results.

1. Establish international and regional pertussis context, then show why the ten country profiles were selected and that calibration reproduces observed data.
2. Test how vaccine mechanism (especially transmission blocking) changes infant burden, total infections and infection-source composition.
3. Show how macrolide resistance and vaccine transmission-blocking interact across a fitness × VE_inf grid.
4. Translate the mechanism results into conditional intervention scenario ordering with uncertainty quantification.
5. Move input data, source provenance, calibration checks, model architecture, temporal diagnostics, reporting assumptions, resistance hindcast plausibility checks and sensitivity analysis to JAMA-style eFigures.

All panels are labelled A-F in the figure files. Descriptive panel titles, roles and explanatory details are kept here in the legend. Each main figure carries one dominant claim (stated explicitly below each figure heading).

**Posterior-validity elements:** Figure 1D and Figure 4D incorporate conditional posterior predictive intervals only when the beta-grid posterior validity checks pass. If posterior validity is not achieved, these panels fall back to deterministic point estimates (Fig 1D) or a resistance-benefit scatter (Fig 4D). Figure 4B cell annotations use approximate horizon-scaled predictive intervals around deterministic intervention comparisons, labelled with JAMA-style interval wording as "95% PI" followed by "lower to upper"; these are not full intervention posterior credible intervals or full structural-uncertainty intervals. Cross-country summary intervals in other deterministic scenario panels are empirical 2.5th-97.5th percentile ranges across country profiles, with 25th-75th percentile intervals shown as the thicker inner band where space permits.

## Main Figure 1. Global context, country selection and baseline heterogeneity

File: `outputs/figures/figure_1_baseline_heterogeneity.pdf/png`

**Claim:** The 10 country profiles span sufficient heterogeneity in demography, immunization programmes, reported incidence and resistance starting points, and the calibrated model reproduces observed reported-case levels.

**A. WHO regional reported incidence context.** Reported pertussis incidence is shown for the global total and the five WHO regions represented in the ten-country set, with the remaining WHO regions shown as a grey background context. The selected country profiles come from the Western Pacific, South-East Asia, European, Americas and African regions, so this panel establishes the wider surveillance backdrop rather than claiming global representativeness.

**B. Country selection basis.** The panel summarizes the profile dimensions that motivated the ten-country set: WHO region, population size, observed mean reported incidence, starting resistant fraction and routine programme signature. This is intended to make the country choice reproducible and explicit rather than implicit.

**C. Model-data reported incidence anchor.** Observed mean annual reported incidence is compared with modelled annual reported incidence for each country profile. Points are coloured by the resistant infection fraction at the start of the saved analysis period. The dashed line indicates equality between observed and modelled reported incidence; countries with accepted calibration artifacts are based on calibrated configurations, while the remaining country runs should still be interpreted as scenario analyses rather than definitive inference.

**D. Baseline burden metrics.** Annualized modelled incidence of all infections, reported cases and infant cases is shown by country on a log scale, with conditional beta-grid posterior predictive intervals that include transmission-rate uncertainty plus horizon-scaled stochastic observation/process dispersion. Countries are ordered by modelled infant case incidence.

**Panel roles:** A = context/motivation; B = methodological bridge (country selection justification); C = calibration check; D = anchor panel (core baseline result).

**Note:** Resistance trajectory and epidemic recurrence diagnostics are shown in eFigure 6 (baseline temporal dynamics) and eFigure 8 (resistance dynamics).

## Main Figure 2. Vaccine mechanism scenarios

File: `outputs/figures/figure_2_vaccine_mechanisms.pdf/png`

**Claim:** Stronger vaccine transmission-blocking effects (VE_inf) produce progressively larger reductions in both infant cases and total infections, and the mechanism differences are visible in infection-source decomposition.

**A. Vaccine scenario parameter matrix.** The five vaccine profiles (no vaccine, symptom-protective aP, infection-blocking, transmission-blocking, upper-bound high-transmission-blocking) are shown as a tile plot of VE_sus, VE_sym, VE_inf and VE_dur values. This panel defines the scenarios for the reader.

**B. Infant case burden by vaccine scenario.** Annualized infant case incidence is shown across countries for each vaccine scenario, with country-level points, cross-country median, 50% interval and 95% interval on a log scale.

**C. Infection-source decomposition.** Median infection shares by maternal, dose-1, dose-2, dose-3-plus and waned source histories are shown as stacked bars for each vaccine scenario, illustrating how stronger vaccine profiles shift the origin composition of infections.

**D. Total infection burden by vaccine scenario.** Annualized all-infection incidence is shown across countries for each vaccine scenario, with country-level points, cross-country median, 50% interval and 95% interval on a log scale.

**Panel roles:** A = methodological bridge (scenario definition); B = anchor panel (core evidence); C = mechanistic explanation; D = trade-off/translational consequence.

**Note:** Country-specific outcome breakdowns, representative trajectories and the full parameter matrix are shown in eFigure 7 (vaccine mechanism deep dive).

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

**Note:** The full country-specific fitness × VE_inf grid, threshold analysis and extended resistance dynamics are shown in eFigure 9 (full grid) and eFigure 8 (resistance dynamics). Resistance hindcast plausibility checks against observed trajectories in China, Japan and Australia are shown in eFigure 13.

## Main Figure 4. Projected intervention scenario ordering

File: `outputs/figures/figure_4_intervention_prioritisation.pdf/png`

**Claim:** Projected intervention scenario ordering depends on vaccine transmission-blocking assumptions and resistance-aware treatment assumptions; the combined strategy (transmission-blocking vaccine profile + pregnancy vaccination plus adult/household transmission-reduction proxies + adolescent boosting + resistance-guided treatment and PEP) is associated with the largest modeled infant-case reductions, while resistance-guided treatment alone provides projected benefit that scales with starting resistance prevalence.

**A. Infant case burden by intervention and country.** Annualized infant case incidence is shown for the current strategy and each intervention. Individual country points are jittered around the strategy axis; black diamonds show cross-country medians with 50% and 95% intervals.

**B. Country × strategy heatmap.** Within-country relative infant-case reduction versus current practice is shown for each country-strategy combination. Cell annotations show the point estimate followed by the approximate 95% PI using "lower to upper" interval wording, derived from the same negative-binomial stochastic overlay used for annualized burden displays. These approximate PIs are not full posterior intervention uncertainty. This avoids comparing absolute burden levels across countries with different baseline incidence and makes within-country intervention scenario ordering visible.

**C. Median intervention burden across outcomes.** Median annualized incidence across countries is shown for infant cases, reported cases and all infections, with 50% and 95% intervals, showing how intervention scenario orderings compare across outcome measures and differ in magnitude.

**D. Conditional beta-grid posterior predictive intervals or resistance-benefit relationship.** When beta-grid posterior checks pass: conditional posterior predictive intervals for baseline infant case incidence are shown by country, with calibrated point estimates overlaid as crosses. If posterior checks are not achieved: the benefit of resistance-guided treatment for infant cases is plotted against starting resistant fraction, with a descriptive fitted line showing that higher starting resistance is associated with greater benefit from resistance-guided treatment.

**Panel roles:** A = anchor panel (core ordering evidence); B = ordering/benchmark comparison (country heterogeneity); C = multi-outcome consistency check; D = conditional uncertainty quantification or translational consequence (resistance-benefit relationship).

**Note:** Pregnancy package decomposition (direct antibody, adult boosting, cocooning components), intervention lever definitions, country-specific trajectories and intervention rank tables are shown in eFigure 10 (intervention extended outcomes).

## eFigure 1. Country profile inputs

File: `outputs/appendix/extended_data_figure_1_country_inputs.pdf/png`

**A. Vaccine programme coverage.** DTP1, DTP3 and pregnancy Tdap coverage values used in the country profiles.

**B. Routine schedule timing.** Age at first and last routine pertussis-containing vaccine dose. Point size denotes routine dose count; fill denotes whether a maternal programme is included.

**C. Seasonal forcing inputs.** Country-specific seasonal peak day and seasonal amplitude derived from the processed surveillance time series. Point size denotes observed mean annual reported incidence; fill denotes whether multi-year recurrence support was identified.

**D. Aggregated contact intensity.** Total contacts per day by source age group after aggregation to the eight model age groups.

## eFigure 2. Diagnostics and robustness checks

File: `outputs/appendix/extended_data_figure_2_diagnostics_sensitivity.pdf/png`

**A. Observed surveillance time series.** Annual reported incidence time series used for country-profile input derivation, shown by country code.

**B. Calibration diagnostic.** For available calibration output, the grey line shows observed reported-case intervals and the orange line/shaded band shows the calibrated model mean and approximate predictive interval.

**C. Reporting-rate sensitivity.** Median annualized all-infection, reported-case and infant-case incidence across countries under reporting-rate assumptions, with 50% and 95% cross-country intervals.

**D. Global sensitivity analysis.** Pearson, Spearman, and partial-rank screening correlations between sampled parameter values and annualized infant case incidence. Positive correlations indicate parameters associated with higher infant burden in the Latin-hypercube sensitivity runs.

## eFigure 3. Data provenance and preprocessing audit

File: `outputs/appendix/extended_data_figure_3_data_provenance.pdf/png`

**A. Registered source domains.** Source registry entries are grouped into country input data, clinical/model assumptions and resistance evidence domains.

**B. Repository data footprint.** File counts and disk footprint are summarized for raw inputs, processed inputs, simulation outputs, summaries, calibration/tables and manuscript notes.

**C. Country evidence completeness matrix.** Availability of the main country-specific evidence domains is shown for each modeled country profile.

**D. Macrolide-resistance evidence timeline.** Country-specific resistance anchors and measured isolate fractions are plotted by evidence year with reported uncertainty intervals where available.

## eFigure 4. Calibration acceptance and fit diagnostics

File: `outputs/appendix/extended_data_figure_4_calibration_diagnostics.pdf/png`

**A. Calibration acceptance and fit score.** Accepted country calibration artifacts are shown with their final fit scores.

**B. Observed and calibrated reports.** Observed reported-case intervals are shown against the calibrated model mean and approximate predictive interval for each country.

**C. Fitted reporting probabilities by age.** Age-specific reporting probabilities retained in the accepted calibration artifacts are shown by country.

**D. Calibrated transmission and interval width.** The calibrated transmission rate is plotted against the relative width of the approximate predictive interval, with point colour showing data fit score.

## eFigure 5. Model architecture and state-space accounting

File: `outputs/appendix/extended_data_figure_5_model_architecture.pdf/png`

**A. State-space components.** The model includes eight age groups, two strains, eight immune/dose origins, 74 compartments per age group and 592 ODE state variables.

**B. Compartment block accounting.** The 74 compartments per age group are decomposed into susceptible-origin, exposed, infectious, treated and natural/waned-immunity blocks.

**C. Vaccine-effect routes.** The four vaccine mechanism parameters are mapped to susceptibility, symptomatic disease, onward infectiousness and infectious duration.

**D. Origin-specific effect weights.** Maternal, partial-dose, recent and waned vaccine histories carry different relative vaccine-effect weights.

## eFigure 6. Baseline temporal dynamics

File: `outputs/appendix/extended_data_figure_6_baseline_dynamics.pdf/png`

**A. All-infection incidence.** Baseline infection incidence is shown over the saved analysis period when detailed trajectories are available; otherwise the annualized summary endpoint is shown by country.

**B. Infant case incidence.** Baseline infant case incidence is shown over time when detailed trajectories are available; otherwise the annualized summary endpoint is shown by country.

**C. Resistant fraction dynamics.** The resistant infection fraction is shown through the saved analysis period when detailed trajectories are available; otherwise start-to-end resistant fraction endpoints are shown.

**D. Infection contribution.** The share of all infections attributable to each age group and strain is summarized over the analysis period when detailed trajectories are available; otherwise source-history shares are shown from the summary outputs.

## eFigure 7. Vaccine mechanism deep dive

File: `outputs/appendix/extended_data_figure_7_vaccine_deep_dive.pdf/png`

**A. Vaccine scenario parameter matrix.** The no-vaccine, current aP, infection-blocking, transmission-blocking, and upper-bound high-transmission-blocking scenarios are shown across `VE_sus`, `VE_sym`, `VE_inf` and `VE_dur`.

**B. Country-specific outcome reductions.** Relative reductions in infant cases, reported cases, all infections and resistant infections are shown for each vaccine scenario and country.

**C. Infection-source histories.** Median infection shares by maternal, dose-1, dose-2, dose-3-plus and waned source histories are summarized across countries, with annotated 95% cross-country intervals.

**D. Representative vaccine trajectories.** Infant case trajectories are shown for Australia and China under the vaccine mechanism scenarios when detailed trajectories are available; otherwise annualized scenario endpoints are shown.

## eFigure 8. Resistance evidence, initialization and dynamics

File: `outputs/appendix/extended_data_figure_8_resistance_dynamics.pdf/png`

**A. Scenario target versus realized initialization.** Fixed resistance scenarios are compared with their realized starting resistant fraction; country-timeline runs use the country-specific anchor.

**B. Resistant infection burden.** Annualized resistant infection incidence is shown by country and resistance scenario.

**C. Treatment and PEP event burden.** Median treated-case and PEP-averted event rates are summarized across resistance scenarios, with 50% and 95% cross-country intervals.

**D. Sensitive and resistant strain trajectories.** Country-timeline infection trajectories are shown by strain for Australia and China when detailed trajectories are available; otherwise annualized strain-specific endpoints are shown.

## eFigure 9. Full VEinf-fitness grid

File: `outputs/appendix/extended_data_figure_9_full_grid.pdf/png`

**A. Country-specific infant burden grid.** Annualized infant case incidence is shown for the full `VE_inf` and resistant-strain fitness grid in each country.

**B. Benefit of high transmission blocking.** The relative infant-case benefit of increasing `VE_inf` from the lowest to the highest grid value is shown by country and resistant-strain fitness.

**C. Median burden across countries.** Median infant-case and all-infection incidence are summarized across countries over the same grid.

**D. End-period resistance.** Median end-period resistant fraction is summarized across countries over the same grid.

## eFigure 10. Intervention strategy extended outcomes

File: `outputs/appendix/extended_data_figure_10_intervention_extended.pdf/png`

**A. Intervention lever matrix.** Each intervention strategy is mapped to the child-coverage, adolescent-booster, maternal-immunization, resistance-guided-treatment and vaccine-improvement levers it modifies.

**B. Country-specific outcome reductions.** Relative reductions in infant cases, reported cases, all infections and resistant infections are shown by strategy and country.

**C. Pregnancy package decomposition.** Infant-case reductions are shown separately for the three mechanistic components of the modeled package: direct antibody protection (passive transfer to neonates), adult boosting (reduced reproductive-age adult susceptibility and infectiousness), and cocooning (reduced household contact intensity). The full package is shown for comparison, with 50% and 95% cross-country intervals.

**D. Current versus combined trajectories.** Infant case trajectories compare the current strategy with the combined strategy for Australia and China when detailed trajectories are available; otherwise annualized endpoints are shown.

**E. Intervention rank by country.** Strategies are ranked within each country by relative reduction in infant cases.

## eFigure 11. Model structure schematic

File: `outputs/appendix/extended_data_figure_11_model_structure.pdf/png`

**A. Age-omitted transmission schematic.** The figure condenses the full model into a single schematic panel showing the origin-specific susceptible block, strain-specific exposed and infectious branches, and the retained history of the eight susceptible-origin states. Age is omitted for clarity, and the full ODE repeats the same template across eight age groups with treated states also present in the dynamic system.

## eFigure 12. Contact matrix reconstruction

File: `outputs/appendix/extended_data_figure_12_contact_matrix_reconstruction.pdf/png`

The dynamic layout shows each country twice: the raw Prem/contactdata matrix binned in 5-year age classes, and the population-weighted reconstructed matrix used in the model after aggregation to the eight model age groups and reciprocity balancing. The panels are ordered row-wise by country in the standard project country order, with original and reconstructed matrices paired for Australia, China, Japan, New Zealand, Sweden, United Kingdom, United States, Brazil and Thailand.

## eFigure 13. Resistance Hindcast Plausibility Checks

File: `outputs/appendix/extended_data_figure_13_resistance_hindcast.pdf/png`

**Claim:** The model's resistance dynamics module is broadly compatible with observed macrolide-resistance trajectories in countries with multi-time-point surveillance data, supporting plausibility checks for the resistance projections used in the main analysis.

**A. China hindcast (2016–2025).** Modelled resistant fraction trajectories are shown for seven fitness values (f_R = 0.70–1.25) against observed resistance prevalence data points (Fu et al. 2024: 36% in 2016; Cai et al. 2025: 99.7% in 2024). The neutral-fitness scenario (f_R = 1.0) is highlighted. Observed data points are shown with reported uncertainty intervals where available.

**B. Japan hindcast (2024–2026).** Modelled resistant fraction trajectories are shown against the observed resistance estimate from Kobe (83–88% in 2024–2025). The short hindcast window reflects limited multi-time-point data availability.

**C. Australia hindcast (2022–2025).** Modelled resistant fraction trajectories are shown against the genomic epidemiology estimate (4.3% in 2024, Fong et al. 2026). Australia's low starting prevalence tests whether the model correctly maintains low resistance when fitness is neutral and importation pressure is limited.

**D. Hindcast scoring summary.** Mean absolute error between modelled and observed resistant fractions is shown for each country and fitness value. The best-fitting fitness value is highlighted for each country. This panel summarizes which fitness assumptions are most consistent with observed resistance trajectories.

**Panel roles:** A-C = observed-data plausibility checks (country-specific hindcast); D = benchmark comparison (fitness scoring).

**Note:** The hindcast uses shortened simulation horizons (country-specific) with 10-year burn-in and the same stochastic resistance overlay as the main analysis. Results are generated by `python -m src_python.simulation.run_resistance_hindcast` and scored outputs are in `outputs/tables/resistance_hindcast_results.csv`.

## Output and Style Notes

Figures are exported as editable vector PDF and 300 dpi PNG. The plotting style uses a consistent sans-serif font, 8.5 pt bold panel labels, restrained line widths and colour-blind-aware palettes. Main and supplementary figures use upper-case A-F panel labels to keep the manuscript convention consistent.
