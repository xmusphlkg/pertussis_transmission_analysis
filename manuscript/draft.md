# Infant Pertussis Burden, Vaccine Transmission Blocking, and Macrolide Resistance

**Article type:** Original Investigation; Transmission Modeling Scenario Analysis

**Target journal:** JAMA Network Open

**Authors:** Kangguo Li, Yulun Xie, Yunzhi Zenghuang, Tao Chen, Sha Chen, Yue He, Tianmu Chen

**Affiliations:** State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine Laboratory, National Innovation Platform for Industry-Education Integration in Vaccine Research, School of Public Health, Xiamen University, Xiamen, China

**Manuscript word count:** 2933

## Key Points

**Question:** How do vaccine transmission blocking and macrolide-resistant *Bordetella pertussis* dynamics alter scenario projections of infant pertussis burden?

**Findings:** In this deterministic transmission-modeling scenario analysis of 10 illustrative country profiles, simulated infant burden varied across vaccine mechanism and resistance-management scenarios. A hypothetical high-transmission-blocking vaccine profile had the largest reductions, whereas maternal-household composite and resistance-guided treatment scenarios were sensitive to implementation and resistance-fitness assumptions.

**Meaning:** Pertussis transmission models should report clinical protection, transmission blocking, infant burden, total infections, and resistant infections separately; these scenario projections should not be interpreted as national forecasts or policy rankings.

## Abstract

**Importance:** Pertussis continues to threaten young infants despite established vaccination programs, and macrolide-resistant *Bordetella pertussis* is spreading internationally. Scenario models that combine clinical protection with transmission blocking may obscure mechanisms relevant to infant burden and antimicrobial resistance.

**Objective:** To evaluate how vaccine transmission-blocking assumptions and macrolide-resistant strain dynamics alter scenario projections of infant pertussis burden.

**Design:** Deterministic age-structured transmission-modeling scenario analysis using a 15-year burn-in and a 26-year horizon beginning January 1, 2025.

**Setting:** Population-level scenario profiles for 10 countries using evidence accessed through May 9, 2026.

**Participants:** No individual participants were included; analyses used purposively selected country profiles.

**Exposures:** Vaccine mechanism profiles, resistance prevalence and fitness assumptions, current-program modifications, implementation-dependent maternal-household and resistance-guided management scenarios, and hypothetical transmission-blocking product profiles.

**Main Outcomes and Measures:** Annualized infant symptomatic cases, all incident infections, reported cases, resistant-strain incident infections, resistant fraction, and relative reductions.

**Results:** Across 10 calibrated illustrative profiles, conditional-overlay median annualized infant case incidence under current practice ranged from 15 in Thailand to 2,517 in Australia per 100,000 infants; infant incidence was not directly calibrated, so absolute rates are comparative endpoints. Overall calibration-window mean absolute percentage error for reported cases was 5.4% (interquartile range, 3.9%-7.8%). Stronger transmission-blocking vaccine profiles reduced infant cases more than the symptom-protective profile. Compared with current practice, the maternal-household composite transmission-reduction proxy and resistance-guided treatment had median infant-case reductions of 44.4% and 40.5%, respectively; scenarios including a hypothetical high-transmission-blocking vaccine profile had reductions exceeding 95%. Resistance-management findings were sensitive to resistant-strain fitness, testing reach, and postexposure prophylaxis assumptions.

**Conclusions and Relevance:** In this scenario-based transmission-modeling analysis, infant pertussis burden was sensitive to assumptions about vaccine transmission blocking and macrolide-resistant strain dynamics. These findings support reporting clinical protection and onward transmission effects separately in pertussis models and should be interpreted as scenario projections rather than national forecasts or policy recommendations.

## Introduction

Pertussis continues to cause substantial morbidity among young infants despite established childhood vaccination programs and maternal immunization in many settings.^1-3^ Current policy debates include maternal immunization, booster strategies, improved vaccines, treatment, postexposure prophylaxis (PEP), and antimicrobial resistance.^4-6^ Interpreting vaccination scenarios is challenging because vaccines may reduce symptoms, susceptibility, infectiousness, and infectious duration to different degrees, especially when infant protection depends on reduced transmission from older age groups.

Post-pandemic pertussis resurgence has occurred despite high routine childhood vaccination coverage, consistent with models in which waning and immune boosting shape long-term dynamics.^7,8^ Acellular pertussis (aP) vaccines can prevent disease while providing incomplete protection against infection and onward transmission.^9^ Epidemiologic evidence similarly indicates that aP-derived protection against infection wanes substantially within 3 to 5 years, while protection against severe disease persists longer.^10-13^

