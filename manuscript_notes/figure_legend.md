# Figure Logic and Legends

## Manuscript Logic

The revised figure sequence is designed to move from context to mechanism to decision-relevant results.

1. Establish global and regional pertussis context, then show why the ten country profiles were selected.
2. Test how vaccine mechanism changes infant burden, total infections and resistant infections.
3. Show how macrolide resistance and vaccine transmission-blocking interact.
4. Translate the mechanism results into intervention prioritisation.
5. Move input data, source provenance, calibration checks, model architecture, temporal diagnostics, reporting assumptions and sensitivity analysis to JAMA-style eFigures.

All panels are labelled only as A-F in the figure files. Descriptive panel titles and explanatory details are kept here in the legend.

## Main Figure 1. Global context, country selection and baseline heterogeneity

File: `outputs/figures/figure_1_baseline_heterogeneity.pdf/png`

**A. WHO regional reported incidence context.** Reported pertussis incidence is shown for the global total and the four WHO regions represented in the nine-country set, with the remaining WHO regions shown as a grey background context. The selected country profiles come from the Western Pacific, South-East Asia, European and Americas regions, so this panel establishes the wider surveillance backdrop rather than claiming global representativeness.

**B. Country selection basis.** The panel summarizes the profile dimensions that motivated the nine-country set: WHO region, population size, observed mean reported incidence, starting resistant fraction and routine programme signature. This is intended to make the country choice reproducible and explicit rather than implicit.

**C. Model-data reported incidence anchor.** Observed mean annual reported incidence is compared with modelled annual reported incidence for each country profile. Points are coloured by the resistant infection fraction at the start of the saved analysis period. The dashed line indicates equality between observed and modelled reported incidence; countries with accepted calibration artifacts are based on calibrated configurations, while the remaining country runs should still be interpreted as scenario analyses rather than definitive inference.

**D. Baseline burden metrics.** Annualized modelled incidence of all infections, reported cases and infant cases is shown by country on a log scale. Countries are ordered by modelled infant case incidence.

**E. Resistance trajectory over the analysis period.** Open points show the starting resistant infection fraction and filled points show the end-of-analysis fraction. Horizontal segments show the direction and magnitude of change during the 26-year analysis period.

**F. Epidemic recurrence and infant burden.** Mean interval between model-detected epidemic peaks is plotted against infant case incidence. Dashed vertical lines mark 3- and 5-year intervals as reference recurrence periods.

## Main Figure 2. Vaccine mechanism scenarios

File: `outputs/figures/figure_2_vaccine_mechanisms.pdf/png`

**A. Infant cases under vaccine scenarios.** Annualized infant case incidence is shown for no vaccine, the current acellular pertussis profile, infection-blocking, transmission-blocking and next-generation vaccine profiles.

**B. Infant case reduction versus no vaccine.** Relative reduction in infant cases is summarized across countries for each vaccine scenario.

**C. Total infection reduction versus infant case reduction.** Each point is a country-scenario combination. The diagonal reference line indicates equal relative reductions in total infections and infant cases; points above the line indicate scenarios with stronger infant case reduction than total infection reduction.

**D. Resistant infection reduction versus no vaccine.** Relative reduction in resistant infections is shown for countries where the no-vaccine comparator had resistant infections. Countries with zero resistant infections in the comparator are excluded from this panel.

## Main Figure 3. Macrolide resistance and vaccine transmission blocking

File: `outputs/figures/figure_3_resistance_interaction.pdf/png`

**A. Resistant fraction trajectories.** Resistant infection fractions are shown over 30 simulated years for Australia and China under country-timeline, low, moderate, high and very high initial resistance scenarios.

**B. Infant burden under resistance scenarios.** Annualized infant case incidence is summarized across countries for each resistance scenario.

**C. Median infant burden across the VEinf-resistance grid.** Median annualized infant case incidence across countries is shown over the grid of vaccine reduction in infectiousness and initial resistant prevalence.

