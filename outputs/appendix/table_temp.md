## eTables

<!-- BEGIN ETABLE 1 -->
**eTable 1. Country-specific population, surveillance, vaccination, and seasonal-forcing inputs.**

<!-- Generated from `manuscript_notes/country_profile_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Population | Seasonal phase | Seasonal amplitude | Mean reported incidence per 100k | Vaccine product | Adolescent booster | Maternal program |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | 26,451,124 | 293.48 | 0.1638 | 58.65 | aP | Yes | Yes |
| China | 1,422,584,932 | 155.58 | 0.3042 | 4.502 | aP | No | No |
| United Kingdom | 68,682,962 | 133.56 | 0.1959 | 7.317 | aP | No | Yes |
| Japan | 124,370,946 | 186.12 | 0.3247 | 8.986 | aP | No | No |
| New Zealand | 5,172,836 | 355.93 | 0.1744 | 24.26 | aP | Yes | Yes |
| Sweden | 10,551,494 | 277.05 | 0.206 | 6.390 | aP | Yes | Yes |
| United States | 343,477,335 | 274.81 | 0.09354 | 1.462 | aP | Yes | Yes |
| Brazil | 211,140,729 | 325.83 | 0.18 | 0.8636 | wP | No | Yes |
| Thailand | 71,702,435 | 28.67 | 0.2359 | 0.1976 | wP | No | Yes |
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
| natural_history.infectious_duration_symptomatic | Symptomatic infectious duration | 21.00 | see config/model_settings.yaml sensitivity_parameters | days | cdc_clinical | Yes |
| natural_history.infectious_duration_asymptomatic | Asymptomatic infectious duration | 14.00 | see config/model_settings.yaml sensitivity_parameters | days | cdc_clinical | Yes |
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
| Brazil | BRA | 2025 |  | 0.01 | 0 | 0.05 | low_detected_model_anchor | https://www.paho.org/en/news/26-8-2025-paho-calls-strengthened-vaccination-and-surveillance-amid-spread-antibiotic |
| China | CHN | 2016 |  | 0.364 | 0.28 | 0.45 | measured_regional_isolate_fraction | https://wwwnc.cdc.gov/eid/article/30/1/22-1588_article |
| China | CHN | 2022 |  | 0.972 | 0.94 | 0.99 | measured_regional_isolate_fraction | https://wwwnc.cdc.gov/eid/article/30/1/22-1588_article |
| China | CHN | 2024 | 394 | 0.997 | 0.986 | 1.000 | measured_multicenter_isolate_fraction | https://www.sciencedirect.com/science/article/pii/S2666606525001658 |
| Japan | JPN | 2024 | 8 | 0.875 | 0.473 | 0.997 | measured_regional_case_series_fraction | https://www.sciencedirect.com/science/article/pii/S1341321X26000140 |
| Japan | JPN | 2025 | 52 | 0.827 | 0.697 | 0.918 | measured_multicenter_isolate_fraction | https://www.mdpi.com/2227-9059/14/1/167 |
| New Zealand | NZL | 1995 | 88 | 0 | 0 | 0.041 | measured_historical_national_isolate_fraction | https://pubmed.ncbi.nlm.nih.gov/9579709/ |
| New Zealand | NZL | 2025 |  | 0.01 | 0 | 0.05 | low_detected_model_anchor | https://www.tewhatuora.govt.nz/for-health-professionals/clinical-guidance/communicable-disease-control-manual/pertussis |
| Sweden | SWE | 2025 |  | 0.01 | 0 | 0.05 | low_imported_model_anchor | https://www.folkhalsomyndigheten.se/contentassets/975cc036216b48a39b7bf34319d4ecee/pertussis-surveillance-sweden-23rd-annual-report.pdf |
| Thailand | THA | 2025 |  | 0.01 | 0 | 0.05 | low_imported_model_anchor | https://www.cdc.gov/pertussis/hcp/antibiotic-resistance/index.html |
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
| Australia | Yes | Yes | calibrated_to_reported_cases | 55.38 | 55.38 | 1 | 5,305.8 | 5,305.8 | 0.02 |
| Brazil | Yes | Yes | calibrated_to_reported_cases | 1.002 | 1.002 | 1.000 | 3,482.4 | 3,482.4 | 0.01116 |
| China | Yes | Yes | calibrated_to_reported_cases | 7.559 | 8.143 | 1.077 | 27,104.3 | 27,380.7 | 0.01861 |
| Japan | Yes | Yes | calibrated_to_reported_cases | 10.50 | 10.98 | 1.045 | 25,359.4 | 25,456.2 | 0.015 |
| New Zealand | Yes | Yes | calibrated_to_reported_cases | 14.16 | 14.16 | 1 | 2,829.3 | 2,829.3 | 0.01253 |
| Sweden | Yes | Yes | calibrated_to_reported_cases | 5.938 | 5.938 | 1 | 2,384.1 | 2,384.1 | 0.01242 |
| Thailand | Yes | Yes | calibrated_to_reported_cases | 0.4603 | 0.4603 | 1.000 | 1,849.4 | 1,849.4 | 0.01144 |
| United Kingdom | Yes | Yes | calibrated_to_reported_cases | 9.617 | 9.617 | 1.000 | 15,374.2 | 15,374.2 | 0.01371 |
| United States | Yes | Yes | calibrated_to_reported_cases | 1.220 | 1.220 | 1 | 7,043.6 | 7,043.6 | 0.01174 |
<!-- END ETABLE 8 -->

<!-- BEGIN ETABLE 9 -->
**eTable 9. Intervention outcome summaries by country and strategy.**

<!-- Generated from `outputs/tables/table_4_intervention_comparison.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Strategy | Total infections | Reported cases | Infant cases | Resistant infections | Infant-case reduction | Infection reduction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | adolescent_booster | 25,681,857 | 405,630 | 152,593 | 2,672,561 | 0.152 | 0.09811 |
| Australia | combined_strategy | 12,534,308 | 181,879 | 60,343.4 | 4,335.6 | 0.6647 | 0.5598 |
| Australia | current | 28,475,713 | 459,175 | 179,954 | 7,896,571 | 0 | 0 |
| Australia | higher_child_coverage | 28,474,179 | 461,053 | 184,799 | 8,166,891 | -0.02693 | 5.389e-05 |
| Australia | maternal_immunization | 24,917,836 | 383,379 | 153,889 | 1,011,228 | 0.1448 | 0.1249 |
| Australia | next_generation_vaccine | 8,828,425 | 123,124 | 40,910.1 | 20,071.5 | 0.7727 | 0.69 |
| Australia | resistance_guided_treatment | 26,920,085 | 430,550 | 164,832 | 9,810.1 | 0.08403 | 0.05463 |
| Brazil | adolescent_booster | 222,160 | 3,560.1 | 1,177.1 | 1,005.4 | 0.8857 | 0.8888 |
| Brazil | combined_strategy | 38,066.6 | 617.79 | 218.83 | 158.90 | 0.9787 | 0.9809 |
| Brazil | current | 1,997,931 | 33,131.7 | 10,294.0 | 2,469.8 | 0 | 0 |
| Brazil | higher_child_coverage | 2,198,946 | 36,736.6 | 11,498.7 | 2,569.1 | -0.117 | -0.1006 |
| Brazil | maternal_immunization | 319,959 | 5,248.5 | 1,713.1 | 1,261.2 | 0.8336 | 0.8399 |
| Brazil | next_generation_vaccine | 39,497.7 | 643.72 | 222.49 | 290.84 | 0.9784 | 0.9802 |
| Brazil | resistance_guided_treatment | 406,097 | 6,777.6 | 2,115.1 | 443.63 | 0.7945 | 0.7967 |
| China | adolescent_booster | 1,534,483,312 | 25,060,037 | 7,562,869 | 1,533,474,858 | 0.1098 | 0.06735 |
| China | combined_strategy | 946,692,443 | 14,401,034 | 3,829,080 | 4,632,198 | 0.5493 | 0.4246 |
| China | current | 1,645,289,757 | 27,186,609 | 8,496,115 | 1,644,409,033 | 0 | 0 |
| China | higher_child_coverage | 1,645,669,595 | 27,260,282 | 8,627,155 | 1,644,799,324 | -0.01542 | -0.0002309 |
| China | maternal_immunization | 1,497,539,742 | 23,823,511 | 7,571,497 | 1,496,112,625 | 0.1088 | 0.0898 |
| China | next_generation_vaccine | 908,483,077 | 13,813,501 | 3,653,384 | 598,012,241 | 0.57 | 0.4478 |
| China | resistance_guided_treatment | 1,507,344,904 | 24,661,258 | 7,403,973 | 8,659,269 | 0.1285 | 0.08384 |
| Japan | adolescent_booster | 11,665,572 | 156,519 | 32,280.4 | 458,288 | 0.5018 | 0.4793 |
| Japan | combined_strategy | 30,320.9 | 420.68 | 101.15 | 13,945.2 | 0.9984 | 0.9986 |
| Japan | current | 22,402,474 | 313,374 | 64,798.3 | 946,782 | 0 | 0 |
| Japan | higher_child_coverage | 22,502,136 | 315,589 | 65,803.3 | 956,077 | -0.01551 | -0.004449 |
| Japan | maternal_immunization | 13,992,925 | 190,166 | 39,274.5 | 568,448 | 0.3939 | 0.3754 |
| Japan | next_generation_vaccine | 64,310.2 | 873.02 | 186.22 | 43,063.1 | 0.9971 | 0.9971 |
| Japan | resistance_guided_treatment | 12,669,828 | 176,732 | 35,614.6 | 71,453.9 | 0.4504 | 0.4344 |
| New Zealand | adolescent_booster | 379,276 | 6,249.0 | 1,922.4 | 176.89 | 0.6413 | 0.6251 |
| New Zealand | combined_strategy | 1,424.2 | 23.79 | 7.877 | 4.969 | 0.9985 | 0.9986 |
| New Zealand | current | 1,011,756 | 17,114.8 | 5,359.5 | 498.25 | 0 | 0 |
| New Zealand | higher_child_coverage | 1,024,837 | 17,483.1 | 5,527.9 | 510.72 | -0.03142 | -0.01293 |
| New Zealand | maternal_immunization | 367,761 | 6,093.0 | 1,933.9 | 176.34 | 0.6392 | 0.6365 |
| New Zealand | next_generation_vaccine | 1,085.7 | 18.13 | 6.266 | 7.719 | 0.9988 | 0.9989 |
| New Zealand | resistance_guided_treatment | 651,090 | 10,988.5 | 3,366.3 | 63.31 | 0.3719 | 0.3565 |
| Sweden | adolescent_booster | 41,521.9 | 660.43 | 177.82 | 90.76 | 0.9436 | 0.9425 |
| Sweden | combined_strategy | 2,378.3 | 38.50 | 11.76 | 9.132 | 0.9963 | 0.9967 |
| Sweden | current | 722,066 | 11,623.5 | 3,150.8 | 353.66 | 0 | 0 |
| Sweden | higher_child_coverage | 746,934 | 12,078.4 | 3,363.0 | 365.22 | -0.06736 | -0.03444 |
| Sweden | maternal_immunization | 29,768.5 | 465.37 | 134.78 | 81.52 | 0.9572 | 0.9588 |
| Sweden | next_generation_vaccine | 1,716.7 | 27.50 | 8.872 | 12.66 | 0.9972 | 0.9976 |
| Sweden | resistance_guided_treatment | 116,866 | 1,882.7 | 501.68 | 33.48 | 0.8408 | 0.8382 |
| Thailand | adolescent_booster | 86,806.5 | 1,338.5 | 346.38 | 377.82 | 0.7655 | 0.7711 |
| Thailand | combined_strategy | 16,498.3 | 254.06 | 69.48 | 61.11 | 0.953 | 0.9565 |
| Thailand | current | 379,204 | 6,052.7 | 1,477.1 | 729.93 | 0 | 0 |
| Thailand | higher_child_coverage | 376,486 | 6,005.9 | 1,456.4 | 727.79 | 0.01398 | 0.007168 |
| Thailand | maternal_immunization | 113,593 | 1,779.1 | 450.62 | 451.67 | 0.6949 | 0.7004 |
| Thailand | next_generation_vaccine | 18,105.4 | 283.14 | 77.15 | 125.16 | 0.9478 | 0.9523 |
| Thailand | resistance_guided_treatment | 123,232 | 1,981.3 | 486.95 | 154.23 | 0.6703 | 0.675 |
| United Kingdom | adolescent_booster | 278,136 | 4,322.8 | 1,389.0 | 179.38 | 0.9683 | 0.9676 |
| United Kingdom | combined_strategy | 16,218.6 | 256.52 | 90.94 | 18.56 | 0.9979 | 0.9981 |
| United Kingdom | current | 8,589,064 | 141,451 | 43,863.2 | 1,160.1 | 0 | 0 |
| United Kingdom | higher_child_coverage | 8,785,194 | 145,941 | 45,725.3 | 1,199.0 | -0.04245 | -0.02283 |
| United Kingdom | maternal_immunization | 2,053,026 | 33,123.0 | 10,340.8 | 401.67 | 0.7642 | 0.761 |
| United Kingdom | next_generation_vaccine | 19,081.9 | 304.61 | 100.20 | 39.91 | 0.9977 | 0.9978 |
| United Kingdom | resistance_guided_treatment | 3,679,390 | 60,541.7 | 18,340.2 | 102.63 | 0.5819 | 0.5716 |
| United States | adolescent_booster | 501,000 | 8,085.7 | 2,331.5 | 0 | 0.9006 | 0.902 |
| United States | combined_strategy | 62,037.2 | 1,017.8 | 327.36 | 0 | 0.986 | 0.9879 |
| United States | current | 5,111,672 | 82,812.4 | 23,458.7 | 0 | 0 | 0 |
| United States | higher_child_coverage | 5,710,449 | 93,012.0 | 27,048.9 | 0 | -0.153 | -0.1171 |
| United States | maternal_immunization | 433,951 | 6,906.6 | 2,142.5 | 0 | 0.9087 | 0.9151 |
| United States | next_generation_vaccine | 45,860.0 | 746.87 | 253.02 | 0 | 0.9892 | 0.991 |
| United States | resistance_guided_treatment | 768,632 | 12,528.8 | 3,558.8 | 0 | 0.8483 | 0.8496 |
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
| Calibration target | Reported surveillance intervals | The fit uses a negative binomial likelihood and requires the retained solution to match the observed annualized mean within tolerance. |
| Resistance anchoring | Evidence-based initialization | Country-specific anchors use the latest admissible evidence through 2025, with low-level importation preventing deterministic extinction. |
| Sensitivity screening | Latin-hypercube screening | Forty-eight parameter sets were used for Pearson-correlation robustness screening, separate from posterior inference. |
| Bayesian uncertainty | Pragmatic posterior predictive analysis | A negative binomial reported-case likelihood and literature-informed priors propagate parameter and observation uncertainty into credible intervals. |
| Resistance fitness stress test | Continuous fitness_R grid | Macrolide-resistant strain fitness is varied from 0.70 to 1.25 and crossed with vaccine infectiousness-effect assumptions. |
<!-- END ETABLE 11 -->