Macrolide-resistant *B pertussis* (MRBP) has also emerged internationally. Shanghai genomic surveillance found resistance rose from 50% or less before 2020 to nearly 100% after 2020, linked to the 23S rRNA A2047G mutation; in a 2024 multicenter China outbreak study, 99.5% of isolates belonged to an MT28-Shanghai clone carrying ptxP3, A2047G, and prn150.^2,14,15^ MRBP and related lineages have been reported in public health summaries for the Americas and elsewhere, with genomic reports from Australia and Japan and global spread analyses providing further dissemination evidence.^16-21^ These patterns challenge the assumption that resistant strains necessarily carry a major transmission disadvantage.

Most pertussis policy models report vaccine effectiveness as a single composite endpoint and do not explicitly model how transmission-blocking properties interact with antimicrobial resistance. We therefore used 10 purposively selected country profiles as contrasting policy-relevant scenarios, not as a representative global sample, to evaluate how alternative vaccine-mechanism and resistance assumptions alter simulated infant burden, total infections, reported cases, and resistant infections under specified assumptions.

## Methods

### Design and Data Sources

This deterministic transmission-modeling scenario analysis synthesized demographic, surveillance, immunization, contact, treatment, and resistance evidence in an age-structured pertussis framework. Current practice was each profile's routine vaccination schedule and standard macrolide treatment/PEP assumptions. The analysis compared epidemiologic scenario projections under specified assumptions; it did not forecast national epidemics or estimate cost-effectiveness, feasibility, equity, or a complete policy appraisal. Reporting followed relevant non-cost CHEERS 2022 elements and WHO immunization-modeling guidance.^22,23^ Institutional review board review was not applicable because no individual-level data were used.

Ten purposively selected country profiles were analyzed: Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, the United Kingdom, and the United States. The profiles are illustrative settings chosen to span program, surveillance, contact, and resistance contrasts, not to estimate region-level or global averages. Inputs included United Nations World Population Prospects 2024 denominators, WHO/UNICEF and national immunization records, Prem/contactdata contact matrices, harmonized surveillance intervals, and resistance evidence accessed through May 9, 2026.^24-27^ Selection rationale and data-quality dimensions are reported in <span style="color:#5DADE2;">eTable 1</span>.

### Model Structure and Calibration

The model tracked 8 age groups, 2 strains, and susceptible origin histories reflecting maternal protection and recent or waned dose histories. Four vaccine mechanism parameters were represented separately: VE_sus, reduced susceptibility to infection; VE_sym, reduced symptoms given infection; VE_inf, reduced onward infectiousness; and VE_dur, shortened infectious duration. Immunity followed a SIRWS structure with immune boosting, waning from recovered to partially immune status over approximately 5 years, and return to susceptibility over approximately 10 years.^7,8^ Transmission used country-specific contact matrices, seasonality, aging and birth turnover, vaccination maintenance, importation, COVID-19 non-pharmaceutical intervention (NPI) contact reductions, treatment, and PEP. <span style="color:#5DADE2;">Table 1</span> classifies main model components; <span style="color:#5DADE2;">eTable 2</span> provides the full parameter-design matrix, source/provenance links, and detailed model documentation.

Calibration targeted reported pertussis case counts over the 6 most recent observed calendar years in each harmonized surveillance series, except South Africa, where 3 overlapping years were available. The retained fit minimized a negative-binomial reporting-interval likelihood plus penalties for age-specific reporting probabilities outside literature-informed bounds. Model-data checks included observed-vs-modeled reporting intervals, reporting probabilities, fit scores, mean absolute percentage errors, peak timing errors, and peak magnitude ratios (<span style="color:#5DADE2;">Figure 1C</span>, <span style="color:#5DADE2;">eFigure 2B and 2D</span>, and <span style="color:#5DADE2;">eTables 7 and 12</span>). Consistent age-specific observed incidence series were unavailable across all 10 profiles, so age-specific incidence was not a calibration target; resistance hindcasts were plausibility checks rather than held-out validation.

Calibrated parameters included country-specific transmission \(\beta_S\) and reporting multipliers, with age-specific reporting probabilities constrained by broad prior bands; natural-history, contact, vaccine-mechanism, and resistance parameters were fixed or varied in scenarios and sensitivity analyses. Because infant incidence was not directly calibrated, infant outcomes are internally consistent scenario endpoints rather than externally validated forecasts. Credibility checks relied on reported-incidence fit, fitted infant reporting gradients, separate 0-2 month and 3-11 month strata, infant-contact sensitivity, age-shift diagnostics, and infant-age-stratified intervention-window diagnostics (<span style="color:#5DADE2;">eTables 7, 12, 17, 18, and 22</span>). Consistent country-specific hospitalization or severity series were unavailable for calibration.

### Scenarios and Outcomes

Five vaccine profiles were compared: no vaccine, symptom-protective aP-like protection, infection-blocking protection, transmission-blocking protection, and a hypothetical high-transmission-blocking profile motivated by upper-bound mucosal-immunity product targets rather than an available vaccine (<span style="color:#5DADE2;">eTable 2</span>).^28,29^ Resistance scenarios used country-specific timelines or fixed low-to-very-high resistant prevalence, then allowed resistant dynamics to depend on importation, relative fitness, treatment shortening, strain-specific PEP effectiveness, and age/contact transmission.

