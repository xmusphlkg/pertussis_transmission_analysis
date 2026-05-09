## Supplementary tables

**Table S1. Country-specific population, surveillance, vaccination, and seasonal-forcing inputs.**

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

**Table S2. Vaccine-mechanism parameterization used in scenario analyses.**

| Scenario | VE_sus | VE_sym | VE_inf | VE_dur | Description |
| --- | --- | --- | --- | --- | --- |
| no_vaccine | 0 | 0 | 0 | 0 | No vaccine protection. |
| symptom_protective | 0.15 | 0.85 | 0.08 | 0 | aP-like disease protection with limited infection/transmission blocking. |
| infection_blocking | 0.7 | 0.85 | 0.2 | 0.1 | Stronger reduction in susceptibility to infection. |
| transmission_blocking | 0.3 | 0.85 | 0.7 | 0.3 | Strong reduction in onward infectiousness and duration. |
| next_generation | 0.8 | 0.9 | 0.75 | 0.4 | Strong infection, symptom, and transmission protection. |

**Table S3. Macrolide-resistance initialization, importation, and fitness assumptions.**

| Scenario | Target resistant fraction | Importation resistant fraction | Nominal anchor rate per year | Country timeline | Fitness_R | Description |
| --- | --- | --- | --- | --- | --- | --- |
| country_timeline | 0.3 | 0.3 | 2 | Yes | 0.7 | Country-specific macrolide-resistance prevalence based on measured surveillance or isolate evidence, supplemented with conservative low-prevalence anchors where numeric estimates were unavailable. |
| low | 0.05 | 0.05 | 2 | No | 0.7 | Low macrolide resistance prevalence. |
| moderate | 0.3 | 0.3 | 2 | No | 0.7 | Moderate macrolide resistance prevalence. |
| high | 0.7 | 0.7 | 2 | No | 0.7 | High macrolide resistance prevalence. |
| very_high | 0.95 | 0.95 | 2 | No | 0.7 | Very high macrolide resistance prevalence. |

**Table S4. Intervention strategy definitions and modified control levers.**

| Strategy | Description |
| --- | --- |
| current | Current vaccination and standard macrolide treatment. |
| higher_child_coverage | Increased routine childhood vaccine coverage. |
| adolescent_booster | Additional booster for school-age children and adolescents. |
| maternal_immunization | Direct infant protection through maternal immunization. |
| resistance_guided_treatment | Resistance testing plus alternative treatment for resistant infections. |
| next_generation_vaccine | Improved transmission-blocking vaccine. |
| combined_strategy | Maternal immunization, adolescent booster, and resistance-guided treatment. |

**Table S5. Baseline parameter values, admissible ranges, and evidence provenance.**

| Parameter | Description | Baseline value | Range | Unit | Source or assumption | Sensitivity |
| --- | --- | --- | --- | --- | --- | --- |
| simulation.end_time | Simulation analysis horizon | 10,950.0 | Fixed main-analysis value | days | Pertussis recurrence literature | No |
| simulation.burn_in_years | Pre-analysis burn-in horizon | 60.00 | Fixed main-analysis value | years | Pertussis recurrence literature | No |
| transmission.beta_S | Transmission rate for macrolide-sensitive pertussis | 0.03 | Country-calibrated where accepted | per contact day | Surveillance calibration | No |
| transmission.relative_infectiousness_asymptomatic | Relative infectiousness of asymptomatic infection | 0.35 | 0.25-0.85 | ratio | WHO position paper and mechanistic assumption | Yes |
| transmission.multi_year_period_years | Target/diagnostic inter-epidemic period | 4.000 | Fixed unless supported by country recurrence diagnostics | years | Pertussis recurrence literature | No |
| transmission.multi_year_amplitude | Weak multi-year phase-locking amplitude | 0 | 0-0.18 | ratio | Recurrence diagnostic assumption | Yes |
| natural_history.latent_duration | Latent period duration | 8.000 | Fixed main-analysis value | days | Clinical pertussis guidance | No |
| natural_history.infectious_duration_symptomatic | Symptomatic infectious duration | 21.00 | Fixed main-analysis value | days | Clinical pertussis guidance | No |
| natural_history.infectious_duration_asymptomatic | Asymptomatic infectious duration | 14.00 | Fixed main-analysis value | days | Clinical pertussis guidance | No |
| natural_history.recovered_immunity_duration | Duration of post-infection protection | 3,285.0 | 2,000-10,000 | days | Natural-immunity literature and sensitivity range | Yes |
| natural_history.vaccine_protection_duration | Duration of vaccine-derived protection proxy | 1,825.0 | 909-5,000 | days | Acellular-vaccine waning evidence | Yes |
| treatment.treatment_rate_symptomatic | Daily transition from symptomatic infection to treatment | 0.05 | 0.020-0.090 | per day | Treatment and PEP guidance | Yes |
| PEP.coverage_household_contacts | Dynamic PEP coverage ceiling among close contacts | 0.3 | 0.05-0.60 | proportion | Close-contact PEP guidance and modeling assumption | Yes |

