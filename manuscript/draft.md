# Infant Pertussis Vaccination Prioritization With Transmission Blocking and Macrolide Resistance

**Article type:** Original Investigation

**Study type:** Decision Analytical Model

**Target journal:** JAMA Network Open

**Authors:** Kangguo Li, Yulun Xie, Yunzhi Zenghuang, Tao Chen, Sha Chen, Yue He, Tianmu Chen

**Affiliations:** State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine Laboratory, National Innovation Platform for Industry-Education Integration in Vaccine Research, School of Public Health, Xiamen University, Xiamen, China

**Manuscript word count:** 2705

## Key Points

**Question:** Which pertussis strategy characteristics were associated with lower modeled infant burden when routine vaccination, pregnancy Tdap, infant-exposure reduction, management modifiers, vaccine transmission blocking, and macrolide resistance were compared in a common decision framework?

**Findings:** In this decision analytical model of 10 illustrative country profiles, routine childhood coverage floors and adolescent boosting produced small or inconsistent additional infant-case reductions, pregnancy Tdap scale-up produced modest direct protection, and infant-exposure reduction, resistance-guided management, and high-transmission-blocking vaccine profiles produced larger modeled reductions. Resistance-guided management reduced resistant infections under specified assumptions but depended on testing reach, postexposure prophylaxis, and resistant-strain fitness.

**Meaning:** Model-informed pertussis prioritization for infant protection should separate foundational routine vaccination, direct pregnancy Tdap protection, exposure-reduction adjuncts, resistance-management modifiers, and hypothetical transmission-blocking vaccine targets rather than treating them as a single ranked policy list.

## Abstract

**Importance:** Young infants remain at greatest risk from pertussis because they are too young to have completed primary vaccination. Strategy comparisons are difficult in the acellular vaccine era because symptom prevention, transmission blocking, infant exposure, and macrolide-resistant *Bordetella pertussis* may affect infant outcomes through different pathways.

**Objective:** To compare model-informed pertussis strategy profiles for infant protection, distinguishing available program levers, infant-exposure strategies, management modifiers, and vaccine transmission-blocking product targets under macrolide-resistance assumptions.

**Design:** Deterministic age-structured decision analytical transmission-modeling study using a 15-year burn-in and a 26-year horizon beginning January 1, 2025.

**Setting:** Ten illustrative country profiles using evidence accessed through May 9, 2026.

**Participants:** No individual participants were included; analyses used population-level country profiles.

**Exposures:** Current practice; routine childhood coverage floors; adolescent booster scale-up; pregnancy Tdap scale-up; close-contact/cocooning adjuncts; targeted high-risk postexposure prophylaxis (PEP); resistance-guided management; hypothetical vaccine profiles with stronger transmission-blocking properties; and combined stress-test profiles.

**Main Outcomes and Measures:** Annualized infant symptomatic cases, all incident infections, reported cases, resistant-strain infections, resistant fraction, and relative reductions vs current practice.

**Results:** Across calibrated profiles, current-practice annual infant case incidence ranged from approximately 16 to 2393 per 100,000 infants; infant incidence was not directly calibrated and was interpreted as a comparative endpoint. Calibration-window mean absolute percentage error for reported cases was 5.5% (interquartile range [IQR], 3.9%-7.8%). Routine childhood coverage floors did not produce a consistent infant-case reduction (median, -1%; IQR, -5% to -1%), and adolescent boosting had a small and uncertain reduction (median, 2%; IQR, 0%-58%). Pregnancy Tdap scale-up produced a median 12% reduction (IQR, 10%-14%); the infant-exposure reduction composite produced a median 45% reduction (IQR, 25%-77%). Targeted high-risk PEP produced a smaller median reduction (5%), while resistance-guided management produced median reductions of 41% for infant cases and 97% for resistant infections under fixed implementation assumptions. High-transmission-blocking and combined stress-test profiles produced median reductions of 97% or higher.

**Conclusions and Relevance:** In this decision analytical modeling study, additional infant protection depended more on reducing infant exposure, improving transmission blocking, and addressing resistance-sensitive management than on marginal increases in already high childhood coverage. Results support strategy-profile prioritization, not formal optimization, country-specific rankings, or national forecasts.

