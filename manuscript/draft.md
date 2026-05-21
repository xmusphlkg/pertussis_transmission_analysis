# Pertussis Vaccine Transmission Blocking, Macrolide Resistance, and Projected Infant Burden: A Decision Analytical Model

**Article type:** Original Investigation; Decision Analytical Model

**Target journal:** JAMA Network Open

**Authors:** Kangguo Li, Yulun Xie, Yunzhi Zenghuang, Tao Chen, Sha Chen, Yue He, Tianmu Chen

**Affiliations:** State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine Laboratory, National Innovation Platform for Industry-Education Integration in Vaccine Research, School of Public Health, Xiamen University, Xiamen, China

**Manuscript word count:** 2934

## Key Points

**Question:** How do vaccine transmission-blocking assumptions and macrolide resistance alter projected infant pertussis burden and conditional scenario ordering?

**Findings:** In this decision analytical model of 10 purposively selected country profiles, projected infant-case reductions were larger for resistance-guided treatment and a maternal-plus-household proxy package, not passive maternal antibody protection alone, than for marginal child-coverage increases. Hypothetical upper-bound high-transmission-blocking product-target scenarios had the largest reductions; scenario ordering remained conditional on mechanism, reporting, and resistance assumptions.

**Meaning:** Pertussis decision models should separate clinical protection from transmission blocking and report resistance-aware treatment assumptions, calibration checks, and uncertainty explicitly.

## Abstract

**Importance:** Pertussis persists despite high acellular pertussis vaccine coverage, and macrolide-resistant *Bordetella pertussis* is spreading internationally. Models that combine symptom protection with transmission blocking may misrepresent projected scenario ordering.

**Objective:** To evaluate how vaccine transmission-blocking assumptions and macrolide resistance alter projected infant burden and conditional scenario ordering.

**Design:** A decision analytical model used a deterministic age-structured framework with 8 age groups, 2 strain classes, dose-history immunity, contact matrices, and sensitivity analyses. Simulations used a 15-year burn-in and a 26-year horizon beginning January 1, 2025.

**Setting and Data Sources:** Ten purposively selected country profiles used population, immunization, contact, surveillance, and resistance evidence accessed through May 9, 2026.

**Exposures:** Vaccine mechanism profiles, resistance prevalence assumptions, and intervention scenarios, including coverage increases, boosting, a maternal-plus-household proxy package (pregnancy vaccination plus adult/household transmission-reduction proxies), resistance-guided treatment, hypothetical upper-bound high-transmission-blocking vaccination, and combined intervention.

**Main Outcomes and Measures:** Annualized infant symptomatic cases, all incident infections, reported cases, resistant-strain incident infections, resistant fraction, and relative reductions.

**Results:** Within calibrated country-profile scenarios, baseline annualized infant case incidence ranged from 17 per 100,000 infants in Thailand to 2,574 per 100,000 infants in Australia. Calibration checks showed close agreement in mean reported incidence but variable peak-magnitude agreement, supporting scenario comparison rather than outbreak forecasting. Compared with no vaccination, profiles with stronger transmission blocking had larger projected infant-case reductions than the symptom-protective profile. Compared with current practice, the maternal-plus-household proxy package and resistance-guided treatment were associated with moderate projected infant-case reductions of approximately 40%, whereas hypothetical upper-bound vaccine-containing scenarios had reductions greater than 95%. Higher child coverage yielded no consistent median infant-case reduction and should not be interpreted as evidence against routine childhood coverage. Resistance trajectories were conditional on resistant-fitness, treatment, and PEP assumptions.

**Conclusions and Relevance:** In this deterministic scenario-analysis model of 10 purposively selected country profiles, projected infant pertussis burden and scenario ordering were highly sensitive to assumptions about vaccine effects on infection, onward transmission, and macrolide-resistant strain dynamics. These findings should be interpreted as conditional mechanism-focused scenario comparisons rather than national forecasts, cost-effectiveness estimates, or complete policy recommendations.

## Introduction

Pertussis has resurged internationally in the post-pandemic period, with China reporting a 65-fold increase in cases between 2023 and 2024, Japan recording over 60,000 cases in the first 7 months of 2025, and South Korea reporting a greater than 20-fold increase.^1-5,34^ These outbreaks occurred despite high primary vaccination coverage (94%-97% DTP3), underscoring that acellular pertussis (aP) vaccines, while effective against severe disease, provide incomplete and waning protection against infection and onward transmission.^6-12^

The distinction between clinical protection and transmission blocking has become operationally important. Nonhuman primate studies demonstrate that aP-vaccinated animals develop reduced symptoms but remain colonized and transmit *B pertussis* to naive contacts.^8^ Epidemiologic modeling and meta-analyses confirm that aP-derived protection against infection wanes substantially within 3 to 5 years, while protection against severe disease persists longer.^9-12^ This mechanistic gap means that high routine coverage may reduce disease burden without proportionally reducing circulation, leaving infants—who are too young for complete vaccination—exposed through household and community transmission from older age groups.