**Table S6. Reporting-rate sensitivity scenarios used to probe surveillance uncertainty.**

| Scenario | Multiplier | Age multipliers | Time variation | Description |
| --- | --- | --- | --- | --- |
| medium | 1.000 | No | No | Baseline age-specific reporting probabilities. |
| high | 1.500 | No | No | Uniform 50% increase in reporting probabilities, clipped at 1. |
| low | 0.5 | No | No | Uniform 50% reduction in reporting probabilities. |
| age_biased |  | Yes | No | Higher infant ascertainment and lower school-age/adult ascertainment. |
| time_varying | 1.000 | No | Yes | Linear transition from lower to higher ascertainment across the analysis interval. |

**Table S7. Country-specific macrolide-resistance evidence used for resistance anchoring.**

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

**Table S8. Calibration acceptance, absolute-fit diagnostics, and fitted transmission parameters.**

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

**Table S9. Intervention outcome summaries by country and strategy.**

| Country | Strategy | Total infections | Reported cases | Infant cases | Resistant infections | Infant-case reduction | Infection reduction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | adolescent_booster | 1,728,525 | 26,567.2 | 7,925.3 | 29,746.8 | 0.1833 | 0.1394 |
| Australia | combined_strategy | 3,018.6 | 45.57 | 13.61 | 30.69 | 0.9986 | 0.9985 |
| Australia | current | 2,008,520 | 31,414.4 | 9,703.8 | 32,947.0 | 0 | 0 |
| Australia | higher_child_coverage | 2,010,544 | 31,582.5 | 9,973.7 | 33,407.5 | -0.02781 | -0.001008 |
| Australia | maternal_immunization | 1,568,373 | 23,628.3 | 7,469.7 | 26,335.4 | 0.2302 | 0.2191 |
| Australia | next_generation_vaccine | 1,987.3 | 29.84 | 9.215 | 52.25 | 0.9991 | 0.999 |
| Australia | resistance_guided_treatment | 1,751,929 | 27,253.0 | 8,242.4 | 5,009.6 | 0.1506 | 0.1278 |
| China | adolescent_booster | 381,046 | 6,094.0 | 1,342.1 | 371,930 | 0.955 | 0.9565 |
| China | combined_strategy | 30,360.8 | 508.17 | 128.97 | 30,063.4 | 0.9957 | 0.9965 |
| China | current | 8,754,511 | 145,589 | 29,821.1 | 6,551,764 | 0 | 0 |
| China | higher_child_coverage | 8,741,218 | 145,505 | 30,201.4 | 6,531,065 | -0.01275 | 0.001518 |
| China | maternal_immunization | 654,385 | 10,636.8 | 2,309.2 | 624,355 | 0.9226 | 0.9253 |
| China | next_generation_vaccine | 74,143.6 | 1,202.5 | 276.51 | 73,787.8 | 0.9907 | 0.9915 |
| China | resistance_guided_treatment | 114,288 | 1,976.8 | 426.19 | 87,421.9 | 0.9857 | 0.9869 |
| Japan | adolescent_booster | 100,548 | 1,422.2 | 278.33 | 38,388.4 | 0.9603 | 0.9605 |
| Japan | combined_strategy | 3,836.4 | 57.84 | 14.32 | 2,169.3 | 0.998 | 0.9985 |
| Japan | current | 2,548,707 | 37,319.0 | 7,017.0 | 568,905 | 0 | 0 |
| Japan | higher_child_coverage | 2,556,734 | 37,534.4 | 7,115.9 | 564,532 | -0.01409 | -0.00315 |
| Japan | maternal_immunization | 241,573 | 3,454.2 | 661.60 | 71,938.0 | 0.9057 | 0.9052 |
| Japan | next_generation_vaccine | 7,870.2 | 115.02 | 24.68 | 5,778.7 | 0.9965 | 0.9969 |
| Japan | resistance_guided_treatment | 93,900.2 | 1,383.5 | 261.69 | 9,620.3 | 0.9627 | 0.9632 |
| New Zealand | adolescent_booster | 302,144 | 5,231.3 | 1,605.0 | 1,132.7 | 0.2225 | 0.1809 |
| New Zealand | combined_strategy | 510.02 | 8.822 | 2.691 | 1.365 | 0.9987 | 0.9986 |
| New Zealand | current | 368,877 | 6,533 | 2,064.4 | 1,341.6 | 0 | 0 |
| New Zealand | higher_child_coverage | 375,592 | 6,706.8 | 2,139.4 | 1,418.5 | -0.03633 | -0.0182 |
| New Zealand | maternal_immunization | 283,526 | 4,923.5 | 1,565.7 | 1,089.6 | 0.2416 | 0.2314 |
| New Zealand | next_generation_vaccine | 375.60 | 6.510 | 2.045 | 2.383 | 0.999 | 0.999 |
| New Zealand | resistance_guided_treatment | 321,276 | 5,680.3 | 1,754.3 | 211.40 | 0.1502 | 0.129 |
| Singapore | adolescent_booster | 3,576.4 | 50.19 | 12.68 | 12.26 | 0.8726 | 0.874 |
| Singapore | combined_strategy | 408.77 | 5.855 | 1.614 | 1.502 | 0.9838 | 0.9856 |
| Singapore | current | 28,385.5 | 399.11 | 99.58 | 40.19 | 0 | 0 |
| Singapore | higher_child_coverage | 28,914.9 | 407.60 | 103.58 | 40.44 | -0.0401 | -0.01865 |
| Singapore | maternal_immunization | 2,951.4 | 40.89 | 10.93 | 11.11 | 0.8902 | 0.896 |
| Singapore | next_generation_vaccine | 320.84 | 4.541 | 1.310 | 2.314 | 0.9868 | 0.9887 |
| Singapore | resistance_guided_treatment | 3,821.2 | 54.17 | 13.62 | 4.162 | 0.8633 | 0.8654 |
| Sweden | adolescent_booster | 5,256.3 | 84.93 | 22.63 | 18.92 | 0.9559 | 0.956 |
| Sweden | combined_strategy | 442.82 | 7.308 | 2.199 | 1.807 | 0.9957 | 0.9963 |
| Sweden | current | 119,559 | 1,952 | 512.94 | 186.71 | 0 | 0 |
| Sweden | higher_child_coverage | 122,101 | 2,002.1 | 540.42 | 187.93 | -0.05359 | -0.02126 |
| Sweden | maternal_immunization | 4,255.8 | 67.86 | 19.37 | 16.68 | 0.9622 | 0.9644 |
| Sweden | next_generation_vaccine | 328.81 | 5.372 | 1.696 | 2.477 | 0.9967 | 0.9972 |
| Sweden | resistance_guided_treatment | 11,583.9 | 189.97 | 49.75 | 9.375 | 0.903 | 0.9031 |
| United Kingdom | adolescent_booster | 21,756.2 | 366.35 | 110.63 | 29.63 | 0.9621 | 0.9632 |
| United Kingdom | combined_strategy | 2,775.1 | 47.56 | 15.79 | 3.537 | 0.9946 | 0.9953 |
| United Kingdom | current | 590,886 | 10,466.9 | 2,915.4 | 376.06 | 0 | 0 |
| United Kingdom | higher_child_coverage | 535,540 | 9,476.5 | 2,682.7 | 322.77 | 0.07982 | 0.09367 |
| United Kingdom | maternal_immunization | 47,896.7 | 836.70 | 242.23 | 53.64 | 0.9169 | 0.9189 |
| United Kingdom | next_generation_vaccine | 3,311.6 | 57.41 | 17.54 | 7.315 | 0.994 | 0.9944 |
| United Kingdom | resistance_guided_treatment | 70,620.6 | 1,256.8 | 349.48 | 20.06 | 0.8801 | 0.8805 |
| United States | adolescent_booster | 183,707 | 2,912.4 | 860.29 | 0 | 0.961 | 0.9611 |
| United States | combined_strategy | 15,658.1 | 253.11 | 82.72 | 0 | 0.9963 | 0.9967 |
| United States | current | 4,725,321 | 75,773.6 | 22,059.2 | 0 | 0 | 0 |
| United States | higher_child_coverage | 4,842,313 | 78,027.6 | 23,210.8 | 0 | -0.05221 | -0.02476 |
| United States | maternal_immunization | 154,602 | 2,428.1 | 762.77 | 0 | 0.9654 | 0.9673 |
| United States | next_generation_vaccine | 11,891.4 | 191.36 | 65.74 | 0 | 0.997 | 0.9975 |
| United States | resistance_guided_treatment | 435,756 | 7,009.9 | 2,027.4 | 0 | 0.9081 | 0.9078 |