## Introduction

Pertussis prevention programs are usually built on routine childhood vaccination, but the most severe burden remains concentrated in young infants who are not yet fully vaccinated.^1-3^ Infant protection therefore depends on several linked pathways: direct passive protection after pregnancy vaccination, reduced household or caregiver exposure, adolescent and adult transmission, treatment and PEP delivery, and broader population circulation.^4-6^ These pathways are not interchangeable for decision making.

Post-pandemic pertussis resurgence has reinforced this prioritization problem. High childhood coverage remains essential, yet acellular pertussis (aP) vaccines prevent symptomatic disease more reliably than infection or onward transmission, and protection against infection wanes over time.^7-13^ A model that represents vaccine effect as a single composite parameter may therefore overstate the value of strategies that prevent symptoms but do little to reduce infant exposure, or understate the value of vaccines and program designs that reduce transmission.

Macrolide-resistant *B pertussis* (MRBP) adds a management and interpretation challenge. Reports from China, the Americas, Australia, Japan, and global genomic analyses indicate that resistant lineages can expand and spread internationally.^14-21^ Resistance affects the expected value of treatment and PEP, but it should be interpreted as a modifier of vaccination strategy comparisons rather than as a replacement for the infant-protection question.

We used an age-structured decision analytical transmission model to compare pertussis strategy profiles for infant protection across 10 illustrative country settings. The analysis was designed around a policy question: which strategy characteristics are associated with lower modeled infant burden when routine program levers, pregnancy Tdap, infant-exposure reduction, management modifiers, and vaccine transmission-blocking product targets are placed in the same framework? The study was not a formal optimization, national forecast, or country-specific policy ranking.

## Methods

### Study Design and Decision Frame

This deterministic transmission-modeling study synthesized demographic, surveillance, immunization, contact, treatment, and resistance evidence in a common age-structured pertussis framework. Current practice was each profile's routine vaccination schedule and standard macrolide treatment/PEP assumptions. The analysis compared predefined strategy profiles under specified assumptions and did not estimate cost-effectiveness, feasibility, equity, budget impact, or a complete policy appraisal. Reporting followed relevant non-cost CHEERS 2022 elements and WHO immunization-modeling guidance.^22,23^ Institutional review board review was not applicable because no individual-level data were used.

Ten purposively selected profiles were analyzed: Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, the United Kingdom, and the United States. The profiles were chosen to span program, surveillance, contact, and resistance contrasts, not to estimate global or regional averages. Inputs included United Nations World Population Prospects 2024 denominators, WHO/UNICEF and national immunization records, Prem/contactdata contact matrices, harmonized surveillance intervals, pregnancy-vaccination evidence, and resistance evidence accessed through May 9, 2026.^24-27^ Selection rationale and data-quality dimensions are reported in <span style="color:#5DADE2;">eTable 1</span>.

### Model and Calibration

The model tracked 8 age groups, macrolide-sensitive and macrolide-resistant strains, and susceptible vaccine-origin histories reflecting maternal protection and recent or waned dose histories. Four vaccine mechanism parameters were represented separately: VE_sus, reduced susceptibility to infection; VE_sym, reduced symptoms given infection; VE_inf, reduced onward infectiousness; and VE_dur, shortened infectious duration. Immunity followed an SIRWS structure with immune boosting and waning.^7,8^ Transmission used country-specific contact matrices, seasonality, aging and birth turnover, vaccination maintenance, importation, COVID-19 non-pharmaceutical intervention contact reductions, treatment, and PEP. <span style="color:#5DADE2;">eTable 2</span> provides equations, parameter provenance, and source links.