Simultaneously, macrolide-resistant *B pertussis* (MRBP) has emerged as an international concern. The MT28-ptxP3 clone carrying the 23S rRNA A2047G mutation escalated from less than 50% prevalence in China before 2020 to near-complete predominance (>99%) by 2024, and has since been reported in Japan, Australia, the Americas, and Europe.^13-20,32^ Genomic surveillance links resistance to the A2047G mutation and to vaccine-era genomic changes including ptxP3 predominance and pertactin deficiency.^17,18,32^ This rapid dissemination without an obvious fitness cost challenges the assumption that resistant strains carry a transmission disadvantage and raises the prospect that macrolide treatment and postexposure prophylaxis (PEP)—standard first-line interventions—may become progressively less effective.

Most pertussis policy models report vaccine effectiveness as a single composite endpoint and do not explicitly model how transmission-blocking properties interact with antimicrobial resistance to shape projected scenario ordering. We therefore used 10 purposively selected country profiles as contrasting policy-relevant scenarios, not as a representative global sample, to evaluate how alternative vaccine-mechanism and resistance assumptions alter projected infant burden and conditional intervention-scenario ordering.

## Methods

### Design and Data Sources

This decision analytical model synthesized demographic, surveillance, immunization, contact, treatment, and resistance evidence in a deterministic age-structured pertussis transmission framework. It was designed to compare conditional epidemiologic scenario orderings, not to forecast national epidemics or estimate cost-effectiveness, feasibility, equity, or a complete policy appraisal. The analysis was reported in accordance with relevant non-cost elements of CHEERS 2022, an EQUATOR reporting guideline, and WHO immunization-modeling guidance.^21,22^ Because only aggregated public data and simulated populations were used, institutional review board review was not applicable.

Ten purposively selected country profiles were analyzed: Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, the United Kingdom, and the United States. Countries were selected to maximize contrast in programmatic and resistance assumptions, not to estimate region-level or global averages. Inputs included United Nations World Population Prospects 2024 denominators, WHO/UNICEF and national immunization records, Prem/contactdata all-setting contact matrices aggregated to 8 age groups with reciprocity correction, harmonized surveillance intervals, and resistance evidence accessed through May 9, 2026.^23-26^ Country-selection rationale and data-quality dimensions are reported in eTable 15.

### Model Structure and Calibration

The model tracked 8 age groups, 2 strains, and susceptible origin histories reflecting maternal protection and recent or waned dose histories. Four vaccine mechanism parameters were represented separately: VE_sus, reduced susceptibility to infection; VE_sym, reduced symptoms given infection; VE_inf, reduced onward infectiousness; and VE_dur, shortened infectious duration. Immunity followed a SIRWS structure with immune boosting, waning from recovered to partially immune status over approximately 5 years, and return to susceptibility over approximately 10 years.^6,7^ Transmission used country-specific contact matrices, seasonality, aging and birth turnover, vaccination maintenance, importation, COVID-19 non-pharmaceutical intervention (NPI) contact reductions, treatment, and PEP. The complete equations, compartment diagram, transition table, vaccination schedule implementation, and parameter classification are provided in the Supplement and Table 1.

Calibration targeted reported pertussis case counts over the 6 most recent observed calendar years in each harmonized surveillance series, except South Africa, where 3 overlapping years were available. The retained fit minimized a negative-binomial reporting-interval likelihood plus penalties for age-specific reporting probabilities outside literature-informed bounds. Model-data checks included observed-vs-modeled reporting intervals, reporting probabilities, fit scores, mean absolute percentage errors, peak timing errors, and peak magnitude ratios (Figure 1, eFigure 4, eTable 16, and eTable 19). Consistent age-specific observed incidence series were not available across all 10 profiles, so age-specific incidence was not a calibration target. The 2024-2025 resurgence records were used as inputs when present, not held-out validation data; resistance hindcasts were treated as plausibility checks.

Calibrated parameters included country-specific transmission \(\beta_S\) and reporting multipliers, with age-specific reporting probabilities constrained by broad prior bands; natural-history, contact, vaccine-mechanism, and resistance parameters were fixed or varied in prespecified scenarios and sensitivity analyses. Because infant incidence was not directly calibrated, infant outcomes are internally consistent scenario endpoints generated by the age-structured model rather than externally validated infant forecasts. Credibility checks relied on overall reported-incidence fit, fitted infant reporting gradients within prior bounds, separate 0-2 month and 3-11 month model strata, infant-contact sensitivity, age-shift diagnostics, and infant-age-stratified intervention-window diagnostics (eTables 16, 21, 23, 30, and 31). Consistent country-specific hospitalization or severity series were not available for formal calibration.