**D. Country-specific benefit of high VEinf.** The heat map shows the relative infant case reduction when VEinf is increased from the lowest to the highest grid value, by country and initial resistant prevalence.

## Main Figure 4. Intervention prioritisation

File: `outputs/figures/figure_4_intervention_prioritisation.pdf/png`

**A. Infant case reduction by intervention and country.** Relative reduction in infant cases versus the current strategy is shown for higher child coverage, resistance-guided treatment, adolescent booster, maternal immunization, next-generation vaccine and the combined strategy.

**B. Infection-burden trade-off.** Relative reduction in all infections is plotted against relative reduction in infant cases for each intervention-country combination.

**C. Median intervention effect across outcomes.** Median relative reductions across countries are shown for infant cases, reported cases and all infections.

**D. Resistance-guided treatment and starting resistance.** The benefit of resistance-guided treatment for infant cases is plotted against starting resistant fraction. The fitted line is descriptive and is not intended as a calibrated causal regression.

## eFigure 1. Country profile inputs

File: `outputs/appendix/extended_data_figure_1_country_inputs.pdf/png`

**A. Vaccine programme coverage.** DTP1, DTP3 and maternal immunization coverage values used in the country profiles.

**B. Routine schedule timing.** Age at first and last routine pertussis-containing vaccine dose. Point size denotes routine dose count; fill denotes whether a maternal programme is included.

**C. Seasonal forcing inputs.** Country-specific seasonal peak day and seasonal amplitude derived from the processed surveillance time series. Point size denotes observed mean annual reported incidence; fill denotes whether multi-year recurrence support was identified.

**D. Aggregated contact intensity.** Total contacts per day by source age group after aggregation to the eight model age groups.

## eFigure 2. Diagnostics and robustness checks

File: `outputs/appendix/extended_data_figure_2_diagnostics_sensitivity.pdf/png`

**A. Observed surveillance time series.** Annual reported incidence time series used for country-profile input derivation, shown by country code.

**B. Calibration diagnostic.** For available calibration output, the grey line shows observed reported-case intervals and the orange line/shaded band shows the calibrated model mean and approximate predictive interval.

**C. Reporting-rate sensitivity.** Median annualized all-infection, reported-case and infant-case incidence across countries under reporting-rate assumptions.

**D. Global sensitivity analysis.** Pearson correlations between sampled parameter values and annualized infant case incidence. Positive correlations indicate parameters associated with higher infant burden in the Latin-hypercube sensitivity runs.

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

**A. State-space components.** The model includes eight age groups, two strains, eight immune/dose origins, 73 compartments per age group and 584 ODE state variables.

**B. Compartment block accounting.** The 73 compartments per age group are decomposed into susceptible-origin, exposed, infectious, treated and natural-immunity blocks.

**C. Vaccine-effect routes.** The four vaccine mechanism parameters are mapped to susceptibility, symptomatic disease, onward infectiousness and infectious duration.

**D. Origin-specific effect weights.** Maternal, partial-dose, recent and waned vaccine histories carry different relative vaccine-effect weights.

## eFigure 6. Baseline temporal dynamics

File: `outputs/appendix/extended_data_figure_6_baseline_dynamics.pdf/png`

**A. Weekly all-infection incidence.** Baseline weekly infection incidence is shown over the 30-year saved analysis period for each country.

**B. Weekly infant case incidence.** Baseline weekly infant case incidence is shown using infant population denominators.

**C. Resistant fraction dynamics.** The resistant infection fraction is shown through the saved analysis period.

**D. Age and strain contribution.** The share of all infections attributable to each age group and strain is summarized over the analysis period.

## eFigure 7. Vaccine mechanism deep dive

File: `outputs/appendix/extended_data_figure_7_vaccine_deep_dive.pdf/png`

