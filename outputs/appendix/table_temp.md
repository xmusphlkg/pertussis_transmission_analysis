## eTables

<!-- BEGIN ETABLE 1 -->
**eTable 1. Country-specific population, surveillance, vaccination, and seasonal-forcing inputs.**

<!-- Generated from `manuscript_notes/country_profile_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Population | Seasonal phase | Seasonal amplitude | Mean reported incidence per 100k | Vaccine product | Adolescent booster | Maternal program |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | 26,451,124 | 310.63 | 0.149 | 36.32 | aP | Yes | Yes |
| China | 1,422,584,932 | 223.07 | 0.1738 | 1.315 | aP | No | No |
| United Kingdom | 68,682,962 | 335.29 | 0.1236 | 3.460 | aP | No | Yes |
| Japan | 124,370,946 | 250.79 | 0.1377 | 2.752 | aP | No | No |
| New Zealand | 5,172,836 | 343.47 | 0.1689 | 20.01 | aP | Yes | Yes |
| Sweden | 10,551,494 | 292.99 | 0.1788 | 4.253 | aP | Yes | Yes |
| Singapore | 5,789,090 | 71.72 | 0.1119 | 0.8004 | aP | Yes | Yes |
| United States | 343,477,335 | 147.97 | 0.08455 | 1.108 | aP | Yes | Yes |
<!-- END ETABLE 1 -->

<!-- BEGIN ETABLE 2 -->
**eTable 2. Vaccine-mechanism parameterization used in scenario analyses.**

<!-- Generated from `manuscript_notes/scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Scenario | VE_sus | VE_sym | VE_inf | VE_dur | Description |
| --- | --- | --- | --- | --- | --- |
| no_vaccine | 0 | 0 | 0 | 0 | No vaccine protection. |
| symptom_protective | 0.15 | 0.85 | 0.08 | 0 | aP-like disease protection with limited infection/transmission blocking. |
| infection_blocking | 0.7 | 0.85 | 0.2 | 0.1 | Stronger reduction in susceptibility to infection. |
| transmission_blocking | 0.3 | 0.85 | 0.7 | 0.3 | Strong reduction in onward infectiousness and duration. |
| next_generation | 0.8 | 0.9 | 0.75 | 0.4 | Strong infection, symptom, and transmission protection. |
<!-- END ETABLE 2 -->

<!-- BEGIN ETABLE 3 -->
**eTable 3. Macrolide-resistance initialization, importation, and fitness assumptions.**

<!-- Generated from `manuscript_notes/resistance_scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Scenario | Target resistant fraction | Importation resistant fraction | Anchor rate per year | Country timeline | Fitness_R | Description |
| --- | --- | --- | --- | --- | --- | --- |
| country_timeline | 0.3 | 0.3 | 2 | Yes | 0.7 | Country-specific macrolide resistance prevalence from data/raw/country_resistance_timeline.csv, mixing measured surveillance/isolate rows with conservative low anchors where public numeric estimates were not found. |
| low | 0.05 | 0.05 | 2 | No | 0.7 | Low macrolide resistance prevalence. |
| moderate | 0.3 | 0.3 | 2 | No | 0.7 | Moderate macrolide resistance prevalence. |
| high | 0.7 | 0.7 | 2 | No | 0.7 | High macrolide resistance prevalence. |
| very_high | 0.95 | 0.95 | 2 | No | 0.7 | Very high macrolide resistance prevalence. |
<!-- END ETABLE 3 -->

<!-- BEGIN ETABLE 4 -->
**eTable 4. Intervention strategy definitions and modified control levers.**

<!-- Generated from `manuscript_notes/intervention_scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Strategy | Description |
| --- | --- |
| current | Current vaccination and standard macrolide treatment. |
| higher_child_coverage | Increased routine childhood vaccine coverage. |
| adolescent_booster | Additional booster for school-age children and adolescents. |
| maternal_immunization | Direct infant protection through maternal immunization. |
| resistance_guided_treatment | Resistance testing plus alternative treatment for resistant infections. |
| next_generation_vaccine | Improved transmission-blocking vaccine. |
| combined_strategy | Maternal immunization, adolescent booster, and resistance-guided treatment. |
<!-- END ETABLE 4 -->