### Scenarios and Outcomes

Five vaccine profiles were compared: no vaccine, symptom-protective aP-like protection, infection-blocking protection, transmission-blocking protection, and a hypothetical upper-bound high-transmission-blocking profile motivated by mucosal-immunity product targets rather than an available vaccine.^27,33^ Resistance scenarios used country-specific timelines or fixed low-to-very-high resistant prevalence, then allowed resistant dynamics to depend on importation, relative fitness, treatment shortening, strain-specific PEP effectiveness, and age/contact transmission.

Interventions included higher child coverage, adolescent boosting, pregnancy vaccination plus adult/household transmission-reduction proxies, resistance-guided treatment, the hypothetical upper-bound high-transmission-blocking vaccine profile, and a combined strategy.^29^ The intervention set intentionally mixed available or near-available levers, implementation-dependent proxy packages, and a hypothetical product-target vaccine scenario rather than a single menu of directly substitutable policies. After first definition, the pregnancy vaccination plus adult/household transmission-reduction proxies scenario is referred to as the maternal-plus-household proxy package. This package combined passive newborn antibody protection, a reproductive-age adult boosting proxy, and a cocooning contact modifier; decomposition runs isolated these components.

Infant outcomes combined the 0-2 month and 3-11 month age groups, with the 2 strata retained separately for reporting-probability, age-shift, and intervention-window diagnostics. Symptomatic cases were incident infections after VE_sym modification; reported cases applied age- and country-specific reporting probabilities; all infections included incident symptomatic and asymptomatic infections; resistant infections were incident infections caused by the resistant strain. Annualized outcomes were averaged over the 26-year saved analysis horizon unless otherwise specified. Relative reduction was defined as \(1-Z/Z_0\).

### Sensitivity Analysis

Sensitivity analyses included vaccine-mechanism thresholds, resistant-fitness grids, reporting assumptions, resistance-mechanism decomposition, treatment and PEP implementation scenarios, infant contact-matrix multipliers, burn-in and COVID-19 NPI temporal assumptions, higher child-coverage mechanism diagnostics, intervention orderings across analysis windows and infant strata, rank-stability summaries, event-scale diagnostics, joint probabilistic sensitivity analysis (PSA) rank acceptability, a contactdata setting-specific stochastic toy model, exploratory QALY-like burden translation, and vaccine-pipeline mapping. A 48-run Latin-hypercube analysis used Pearson, Spearman, and partial-rank correlations as exploratory parameter-screening diagnostics, not variance decomposition. Conditional Bayesian posterior predictive intervals propagated transmission-rate uncertainty over an adaptive log-\(\beta_S\) grid with nuisance parameters fixed; Figure 4B intervals are approximate predictive intervals, not full intervention posterior uncertainty.

## Results

### Baseline Country Heterogeneity

The 10 calibrated country-profile scenarios produced wide variation in projected burden under current aP-like vaccination and country-specific resistance anchors (Figure 1). Modeled mean annual reported incidence differed from observed incidence by a median of 3.4% (IQR, 1.7%-4.1%; range, 0.4%-13.7%). Interval-level diagnostics showed median mean absolute percentage error of 5.4% across overall calibration windows, median absolute peak-timing error of 1 year, and variable peak-magnitude ratios, underscoring that the fits support scenario comparison rather than outbreak forecasting (eTable 19). Within these calibrated profiles, annualized infant case incidence ranged from 17 per 100,000 infants in Thailand to 2,574 in Australia, all-infection incidence from 38 to 3,080 per 100,000 persons, and reported incidence from 1 to 47 per 100,000 persons. Near-term checks showed sensitivity to burn-in duration and, in Australia, NPI contact-shock magnitude (eTable 29).

### Vaccine Mechanism Scenarios

Vaccine profiles with stronger infection or transmission effects yielded progressively lower projected infant and population burden (Figure 2). Compared with no vaccination, the symptom-protective aP-like profile was associated with an 81.6% projected infant-case reduction, whereas infection-blocking and hypothetical upper-bound high-transmission-blocking profiles reduced residual infant burden to near-zero levels in several profiles. All-infection outcomes followed the same ordering. Vaccine-history decomposition showed that infections under the current aP-like profile remained concentrated in dose-3-or-more and waned histories, whereas residual infections under the upper-bound profile were more concentrated in unvaccinated histories. Threshold analyses suggested that VE_inf values near 0.40 to 0.50 were needed to cross selected infant-case reduction or comparator thresholds when other vaccine mechanisms were held fixed (eTable 18 and eTable 27).

### Macrolide Resistance and Transmission-Blocking Interaction