**A. Vaccine scenario parameter matrix.** The no-vaccine, current aP, infection-blocking, transmission-blocking and next-generation scenarios are shown across `VE_sus`, `VE_sym`, `VE_inf` and `VE_dur`.

**B. Country-specific outcome reductions.** Relative reductions in infant cases, reported cases, all infections and resistant infections are shown for each vaccine scenario and country.

**C. Infection-source histories.** Median infection shares by maternal, dose-1, dose-2, dose-3-plus and waned source histories are summarized across countries.

**D. Representative vaccine trajectories.** Infant case trajectories are shown for Australia and China under the vaccine mechanism scenarios.

## eFigure 8. Resistance evidence, initialization and dynamics

File: `outputs/appendix/extended_data_figure_8_resistance_dynamics.pdf/png`

**A. Scenario target versus realized initialization.** Fixed resistance scenarios are compared with their realized starting resistant fraction; country-timeline runs use the country-specific anchor.

**B. Resistant infection burden.** Annualized resistant infection incidence is shown by country and resistance scenario.

**C. Treatment and PEP event burden.** Median treated-case and PEP-averted event rates are summarized across resistance scenarios.

**D. Sensitive and resistant strain trajectories.** Country-timeline infection trajectories are shown by strain for Australia and China.

## eFigure 9. Full VEinf-resistance grid

File: `outputs/appendix/extended_data_figure_9_full_grid.pdf/png`

**A. Country-specific infant burden grid.** Annualized infant case incidence is shown for the full seven-by-seven `VE_inf` and initial-resistance grid in each country.

**B. Benefit of high transmission blocking.** The relative infant-case benefit of increasing `VE_inf` from the lowest to the highest grid value is shown by country and resistance prevalence.

**C. Median burden across countries.** Median infant-case and all-infection incidence are summarized across countries over the same grid.

**D. Threshold for 50% infant-case reduction.** The minimum `VE_inf` required to reduce infant cases by at least 50% versus the lowest grid value is shown where reached.

## eFigure 10. Intervention strategy extended outcomes

File: `outputs/appendix/extended_data_figure_10_intervention_extended.pdf/png`

**A. Intervention lever matrix.** Each intervention strategy is mapped to the child-coverage, adolescent-booster, maternal-immunization, resistance-guided-treatment and vaccine-improvement levers it modifies.

**B. Country-specific outcome reductions.** Relative reductions in infant cases, reported cases, all infections and resistant infections are shown by strategy and country.

**C. Current versus combined trajectories.** Infant case trajectories compare the current strategy with the combined strategy for Australia and China.

**D. Intervention rank by country.** Strategies are ranked within each country by relative reduction in infant cases.

## eFigure 11. Model structure schematic

File: `outputs/appendix/extended_data_figure_11_model_structure.pdf/png`

**A. Age-omitted transmission schematic.** The figure condenses the full model into a single schematic panel showing the origin-specific susceptible block, strain-specific exposed and infectious branches, and the retained history of the eight susceptible-origin states. Age is omitted for clarity, and the full ODE repeats the same template across eight age groups with treated states also present in the dynamic system.

## eFigure 12. Contact matrix reconstruction

File: `outputs/appendix/extended_data_figure_12_contact_matrix_reconstruction.pdf/png`

The dynamic layout shows each country twice: the raw Prem/contactdata matrix binned in 5-year age classes, and the population-weighted reconstructed matrix used in the model after aggregation to the eight model age groups and reciprocity balancing. The panels are ordered row-wise by country in the standard project country order, with original and reconstructed matrices paired for Australia, China, Japan, New Zealand, Sweden, United Kingdom, United States, Brazil and Thailand.

## Output and Style Notes

Figures are exported as editable vector PDF and 300 dpi PNG. The plotting style uses a consistent sans-serif font, 8.5 pt bold panel labels, restrained line widths and colour-blind-aware palettes. Main and supplementary figures use upper-case A-F panel labels to keep the manuscript convention consistent.
