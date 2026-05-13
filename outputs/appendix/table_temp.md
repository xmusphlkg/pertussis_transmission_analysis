## eTables

<!-- BEGIN ETABLE 1 -->
**eTable 1. Country-specific population, surveillance, vaccination, and seasonal-forcing inputs.**

<!-- Generated from `manuscript_notes/country_profile_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Population | Seasonal phase | Seasonal amplitude | Mean reported incidence per 100k | Vaccine product | Adolescent booster | Maternal program |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | 26,713,206 | 300.45 | 0.1646 | 54.98 | aP | Yes | Yes |
| Brazil | 211,998,565 | 325.83 | 0.18 | 0.8601 | wP | No | Yes |
| China | 1,419,321,285 | 155.34 | 0.2994 | 4.431 | aP | No | No |
| Japan | 123,753,042 | 191.35 | 0.2794 | 7.837 | aP | No | No |
| New Zealand | 5,213,946 | 358.27 | 0.1963 | 25.11 | aP | Yes | Yes |
| South Africa | 64,007,189 | 184.59 | 0.2007 | 2.276 | aP | Yes | Yes |
| Sweden | 10,606,995 | 281.95 | 0.2059 | 5.955 | aP | Yes | Yes |
| Thailand | 71,668,012 | 28.67 | 0.2359 | 0.1977 | wP | No | Yes |
| United Kingdom | 69,138,185 | 133.56 | 0.1959 | 7.268 | aP | No | Yes |
| United States | 345,426,570 | 335.77 | 0.1043 | 1.439 | aP | Yes | Yes |
<!-- END ETABLE 1 -->

<!-- BEGIN ETABLE 2 -->
**eTable 2. Vaccine-mechanism parameterization used in scenario analyses.**

<!-- Generated from `manuscript_notes/scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Scenario | VE_sus | VE_sym | VE_inf | VE_dur | Description |
| --- | --- | --- | --- | --- | --- |
| no_vaccine | 0 | 0 | 0 | 0 | No vaccine protection. |
| symptom_protective | 0.15 | 0.85 | 0.25 | 0 | aP-like disease protection with moderate infection/transmission blocking. VE_inf = 0.25 represents the time-averaged effect of aP vaccination on onward infectiousness, accounting for rapid waning from initial ~50-60% to <10% within 3-5 years post-vaccination (Warfel et al. 2014 baboon model; Althouse & Scarpino 2015; McGirr & Fisman 2015 meta-analysis). This is a population-average across recently and distantly vaccinated individuals. |
| infection_blocking | 0.7 | 0.85 | 0.4 | 0.1 | Stronger reduction in susceptibility to infection. VE_inf = 0.40 represents the upper range of current aP effectiveness against transmission in recently vaccinated individuals. |
| transmission_blocking | 0.3 | 0.85 | 0.55 | 0.3 | Strong reduction in onward infectiousness and duration. Represents an improved aP formulation or wP-like transmission blocking. |
| next_generation | 0.8 | 0.9 | 0.65 | 0.4 | Strong infection, symptom, and transmission protection. Represents a next-generation pertussis vaccine with mucosal immunity induction (e.g. live-attenuated nasal or outer membrane vesicle platforms). |
<!-- END ETABLE 2 -->

<!-- BEGIN ETABLE 3 -->
**eTable 3. Macrolide-resistance initialization, importation, and fitness assumptions.**