Resistant infection burden was sensitive to initial resistance prevalence, treatment pressure, PEP effectiveness, resistant-strain fitness, and vaccine infectiousness effects (Figure 3). Under neutral-fitness country-timeline assumptions, the median resistant fraction increased from 1.0% to 99.6%. Mechanism decomposition suggested that ongoing resistant importation was not the main driver of high end fractions, whereas equalizing PEP effectiveness lowered the median end resistant fraction to 12.2%, equalizing both treatment and PEP effects lowered it to 1.0%, and imposing \(f_R = 0.85\) lowered it to 0.01% (eTable 17). Together, these decompositions indicated that resistant fitness and treatment/PEP differentials, especially PEP effectiveness in these runs, explained most divergence in end-period resistant fraction; importation mainly affected persistence and timing rather than the direction of selection. Because PEP assumptions were influential in these decomposition runs, resistant-fraction projections should be interpreted as stress tests of plausible selection mechanisms conditional on prophylaxis reach, timing, and strain-specific effectiveness rather than predictions of inevitable replacement. In the resistant-fitness grid, the median end resistant fraction was 0.2% with \(f_R = 0.85\), 98.5% with \(f_R = 1.00\), and 99.9% with \(f_R = 1.15\). Hindcast plausibility checks did not rule out neutral or above-neutral fitness in Australia, Japan, and China. Increasing VE_inf from 0.05 to 0.55 was associated with lower projected infant burden across fitness assumptions, but the magnitude was fitness-dependent.

### Projected Intervention Scenario Ordering

Median intervention scenario ordering was heterogeneous and conditional on resistance-fitness, reporting, and vaccine-infectiousness assumptions (Figure 4). Current practice had median annualized infant case incidence of 358 per 100,000 infants/year. Higher child coverage alone yielded no consistent median infant-case reduction in these already high-coverage profiles (-4.1%; IQR, -4.8% to -3.1%). Mechanism diagnostics suggested small age-shift and waning-immunity composition changes under specified assumptions; this unstable model response should not be interpreted as evidence against maintaining high routine childhood coverage, which remained a prerequisite baseline assumption in these scenarios (eTables 22, 23, and 28). Adolescent boosting was associated with a small median projected reduction (1.9%; IQR, -0.2% to 58.9%).

The maternal-plus-household proxy package was associated with a projected 43.1% infant-case reduction, but decomposition attributed a median 5.5% reduction to direct antibody protection alone, 34.5% to the reproductive-age adult boosting proxy, and 6.4% to cocooning. Thus, the package estimate should not be interpreted as passive maternal antibody protection alone. Infant contact-matrix sensitivity confirmed that adult-to-infant contact assumptions influenced absolute infant burden (eTable 21). Resistance-guided treatment was associated with projected reductions of 40.7% for infant cases and 96.9% for resistant infections in the main implementation scenario, but near-term implementation checks showed dependence on uptake, testing reach, PEP restoration, and PEP reach (eTable 20).

The hypothetical upper-bound high-transmission-blocking vaccine and combined scenarios were associated with projected infant-case reductions greater than 95%; the upper-bound vaccine scenario represents a product target rather than an available intervention. Near-term analysis-window checks (2025-2029, 2025-2034, 2025-2039, and full horizon) retained the largest point-estimate reductions for combined and hypothetical upper-bound vaccine-containing scenarios but changed the ordering of maternal-plus-household, adolescent-booster, and resistance-guided-treatment scenarios (eTable 25). Infant-age-stratified diagnostics showed additional variation between the 0-2 month and 3-11 month strata, especially in near-term windows (eTables 30 and 31). Across 100 country-window-infant-age cells, the combined strategy ranked first in 78 and top 2 in 97, while the upper-bound vaccine ranked top 2 in 95; maternal-plus-household and resistance-guided treatment had positive reductions in 94 and 92 cells, respectively, but were rarely first (eTable 33). Event-scale diagnostics identified low-event near-elimination cells in upper-bound vaccine-containing scenarios, supporting interpretation of near-zero deterministic burdens as low-burden thresholds rather than stochastic elimination probabilities (eTable 34). In an exploratory 128-draw joint PSA used as a rank-stability diagnostic, the combined strategy ranked first in 69.5% of pooled country draws and top 2 in 100%, while the hypothetical upper-bound vaccine ranked first in 30.5% and top 2 in 99.6%; the upper-bound vaccine had the highest first-rank probability in Australia, New Zealand, Sweden, and the United States (eTables 37 and 38). Exploratory QALY-like translation and a contactdata setting-specific stochastic toy model added context without converting the analysis into cost-effectiveness or stochastic elimination inference (eTables 36, 39, and 40). The largest screening correlations with infant cases were asymptomatic infectious duration, relative asymptomatic infectiousness, and resistance fitness (eTable 26).

## Discussion