Interventions included marginal child-coverage increases in already high-coverage profiles, adolescent boosting, a maternal-household composite transmission-reduction proxy, resistance-guided treatment under a main implementation scenario, the hypothetical high-transmission-blocking vaccine profile, and a combined strategy.^30^ Because scenarios mixed available or near-available levers, proxy packages, and hypothetical product targets, they were grouped as current-program modifications, implementation-dependent management or proxy packages, and hypothetical product-target vaccine profiles. The maternal-household composite transmission-reduction proxy combined passive newborn antibody protection, a reproductive-age adult boosting proxy, and a cocooning contact modifier; decomposition runs isolated these components.

The primary analysis compared current practice with predefined interventions for annualized infant symptomatic cases; vaccine transmission-blocking profiles and resistance-fitness interactions were key mechanistic analyses. Order-stability summaries, selected-parameter joint parameter-sampling diagnostics, QALY-like translation, the stochastic toy model, and vaccine-pipeline mapping were exploratory diagnostics.

Infant outcomes combined the 0-2 month and 3-11 month age groups, with both strata retained for reporting-probability, age-shift, and intervention-window diagnostics. Symptomatic cases were incident infections after VE_sym modification; reported cases applied age- and country-specific reporting probabilities; all infections included incident symptomatic and asymptomatic infections; resistant infections were caused by the resistant strain. Annualized outcomes were averaged over the 26-year saved horizon unless otherwise specified. Relative reduction was defined as \(1-Z/Z_0\).

### Sensitivity Analysis

Sensitivity analyses included vaccine-mechanism thresholds, resistant-fitness grids, reporting assumptions, resistance-mechanism decomposition, treatment and PEP implementation scenarios, infant contact multipliers, maternal passive-protection duration, burn-in and COVID-19 NPI assumptions, child-coverage diagnostics, scenario order across windows and infant strata, event-scale diagnostics, joint order-stability diagnostics, a contactdata stochastic toy model, QALY-like translation, and vaccine-pipeline mapping. A 48-run Latin-hypercube analysis used correlation diagnostics for exploratory parameter screening; a separate 128-sample selected-parameter diagnostic varied reporting, infant contacts, VE_inf, resistant fitness, asymptomatic transmission, resistance-management uptake, and PEP reach. Conditional beta-grid intervals propagated transmission-rate uncertainty over an adaptive log-\(\beta_S\) grid with nuisance parameters fixed; they do not jointly propagate structural, resistance-fitness, contact-matrix, or implementation uncertainty.

## Results

### Simulated Burden Under Current Practice

The 10 illustrative calibrated country-profile scenarios produced wide variation in simulated burden under current aP-like vaccination and country-specific resistance anchors (<span style="color:#5DADE2;">Figure 1C and 1D</span>). In the saved-horizon comparison plotted in <span style="color:#5DADE2;">Figure 1C</span>, model-reported incidence differed from recent observed mean reported incidence by a median of 65.0% (IQR, 14.1%-143.4%; range, 6.2%-350.3%); this horizon-scale comparison differs from the interval-level calibration target. Direct calibration-window diagnostics showed mean absolute percentage error of 5.4% (IQR, 3.9%-7.8%; range, 1.2%-10.5%), median absolute peak-timing error of 1 year, and variable peak-magnitude ratios, supporting scenario comparison rather than outbreak forecasting (<span style="color:#5DADE2;">eTable 7</span>). Within these calibrated profiles, conditional-overlay median annualized infant case incidence ranged from 15 per 100,000 infants in Thailand to 2,517 in Australia, all-infection incidence from 33 to 3,192 per 100,000 persons, and reported incidence from 0.5 to 53.4 per 100,000 persons (<span style="color:#5DADE2;">Figure 1D</span>). Because infant-specific incidence was not a calibration target, absolute infant rates should be read as internally consistent comparative endpoints. Near-term checks showed sensitivity to burn-in duration and, in Australia, NPI contact-shock magnitude (<span style="color:#5DADE2;">eTable 21</span>).

### Infant-Outcome Robustness Diagnostics

Because infant incidence was not calibrated directly, the infant endpoint is the main calibration vulnerability; <span style="color:#5DADE2;">eTable 22</span> therefore reports 0-2 month and 3-11 month scenario contrasts across analysis windows. In the contact-matrix sensitivity, increasing child, adolescent, and adult sources into infant target groups from 0.75 to 1.50 changed current-practice 5-year median infant burden from 145.8 to 228.3 cases per 100,000 infants; the maternal-household composite transmission-reduction proxy remained lower across the same multipliers (93.4 to 138.5 per 100,000 infants). Varying passive maternal protection from 90 to 270 days changed direct-antibody-only 5-year reductions from 2.7% to 4.3% and the maternal-household composite transmission-reduction proxy from 55.1% to 56.8% (both in <span style="color:#5DADE2;">eTable 17</span>).