Calibration targeted reported pertussis case counts over the 6 most recent observed calendar years in each surveillance series, except South Africa, where 3 overlapping years were available. The retained fit minimized a negative-binomial reporting-interval likelihood plus penalties for age-specific reporting probabilities outside broad prior bounds. Calibration diagnostics included observed-vs-modeled reporting intervals, fit scores, mean absolute percentage errors, peak timing, and reporting probabilities (<span style="color:#5DADE2;">eFigure 2B and 2D</span> and <span style="color:#5DADE2;">eTables 7 and 12</span>). Consistent age-specific observed incidence series were unavailable across all profiles, so infant incidence was not directly calibrated and was interpreted as an internally consistent comparative endpoint rather than an externally validated national estimate.

### Strategy Profiles

Strategy profiles were organized by decision role rather than as directly substitutable policies (<span style="color:#5DADE2;">Table 1</span>). Routine-program levers included current practice, routine childhood coverage floors, and adolescent booster scale-up. Infant-protection levers separated pregnancy Tdap scale-up for direct passive newborn protection, a close-contact/cocooning adjunct, and an infant-exposure reduction composite. Component diagnostics isolated pregnancy Tdap, reproductive-age adult boosting, and cocooning/contact reduction, so the composite should not be interpreted as a maternal-immunization-only effect estimate. Management modifiers included targeted high-risk PEP and resistance-guided treatment with restored resistant-strain management effects. Product-target profiles compared current aP-like vaccination with infection-blocking, transmission-blocking, and hypothetical high-transmission-blocking vaccine profiles motivated by upper-bound mucosal-immunity product targets rather than licensed products.^28,29^

Resistance analyses were tiered into country-specific starting-composition baselines, mechanistic stress tests varying resistant prevalence and fitness, and implementation-dependent resistance-management scenarios. Because the profile set mixed available program levers, implementation-dependent adjuncts, management modifiers, and hypothetical product targets, the results were interpreted as a prioritization pattern rather than a definitive ranking or formal optimization.^30^

The primary endpoint was annualized infant symptomatic cases over the 26-year saved horizon. Secondary outcomes included all infections, reported cases, resistant infections, resistant fraction, deaths, and infant deaths where available. Relative reduction was calculated as 1 - Z/Z0, where Z was the strategy outcome and Z0 was current practice.

### Sensitivity Analysis

Sensitivity analyses evaluated vaccine-mechanism thresholds, resistance-fitness grids, reporting assumptions, treatment and PEP implementation, infant contacts, maternal passive-protection duration, temporal windows, child-coverage mechanisms, strategy ordering, event scale, stochastic contact clustering, QALY-like translation, and vaccine-pipeline mapping. Conditional beta-grid intervals propagated transmission-rate uncertainty with nuisance parameters fixed; they are not confidence intervals and do not jointly propagate structural, contact-matrix, resistance-fitness, or implementation uncertainty.

## Results

### Calibration and Baseline Infant Burden

Across the 10 calibrated profiles, current-practice modeled annual infant case incidence ranged from approximately 16 per 100,000 infants in Thailand to 2393 in Australia (<span style="color:#5DADE2;">Figure 1D</span>). The fitted reported-case calibration-window target had mean absolute percentage error of 5.5% (IQR, 3.9%-7.8%; range, 1.2%-10.5%), with median absolute peak-timing error of 1 year (<span style="color:#5DADE2;">eTable 7</span>). Because infant incidence was not directly calibrated, absolute infant-burden estimates were treated as conditional scenario outputs; the main inferential target was comparison among strategy profiles.

### Strategy-Profile Prioritization

Strategy profiles showed a clear separation by decision role (<span style="color:#5DADE2;">Figure 4A-4C</span>). Routine childhood coverage floors did not produce a consistent infant-case reduction (median, -1%; IQR, -5% to -1%), and adolescent booster scale-up produced a small and uncertain reduction (median, 2%; IQR, 0%-58%). These results should not be read as evidence against maintaining high routine childhood vaccination. Rather, they indicate that once childhood coverage is already high, marginal coverage gains may be less informative for additional infant protection than strategies that reduce exposure or transmission.