In this decision analytical model using 10 purposively selected country profiles, projected infant pertussis burden and intervention scenario ordering varied according to vaccine-mechanism and macrolide-resistance assumptions. Scenarios representing reduced onward transmission, direct infant protection, or restored modeled effectiveness against resistant infections had lower modeled infant burden than marginal child-coverage increases in already high-coverage profiles. These findings should be interpreted as conditional scenario comparisons, not as national forecasts, global estimates, or complete policy appraisals.

The distinction between clinical protection and transmission blocking had quantifiable consequences. A symptom-protective aP-like profile was associated with lower projected infant cases than no vaccination, but stronger transmission-blocking profiles were associated with larger projected decreases in infant cases and total infections. This is consistent with evidence that aP vaccination prevents disease more strongly than colonization or transmission,^8^ and suggests that models using a single composite vaccine-effectiveness parameter may underestimate the hypothetical upper-bound projected benefit of vaccines designed to reduce onward transmission.^27,33^

Resistance-guided treatment had projected benefit under the main implementation assumptions, aligning with guidance emphasizing susceptibility testing and alternative treatment when resistance is suspected or confirmed.^15,16,29^ However, near-term implementation scenarios showed that projected benefit depended on uptake, testing reach, and PEP assumptions; real-world benefit would depend on testing availability, turnaround time, clinician suspicion, adherence, alternative-drug tolerability, and public health capacity.

The projected increase in resistant fraction should be read as conditional rather than deterministic. Hindcast plausibility checks did not rule out neutral or above-neutral fitness in China, Japan, and Australia, but the fitness-cost counterfactual produced different dynamics. Mechanism-decomposition scenarios distinguished importation, treatment-selection, PEP-selection, and intrinsic-fitness assumptions. Because PEP assumptions strongly influenced resistant-fraction trajectories, these projections should be interpreted as conditional on prophylaxis reach, timing, and strain-specific effectiveness rather than as unconditional predictions of resistant-strain replacement.

Intervention scenario ordering depended on the interaction between vaccine mechanism and resistance. Higher child coverage alone was not associated with a consistent median projected infant-case reduction, and age-shift diagnostics suggested that the small modeled increase was not a robust policy signal or evidence against maintaining high coverage. The maternal-plus-household proxy package requires careful interpretation because the adult-boosting component should not be attributed to passive transplacental antibody protection alone, and infant-contact sensitivity analyses indicate that household-like contact assumptions remain important for infant outcomes.

These findings should be interpreted in the context of international pertussis resurgence and genomic evidence of macrolide-resistant clone spread.^3,4,17,32^ A recent multi-country model similarly identified waning aP immunity and incomplete transmission blocking as key drivers of resurgence, though without explicitly modeling resistance interactions.^28^

### Limitations

This analysis has limitations. Structural limitations include deterministic compartmental dynamics without stochastic extinction, explicit household clustering, contact tracing, adherence, or superspreading. Deterministic event-scale diagnostics, infant contact-matrix sensitivity, treatment-implementation sensitivity, and the individual stochastic toy model probe parts of these limitations, but do not replace calibrated stochastic household or contact-tracing models. Immunity waning and boosting are simplified compartmental transitions, and near-term burn-in and COVID-19 NPI checks showed temporal-assumption sensitivity, especially for current-practice burden.

Data and calibration limitations include sparse age- and country-specific reporting probabilities,^30,31^ lack of consistent age-specific observed incidence targets, heterogeneous resistance anchors, and variable peak-magnitude agreement in calibration diagnostics. Cross-country contrasts should therefore be interpreted as conditional scenario comparisons rather than national forecasts or global estimates, and resistance scenarios remain stress tests.

Interpretation limitations include the use of age-structured proxies rather than explicit pregnant-person or household compartments for the maternal-plus-household proxy package. The upper-bound high-transmission-blocking vaccine profile is a hypothetical product target, not an available option; intranasal BPZE1, OMV-based platforms, genetically detoxified recombinant acellular vaccines, and new multicomponent aP candidates were therefore mapped to mechanism profiles rather than modeled as licensed policy options (eTable 41). Joint PSA rank acceptability varied selected parameters but did not propagate all structural uncertainty, and exploratory QALY-like translations did not include costs, discounting, age weighting, or formal decision thresholds. Despite these limitations, the qualitative conclusion that transmission-blocking and resistance-aware management assumptions materially altered scenario ordering was consistent across multiple diagnostic analyses. A limitation-to-diagnostic map summarizes which concerns were probed and which remain structural (eTable 35).

## Conclusions

Across 10 purposively selected country profiles, deterministic scenario-based projections of infant pertussis burden and intervention scenario ordering were sensitive to assumptions about vaccine effects on infection and onward transmission and to macrolide-resistant strain dynamics. Decision analyses for pertussis should report infant burden, total infections, and resistant infections separately, distinguish clinical protection from effects on onward transmission, and incorporate resistance-aware treatment assumptions.