<!-- BEGIN ETABLE 5 -->
**eTable 5. Baseline parameter values, admissible ranges, and evidence provenance.**

<!-- Generated from `manuscript_notes/parameter_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Parameter | Description | Baseline value | Range | Unit | Source or assumption | Sensitivity |
| --- | --- | --- | --- | --- | --- | --- |
| simulation.end_time | Simulation analysis horizon | 10,950.0 | see config/model_settings.yaml sensitivity_parameters | days | pertussis_cycle_model | No |
| simulation.burn_in_years | Pre-analysis burn-in horizon | 60.00 | see config/model_settings.yaml sensitivity_parameters | years | pertussis_cycle_model | No |
| transmission.beta_S | Transmission rate for macrolide-sensitive pertussis | 0.03 | see config/model_settings.yaml sensitivity_parameters | per contact day | pertussis_incidence | No |
| transmission.relative_infectiousness_asymptomatic | Relative infectiousness of asymptomatic infection | 0.35 | see config/model_settings.yaml sensitivity_parameters | ratio | who_pertussis_position | Yes |
| transmission.multi_year_period_years | Target/diagnostic inter-epidemic period | 4.000 | see config/model_settings.yaml sensitivity_parameters | years | pertussis_cycle_model | No |
| transmission.multi_year_amplitude | Weak multi-year phase-locking amplitude | 0 | see config/model_settings.yaml sensitivity_parameters | ratio | pertussis_cycle_model | Yes |
| natural_history.latent_duration | Latent period duration | 8.000 | see config/model_settings.yaml sensitivity_parameters | days | cdc_clinical | No |
| natural_history.infectious_duration_symptomatic | Symptomatic infectious duration | 21.00 | see config/model_settings.yaml sensitivity_parameters | days | cdc_clinical | No |
| natural_history.infectious_duration_asymptomatic | Asymptomatic infectious duration | 14.00 | see config/model_settings.yaml sensitivity_parameters | days | cdc_clinical | No |
| natural_history.recovered_immunity_duration | Duration of post-infection protection | 3,285.0 | see config/model_settings.yaml sensitivity_parameters (reciprocal of rates.waning_natural) | days | cdc_clinical | Yes |
| natural_history.vaccine_protection_duration | Duration of vaccine-derived protection proxy | 1,825.0 | see config/model_settings.yaml sensitivity_parameters (reciprocal of rates.waning_vaccine) | days | ap_waning_meta_analysis | Yes |
| treatment.treatment_rate_symptomatic | Daily transition from symptomatic infection to treatment | 0.05 | see config/model_settings.yaml sensitivity_parameters | per day | cdc_treatment_pep | Yes |
| PEP.coverage_household_contacts | Dynamic PEP coverage ceiling among close contacts | 0.3 | see config/model_settings.yaml sensitivity_parameters | proportion | cdc_treatment_pep | Yes |
<!-- END ETABLE 5 -->

<!-- BEGIN ETABLE 6 -->
**eTable 6. Reporting-rate sensitivity scenarios used to probe surveillance uncertainty.**

<!-- Generated from `manuscript_notes/reporting_scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Scenario | Multiplier | Age multipliers | Time variation | Description |
| --- | --- | --- | --- | --- |
| medium | 1.000 | No | No | Reporting-rate sensitivity assumption. |
| high | 1.500 | No | No | Reporting-rate sensitivity assumption. |
| low | 0.5 | No | No | Reporting-rate sensitivity assumption. |
| age_biased |  | Yes | No | Reporting-rate sensitivity assumption. |
| time_varying | 1.000 | No | Yes | Reporting-rate sensitivity assumption. |
<!-- END ETABLE 6 -->

<!-- BEGIN ETABLE 7 -->
**eTable 7. Country-specific macrolide-resistance evidence used for resistance anchoring.**