Across 5-, 10-, and 26-year windows, median reductions were 57.6%, 49.5%, and 43.1% for the maternal-household composite transmission-reduction proxy and 15.9%, 43.7%, and 40.7% for resistance-guided treatment, respectively (<span style="color:#5DADE2;">eTable 19</span>). In the 128-sample joint order-stability diagnostic, the lowest simulated infant burden occurred in combined (69.5%) or hypothetical high-transmission-blocking vaccine (30.5%) scenarios, while maternal-household composite and resistance-guided treatment scenarios remained intermediate (<span style="color:#5DADE2;">eTable 25</span>). These diagnostics support broad separation among mechanism categories but do not externally validate infant forecasts.

### Vaccine Transmission-Blocking Mechanism Scenarios

Vaccine profiles with stronger infection or transmission effects yielded progressively lower simulated infant and population burden (<span style="color:#5DADE2;">Figure 2A, 2B, and 2D</span>). Compared with no vaccination, the symptom-protective aP-like profile produced an 82.0% simulated infant-case reduction, whereas infection-blocking and hypothetical high-transmission-blocking profiles reduced residual infant burden to very low deterministic levels in several profiles (<span style="color:#5DADE2;">Figure 2B</span>); these low levels should not be interpreted as stochastic elimination probabilities. Vaccine-history decomposition showed that infections under the current aP-like profile remained concentrated in dose-3-or-more and waned histories, whereas residual infections under the hypothetical high-transmission-blocking profile were more concentrated in unvaccinated histories (<span style="color:#5DADE2;">Figure 2C</span>). Threshold analyses suggested that VE_inf values near 0.35 to 0.50 were needed to cross selected infant-case reduction or comparator thresholds when other vaccine mechanisms were held fixed (<span style="color:#5DADE2;">eTable 14</span>).

### Macrolide-Resistance Sensitivity Analyses

Resistant infection burden was sensitive to initial resistance prevalence, treatment pressure, PEP effectiveness, resistant-strain fitness, and vaccine infectiousness effects (<span style="color:#5DADE2;">Figure 3A-3F</span>). Under neutral-fitness country-timeline assumptions, the model generated a high median end resistant fraction (99.7%, from 1.0%; <span style="color:#5DADE2;">Figure 3A</span>), but this should be interpreted as a stress-test output rather than a forecast of inevitable resistant-strain replacement. Mechanism decomposition suggested that resistant fitness and treatment/PEP differentials drove most divergence: equalizing PEP effectiveness lowered the median end resistant fraction to 12.2%, equalizing both treatment and PEP effects lowered it to 1.0%, and imposing \(f_R = 0.85\) lowered it to 0.01% (<span style="color:#5DADE2;">Figure 3C</span> and <span style="color:#5DADE2;">eTable 13</span>). In the resistant-fitness sensitivity and fitness-by-VE_inf grid, the median end resistant fraction was less than 0.1% with \(f_R = 0.85\), 99.7% with \(f_R = 1.00\), and 99.9% with \(f_R = 1.15\) (<span style="color:#5DADE2;">Figure 3B and 3D</span>). Increasing VE_inf from 0.05 to 0.55 produced lower simulated infant burden across fitness assumptions, but the magnitude was fitness-dependent (<span style="color:#5DADE2;">Figure 3E and 3F</span>).

### Scenario Projections by Intervention Category

Scenario projections were grouped by interpretability rather than presenting them as mutually substitutable policy options (<span style="color:#5DADE2;">Figure 4A-4C</span>). Current practice had median annualized infant case incidence of 341 per 100,000 infants/year (<span style="color:#5DADE2;">Figure 4A and 4D</span>). Among current-program modification scenarios, marginal child-coverage increases in already high-coverage profiles yielded no consistent median infant-case reduction (-4.2%; IQR, -4.7% to -3.4%; <span style="color:#5DADE2;">Figure 4B</span>). Mechanism diagnostics suggested small age-shift and waning-immunity composition changes under specified assumptions; this unstable response should not be interpreted as evidence against maintaining high routine childhood coverage (<span style="color:#5DADE2;">eTable 18</span>). This result reflects marginal changes in already high-coverage profiles, not the value of routine childhood vaccination itself. Adolescent boosting produced a small median simulated reduction (1.9%; IQR, -0.2% to 58.4%; <span style="color:#5DADE2;">Figure 4B</span>).