## Supplement

**Supplement 1.** eMethods (full model equations, country-profile construction, calibration methods, scenario definitions, resistance hindcast plausibility checks, parameter identifiability classification), eReferences, eFigures 1-13, and eTables 1-42.

## Article Information

**Previous Presentation:** None.

**Corresponding Author:** Tianmu Chen, PhD, State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine Laboratory, National Innovation Platform for Industry-Education Integration in Vaccine Research, School of Public Health, Xiamen University, Xiamen, China (chentianmu@xmu.edu.cn).

**Author Contributions:** Kangguo Li and Tianmu Chen had full access to all data and code in the study and take responsibility for the integrity of the data and the accuracy of the analysis. Concept and design: Kangguo Li. Acquisition, analysis, or interpretation of data: Yulun Xie, Yunzhi Zenghuang, Tao Chen, Sha Chen, and Yue He. Drafting of the manuscript: Kangguo Li and Yulun Xie. Critical revision of the manuscript for important intellectual content: Kangguo Li. Statistical analysis: Kangguo Li. Administrative, technical, or material support: Kangguo Li and Tianmu Chen. Supervision: Tianmu Chen.

**Reporting Guideline:** Relevant non-cost elements of CHEERS 2022 and WHO immunization-modeling guidance were followed; model equations, parameter classification, calibration diagnostics, and sensitivity analyses are provided in the Supplement.

**Conflict of Interest Disclosures:** The authors have no conflicts of interest to disclose.

**Funding/Support:** This work was supported by the National Natural Science Foundation of China (825B2104 to Kangguo Li), and the National Key Research and Development Program of China (2024YFC2311404 to Tianmu Chen).

**Role of the Funder/Sponsor:** The funders had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.

**Data Sharing Statement:** Publicly available processed inputs, model code, configuration files, and generated outputs are available in a public repository at https://github.com/xmusphlkg/pertussis_transmission_analysis. No individual-level participant data were used.

**Additional Contributions:** None.

**Use of Artificial Intelligence:** AI-assisted drafting and code-assistance tools (Codex, OpenAI; used in May 2026) were used for language organization, code assistance, and implementation checks. They were not used to generate data, make autonomous analytic decisions, or replace author verification. The authors reviewed and edited all AI-assisted content and take full responsibility for the integrity of the final manuscript.

## References