<!-- Generated from `data/raw/country_resistance_timeline.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | ISO3 | Year | Sample size | Resistant fraction | Lower | Upper | Evidence type | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | AUS | 2024 | 188 | 0.043 | 0.019 | 0.082 | measured_national_genomic_surveillance_fraction | https://doi.org/10.1016/j.lanmic.2025.101286 |
| China | CHN | 2016 |  | 0.364 | 0.28 | 0.45 | measured_regional_isolate_fraction | https://wwwnc.cdc.gov/eid/article/30/1/22-1588_article |
| China | CHN | 2022 |  | 0.972 | 0.94 | 0.99 | measured_regional_isolate_fraction | https://wwwnc.cdc.gov/eid/article/30/1/22-1588_article |
| China | CHN | 2024 | 394 | 0.997 | 0.986 | 1.000 | measured_multicenter_isolate_fraction | https://www.sciencedirect.com/science/article/pii/S2666606525001658 |
| Japan | JPN | 2024 | 8 | 0.875 | 0.473 | 0.997 | measured_regional_case_series_fraction | https://www.sciencedirect.com/science/article/pii/S1341321X26000140 |
| Japan | JPN | 2025 | 52 | 0.827 | 0.697 | 0.918 | measured_multicenter_isolate_fraction | https://www.mdpi.com/2227-9059/14/1/167 |
| New Zealand | NZL | 1995 | 88 | 0 | 0 | 0.041 | measured_historical_national_isolate_fraction | https://pubmed.ncbi.nlm.nih.gov/9579709/ |
| New Zealand | NZL | 2025 |  | 0.01 | 0 | 0.05 | low_detected_model_anchor | https://www.tewhatuora.govt.nz/for-health-professionals/clinical-guidance/communicable-disease-control-manual/pertussis |
| Singapore | SGP | 2025 |  | 0.01 | 0 | 0.05 | low_imported_model_anchor | https://www.cda.gov.sg/professionals/diseases/pertussis |
| Sweden | SWE | 2025 |  | 0.01 | 0 | 0.05 | low_imported_model_anchor | https://www.folkhalsomyndigheten.se/contentassets/975cc036216b48a39b7bf34319d4ecee/pertussis-surveillance-sweden-23rd-annual-report.pdf |
| United Kingdom | GBR | 2009 | 583 | 0 | 0 | 0.006 | measured_historical_national_isolate_fraction | https://researchportal.ukhsa.gov.uk/en/publications/antimicrobial-susceptibility-testing-of-historical-and-recent-cli/ |
| United Kingdom | GBR | 2024 | 661 | 0.003 | 0 | 0.011 | measured_national_surveillance_fraction | https://www.postersessiononline.eu/173580348_eu/congresos/UKHSA2025/aula/-P_58_UKHSA2025.pdf |
| United States | USA | 1997 | 47 | 0.021 | 0.001 | 0.113 | measured_regional_isolate_fraction | https://pubmed.ncbi.nlm.nih.gov/9350776/ |
| United States | USA | 2015 | 1,208 | 0 | 0 | 0.003 | measured_multistate_surveillance_fraction | https://www.walshmedicalmedia.com/conference-abstracts-files/2155-9597.C1.016-015.pdf |
<!-- END ETABLE 7 -->

<!-- BEGIN ETABLE 8 -->
**eTable 8. Calibration acceptance, absolute-fit diagnostics, and fitted transmission parameters.**

<!-- Generated from `outputs/tables/calibration_all_countries.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Accepted | Optimizer success | Fit status | Observed reported incidence per 100k | Model reported incidence per 100k | Model/observed ratio | Data fit score | Fit score | Calibrated beta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | Yes | Yes | calibrated_to_reported_cases | 19.85 | 19.79 | 0.9972 | 216.30 | 216.31 | 0.015 |
| China | Yes | Yes | calibrated_to_reported_cases | 1.706 | 1.706 | 1 | 111.04 | 111.04 | 0.01192 |
| Japan | Yes | Yes | calibrated_to_reported_cases | 5.001 | 5.001 | 1.000 | 221.81 | 221.81 | 0.01434 |
| New Zealand | Yes | Yes | calibrated_to_reported_cases | 21.05 | 21.05 | 1 | 319.38 | 319.38 | 0.01346 |
| Singapore | Yes | Yes | calibrated_to_reported_cases | 0.7802 | 0.766 | 0.9818 | 79.04 | 79.04 | 0.01165 |
| Sweden | Yes | Yes | calibrated_to_reported_cases | 3.083 | 3.083 | 1.000 | 241.94 | 241.94 | 0.01222 |
| United Kingdom | Yes | Yes | calibrated_to_reported_cases | 2.508 | 2.540 | 1.013 | 304.94 | 305.09 | 0.01303 |
| United States | Yes | Yes | calibrated_to_reported_cases | 3.129 | 3.152 | 1.007 | 136.04 | 136.05 | 0.01188 |
<!-- END ETABLE 8 -->