Among implementation-dependent management or proxy scenarios, the maternal-household composite transmission-reduction proxy produced a simulated 44.4% infant-case reduction under specified implementation assumptions. Decomposition attributed a median 7.4% reduction to direct antibody protection alone, 34.7% to the reproductive-age adult boosting proxy, and 6.4% to cocooning; therefore, the proxy estimate should not be interpreted as passive maternal antibody protection alone. Infant contact-matrix sensitivity confirmed that adult-to-infant contact assumptions influenced absolute infant burden (<span style="color:#5DADE2;">eTable 17</span>). Resistance-guided treatment produced simulated reductions of 40.5% for infant cases and 96.7% for resistant infections in the main implementation scenario, but near-term implementation checks showed dependence on uptake, testing reach, PEP restoration, and PEP reach (<span style="color:#5DADE2;">eTable 16</span>).

Among hypothetical product-target vaccine profiles, the high-transmission-blocking vaccine and combined stress-test scenarios produced simulated infant-case reductions greater than 95%; the vaccine scenario represents a product target rather than an available intervention. Near-term analysis-window checks retained very large point estimates for scenarios including the hypothetical high-transmission-blocking vaccine profile but changed the relative positions of the maternal-household composite transmission-reduction proxy, adolescent-booster, and resistance-guided-treatment scenarios (<span style="color:#5DADE2;">eTable 19</span>). Exploratory infant-stratum, event-scale, order-stability, and stochastic toy-model diagnostics are summarized in the Supplement and support interpreting very low deterministic burdens as low-burden thresholds rather than stochastic elimination probabilities (<span style="color:#5DADE2;">eTables 20, 22, 23, 25, and 26</span>).

## Discussion

In this deterministic scenario-modeling analysis across 10 illustrative country profiles, projected infant pertussis burden varied substantially according to assumptions about vaccine transmission blocking and macrolide-resistant strain dynamics. Scenarios that reduced onward transmission generally had larger simulated infant-burden reductions than scenarios that primarily increased clinical protection. Resistance-management scenarios also altered both infant burden and resistant infections, but these results depended strongly on assumptions about resistant-strain fitness, diagnostic capacity, and PEP effectiveness.

The distinction between clinical protection and transmission blocking had quantifiable consequences. A symptom-protective aP-like profile had lower simulated infant cases than no vaccination, but stronger transmission-blocking profiles had larger simulated decreases in infant cases and total infections. This is consistent with evidence that aP vaccination prevents disease more strongly than colonization or transmission,^9^ and suggests that single composite vaccine-effectiveness parameters may underestimate the hypothetical simulated benefit of vaccines designed to reduce onward transmission.^28,29^

Resistance-guided treatment had simulated benefit under the main implementation assumptions, aligning with guidance emphasizing susceptibility testing and alternative treatment when resistance is suspected or confirmed.^16,17,30^ However, near-term scenarios showed dependence on uptake, testing reach, and PEP assumptions; real-world benefit would also depend on diagnostic capacity, rapid turnaround, clinician suspicion, alternative-drug availability, adherence, tolerability, and public health capacity.

The simulated increase in resistant fraction should be interpreted as conditional rather than deterministic. In particular, high resistant fractions under neutral-fitness assumptions represent stress-test outputs under specified treatment and PEP assumptions, not predictions of inevitable resistant-strain replacement. Hindcast plausibility checks did not rule out neutral or above-neutral fitness in China, Japan, and Australia, but they should not be read as validating a unique fitness estimate. A conservative \(f_R=0.85\) counterfactual produced a median end resistant fraction below 0.1% in the fitness sensitivity and 0.01% in the mechanism-decomposition run, highlighting that resistance conclusions depend on fitness and management assumptions.

Scenario contrasts depended on the interaction between vaccine mechanism and resistance. Marginal child-coverage increases in already high-coverage profiles did not produce a consistent median simulated infant-case reduction, and age-shift diagnostics suggested that the small modeled increase was not a robust policy signal or evidence against maintaining high coverage. The maternal-household composite transmission-reduction proxy also requires careful interpretation: the adult-boosting component should not be attributed to passive transplacental antibody protection alone, and infant-contact sensitivity analyses indicate that household-like contact assumptions remain important.

### Limitations

This study has limitations that should guide interpretation of the scenario projections. First, infant incidence was not directly calibrated because consistent age-specific observed incidence targets were unavailable across the 10 profiles. Absolute infant-burden estimates are therefore less secure than internally consistent contrasts in scenario direction, although fitted reporting gradients, separate infant strata, infant-contact sensitivity, and age-window diagnostics probed this vulnerability.

Second, intervals are conditional and do not include full structural or implementation uncertainty. The beta-grid intervals propagate transmission-rate uncertainty with nuisance parameters fixed; they do not jointly propagate contact-matrix uncertainty, resistance-fitness uncertainty, implementation heterogeneity, or alternative structural assumptions. Deterministic compartmental dynamics also do not represent stochastic extinction, household clustering, contact tracing, adherence, or superspreading.