Pregnancy Tdap scale-up produced a median 12% infant-case reduction (IQR, 10%-14%). The close-contact/cocooning adjunct produced a median 37% reduction, and the infant-exposure reduction composite produced a median 45% reduction (IQR, 25%-77%). Component diagnostics attributed median reductions of 12% to pregnancy Tdap alone, 35% to reproductive-age adult boosting, and 3% to cocooning/contact reduction alone, indicating that the composite should not be attributed to maternal immunization alone. Targeted high-risk PEP produced a median 5% reduction. Resistance-guided management produced median reductions of 41% for infant cases and 97% for resistant infections under fixed implementation assumptions, but was interpreted as a management modifier rather than a vaccination strategy rank. The high-transmission-blocking vaccine target and combined stress-test profiles produced median reductions of 97% or higher.

### Mechanistic Drivers

Vaccine profiles with stronger infection or transmission effects yielded progressively lower infant and population burden (<span style="color:#5DADE2;">Figure 2A, 2B, and 2D</span>). Compared with no vaccination, the symptom-protective aP-like profile produced an 82% simulated infant-case reduction, while infection-blocking, transmission-blocking, and high-transmission-blocking profiles reduced residual burden further. Threshold analyses suggested that VE_inf values near 0.35 to 0.50 were needed to cross selected infant-case reduction or comparator thresholds when other vaccine mechanisms were held fixed (<span style="color:#5DADE2;">eTable 14</span>). These findings explain why strategy profiles that reduced infant exposure or onward transmission outperformed marginal coverage changes.

### Macrolide Resistance as a Modifier

Resistance results were interpreted as starting-composition baselines, mechanistic stress tests, and implementation-dependent management scenarios (<span style="color:#5DADE2;">Figure 3A-3F</span>). In stress tests with country-timeline anchors plus strain-specific treatment and PEP differentials, the median end resistant fraction reached 99.7% from 1.0%; equalizing PEP effectiveness lowered it to 12%, equalizing both treatment and PEP effects lowered it to 1%, and imposing f_R = 0.85 lowered it to less than 0.1% (<span style="color:#5DADE2;">eTable 13</span>). Increasing VE_inf reduced infant burden across fitness assumptions, but resistant fraction remained highly dependent on resistant-strain fitness.

### Robustness

Infant-endpoint diagnostics supported the broad prioritization pattern but not precise country-specific rankings. In infant-contact sensitivity analyses, increasing child, adolescent, and adult sources into infant target groups from 0.75 to 1.50 changed current-practice 5-year median infant burden from 120 to 186 cases per 100,000 infants; the infant-exposure reduction strategy remained lower across the same multipliers (52 to 78 per 100,000 infants). Varying passive maternal protection from 90 to 270 days changed direct pregnancy Tdap 5-year reductions from 9% to 12% and the infant-exposure reduction strategy from 57% to 59% (<span style="color:#5DADE2;">eTable 17</span>). External age-pattern triangulation was mixed, with better agreement for the United States than for England, Sweden/EU/EEA, and Australia.^31-34^ Across analysis windows and selected-parameter sampling, combined and high-transmission-blocking profiles most often had the lowest infant burden, whereas infant-exposure reduction and resistance-guided management were not separable enough for precise ranking (<span style="color:#5DADE2;">eTables 19, 20, and 25</span>).

## Discussion

This decision analytical modeling study reframed pertussis vaccination analysis as an infant-protection prioritization problem. Across 10 illustrative profiles, routine childhood vaccination remained foundational, but marginal increases in already high childhood coverage were not the main source of additional modeled infant protection. Larger reductions were associated with strategy characteristics that reduced infant exposure, improved onward-transmission blocking, or modified resistant-strain management.

The strategy taxonomy is central to interpretation. Pregnancy Tdap scale-up represented direct passive protection and produced modest, consistent infant benefit. The infant-exposure reduction composite produced larger reductions, but those reductions reflected adult-boosting and contact assumptions as well as pregnancy Tdap; they should not be described as a maternal-immunization-only effect. Targeted high-risk PEP had smaller average benefit and should be read as outbreak or contact-management support, not a broad population-control strategy.

The model also clarifies why transmission blocking matters for prioritization. A symptom-protective aP-like profile reduced modeled infant cases compared with no vaccination, but stronger infection- and transmission-blocking profiles reduced residual infant burden and total infections further. This supports distinguishing vaccine protection against clinical disease from protection against infection, onward infectiousness, and infectious duration when interpreting new pertussis vaccine targets.