1. World Health Organization. Pertussis vaccines: WHO position paper, August 2015. *Wkly Epidemiol Rec*. 2015;90:433-458.
2. Cai J, Liu Q, Chen B, et al. Waning immunity, prevailing non-vaccine type ptxP3 and macrolide-resistant strains in the 2024 pertussis outbreak in China: a multicentre cross-sectional descriptive study. *Lancet Reg Health West Pac*. 2025;60:101628. doi:10.1016/j.lanwpc.2025.101628
3. Ai X, Mori H, Krokva D, et al. Pertussis resurgence after the COVID-19 pandemic in four Western Pacific countries and the USA, highlighting the 2025 outbreak in Japan. *Sci Rep*. Published online April 18, 2026. doi:10.1038/s41598-026-47780-4
4. Akhmetzhanov AR, de Padua B, Dushoff J. Serial interval and intervention efficiency in pertussis outbreak, South Korea, 2024. *Emerg Infect Dis*. 2026;32(5):809-811. doi:10.3201/eid3205.251304
5. Zhang S, Xu Y, Xiao Y. Revisiting whooping cough: global drivers and implications of pertussis resurgence in the acellular vaccine era. *Vaccines (Basel)*. 2026;14(1):35. doi:10.3390/vaccines14010035
6. Wearing HJ, Rohani P. Estimating the duration of pertussis immunity using epidemiological signatures. *PLoS Pathog*. 2009;5:e1000647. doi:10.1371/journal.ppat.1000647
7. Lavine JS, King AA, Bjornstad ON. Natural immune boosting in pertussis dynamics and the potential for long-term vaccine failure. *Proc Natl Acad Sci U S A*. 2011;108:7259-7264. doi:10.1073/pnas.1014394108
8. Warfel JM, Zimmerman LI, Merkel TJ. Acellular pertussis vaccines protect against disease but fail to prevent infection and transmission in a nonhuman primate model. *Proc Natl Acad Sci U S A*. 2014;111:787-792. doi:10.1073/pnas.1314688110
9. Klein NP, Bartlett J, Rowhani-Rahbar A, Fireman B, Baxter R. Waning protection after fifth dose of acellular pertussis vaccine in children. *N Engl J Med*. 2012;367:1012-1019. doi:10.1056/NEJMoa1200850
10. McGirr A, Fisman DN. Duration of pertussis immunity after DTaP immunization: a meta-analysis. *Pediatrics*. 2015;135:331-343. doi:10.1542/peds.2014-1729
11. Chit A, Zivaripiran H, Shin T, et al. Acellular pertussis vaccines effectiveness over time: a systematic review, meta-analysis and modeling study. *PLoS One*. 2018;13:e0197970. doi:10.1371/journal.pone.0197970
12. Domenech de Cellès M, Magpantay FMG, King AA, Rohani P. The impact of past vaccination coverage and immunity on pertussis resurgence. *Sci Transl Med*. 2018;10:eaaj1748. doi:10.1126/scitranslmed.aaj1748
13. Althouse BM, Scarpino SV. Asymptomatic transmission and the resurgence of *Bordetella pertussis*. *BMC Med*. 2015;13:146. doi:10.1186/s12916-015-0382-8
14. Fu P, Zhou J, Yang C, et al. Molecular evolution and increasing macrolide resistance of *Bordetella pertussis*, Shanghai, China, 2016-2022. *Emerg Infect Dis*. 2024;30:117-127. doi:10.3201/eid3001.221588
15. Centers for Disease Control and Prevention. Antibiotic-resistant *Bordetella pertussis*. Accessed May 9, 2026. https://www.cdc.gov/pertussis/hcp/antibiotic-resistance/index.html
16. Pan American Health Organization. PAHO calls for strengthened vaccination and surveillance amid the spread of antibiotic-resistant pertussis in the Americas. August 26, 2025. https://www.paho.org/en/news/26-8-2025-paho-calls-strengthened-vaccination-and-surveillance-amid-spread-antibiotic
17. Xu Z, Huang Z, Yuan L, et al. Genomic surveillance reveals global spread of macrolide-resistant *Bordetella pertussis* linked to vaccine changes. *J Clin Microbiol*. 2025;63(12):e01064-25. doi:10.1128/jcm.01064-25
18. Fong W, Rockett RJ, Tam KKG, et al. Characterisation of *Bordetella pertussis* virulence and macrolide resistance in Australia by targeted culture-independent sequencing: a genomic epidemiology study. *Lancet Microbe*. 2026;7(3):101286. doi:10.1016/j.lanmic.2025.101286
19. Komatsu S, Nakanishi N, Matsubara K, et al. Molecular analysis of emerging MT27 macrolide-resistant *Bordetella pertussis*, Kobe, Japan, 2025. *Emerg Infect Dis*. 2026;32:150-153. doi:10.3201/eid3201.250890
20. Obara T, Kano K, Yorifuji T, et al. Localized outbreak of macrolide-resistant pertussis in infants, Japan, March-May 2025. *Emerg Infect Dis*. 2026;32(1):158-161. doi:10.3201/eid3201.250824
21. Husereau D, Drummond M, Augustovski F, et al. Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) statement. *BMJ*. 2022;376:e067975. doi:10.1136/bmj-2021-067975
22. World Health Organization. Guidance for using modelling for immunization decision-making. Geneva: World Health Organization; 2026. Accessed May 9, 2026. https://iris.who.int/handle/10665/385083
23. United Nations Department of Economic and Social Affairs, Population Division. World Population Prospects 2024. Accessed May 9, 2026. https://population.un.org/wpp/
24. Prem K, Cook AR, Jit M. Projecting social contact matrices in 152 countries using contact surveys and demographic data. *PLoS Comput Biol*. 2017;13:e1005697. doi:10.1371/journal.pcbi.1005697
25. Amirthalingam G, Andrews N, Campbell H, et al. Effectiveness of maternal pertussis vaccination in England: an observational study. *Lancet*. 2014;384:1521-1528. doi:10.1016/S0140-6736(14)60686-3
26. Baxter R, Bartlett J, Fireman B, Lewis E, Klein NP. Effectiveness of vaccination during pregnancy to prevent infant pertussis. *Pediatrics*. 2017;139:e20164091. doi:10.1542/peds.2016-4091
27. da Silva Antunes R, Sette A. New life into pertussis prevention. *Nat Microbiol*. 2025;10:3045-3046. doi:10.1038/s41564-025-02169-3
28. Campbell PT, Choi YH, Gambhir M, McVernon J. Identifying drivers of pertussis disease resurgence pilot study: final report. *medRxiv*. 2025. doi:10.1101/2025.05.22.25328117
29. Centers for Disease Control and Prevention. Treatment of pertussis and postexposure antimicrobial prophylaxis. Accessed May 9, 2026. https://www.cdc.gov/pertussis/hcp/clinical-care/index.html
30. Clarkson JA, Fine PEM. The efficiency of measles and pertussis notification in England and Wales. *Int J Epidemiol*. 1985;14:153-168. doi:10.1093/ije/14.1.153
31. Crowcroft NS, Johnson C, Chen C, et al. Under-reporting of pertussis in Ontario. *PLoS One*. 2018;13:e0195984. doi:10.1371/journal.pone.0195984
32. Zhang H, Kang Z, Zhang Y, et al. Evolutionary dynamics and global spread of macrolide-resistant *Bordetella pertussis* during the post-pandemic pertussis resurgence. *J Infect*. 2026;92(4):106718. doi:10.1016/j.jinf.2026.106718
33. Yu G, Yang W, Ma Y, et al. Innovative adjuvant strategies for next-generation pertussis vaccines. *Hum Vaccin Immunother*. 2025;21(1):2545636. doi:10.1080/21645515.2025.2545636
34. Sheng Y, Ma S, Zhou Q, Xu J. Pertussis resurgence: epidemiological trends, pathogenic mechanisms, and preventive strategies. *Front Immunol*. 2025;16:1618883. doi:10.3389/fimmu.2025.1618883