**Table S10. Model-derived outcomes and summary definitions.**

| Quantity | Definition | Denominator or reference population | Primary use |
| --- | --- | --- | --- |
| Total infections | Symptomatic plus asymptomatic incident infections integrated over the analysis interval. | Total population averaged over the interval. | Overall transmission burden. |
| Reported cases | Symptomatic incident infections multiplied by age-specific reporting probabilities and integrated over the analysis interval. | Total population averaged over the interval. | Calibration target and surveillance-comparable burden. |
| Infant cases | Symptomatic incident infections in the 0-2 month and 3-11 month age groups. | Mean population in the two infant age groups. | Primary severe-risk outcome. |
| Resistant infections | Total incident infections attributed to the macrolide-resistant strain. | Total population averaged over the interval. | Resistance burden and treatment relevance. |
| Resistant fraction | Resistant infections divided by total infections at a time point or over a summary interval. | Total infections. | Strain-composition diagnostic. |
| PEP-averted cases | Difference between pre-PEP and post-PEP symptomatic infection flows under the same state trajectory. | Not a population-normalized compartment count unless explicitly annualized. | Diagnostic estimate of prophylaxis effect. |
| Relative reduction | \(1-Z/Z_0\), where \(Z\) is the scenario outcome and \(Z_0\) is the comparator outcome. | Scenario-specific comparator. | Cross-scenario intervention comparison. |