<!-- Generated from `manuscript_notes/resistance_scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Scenario | Target resistant fraction | Importation resistant fraction | Anchor rate per year | Country timeline | Fitness_R | Description |
| --- | --- | --- | --- | --- | --- | --- |
| country_timeline | 0.3 | 0.3 | 2 | Yes | 1.000 | Country-specific macrolide resistance prevalence from data/raw/country_resistance_timeline.csv. Fitness set to 1.0 (neutral) based on epidemiological evidence: China MRBP rose from 36% (2016) to near-fixation (>99%, 2024) within 8 years, and the MT28-ptxP3 clone spread to Japan (83-88%, 2024-2025), France, and the US without apparent transmission disadvantage. Rapid fixation is inconsistent with a substantial fitness cost (Fu et al. EID 2024; Cai et al. medRxiv 2025; Fong et al. Lancet Microbe 2026). The fitness_grid and fitness_sensitivity scenarios explore the full range [0.70-1.25]. |
| low | 0.05 | 0.05 | 2 | No | 1.000 | Low macrolide resistance prevalence with fitness-neutral strain. |
| moderate | 0.3 | 0.3 | 2 | No | 1.000 | Moderate macrolide resistance prevalence with fitness-neutral strain. |
| high | 0.7 | 0.7 | 2 | No | 1.000 | High macrolide resistance prevalence with fitness-neutral strain. |
| very_high | 0.95 | 0.95 | 2 | No | 1.000 | Very high macrolide resistance prevalence with fitness-neutral strain. |
| country_timeline_fitness_cost | 0.3 | 0.3 | 2 | Yes | 0.85 | Country-timeline resistance with moderate fitness cost (15%). Retained as a sensitivity scenario representing the traditional assumption that ribosomal mutations impose a growth penalty. Contradicted by the observed rapid fixation in China and Japan but included to bound the optimistic end of resistance projections. |
| country_timeline_fitness_advantage | 0.3 | 0.3 | 2 | Yes | 1.100 | Country-timeline resistance with fitness advantage (10%). The MT28-ptxP3 MRBP clone carries additional virulence-associated alleles (ptxA1, prn- negative, fim3-2) that may confer a selective advantage in partially vaccinated populations (Hu et al. 2025; genomic surveillance studies report co-selection of resistance and vaccine-escape alleles). This scenario tests whether a modest fitness advantage materially changes long-term resistance burden projections. |
| high_fitness_advantage | 0.7 | 0.7 | 2 | No | 1.150 | High resistance prevalence with fitness advantage (15%). Worst-case scenario combining high initial resistance with a fitness-advantaged strain, representing the upper bound of resistant infection burden. Motivated by the observation that MRBP clones in China carry compensatory mutations and virulence factor combinations that may enhance transmissibility in the aP-vaccinated population context. |
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
| simulation.end_time | Simulation analysis horizon | 9,495.0 | see config/model_settings.yaml sensitivity_parameters | days | pertussis_cycle_model | No |
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
| infant_high_adult_very_low |  | Yes | No | Reporting-rate sensitivity assumption. |
| infant_moderate_adult_minimal |  | Yes | No | Reporting-rate sensitivity assumption. |
| enhanced_surveillance |  | Yes | No | Reporting-rate sensitivity assumption. |
| adult_focused_improvement |  | Yes | No | Reporting-rate sensitivity assumption. |
| china_passive_system |  | Yes | No | Reporting-rate sensitivity assumption. |
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
| South Africa | ZAF | 2025 |  | 0.02 | 0.005 | 0.05 | global_surveillance_extrapolation | https://www.cdc.gov/pertussis/hcp/antibiotic-resistance/; https://www.mdpi.com/2079-6382/11/11/1570 |
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
| Australia | Yes | Yes | accepted |  |  |  | 5,639.7 | 5,639.7 | 0.02 |
| Brazil | No | No |  |  |  |  |  |  |  |
| China | Yes | Yes | accepted |  |  |  | 33,266.4 | 33,424.7 | 0.01359 |
| Japan | Yes | Yes | accepted |  |  |  | 7,586.6 | 7,644.8 | 0.01604 |
| New Zealand | Yes | Yes | accepted |  |  |  | 5,829.0 | 5,912.3 | 0.01536 |
| South Africa | Yes | Yes | accepted |  |  |  | 7,319.7 | 7,319.7 | 0.01947 |
| Sweden | Yes | Yes | accepted |  |  |  | 8,646.9 | 8,687.2 | 0.01667 |
| Thailand | Yes | Yes | accepted |  |  |  | 3,394.0 | 3,394.0 | 0.01439 |
| United Kingdom | Yes | Yes | accepted |  |  |  | 22,468.1 | 23,719.8 | 0.01895 |
| United States | Yes | Yes | accepted |  |  |  | 5,936.5 | 5,936.5 | 0.01182 |
<!-- END ETABLE 8 -->

<!-- BEGIN ETABLE 9 -->
**eTable 9. Intervention outcome summaries by country and strategy.**

<!-- Generated from `outputs/tables/table_4_intervention_comparison.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Strategy | Total infections | Reported cases | Infant cases | Resistant infections | Infant-case reduction | Infection reduction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | adolescent_booster | 53,722,240 | 955,792 | 569,827 | 53,380,632 | -1.048e-05 | -9.06e-06 |
| Australia | combined_strategy | 37,141,959 | 567,877 | 249,452 | 35,764,034 | 0.5622 | 0.3086 |
| Australia | current | 53,721,753 | 955,773 | 569,821 | 53,380,778 | 0 | 0 |
| Australia | higher_child_coverage | 53,734,961 | 966,298 | 594,082 | 53,394,478 | -0.04258 | -0.0002459 |
| Australia | maternal_immunization | 51,483,400 | 885,836 | 545,347 | 51,154,434 | 0.04295 | 0.04167 |
| Australia | next_generation_vaccine | 40,227,706 | 622,197 | 296,170 | 39,980,747 | 0.4802 | 0.2512 |
| Australia | resistance_guided_treatment | 44,579,084 | 734,007 | 362,951 | 42,900,214 | 0.363 | 0.1702 |
| Brazil | adolescent_booster | 442,132,771 | 8,206,193 | 5,243,906 | 438,621,180 | -7.982e-06 | -1.524e-05 |
| Brazil | combined_strategy | 328,708,558 | 5,379,481 | 2,613,752 | 310,013,282 | 0.5016 | 0.2565 |
| Brazil | current | 442,126,034 | 8,205,496 | 5,243,864 | 438,618,760 | 0 | 0 |
| Brazil | higher_child_coverage | 442,258,321 | 8,268,900 | 5,370,691 | 438,751,836 | -0.02419 | -0.0002992 |
| Brazil | maternal_immunization | 430,301,790 | 7,775,200 | 5,070,325 | 426,917,501 | 0.03309 | 0.02674 |
| Brazil | next_generation_vaccine | 363,421,589 | 6,062,260 | 3,236,749 | 360,669,777 | 0.3828 | 0.178 |
| Brazil | resistance_guided_treatment | 375,013,465 | 6,522,971 | 3,521,960 | 352,902,682 | 0.3284 | 0.1518 |
| China | adolescent_booster | 2,634,155,791 | 40,963,963 | 24,679,215 | 2,634,132,358 | -3.088e-05 | -7.794e-06 |
| China | combined_strategy | 2,018,078,927 | 28,466,408 | 13,147,220 | 2,017,985,442 | 0.4673 | 0.2339 |
| China | current | 2,634,135,260 | 40,958,897 | 24,678,452 | 2,634,111,825 | 0 | 0 |
| China | higher_child_coverage | 2,634,329,371 | 41,233,468 | 25,278,231 | 2,634,306,002 | -0.0243 | -7.369e-05 |
| China | maternal_immunization | 2,580,024,401 | 39,411,632 | 24,219,545 | 2,580,001,234 | 0.0186 | 0.02054 |
| China | next_generation_vaccine | 2,270,165,370 | 32,703,426 | 16,756,768 | 2,270,144,997 | 0.321 | 0.1382 |
| China | resistance_guided_treatment | 2,242,513,465 | 33,133,645 | 16,890,296 | 2,242,411,133 | 0.3156 | 0.1487 |
| Japan | adolescent_booster | 199,289,973 | 3,000,140 | 1,567,251 | 199,174,690 | -0.0001397 | -0.0001318 |
| Japan | combined_strategy | 146,386,142 | 1,944,647 | 744,267 | 145,957,723 | 0.525 | 0.2654 |
| Japan | current | 199,263,714 | 2,999,302 | 1,567,032 | 199,148,214 | 0 | 0 |
| Japan | higher_child_coverage | 199,299,334 | 3,012,380 | 1,593,542 | 199,184,060 | -0.01692 | -0.0001788 |
| Japan | maternal_immunization | 194,651,003 | 2,846,937 | 1,500,762 | 194,537,143 | 0.04229 | 0.02315 |
| Japan | next_generation_vaccine | 170,621,992 | 2,315,007 | 1,004,114 | 170,521,141 | 0.3592 | 0.1437 |
| Japan | resistance_guided_treatment | 162,854,115 | 2,287,976 | 980,696 | 162,386,003 | 0.3742 | 0.1827 |
| New Zealand | adolescent_booster | 10,852,900 | 201,566 | 131,790 | 10,766,008 | -5.347e-05 | -9.156e-05 |
| New Zealand | combined_strategy | 7,717,592 | 125,261 | 60,909.1 | 7,275,008 | 0.5378 | 0.2888 |
| New Zealand | current | 10,851,906 | 201,546 | 131,783 | 10,765,128 | 0 | 0 |
| New Zealand | higher_child_coverage | 10,856,481 | 203,388 | 135,471 | 10,769,717 | -0.02799 | -0.0004216 |
| New Zealand | maternal_immunization | 10,452,970 | 188,618 | 126,205 | 10,369,832 | 0.04232 | 0.03676 |
| New Zealand | next_generation_vaccine | 8,376,520 | 138,108 | 73,326.2 | 8,313,293 | 0.4436 | 0.2281 |
| New Zealand | resistance_guided_treatment | 9,115,747 | 158,342 | 87,292.8 | 8,570,390 | 0.3376 | 0.16 |
| South Africa | adolescent_booster | 113,389,682 | 2,218,744 | 1,279,003 | 112,940,916 | -0.000329 | -0.0002192 |
| South Africa | combined_strategy | 54,310,595 | 913,395 | 376,545 | 52,542,535 | 0.7055 | 0.5209 |
| South Africa | current | 113,364,828 | 2,217,588 | 1,278,582 | 112,916,019 | 0 | 0 |
| South Africa | higher_child_coverage | 113,785,946 | 2,230,963 | 1,199,700 | 113,337,109 | 0.06169 | -0.003715 |
| South Africa | maternal_immunization | 105,728,695 | 1,958,801 | 1,083,729 | 105,304,828 | 0.1524 | 0.06736 |
| South Africa | next_generation_vaccine | 71,309,025 | 1,317,936 | 668,423 | 70,989,490 | 0.4772 | 0.371 |
| South Africa | resistance_guided_treatment | 79,901,077 | 1,450,442 | 700,808 | 77,075,107 | 0.4519 | 0.2952 |
| Sweden | adolescent_booster | 20,848,793 | 365,216 | 227,696 | 20,704,016 | -4.45e-05 | -7.008e-05 |
| Sweden | combined_strategy | 14,773,609 | 227,422 | 105,785 | 13,942,461 | 0.5354 | 0.2913 |
| Sweden | current | 20,847,332 | 365,192 | 227,686 | 20,702,378 | 0 | 0 |
| Sweden | higher_child_coverage | 20,853,867 | 370,405 | 239,780 | 20,709,353 | -0.05312 | -0.0003135 |
| Sweden | maternal_immunization | 20,096,138 | 343,707 | 222,014 | 19,956,924 | 0.02491 | 0.03603 |
| Sweden | next_generation_vaccine | 16,268,389 | 250,873 | 122,706 | 16,153,124 | 0.4611 | 0.2196 |
| Sweden | resistance_guided_treatment | 17,423,833 | 286,738 | 149,851 | 16,400,999 | 0.3419 | 0.1642 |
| Thailand | adolescent_booster | 135,022,531 | 2,179,336 | 1,258,539 | 133,851,518 | -6.578e-05 | -4.236e-05 |
| Thailand | combined_strategy | 102,308,330 | 1,482,680 | 649,037 | 95,681,723 | 0.4843 | 0.2423 |
| Thailand | current | 135,016,812 | 2,179,048 | 1,258,456 | 133,847,572 | 0 | 0 |
| Thailand | higher_child_coverage | 135,024,036 | 2,176,442 | 1,244,823 | 133,854,194 | 0.01083 | -5.351e-05 |
| Thailand | maternal_immunization | 131,870,652 | 2,065,943 | 1,190,611 | 130,734,511 | 0.05391 | 0.0233 |
| Thailand | next_generation_vaccine | 115,515,342 | 1,723,507 | 872,862 | 114,550,430 | 0.3064 | 0.1444 |
| Thailand | resistance_guided_treatment | 113,887,504 | 1,739,045 | 853,796 | 106,293,395 | 0.3216 | 0.1565 |
| United Kingdom | adolescent_booster | 133,217,282 | 2,517,033 | 1,573,854 | 132,508,166 | -2.334e-05 | -0.0001067 |
| United Kingdom | combined_strategy | 92,314,890 | 1,532,842 | 722,418 | 86,130,037 | 0.541 | 0.307 |
| United Kingdom | current | 133,203,075 | 2,516,401 | 1,573,818 | 132,495,442 | 0 | 0 |
| United Kingdom | higher_child_coverage | 133,255,521 | 2,539,283 | 1,619,064 | 132,548,904 | -0.02875 | -0.0003937 |
| United Kingdom | maternal_immunization | 129,284,123 | 2,377,314 | 1,522,559 | 128,607,588 | 0.03257 | 0.02942 |
| United Kingdom | next_generation_vaccine | 107,075,713 | 1,790,532 | 925,159 | 106,555,397 | 0.4122 | 0.1961 |
| United Kingdom | resistance_guided_treatment | 108,262,489 | 1,926,159 | 1,016,309 | 100,575,077 | 0.3542 | 0.1872 |
| United States | adolescent_booster | 555,430,330 | 9,313,776 | 4,649,480 | 0 | -3.515e-05 | -2.934e-05 |
| United States | combined_strategy | 453,233,942 | 7,131,887 | 3,225,953 | 0 | 0.3061 | 0.184 |
| United States | current | 555,414,036 | 9,313,362 | 4,649,316 | 0 | 0 | 0 |
| United States | higher_child_coverage | 555,242,435 | 9,395,959 | 4,875,858 | 0 | -0.04873 | 0.000309 |
| United States | maternal_immunization | 528,713,427 | 8,596,521 | 4,507,719 | 0 | 0.03046 | 0.04807 |
| United States | next_generation_vaccine | 392,647,306 | 5,840,052 | 2,510,517 | 0 | 0.46 | 0.2931 |
| United States | resistance_guided_treatment | 544,804,219 | 9,079,974 | 4,460,593 | 0 | 0.04059 | 0.0191 |
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
| Age structure | Eight model age groups | 0-2 months, 3-11 months, 1-4 years, 5-9 years, 10-17 years, 18-39 years, 40-64 years, and 65 years or older. |
| Strain structure | Two strain classes | Macrolide-sensitive and macrolide-resistant strains are simulated separately. |
| Vaccine-history structure | Explicit origin states | Unvaccinated, maternally protected, dose-1 recent/waned, dose-2 recent/waned, and dose-3-plus recent/waned states retain distinct effects. |
| Burn-in and horizon | Long burn-in plus analysis window | Sixty-year burn-in followed by a 26-year analysis period beginning on 1 January 2025. |
| Time scale | Daily rates with weekly saved output | All state equations are evaluated in days, and output is stored every 7 days for downstream summaries. |
| Numerical solver | Adaptive Runge-Kutta integration | RK45 with relative tolerance 1e-5 and absolute tolerance 1e-7. |
| Seasonality | Annual cosine forcing | A 4-year diagnostic term is available when surveillance peaks support multi-year recurrence. |
| Demography | WPP trajectory-driven age turnover | Births and aging are driven by UN World Population Prospects 2024 annual trajectories with gentle nudging toward target age profiles; a fixed-profile fallback is retained for tests. |
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
| VE_inf | Beta(mean=0.25, sd=0.12) | Prior centered on 0.25 representing the population-average effect of aP vaccination on onward infectiousness, accounting for the mix of recently vaccinated (VE_inf ~0.50-0.60) and distantly vaccinated (VE_inf ~0.05-0.10) individuals in the population. SD of 0.12 allows the posterior to explore the range [0.05, 0.50] which spans from fully waned to recently boosted. Previous prior (mean 0.40) was too optimistic for a population-average parameter given rapid waning. References: Warfel et al. 2014 (baboon colonization model); Althouse & Scarpino 2015 (transmission model); McGirr & Fisman 2015 (meta-analysis of aP effectiveness). |
| VE_dur | Beta(mean=0.1, sd=0.1) |  |
| relative_infectiousness_asymptomatic | Beta(mean=0.45, sd=0.15) | Relative infectiousness of asymptomatic/subclinical infections compared to symptomatic cases. This parameter has high sensitivity for infant case projections (PRCC ~0.59 in LHS screening) because asymptomatic adult infections are the primary reservoir maintaining transmission to unvaccinated infants. Range [0.15, 0.75] spans from minimal subclinical transmission to near-equal infectiousness. WHO position paper (2015) notes subclinical infections contribute to transmission but at reduced efficiency. |
| infectious_duration_symptomatic | Log-normal around baseline, log_sd=0.2 |  |
| infectious_duration_asymptomatic | Log-normal around baseline, log_sd=0.25 |  |
| fitness_R | Beta(mean=1.0, sd=0.12) | Prior centered on fitness-neutral (1.0) based on epidemiological evidence that MRBP reached near-fixation in China within 8 years and spread globally without apparent transmission disadvantage. SD of 0.12 allows the posterior to explore modest fitness costs (down to ~0.75) or advantages (up to ~1.25). The previous prior (mean 0.95, SD 0.18) was inconsistent with the observed rapid fixation dynamics. |
| resistance_prevalence | {'floor_sd': 0.03} |  |
| reporting_trend | Log-normal around baseline, log_sd=0.4 | Prior on the log of the reporting-trend end multiplier. Centered on log(1.0) = 0 (no secular change) with SD 0.40, allowing the posterior to learn whether reporting completeness has changed over the analysis period. The multiplier maps to [0.3, 3.0] via a scaled logit transform. |
<!-- END ETABLE 12 -->

<!-- BEGIN ETABLE 13 -->
**eTable 13. Continuous macrolide-resistant fitness and vaccine infectiousness grid.**

<!-- Generated from `manuscript_notes/fitness_grid_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Fitness_R | VE_inf | Description |
| --- | --- | --- |
| 0.7 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.7 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.7 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.7 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.7 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.8 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.8 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.8 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.8 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.8 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.85 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.85 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.85 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.85 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.85 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.9 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.9 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.9 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.9 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.9 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.95 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.95 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.95 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.95 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.95 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.98 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.98 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.98 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.98 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 0.98 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.000 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.000 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.000 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.000 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.000 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.020 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.020 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.020 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.020 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.020 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.050 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.050 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.050 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.050 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.050 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.100 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.100 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.100 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.100 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.100 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.150 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.150 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.150 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.150 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.150 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.200 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.200 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.200 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.200 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.200 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.250 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.250 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.250 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.250 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
| 1.250 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-next-generation vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and global MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. |
<!-- END ETABLE 13 -->