## Tables

**Table 1. Key Model Parameter Groups and Their Roles.**

| Parameter group | Main values or range | Status in analysis | Principal role |
| --- | --- | --- | --- |
| Transmission \(\beta_S\) | Country-specific | Calibrated | Matches reported-incidence levels |
| Reporting multiplier and age reporting probabilities | Country-specific within prior bounds | Calibrated/penalized | Observation model only |
| Contact matrix \(C_{ij}\) | Country-specific 8-group matrix | Externally derived | Age mixing and infant exposure routes |
| Natural history | Latent 8 days; symptomatic infectious 21 days; asymptomatic infectious 14 days | Literature-informed fixed; sensitivity varied | Infection progression and duration |
| Waning and immune boosting | R-to-W 5 years; W-to-S 10 years; boosting efficiency 0.70 | Assumed; sensitivity varied | Immunity debt and recurrent dynamics |
| Vaccine mechanisms | VE_sus, VE_sym, VE_inf, VE_dur by profile | Scenario-defined | Direct protection and onward transmission |
| Treatment and PEP | Sensitive vs resistant effectiveness | Scenario-defined; sensitivity varied | Selection pressure and management benefit |
| Resistance anchors and fitness | Country timeline or 5%-95%; \(f_R=0.70-1.25\) | Externally anchored and scenario-defined | Resistant fraction and resistant burden |
| Importation | Country/scenario-specific low-level importation | Calibrated or assumed | Resistant persistence and reintroduction |

## Figure Legends

**Figure 1. International Context, Country Selection, and Baseline Heterogeneity.** (A) WHO regional reported pertussis incidence, establishing the surveillance backdrop for the 10-country set across 5 WHO regions without implying global representativeness. (B) Country selection basis showing profile dimensions (WHO region, population size, reported incidence, starting resistant fraction, and program signature). (C) Model-data reported incidence calibration: observed vs modeled annual reported incidence, with points colored by resistant infection fraction. Dashed line indicates equality. (D) Baseline burden metrics (all infections, reported cases, infant cases per 100,000) by country on log scale; conditional beta-grid posterior predictive intervals include transmission-rate uncertainty plus horizon-scaled stochastic observation/process dispersion.

**Figure 2. Vaccine Mechanism Scenarios.** (A) Vaccine scenario parameter matrix showing VE_sus, VE_sym, VE_inf, and VE_dur values for 5 profiles. (B) Infant-case burden by vaccine scenario and country, with cross-country medians and empirical intervals. (C) Vaccine-history origin decomposition by vaccine profile, showing how stronger profiles shift the origin composition of infections. (D) All-infection burden by vaccine scenario and country, with cross-country medians and empirical intervals.

**Figure 3. Macrolide Resistance and Vaccine Transmission Blocking.** (A) Resistant-fraction dynamics over 5 years by country under country-specific timelines. (B) Fitness-dependent resistant-fraction dynamics (median ± IQR) for fitness_R = 0.85-1.15. (C) Infant burden across resistance scenarios by country. (D) End-period resistant fraction heatmap (fitness × VE_inf). (E) Infant disease burden heatmap (fitness × VE_inf, log10 scale), showing projected infant burden across resistance-fitness and vaccine infectiousness assumptions. (F) Transmission-blocking benefit by country at 3 fitness levels.

**Figure 4. Projected Intervention Scenario Ordering.** (A) Infant-case burden by intervention and country, with individual country points, cross-country medians, and empirical intervals. (B) Country × strategy heatmap showing within-country percentage infant-case reduction vs current practice; cell text gives the point estimate followed by the approximate 95% PI. These approximate PIs should not be read as full posterior intervention uncertainty. (C) Median intervention burden across outcomes (infant cases, reported cases, all infections), comparing point-estimate scenario ordering across outcome measures. (D) Conditional beta-grid Bayesian posterior predictive intervals for baseline infant case incidence, with calibrated deterministic point estimates overlaid.