Third, resistance projections are sensitive to resistant-strain fitness, treatment, and PEP assumptions. The high resistant fractions under neutral-fitness assumptions should be read as stress-test outputs rather than forecasts of inevitable resistant-strain replacement. Fourth, the 10 countries are illustrative rather than representative; cross-country contrasts should not be read as national forecasts, global estimates, or policy rankings. Additional interpretation limits include age-structured proxies rather than explicit pregnant-person or household compartments, a hypothetical high-transmission-blocking vaccine profile rather than an available product, and exploratory QALY-like translations without costs or formal decision thresholds (<span style="color:#5DADE2;">eTables 24 and 27</span>).

## Conclusions

Across 10 purposively selected illustrative country profiles, deterministic scenario-based simulations of infant pertussis burden were sensitive to assumptions about vaccine effects on infection and onward transmission and to macrolide-resistant strain dynamics. These findings support reporting vaccine clinical protection, transmission effects, infant burden, total infections, and resistant infections separately in pertussis transmission models; they should be interpreted as scenario projections rather than national forecasts, cost-effectiveness estimates, or policy recommendations.

## Supplement

**Supplement 1.** eMethods (full model equations, country-profile construction, calibration methods, scenario definitions, resistance hindcast plausibility checks, parameter identifiability classification), eReferences, <span style="color:#5DADE2;">eFigures 1-8</span>, and <span style="color:#5DADE2;">eTables 1-28</span>.

## Article Information

**Previous Presentation:** None.

**Corresponding Author:** Tianmu Chen, PhD, State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine Laboratory, National Innovation Platform for Industry-Education Integration in Vaccine Research, School of Public Health, Xiamen University, Xiamen, China (chentianmu@xmu.edu.cn).

**Author Contributions:** Kangguo Li and Tianmu Chen had full access to all the data in the study and take responsibility for the integrity of the data and the accuracy of the data analysis. Kangguo Li conducted and is responsible for the data analysis. Concept and design: Kangguo Li. Acquisition, analysis, or interpretation of data: Yulun Xie, Yunzhi Zenghuang, Tao Chen, Sha Chen, and Yue He. Drafting of the manuscript: Kangguo Li and Yulun Xie. Critical revision of the manuscript for important intellectual content: Kangguo Li. Statistical analysis: Kangguo Li. Administrative, technical, or material support: Kangguo Li and Tianmu Chen. Supervision: Tianmu Chen.

**Reporting Guideline:** Relevant non-cost elements of CHEERS 2022 and WHO immunization-modeling guidance were followed; model equations, parameter classification, calibration diagnostics, and sensitivity analyses are provided in the Supplement.

**Conflict of Interest Disclosures:** The authors have no conflicts of interest to disclose.

**Funding/Support:** This work was supported by the National Natural Science Foundation of China (825B2104 to Kangguo Li), and the National Key Research and Development Program of China (2024YFC2311404 to Tianmu Chen).

**Role of the Funder/Sponsor:** The funders had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.

**Data Sharing Statement:** Processed inputs, model code, configuration files, and generated outputs are publicly available without access restrictions at https://github.com/xmusphlkg/pertussis_transmission_analysis. A versioned public release with a permanent identifier will be archived at publication. No individual-level participant data were used or are available.

**Additional Contributions:** None.

**Use of Artificial Intelligence:** AI-assisted drafting and code-assistance tools (OpenAI Codex, GPT-5-based coding assistant; OpenAI; no extension number; used in May 2026) were used for language organization, code assistance, and implementation checks. They were not used to generate data, make autonomous analytic decisions, or replace author verification. The authors reviewed and edited all AI-assisted content and take full responsibility for the integrity of the final manuscript.

## References

