# Figure Logic and Legends

## Manuscript Logic

The revised figure sequence is designed to move from context to mechanism to decision-relevant results.

1. Establish country heterogeneity and the uncalibrated model-data anchor.
2. Test how vaccine mechanism changes infant burden, total infections and resistant infections.
3. Show how macrolide resistance and vaccine transmission-blocking interact.
4. Translate the mechanism results into intervention prioritisation.
5. Move input data, calibration checks, reporting assumptions and sensitivity analysis to Extended Data.

All panels are labelled only as A-D in the figure files. Descriptive panel titles and explanatory details are kept here in the legend.

## Main Figure 1. Baseline heterogeneity across country profiles

File: `outputs/figures/figure_1_baseline_heterogeneity.pdf/png`

**A. Model-data reported incidence anchor.** Observed mean annual reported incidence is compared with modelled annual reported incidence for each country profile. Points are coloured by the resistant infection fraction at the start of the saved analysis period. The dashed line indicates equality between observed and modelled reported incidence; the model outputs should be interpreted as scenario analyses rather than definitive country calibrations.

**B. Baseline burden metrics.** Annualized modelled incidence of all infections, reported cases and infant cases is shown by country on a log scale. Countries are ordered by modelled infant case incidence.

**C. Resistance trajectory over the analysis period.** Open points show the starting resistant infection fraction and filled points show the end-of-analysis fraction. Horizontal segments show the direction and magnitude of change during the 30-year analysis period.

**D. Epidemic recurrence and infant burden.** Mean interval between model-detected epidemic peaks is plotted against infant case incidence. Dashed vertical lines mark 3- and 5-year intervals as reference recurrence periods.

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

**D. Country-specific benefit of high VEinf.** The heat map shows the relative infant case reduction when VEinf is increased from 0% to 90%, by country and initial resistant prevalence.

## Main Figure 4. Intervention prioritisation

File: `outputs/figures/figure_4_intervention_prioritisation.pdf/png`

**A. Infant case reduction by intervention and country.** Relative reduction in infant cases versus the current strategy is shown for higher child coverage, resistance-guided treatment, adolescent booster, maternal immunization, next-generation vaccine and the combined strategy.

**B. Infection-burden trade-off.** Relative reduction in all infections is plotted against relative reduction in infant cases for each intervention-country combination.

**C. Median intervention effect across outcomes.** Median relative reductions across countries are shown for infant cases, reported cases and all infections.

**D. Resistance-guided treatment and starting resistance.** The benefit of resistance-guided treatment for infant cases is plotted against starting resistant fraction. The fitted line is descriptive and is not intended as a calibrated causal regression.

## Extended Data Figure 1. Country profile inputs

File: `outputs/appendix/extended_data_figure_1_country_inputs.pdf/png`

**A. Vaccine programme coverage.** DTP1, DTP3 and maternal immunization coverage values used in the country profiles.

**B. Routine schedule timing.** Age at first and last routine pertussis-containing vaccine dose. Point size denotes routine dose count; fill denotes whether a maternal programme is included.

**C. Seasonal forcing inputs.** Country-specific seasonal peak day and seasonal amplitude derived from the processed surveillance time series. Point size denotes observed mean annual reported incidence; fill denotes whether multi-year recurrence support was identified.

**D. Aggregated contact intensity.** Total contacts per day by source age group after aggregation to the five model age groups.

## Extended Data Figure 2. Diagnostics and robustness checks

File: `outputs/appendix/extended_data_figure_2_diagnostics_sensitivity.pdf/png`

**A. Observed surveillance time series.** Annual reported incidence time series used for country-profile input derivation, shown by country code.

**B. Calibration diagnostic.** For available calibration output, the grey line shows observed annual reported cases and the orange line/shaded band shows the calibrated model mean and approximate predictive interval.

**C. Reporting-rate sensitivity.** Median annualized all-infection, reported-case and infant-case incidence across countries under reporting-rate assumptions.

**D. Global sensitivity analysis.** Pearson correlations between sampled parameter values and annualized infant case incidence. Positive correlations indicate parameters associated with higher infant burden in the Latin-hypercube sensitivity runs.

## Output and Style Notes

Figures were exported as editable vector PDF and 300 dpi PNG at approximately Nature double-column width. The plotting style uses a consistent sans-serif font, 8.5 pt bold panel labels, restrained line widths and colour-blind-aware palettes. The Nature production guide uses lower-case panel labels, but these figures use upper-case A-D to match the requested manuscript convention.