Macrolide resistance changed management-related outcomes but did not overturn the main vaccination-prioritization pattern. Resistance-guided management had simulated benefit under fixed assumptions and was strongly associated with lower resistant infections, but its value depended on testing reach, timely detection, alternative-drug availability, PEP implementation, and resistant-strain fitness. Resistance should therefore be treated as a modifier of strategy value and uncertainty, not as an independent claim that a specific vaccination program should be ranked first.

These findings are not implementation recommendations. Local decisions require surveillance quality, feasibility, program cost, equity, acceptability, pregnancy-vaccination uptake, household contact structure, diagnostic capacity, and resistance testing infrastructure. The appropriate use of the model is to identify strategy characteristics that merit priority assessment: maintaining routine childhood vaccination, improving infant exposure reduction, developing or deploying vaccines with stronger transmission-blocking properties, and strengthening resistance-informed management where MRBP is plausible.

### Limitations

This study has limitations. First, infant incidence was not directly calibrated because consistent age-specific observed incidence targets were unavailable across all profiles; absolute infant-burden estimates should not be interpreted as national forecasts. Second, intervals are conditional and do not include full structural, contact-matrix, implementation, or resistance-fitness uncertainty. Third, strategy profiles are simplified proxies, not complete country-specific programs; the model has no explicit pregnant-person or household compartments and does not represent adherence, contact tracing, stochastic fadeout, or individual-level heterogeneity. Fourth, high-transmission-blocking vaccine profiles are hypothetical product targets, and QALY-like translations were exploratory and did not include costs or decision thresholds.

## Conclusions

In this decision analytical modeling study, model-informed infant pertussis prioritization favored strategy characteristics that reduced infant exposure, improved transmission blocking, or strengthened resistance-sensitive management over marginal increases in already high childhood coverage. Pregnancy Tdap scale-up provided direct infant protection, but larger modeled reductions required exposure-reduction or transmission-blocking assumptions. Country-specific estimates are conditional scenario projections, not national forecasts or definitive policy rankings.

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

**Data Sharing Statement:** Processed inputs, model code, configuration files, and generated outputs are publicly available without access restrictions at https://github.com/xmusphlkg/pertussis_transmission_analysis. Permanent archive DOI: [to be inserted after Zenodo, OSF, or figshare archival before journal submission]. No individual-level participant data were used or are available.

**Additional Contributions:** None.

**Use of Artificial Intelligence:** OpenAI Codex (GPT-5-based coding assistant; manufacturer: OpenAI; model/version: GPT-5; browser extension or extension number: not applicable; used in May 2026) was used for language organization, code assistance, and implementation checks. It was not used to generate data, make autonomous analytic decisions, or replace author verification. The authors reviewed and edited all AI-assisted content and take full responsibility for the integrity of the final manuscript.

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
31. Centers for Disease Control and Prevention. 2025 Provisional Pertussis Surveillance Report. 2026. Accessed May 23, 2026. https://www.cdc.gov/pertussis/media/pdfs/2026/02/363295-A_FS_PertussisSurveillanceReport_011626_508pass.pdf
32. UK Health Security Agency. Laboratory confirmed cases of pertussis in England: annual report for 2024. Accessed May 23, 2026. https://www.gov.uk/government/publications/pertussis-laboratory-confirmed-cases-reported-in-england-2024/laboratory-confirmed-cases-of-pertussis-in-england-annual-report-for-2024
33. European Centre for Disease Prevention and Control. Pertussis. In: ECDC. Annual epidemiological report for 2024. Stockholm: ECDC; 2026. Accessed May 23, 2026. https://www.ecdc.europa.eu/en/publications-data/pertussis-annual-epidemiological-report-2024
34. Australian Centre for Disease Control. Whooping cough (pertussis). Accessed May 23, 2026. https://www.cdc.gov.au/diseases/whooping-cough-pertussis

## Tables

**Table 1. Strategy Domains, Decision Role, and Interpretation of Model Assumptions.**