1. World Health Organization. Pertussis vaccines: WHO position paper, August 2015. *Wkly Epidemiol Rec*. 2015;90:433-458.
2. Cai J, Liu Q, Chen B, et al. Waning immunity, prevailing non-vaccine type ptxP3 and macrolide-resistant strains in the 2024 pertussis outbreak in China: a multicentre cross-sectional descriptive study. *Lancet Reg Health West Pac*. 2025;60:101628. doi:10.1016/j.lanwpc.2025.101628
3. Ai X, Mori H, Krokva D, et al. Pertussis resurgence after the COVID-19 pandemic in four Western Pacific countries and the USA, highlighting the 2025 outbreak in Japan. *Sci Rep*. Published online April 18, 2026. doi:10.1038/s41598-026-47780-4
4. Akhmetzhanov AR, de Padua B, Dushoff J. Serial interval and intervention efficiency in pertussis outbreak, South Korea, 2024. *Emerg Infect Dis*. 2026;32(5):809-811. doi:10.3201/eid3205.251304
5. Zhang S, Xu Y, Xiao Y. Revisiting whooping cough: global drivers and implications of pertussis resurgence in the acellular vaccine era. *Vaccines (Basel)*. 2026;14(1):35. doi:10.3390/vaccines14010035
6. Sheng Y, Ma S, Zhou Q, Xu J. Pertussis resurgence: epidemiological trends, pathogenic mechanisms, and preventive strategies. *Front Immunol*. 2025;16:1618883. doi:10.3389/fimmu.2025.1618883
7. Wearing HJ, Rohani P. Estimating the duration of pertussis immunity using epidemiological signatures. *PLoS Pathog*. 2009;5:e1000647. doi:10.1371/journal.ppat.1000647
8. Lavine JS, King AA, Bjornstad ON. Natural immune boosting in pertussis dynamics and the potential for long-term vaccine failure. *Proc Natl Acad Sci U S A*. 2011;108:7259-7264. doi:10.1073/pnas.1014394108
9. Warfel JM, Zimmerman LI, Merkel TJ. Acellular pertussis vaccines protect against disease but fail to prevent infection and transmission in a nonhuman primate model. *Proc Natl Acad Sci U S A*. 2014;111:787-792. doi:10.1073/pnas.1314688110
10. Klein NP, Bartlett J, Rowhani-Rahbar A, Fireman B, Baxter R. Waning protection after fifth dose of acellular pertussis vaccine in children. *N Engl J Med*. 2012;367:1012-1019. doi:10.1056/NEJMoa1200850
11. McGirr A, Fisman DN. Duration of pertussis immunity after DTaP immunization: a meta-analysis. *Pediatrics*. 2015;135:331-343. doi:10.1542/peds.2014-1729
12. Chit A, Zivaripiran H, Shin T, et al. Acellular pertussis vaccines effectiveness over time: a systematic review, meta-analysis and modeling study. *PLoS One*. 2018;13:e0197970. doi:10.1371/journal.pone.0197970
13. Domenech de Cellès M, Magpantay FMG, King AA, Rohani P. The impact of past vaccination coverage and immunity on pertussis resurgence. *Sci Transl Med*. 2018;10:eaaj1748. doi:10.1126/scitranslmed.aaj1748
14. Fu P, Zhou J, Yang C, et al. Molecular evolution and increasing macrolide resistance of *Bordetella pertussis*, Shanghai, China, 2016-2022. *Emerg Infect Dis*. 2024;30(1):29-38. doi:10.3201/eid3001.221588
15. Xu Z, Huang Z, Yuan L, et al. Genomic surveillance reveals global spread of macrolide-resistant *Bordetella pertussis* linked to vaccine changes. *J Clin Microbiol*. 2025;63(12):e01064-25. doi:10.1128/jcm.01064-25
16. Centers for Disease Control and Prevention. Antibiotic-resistant *Bordetella pertussis*. Accessed May 9, 2026. https://www.cdc.gov/pertussis/hcp/antibiotic-resistance/index.html
17. Pan American Health Organization. PAHO calls for strengthened vaccination and surveillance amid the spread of antibiotic-resistant pertussis in the Americas. August 26, 2025. https://www.paho.org/en/news/26-8-2025-paho-calls-strengthened-vaccination-and-surveillance-amid-spread-antibiotic
18. Fong W, Rockett RJ, Tam KKG, et al. Characterisation of *Bordetella pertussis* virulence and macrolide resistance in Australia by targeted culture-independent sequencing: a genomic epidemiology study. *Lancet Microbe*. 2026;7(3):101286. doi:10.1016/j.lanmic.2025.101286
19. Komatsu S, Nakanishi N, Matsubara K, et al. Molecular analysis of emerging MT27 macrolide-resistant *Bordetella pertussis*, Kobe, Japan, 2025. *Emerg Infect Dis*. 2026;32:150-153. doi:10.3201/eid3201.250890
20. Obara T, Kano K, Yorifuji T, et al. Localized outbreak of macrolide-resistant pertussis in infants, Japan, March-May 2025. *Emerg Infect Dis*. 2026;32(1):158-161. doi:10.3201/eid3201.250824
21. Zhang H, Kang Z, Zhang Y, et al. Evolutionary dynamics and global spread of macrolide-resistant *Bordetella pertussis* during the post-pandemic pertussis resurgence. *J Infect*. 2026;92(4):106718. doi:10.1016/j.jinf.2026.106718
22. Husereau D, Drummond M, Augustovski F, et al. Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) statement. *BMJ*. 2022;376:e067975. doi:10.1136/bmj-2021-067975
23. World Health Organization. Guidance for using modelling for immunization decision-making. Geneva: World Health Organization; 2026. Accessed May 9, 2026. https://iris.who.int/handle/10665/385083
24. United Nations Department of Economic and Social Affairs, Population Division. World Population Prospects 2024. Accessed May 9, 2026. https://population.un.org/wpp/
25. Prem K, Cook AR, Jit M. Projecting social contact matrices in 152 countries using contact surveys and demographic data. *PLoS Comput Biol*. 2017;13:e1005697. doi:10.1371/journal.pcbi.1005697
26. Amirthalingam G, Andrews N, Campbell H, et al. Effectiveness of maternal pertussis vaccination in England: an observational study. *Lancet*. 2014;384:1521-1528. doi:10.1016/S0140-6736(14)60686-3
27. Baxter R, Bartlett J, Fireman B, Lewis E, Klein NP. Effectiveness of vaccination during pregnancy to prevent infant pertussis. *Pediatrics*. 2017;139:e20164091. doi:10.1542/peds.2016-4091
28. da Silva Antunes R, Sette A. New life into pertussis prevention. *Nat Microbiol*. 2025;10:3045-3046. doi:10.1038/s41564-025-02169-3
29. Yu G, Yang W, Ma Y, et al. Innovative adjuvant strategies for next-generation pertussis vaccines. *Hum Vaccin Immunother*. 2025;21(1):2545636. doi:10.1080/21645515.2025.2545636
30. Centers for Disease Control and Prevention. Treatment of pertussis and postexposure antimicrobial prophylaxis. Accessed May 9, 2026. https://www.cdc.gov/pertussis/hcp/clinical-care/index.html