<!-- BEGIN ETABLE 9 -->
**eTable 9. Intervention outcome summaries by country and strategy.**

<!-- Generated from `outputs/tables/table_4_intervention_comparison.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Strategy | Total infections | Reported cases | Infant cases | Resistant infections | Infant-case reduction | Infection reduction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | adolescent_booster | 7,214,076 | 112,213 | 33,254.2 | 16,901.2 | 0.3119 | 0.278 |
| Australia | combined_strategy | 14,361.5 | 217.47 | 65.25 | 138.50 | 0.9986 | 0.9986 |
| Australia | current | 9,992,298 | 158,122 | 48,327.3 | 28,390.5 | 0 | 0 |
| Australia | higher_child_coverage | 9,980,713 | 158,456 | 49,549.5 | 28,402.9 | -0.02529 | 0.001159 |
| Australia | maternal_immunization | 6,461,657 | 97,880.8 | 30,874.1 | 13,989.2 | 0.3611 | 0.3533 |
| Australia | next_generation_vaccine | 8,967.5 | 134.85 | 42.45 | 235.48 | 0.9991 | 0.9991 |
| Australia | resistance_guided_treatment | 8,128,345 | 127,832 | 38,300.7 | 3,016.2 | 0.2075 | 0.1865 |
| China | adolescent_booster | 6,076,269 | 96,087.0 | 20,869.8 | 2,736,137 | 0.9656 | 0.9648 |
| China | combined_strategy | 150,248 | 2,517.4 | 641.73 | 148,753 | 0.9989 | 0.9991 |
| China | current | 172,477,209 | 2,859,349 | 607,202 | 12,064,533 | 0 | 0 |
| China | higher_child_coverage | 173,156,035 | 2,873,129 | 618,299 | 12,132,633 | -0.01828 | -0.003936 |
| China | maternal_immunization | 52,359,510 | 841,397 | 182,577 | 4,936,966 | 0.6993 | 0.6964 |
| China | next_generation_vaccine | 357,988 | 5,804.0 | 1,347.1 | 356,257 | 0.9978 | 0.9979 |
| China | resistance_guided_treatment | 67,222,191 | 1,114,058 | 231,075 | 924,985 | 0.6194 | 0.6103 |
| Japan | adolescent_booster | 1,538,147 | 21,630.3 | 4,184.1 | 152,548 | 0.8777 | 0.8735 |
| Japan | combined_strategy | 18,961.9 | 286.16 | 71.40 | 10,597.7 | 0.9979 | 0.9984 |
| Japan | current | 12,156,370 | 178,278 | 34,210.8 | 532,117 | 0 | 0 |
| Japan | higher_child_coverage | 12,251,373 | 180,142 | 34,857.5 | 537,886 | -0.0189 | -0.007815 |
| Japan | maternal_immunization | 4,045,443 | 57,666.4 | 11,083.8 | 240,497 | 0.676 | 0.6672 |
| Japan | next_generation_vaccine | 37,575.6 | 549.44 | 119.75 | 27,478.2 | 0.9965 | 0.9969 |
| Japan | resistance_guided_treatment | 2,366,206 | 34,641.9 | 6,497.7 | 40,857.4 | 0.8101 | 0.8054 |
| New Zealand | adolescent_booster | 1,273,430 | 22,304.2 | 6,797.1 | 682.38 | 0.3529 | 0.3213 |
| New Zealand | combined_strategy | 2,382.1 | 41.04 | 12.64 | 6.182 | 0.9988 | 0.9987 |
| New Zealand | current | 1,876,286 | 33,524.9 | 10,504.3 | 1,260.9 | 0 | 0 |
| New Zealand | higher_child_coverage | 1,887,649 | 34,007.7 | 10,759.9 | 1,294.3 | -0.02434 | -0.006056 |
| New Zealand | maternal_immunization | 1,201,990 | 20,940.1 | 6,648.7 | 631.00 | 0.367 | 0.3594 |
| New Zealand | next_generation_vaccine | 1,675.3 | 28.83 | 9.255 | 10.65 | 0.9991 | 0.9991 |
| New Zealand | resistance_guided_treatment | 1,535,064 | 27,359.1 | 8,387.2 | 138.60 | 0.2015 | 0.1819 |
| Singapore | adolescent_booster | 11,058.5 | 155.60 | 39.31 | 35.41 | 0.8244 | 0.8262 |
| Singapore | combined_strategy | 1,352.5 | 19.40 | 5.355 | 4.933 | 0.9761 | 0.9787 |
| Singapore | current | 63,642.1 | 894.28 | 223.83 | 63.56 | 0 | 0 |
| Singapore | higher_child_coverage | 67,037.2 | 944.57 | 240.68 | 64.84 | -0.0753 | -0.05335 |
| Singapore | maternal_immunization | 9,127.2 | 126.41 | 33.93 | 33.03 | 0.8484 | 0.8566 |
| Singapore | next_generation_vaccine | 1,036.3 | 14.66 | 4.268 | 7.485 | 0.9809 | 0.9837 |
| Singapore | resistance_guided_treatment | 11,479.9 | 162.68 | 41.05 | 11.72 | 0.8166 | 0.8196 |
| Sweden | adolescent_booster | 23,576.8 | 382.45 | 102.08 | 72.99 | 0.9421 | 0.9421 |
| Sweden | combined_strategy | 2,153.6 | 35.61 | 10.80 | 8.675 | 0.9939 | 0.9947 |
| Sweden | current | 407,521 | 6,658.9 | 1,762.2 | 233.22 | 0 | 0 |
| Sweden | higher_child_coverage | 430,318 | 7,063.1 | 1,919.7 | 241.92 | -0.0894 | -0.05594 |
| Sweden | maternal_immunization | 19,104.2 | 304.67 | 87.53 | 67.46 | 0.9503 | 0.9531 |
| Sweden | next_generation_vaccine | 1,574.4 | 25.77 | 8.261 | 11.85 | 0.9953 | 0.9961 |
| Sweden | resistance_guided_treatment | 44,461.2 | 729.76 | 192.17 | 26.61 | 0.891 | 0.8909 |
| United Kingdom | adolescent_booster | 97,206.1 | 1,626.7 | 496.71 | 119.59 | 0.9457 | 0.9473 |
| United Kingdom | combined_strategy | 13,039.6 | 222.43 | 75.06 | 16.38 | 0.9918 | 0.9929 |
| United Kingdom | current | 1,845,700 | 32,447.7 | 9,149.1 | 472.03 | 0 | 0 |
| United Kingdom | higher_child_coverage | 1,971,078 | 34,869.9 | 9,946.4 | 492.37 | -0.08714 | -0.06793 |
| United Kingdom | maternal_immunization | 188,729 | 3,273.4 | 960.84 | 178.43 | 0.895 | 0.8977 |
| United Kingdom | next_generation_vaccine | 15,044.6 | 258.96 | 81.09 | 33.08 | 0.9911 | 0.9918 |
| United Kingdom | resistance_guided_treatment | 270,015 | 4,766.7 | 1,342.4 | 54.58 | 0.8533 | 0.8537 |
| United States | adolescent_booster | 690,418 | 10,987.3 | 3,244.0 | 0 | 0.9463 | 0.9464 |
| United States | combined_strategy | 65,805.1 | 1,065.6 | 349.62 | 0 | 0.9942 | 0.9949 |
| United States | current | 12,881,377 | 206,449 | 60,374.0 | 0 | 0 | 0 |
| United States | higher_child_coverage | 13,650,248 | 219,889 | 65,706.5 | 0 | -0.08832 | -0.05969 |
| United States | maternal_immunization | 568,993 | 8,932.8 | 2,823.4 | 0 | 0.9532 | 0.9558 |
| United States | next_generation_vaccine | 48,657.0 | 783.10 | 272.76 | 0 | 0.9955 | 0.9962 |
| United States | resistance_guided_treatment | 1,259,829 | 20,261.7 | 5,890.9 | 0 | 0.9024 | 0.9022 |
<!-- END ETABLE 9 -->

<!-- BEGIN ETABLE 10 -->
**eTable 10. Model-derived outcomes and summary definitions.**

<!-- Generated from `static outcome definitions` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Quantity | Definition | Denominator or reference population | Primary use |
| --- | --- | --- | --- |
| Total infections | Symptomatic plus asymptomatic incident infections integrated over the analysis interval. | Mean total population over the interval. | Overall transmission burden. |
| Reported cases | Symptomatic incident infections multiplied by age-specific reporting probabilities and integrated over the analysis interval. | Mean total population over the interval. | Calibration target and surveillance-comparable burden. |
| Infant cases | Symptomatic incident infections in the 0-2 month and 3-11 month age groups. | Mean population in the two infant age groups. | Primary severe-risk outcome. |
| Resistant infections | Total incident infections attributed to the macrolide-resistant strain. | Mean total population over the interval. | Resistance burden and treatment relevance. |
| Resistant fraction | Resistant infections divided by total infections at a time point or over a summary interval. | Total infections. | Strain-composition diagnostic. |
| PEP-averted cases | Difference between pre-PEP and post-PEP symptomatic infection flows under the same state trajectory. | Not a population-normalized compartment count unless explicitly annualized. | Diagnostic estimate of prophylaxis effect. |
| Relative reduction | 1 - Z/Z0, where Z is the scenario outcome and Z0 is the comparator outcome. | Scenario-specific comparator. | Cross-scenario intervention comparison. |
<!-- END ETABLE 10 -->

<!-- BEGIN ETABLE 11 -->
**eTable 11. Core model settings and implementation choices.**

<!-- Generated from `configuration summary derived from the analysis pipeline` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Aspect | Setting | Value |
| --- | --- | --- |
| Model class | Deterministic age-structured compartmental ODE | Two strains, country-specific demographics, vaccination histories, treatment, and PEP are tracked explicitly. |
| Age structure | Five model age groups | 0-2 months, 3-11 months, 1-6 years, 7-17 years, and 18 years or older. |
| Strain structure | Two strain classes | Macrolide-sensitive and macrolide-resistant strains are simulated separately. |
| Vaccine-history structure | Explicit origin states | Unvaccinated, maternally protected, dose-1 recent/waned, dose-2 recent/waned, and dose-3-plus recent/waned states retain distinct effects. |
| Burn-in and horizon | Long burn-in plus analysis window | Sixty-year burn-in followed by a 30-year analysis period beginning on 1 January 2026. |
| Time scale | Daily rates with weekly saved output | All state equations are evaluated in days, and output is stored every 7 days for downstream summaries. |
| Numerical solver | Adaptive Runge-Kutta integration | RK45 with relative tolerance 1e-5 and absolute tolerance 1e-7. |
| Seasonality | Annual cosine forcing | A 4-year diagnostic term is available when surveillance peaks support multi-year recurrence. |
| Demography | Fixed age turnover | Births and aging maintain the country age profile used to initialize each profile. |
| Observation model | Age-specific reporting probabilities | Reporting completeness affects observed cases, while PEP activation uses a separate detection proxy. |
| Calibration target | Annual reported cases | The fit uses a negative binomial likelihood and requires the retained solution to match the observed mean within tolerance. |
| Resistance anchoring | Evidence-based initialization | Country-specific anchors use the latest admissible evidence through 2025, with low-level importation preventing deterministic extinction. |
| Sensitivity screening | Latin-hypercube screening | Twenty-four parameter sets were used for Pearson-correlation robustness screening, not posterior inference. |
<!-- END ETABLE 11 -->