<!-- BEGIN ETABLE 12 -->
**eTable 12. Bayesian uncertainty priors used for posterior predictive intervals.**

<!-- Generated from `manuscript_notes/bayesian_prior_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Parameter | Prior | Interpretation |
| --- | --- | --- |
| log_beta_S | Normal(log calibrated beta_S, 0.5) | Transmission-rate uncertainty |
| log_reporting_multiplier | Normal(log calibrated reporting multiplier, 0.7) | Surveillance/reporting uncertainty |
| VE_sus | Beta(mean=0.45, sd=0.12) | Empirical aP infection-protection anchor; VE_sus maps to susceptibility reduction. |
| VE_inf | Beta(mean=0.4, sd=0.15) | Empirical transmission/infectiousness-effect anchor; VE_inf maps to onward infectiousness reduction. |
| VE_dur | Beta(mean=0.1, sd=0.1) |  |
| relative_infectiousness_asymptomatic | Beta(mean=0.45, sd=0.15) |  |
| infectious_duration_symptomatic | Log-normal around baseline, log_sd=0.2 |  |
| infectious_duration_asymptomatic | Log-normal around baseline, log_sd=0.25 |  |
| fitness_R | Beta(mean=0.95, sd=0.18) |  |
| resistance_prevalence | {'floor_sd': 0.03} |  |
<!-- END ETABLE 12 -->

<!-- BEGIN ETABLE 13 -->
**eTable 13. Continuous macrolide-resistant fitness and vaccine infectiousness grid.**

<!-- Generated from `manuscript_notes/fitness_grid_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Fitness_R | VE_inf | Description |
| --- | --- | --- |
| 0.7 | 0.08 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.7 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.7 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.7 | 0.6 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.7 | 0.75 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.75 | 0.08 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.75 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.75 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.75 | 0.6 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.75 | 0.75 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.8 | 0.08 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.8 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.8 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.8 | 0.6 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.8 | 0.75 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.85 | 0.08 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.85 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.85 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.85 | 0.6 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.85 | 0.75 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.9 | 0.08 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.9 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.9 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.9 | 0.6 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.9 | 0.75 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.95 | 0.08 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.95 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.95 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.95 | 0.6 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 0.95 | 0.75 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.000 | 0.08 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.000 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.000 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.000 | 0.6 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.000 | 0.75 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.050 | 0.08 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.050 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.050 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.050 | 0.6 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.050 | 0.75 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.100 | 0.08 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.100 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.100 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.100 | 0.6 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.100 | 0.75 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.150 | 0.08 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.150 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.150 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.150 | 0.6 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.150 | 0.75 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.200 | 0.08 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.200 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.200 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.200 | 0.6 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.200 | 0.75 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.250 | 0.08 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.250 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.250 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.250 | 0.6 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
| 1.250 | 0.75 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. |
<!-- END ETABLE 13 -->