## Tables

**Table 1. Key Model Components and Interpretation.**

| Component | Role in analysis | Source or assumption | Uncertainty propagated? | Interpretation |
| --- | --- | --- | --- | --- |
| Transmission rate \(\beta_S\) | Calibrated country-specific parameter | Reported-incidence series and literature-informed prior | Yes, conditional beta-grid intervals | Anchors overall reported-incidence level |
| Reporting multiplier and age reporting probabilities | Calibrated or penalized observation-model parameters | Broad literature-informed reporting bands | Partly; varied in reporting and selected-parameter diagnostics | Converts infections to reported cases; not a direct burden measure |
| Contact matrix \(C_{ij}\) | Fixed country mixing input | Prem/contactdata matrices aggregated to 8 model age groups | Partly; infant-contact multipliers and stochastic toy model | Defines age mixing and infant exposure routes |
| Vaccine symptom protection | Fixed or scenario-defined mechanism | Literature-informed aP-like profile and mechanism scenarios | Partly; mechanism thresholds and selected-parameter diagnostics | Represents clinical protection given infection |
| Vaccine infectiousness and duration effects | Scenario-defined mechanism | Hypothetical transmission-blocking profiles and product-target assumptions | No full structural propagation | Represents onward transmission blocking rather than clinical efficacy alone |
| Resistant-strain fitness | Sensitivity or scenario parameter | Assumed grid, \(f_R=0.70-1.25\), with hindcast plausibility checks | No in primary intervals | Major determinant of resistant-fraction trajectories |
| Treatment and PEP effectiveness | Scenario and sensitivity parameters | Standard macrolide and resistance-guided management assumptions | No in primary intervals; varied in implementation checks | Drives management benefit and resistant-strain selection pressure |
| Infant incidence | Model-generated endpoint | Not directly calibrated to age-specific observed incidence | No external calibration | Primary comparative endpoint, not a validated national forecast |

## Figure Legends

**Figure 1. International Context, Country Selection, and Baseline Heterogeneity.** (A) WHO regional reported pertussis incidence for context, not global representativeness. (B) Country profile dimensions. (C) Observed vs modeled annual reported incidence; dashed line indicates equality and color indicates resistant infection fraction. (D) Baseline all infections, reported cases, and infant cases per 100,000 on log scale. Conditional beta-grid intervals are not full structural or implementation uncertainty.

**Figure 2. Vaccine Mechanism Scenarios.** (A) VE_sus, VE_sym, VE_inf, and VE_dur values for 5 profiles. (B) Infant-case burden by vaccine scenario and country. (C) Vaccine-history origin decomposition by profile. (D) All-infection burden by vaccine scenario and country. Panels B and D show country points, cross-country medians, and empirical intervals.

**Figure 3. Macrolide Resistance and Vaccine Transmission Blocking.** (A) Five-year resistant-fraction dynamics by country. (B) Fitness-dependent resistant-fraction dynamics for \(f_R=0.85-1.15\). (C) Infant burden across resistance scenarios. (D) End-period resistant fraction by \(f_R\) and VE_inf. (E) Infant disease burden by \(f_R\) and VE_inf on log10 scale. (F) Transmission-blocking benefit by country at 3 fitness levels.

**Figure 4. Scenario Projections by Intervention Category.** Scenarios are grouped by interpretability rather than ordered as mutually substitutable policy options. (A) Infant-case burden by scenario and country; points are countries, with cross-country medians and empirical intervals. Current practice is the status quo baseline comparator and is grouped with current-program modifications, including higher child coverage and adolescent boosting; other scenarios are grouped as implementation-dependent proxy or management scenarios and hypothetical product-target or stress-test scenarios. (B) Within-country percentage infant-case reduction vs current practice; cell text gives the point estimate and conditional 95% interval. (C) Median burden across infant cases, reported cases, and all infections, showing outcome-dependent scenario contrasts. (D) Baseline infant case incidence with conditional beta-grid intervals. Conditional intervals are not full structural or implementation uncertainty.