| Strategy domain or assumption | Evidence strength | Decision role | Interpretation for prioritization |
| --- | --- | --- | --- |
| Routine childhood vaccination | Strong programmatic evidence, but marginal gains are constrained when coverage is already high. | Foundational comparator and maintenance priority. | Small modeled marginal gains should not be interpreted as evidence against sustaining high routine coverage. |
| Pregnancy Tdap scale-up | Stronger evidence for direct early-infant protection than for indirect adult-transmission effects. | Direct infant-protection lever. | Provides modest, consistent direct protection; should be separated from broader infant-exposure composites. |
| Close-contact/cocooning and adult-boosting proxies | More implementation dependent than pregnancy Tdap; sensitive to contact assumptions. | Infant-exposure reduction adjuncts. | Larger modeled composite effects should not be attributed to maternal immunization alone. |
| Targeted high-risk PEP | Guidance informed, but reach and adherence vary. | Contact-management support for infants and high-risk settings. | Interpreted as an outbreak/contact modifier, not broad population control. |
| Resistance-guided management | Dependent on testing reach, turnaround time, alternative treatment, and PEP delivery. | Resistance-sensitive management modifier. | Can reduce resistant infections under specified assumptions, but is not a stable vaccination strategy rank. |
| Vaccine transmission-blocking properties | Evidence is stronger for disease protection than for separate transmission-blocking components. | Product-target and mechanism-prioritization domain. | Strategy comparisons should distinguish symptom prevention from infection, infectiousness, and duration effects. |
| Infant incidence endpoint | Not directly calibrated across all profiles. | Comparative endpoint, not national forecast. | Supports broad prioritization patterns rather than precise country-specific estimates. |

## Figure Legends

**Figure 1. Calibration, Country-Profile Heterogeneity, and Baseline Infant Burden.** (A) WHO regional reported pertussis incidence for context, not global representativeness. (B) Country profile dimensions. (C) Saved-horizon annualized modeled reported incidence vs recent observed mean reported incidence; this scale diagnostic is not the calibration-window likelihood target. Dashed line indicates equality and color indicates resistant infection fraction. (D) Baseline all infections, reported cases, and infant cases per 100,000 on log scale. Infant rates are comparative model endpoints, not national forecasts.

**Figure 2. Vaccine Transmission-Blocking Properties and Infant-Burden Reduction.** (A) VE_sus, VE_sym, VE_inf, and VE_dur values for 5 vaccine profiles. (B) Infant-case burden by vaccine profile and country. (C) Vaccine-history origin decomposition by profile. (D) All-infection burden by vaccine profile and country. Panels B and D show country points, cross-country medians, and empirical intervals.

**Figure 3. Macrolide Resistance as a Management and Uncertainty Modifier.** (A) Country-timeline resistant-fraction dynamics under neutral-fitness stress-test assumptions. (B) Fitness-dependent resistant-fraction stress tests for f_R values from 0.85 to 1.15. (C) Infant burden across resistance-mechanism scenarios. (D) End-period resistant fraction by f_R and VE_inf. (E) Infant disease burden by f_R and VE_inf on log10 scale. (F) Transmission-blocking benefit by country at 3 fitness levels. Neutral-fitness panels are mechanistic stress tests, not base-case replacement forecasts.

**Figure 4. Prioritization of Strategy Profiles for Infant Pertussis Protection.** Strategy profiles are grouped by decision role: current practice comparator, routine-program levers, pregnancy Tdap and close-contact infant-protection levers, targeted PEP and resistance-sensitive management modifiers, hypothetical vaccine property targets, and combined stress-test profile. (A) Cross-country distribution of within-country infant-case reduction vs current practice, with country points, medians, and empirical intervals. (B) Within-country percentage infant-case reduction vs current practice; cell text gives point estimates, with conditional beta-grid interval audit data retained in the repository output. (C) Median burden across infant cases, reported cases, and all infections. (D) Baseline infant case incidence with conditional beta-grid intervals. Conditional intervals are not confidence intervals or full structural or implementation uncertainty.
