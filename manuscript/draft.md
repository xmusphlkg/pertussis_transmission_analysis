# Infant Pertussis Prevention Under Transmission-Blocking Vaccine and Macrolide-Resistance Assumptions

**Article type:** Original Investigation

**Study type:** Decision Analytical Model

**Target journal:** JAMA Network Open

**Authors:** Kangguo Li, Yulun Xie, Yunzhi Zenghuang, Tao Chen, Sha Chen, Yue He, Tianmu Chen

**Affiliations:** State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine Laboratory, National Innovation Platform for Industry-Education Integration in Vaccine Research, School of Public Health, Xiamen University, Xiamen, China

**Main text word count:** 2984

## Key Points

**Question:** Which pertussis prevention strategy characteristics are associated with lower modeled infant burden when vaccine transmission blocking and macrolide resistance are considered?

**Findings:** In this decision analytical model of 10 illustrative country profiles, modeled infant burden was lower under infant-exposure reduction, routine-timeliness improvement, and stronger transmission-blocking assumptions than under marginal routine coverage floors. Pregnancy Tdap showed modest but consistent modeled benefit, and resistance-guided management lowered resistant infections under specified assumptions.

**Meaning:** Infant pertussis planning should evaluate routine vaccination, pregnancy Tdap, infant-exposure reduction, PEP, resistance-sensitive management, and next-generation vaccine targets as distinct strategy domains rather than interchangeable policy options.

## Abstract

**Importance:** Infant pertussis protection requires separating direct protection, exposure reduction, transmission blocking, and macrolide resistance.

**Objective:** To compare pertussis strategy profiles for infant protection across program levers, adjuncts, management modifiers, and product targets.

**Design:** Deterministic age-structured decision analytical transmission-modeling study with a 15-year burn-in and 26-year horizon beginning January 1, 2025.

**Setting:** Ten illustrative country profiles using evidence accessed through May 9, 2026.

**Participants:** No individual participants were included; analyses used population-level country profiles.

**Exposures:** Currently actionable program levers, implementation-dependent adjuncts, resistance-management modifiers, and hypothetical transmission-blocking product-target or stress-test profiles.

**Main Outcomes and Measures:** Primary estimand: within-profile relative change in annualized modeled infant symptomatic cases vs current practice. Descriptive outcomes included absolute modeled infant incidence, infections, reported cases, resistant infections, resistant fraction, and deaths.

**Results:** Infant incidence was not directly calibrated and absolute infant rates were treated as descriptive diagnostics. Calibration-window mean absolute percentage error for reported cases was 5.5% (across-profile interquartile range [IQR], 3.9%-7.8%). Among actionable program levers, routine coverage floors did not produce a consistent modeled infant-case reduction (median, -1%; across-profile IQR, -5% to -1%), adolescent boosting had a small and uncertain modeled reduction (median, 2%; across-profile IQR, 0%-58%), and pregnancy Tdap scale-up produced a smaller but consistent modeled reduction (median, 12%; across-profile IQR, 10%-14%). A routine-timeliness sensitivity produced modeled infant-case reductions in all 10 profiles (median, 35%; across-profile IQR, 31%-51%). The implementation-dependent infant-exposure composite produced a modeled infant-case reduction of 45% (across-profile IQR, 25%-77%); component medians were 12% for pregnancy Tdap alone, 35% for reproductive-age adult boosting, and 3% for contact reduction alone. Targeted high-risk PEP produced a 5% median modeled reduction. Resistance-guided management substantially lowered modeled resistant infections under fixed implementation assumptions, although infant-case effects varied across implementation sensitivities. Hypothetical transmission-blocking and combined stress-test profiles produced larger modeled reductions but were interpreted as product-target sensitivity analyses rather than available interventions. In a selected-parameter deterministic sensitivity envelope, combined and high-transmission-blocking profiles were among the 2 lowest infant-burden strategies in 100% and 99.6% of country-sample observations, respectively.

**Conclusions and Relevance:** In this decision analytical modeling study, within-profile reductions in modeled infant pertussis burden were larger for infant-exposure reduction, routine-timeliness improvement, and stronger vaccine transmission-blocking assumptions than for marginal coverage floors in already high-coverage settings. Because infant incidence was not directly calibrated and several profiles were hypothetical or implementation dependent, findings should be interpreted as conditional scenario comparisons rather than national forecasts or policy rankings.

## Introduction

Pertussis prevention programs are built on routine childhood vaccination, but the most severe burden remains concentrated in young infants who are not yet fully vaccinated.^1-3^ Infant protection depends on direct passive protection after pregnancy vaccination, household or caregiver exposure, adolescent and adult transmission, treatment and PEP delivery, and broader circulation.^4-6^ These pathways are not interchangeable for decision making.

Post-pandemic pertussis resurgence has reinforced this prioritization problem. High childhood coverage remains essential, yet acellular pertussis (aP) vaccines prevent symptomatic disease more reliably than infection or onward transmission, and protection against infection wanes over time.^7-13^ A model that represents vaccine effect as a single composite parameter may therefore overstate the value of strategies that prevent symptoms but do little to reduce infant exposure, or understate the value of vaccines and program designs that reduce transmission.

Macrolide-resistant *B pertussis* (MRBP) adds a management and interpretation challenge. Reports from China, the Americas, Australia, Japan, and global genomic analyses indicate that resistant lineages can expand and spread internationally.^14-21^ Resistance affects the expected value of treatment and PEP, but it should be interpreted as a modifier of vaccination strategy comparisons rather than as a replacement for the infant-protection question.

The practical decision space is therefore broader than whether to add more doses. We used an age-structured decision analytical transmission model to compare infant-protection strategy profiles across 10 illustrative country settings. The decision-support question was not which single policy ranked first, but which mechanisms should be evaluated separately. We compared additional childhood coverage, pregnancy Tdap, adult and close-contact strategies, PEP, resistance-guided management, and future vaccine product targets in one framework while treating them as noninterchangeable strategy classes with different mechanisms and endpoints. The study was not a formal optimization, national forecast, or country-specific policy ranking.

## Methods

### Study Design and Decision Frame

This deterministic transmission-modeling study synthesized demographic, surveillance, immunization, contact, treatment, and resistance evidence in a common age-structured pertussis framework. Current practice was each profile's routine vaccination schedule and standard macrolide treatment/PEP assumptions. The analysis compared predefined strategy profiles and did not estimate cost-effectiveness or implementation feasibility. Institutional review board review and informed consent were not required because only public or aggregate population-level data were used and no individual participants were involved. Relevant non-cost CHEERS 2022 elements were used only for decision-model transparency, and WHO immunization-modeling guidance informed model reporting.^22,23^

Ten purposively selected profiles were analyzed: Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, the United Kingdom, and the United States. They were chosen to span program, surveillance, contact, and resistance contrasts, not to estimate global or regional averages. Inputs included population denominators, immunization records, contact matrices, surveillance intervals, pregnancy-vaccination evidence, and resistance evidence accessed through May 9, 2026.^24-27^ Selection rationale and data-quality dimensions are reported in <span style="color:#5DADE2;">eTable 1</span>.

The 2025 start date was chosen to align vaccination, resistance, and surveillance inputs after the post-pandemic resurgence period, while allowing resistance anchors through the evidence date to inform initial country profiles. The 26-year saved horizon was used to compare medium-term consequences after burn-in and rebalancing, not to predict calendar-year incidence. Country medians were unweighted.

### Model and Calibration

The model tracked 8 age groups, macrolide-sensitive and macrolide-resistant strains, and susceptible vaccine-origin histories reflecting maternal protection and recent or waned dose histories. Four vaccine mechanisms were represented separately: reduced susceptibility to infection (VE_sus), symptoms given infection (VE_sym), onward infectiousness (VE_inf), and infectious duration (VE_dur). Immunity followed an SIRWS structure with immune boosting and waning.^7,8^ Transmission used country-specific contact matrices, seasonality, demography, vaccination maintenance, importation, COVID-19 contact reductions, treatment, and PEP. <span style="color:#5DADE2;">eTable 2</span> provides equations and provenance.

Calibration targeted reported pertussis case counts over the 6 most recent observed calendar years, except South Africa, where 3 overlapping years were available. The retained fit minimized a negative-binomial reporting-interval likelihood plus penalties for age-specific reporting probabilities outside broad prior bounds. Diagnostics included observed-vs-modeled intervals, fit scores, mean absolute percentage errors, peak timing, and reporting probabilities (<span style="color:#5DADE2;">eFigure 2B and 2D</span> and <span style="color:#5DADE2;">eTables 7 and 12</span>). Consistent age-specific incidence series were unavailable across all profiles, so infant incidence was not directly calibrated.

Aggregate reported cases cannot separately identify transmission, reporting, waning, strain fitness, and age mixing. The principal calibration fitted the country-specific sensitive-strain transmission coefficient and reporting multiplier, with age-specific reporting probabilities constrained by broad bounds; seasonal amplitude, importation rate, and resistant-importation fraction were bounded nuisance parameters in the full-vector alternative calibration. Demography, contacts, schedules, waning/boosting, natural history, baseline vaccine effects, treatment/PEP settings, and initial resistance anchors were fixed unless varied in sensitivity analyses. Intervention coverage, vaccine-mechanism profiles, resistance fitness, and management assumptions were scenario-defined. Calibrated profiles were therefore interpreted as scenario-consistent representations rather than uniquely identified national histories.

Because infant incidence could not be directly calibrated across all profiles, the primary estimand was the within-profile relative change in modeled infant symptomatic cases vs current practice. Absolute infant incidence estimates are internal diagnostics, not national forecasts. Across-profile IQRs summarize empirical heterogeneity, not uncertainty intervals. Baseline infant incidence, sensitivity envelopes, and post hoc age-pattern checks were reported to make endpoint uncertainty visible.

### Strategy Profiles

Strategy profiles were grouped by decision domain (<span style="color:#5DADE2;">eTable 29</span>). Routine-program levers included current practice, routine childhood coverage floors, and adolescent booster scale-up. Infant-protection levers separated pregnancy Tdap scale-up, a close-contact adult immunization/contact-reduction adjunct, and an infant-exposure composite with component diagnostics. Management modifiers included targeted high-risk PEP and resistance-guided treatment. Product-target profiles compared current aP-like vaccination with infection-blocking, transmission-blocking, and hypothetical high-transmission-blocking vaccine profiles.^28,29^

The routine coverage scenario raised low infant and childhood coverage values to floors without reducing countries already above them. A routine-timeliness sensitivity accelerated movement toward age-appropriate vaccine-origin targets. The adolescent scenario represented booster scale-up while preserving the current aP-like mechanism. Pregnancy Tdap scale-up increased birth-entry passive protection. The close-contact adult adjunct represented improved Tdap-up-to-date status among close adult contacts and conservative adult-to-infant contact reduction. The infant-exposure composite combined pregnancy Tdap, close-contact adult protection, and reproductive-age adult boosting. Targeted high-risk PEP increased reach for household contacts, infants, and high-risk infant settings. The combined profile was a stress test, not an implementable package.

Resistance-guided management was a reduced-form proxy for rapid MRBP recognition among symptomatic cases plus resistance-appropriate management of exposed contacts, consistent with CDC guidance.^16,30,31^ It acted on cases and contacts. Case eligibility was symptomatic suspected or confirmed pertussis with resistance suspicion or detection; the scenario increased the symptomatic treatment transition from 0.025 to 0.065 per day and represented effective alternative therapy as 45% shorter infectious duration and 35% lower infectiousness for treated resistant infections. Contact eligibility followed household contacts, high-risk individuals, and contacts or settings involving high-risk individuals; resistant-strain PEP effectiveness was restored from 0.10 to 0.45 while baseline household-contact coverage stayed 0.30. Testing coverage, turnaround time, antibiotic choice, and adherence were folded into treatment, PEP, and implementation-sensitivity parameters.

Resistance analyses were tiered into country-specific starting-composition baselines, mechanistic stress tests varying resistant prevalence and fitness, and implementation-dependent resistance-management scenarios. Because the profile set mixed available program levers, implementation-dependent adjuncts, management modifiers, and hypothetical product targets, the results were interpreted as conditional scenario comparisons rather than a definitive ranking or formal optimization.^23^

The primary estimand was within-profile relative reduction in annualized infant symptomatic cases over the 26-year saved horizon. Secondary outcomes included all infections, reported cases, resistant infections, resistant fraction, deaths, and infant deaths where available. Absolute modeled infant incidence was treated as a descriptive internal diagnostic. Relative reduction was calculated as 1 - Z/Z0, where Z was the strategy outcome and Z0 was current practice.

### Sensitivity Analysis

Sensitivity analyses evaluated vaccine-mechanism thresholds, resistance-fitness grids, reporting assumptions, treatment/PEP implementation, infant contacts, maternal passive-protection duration, temporal windows, routine-timeliness mechanisms, strategy ordering, stochastic contact clustering, burden translation, and vaccine-pipeline mapping. Conditional beta-grid intervals propagated transmission-rate uncertainty with nuisance parameters fixed; they are not confidence intervals and do not jointly propagate structural, contact-matrix, resistance-fitness, or implementation uncertainty. Selected-parameter Latin-hypercube analyses were interpreted as deterministic sensitivity envelopes. The model was therefore used to support qualitative prioritization patterns, not precise effect estimates.

## Results

### Calibration and Baseline Infant Burden

Across the 10 calibrated profiles, current-practice modeled annual infant case incidence ranged from approximately 16 per 100,000 infants in Thailand to 2393 in Australia (<span style="color:#5DADE2;">Figure 1D</span>). This absolute range is an internal descriptive diagnostic, not a national burden forecast. The fitted reported-case calibration-window target had mean absolute percentage error of 5.5% (across-profile interquartile range [IQR], 3.9%-7.8%; range, 1.2%-10.5%), with median absolute peak-timing error of 1 year (<span style="color:#5DADE2;">eTable 7</span>). Infant incidence was not directly calibrated.

Baseline profiles also differed substantially in resistance composition and surveillance scale. Starting resistant fractions ranged from 0% in the United States to 99.7% in China, with high starting resistance in Japan and lower but nonzero anchors in Australia, Brazil, Sweden, Thailand, New Zealand, South Africa, and the United Kingdom. Saved-horizon reported incidence under current practice ranged from less than 1 to approximately 52 reported cases per 100,000 population per year, while all-infection incidence exceeded reported incidence in every profile.

Post hoc age-pattern checks for 4 profiles, not calibration targets, were mixed (<span style="color:#5DADE2;">Table 1</span>). Agreement was closest for the United States, where infants younger than 1 year were 12.4% of provisional reported cases vs a model-implied reported infant share of 14.7%. Modeled infant shares were higher than observed in England and Sweden/EU/EEA comparisons; Australia showed the least agreement. No comparable infant or age-specific target was retained for the other 6 profiles. These checks did not uniformly validate the modeled infant endpoint; they support treating absolute infant incidence as descriptive only and interpreting findings as qualitative within-profile scenario comparisons.^32-35^

### Strategy-Profile Prioritization

Strategy profiles showed a separation by decision domain (<span style="color:#5DADE2;">Figure 4A-4C</span>). Routine childhood coverage floors did not produce a consistent modeled infant-case reduction (median, -1%; across-profile IQR, -5% to -1%), and adolescent booster scale-up produced a small and uncertain modeled reduction (median, 2%; across-profile IQR, 0%-58%). This diagnostic evaluated marginal gains above current programs and should not be interpreted as evidence against maintaining or improving timely routine childhood vaccination.

Mechanistically, the small negative coverage-floor estimates were not reporting artifacts and did not compare routine vaccination with no vaccination. They arose because the coverage floor moved susceptible mass into vaccine-origin states within broad age bins, while the aP-like mechanism reduced symptoms more than infection or onward transmission. With waning and immune boosting, this could lower symptomatic infection in children without proportionately reducing circulation and slightly increase infant force of infection. When routine improvement was represented as faster movement toward age-appropriate vaccine-origin targets rather than coverage floors alone, modeled infant cases fell in all 10 profiles (median reduction, 35%; across-profile IQR, 31%-51%) (<span style="color:#5DADE2;">eTable 18</span>).

Pregnancy Tdap scale-up produced a median 12% infant-case reduction (across-profile IQR, 10%-14%). The close-contact adult adjunct produced a median 37% reduction, driven mainly by adult boosting. The infant-exposure composite produced a median 45% reduction (across-profile IQR, 25%-77%) and combined direct passive protection, close-contact adult protection, and reproductive-age adult boosting; component medians were 12%, 35%, and 3%, respectively (<span style="color:#5DADE2;">eTable 29</span>). Targeted high-risk PEP produced a median 5% reduction. Resistance-guided management lowered saved-horizon resistant infections from a median of 2.43 million to 34,103; among 9 profiles with nonzero current resistant infections, the median relative reduction was 97% (across-profile IQR, 62%-100%). Infant-case reductions were more variable across implementation sensitivities. High-transmission-blocking vaccine and combined stress-test profiles produced median infant-case reductions of 97% or higher but were product-target and stress-test results, not available policy options.

Country-level heterogeneity was greater for strategies acting through older-age transmission. The childhood coverage floor improved infant outcomes in 1 of 10 profiles; adolescent boosting produced positive infant-case reductions in 5. Routine timeliness, pregnancy Tdap scale-up, close-contact adult adjuncts, infant-exposure reduction, resistance-guided management, high-transmission-blocking vaccine targets, and combined stress-test profiles produced modeled infant-case reductions in all 10 profiles. Infant-exposure reduction reduced modeled median reported cases by 38% and all infections by 35%.

### Mechanistic Drivers

Vaccine profiles with stronger infection or transmission effects yielded progressively lower infant and population burden (<span style="color:#5DADE2;">Figure 2A, 2B, and 2D</span>). Compared with no vaccination, the symptom-protective aP-like profile produced an 82% simulated infant-case reduction, while infection-blocking, transmission-blocking, and high-transmission-blocking profiles reduced residual burden further. Threshold analyses showed that VE_inf values near 0.35 to 0.50 were needed to cross selected infant-case reduction or comparator thresholds when other vaccine mechanisms were held fixed (<span style="color:#5DADE2;">eTable 14</span>).

The vaccine-history decomposition showed that residual infections under the current aP-like profile were concentrated in waned and unvaccinated histories, with smaller shares from maternal or partial-dose histories. Profiles that reduced susceptibility, infectiousness, or infectious duration shifted both infant-case burden and all-infection burden downward. Transmission-blocking profiles also reduced modeled reported cases and resistant infections.

### Macrolide Resistance as a Modifier

Resistance analyses included starting-composition baselines, mechanistic stress tests, and implementation-dependent management scenarios (<span style="color:#5DADE2;">Figure 3A-3F</span>). In stress tests with country-timeline anchors plus strain-specific treatment and PEP differentials, the median end resistant fraction reached 99.7% from 1.0%; equalizing PEP effectiveness lowered it to 12%, equalizing both treatment and PEP effects lowered it to 1%, and imposing a resistant-strain relative fitness multiplier, fR, of 0.85 lowered it to less than 0.1% (<span style="color:#5DADE2;">eTable 13</span>). Increasing VE_inf reduced infant burden across fitness assumptions, but resistant fraction remained highly dependent on resistant-strain fitness.

Near-term implementation sweeps varied guided-treatment uptake, resistant-strain PEP restoration, and PEP reach; partial uptake with restored PEP produced median infant-case changes ranging from -16% to 16%. Large resistant-infection reductions could coexist with variable infant-case effects because case treatment and contact PEP changed strain competition and resistant-source timing more directly than all-strain infant exposure. Scenarios without restored PEP effectiveness produced larger apparent median infant-case reductions in some settings.

### Robustness

In the selected-parameter deterministic sensitivity envelope (128 Latin-hypercube parameter sets by 10 profiles), combined stress-test and high-transmission-blocking profiles were among the 2 lowest infant-burden strategies in 100% and 99.6% of country-sample observations, respectively; their 2.5th to 97.5th percentile reduction envelopes were 37% to 100% and 32% to 100%. Infant-exposure reduction had a median third-place rank and a 3% to 80% envelope, while routine coverage floors and adolescent booster scale-up had median reductions near 0% and were never among the 2 lowest-burden strategies (<span style="color:#5DADE2;">eTable 25</span>).

In infant-contact sensitivity analyses, increasing child, adolescent, and adult sources into infant target groups from 0.75 to 1.50 changed current-practice 5-year median infant burden from 120 to 186 cases per 100,000 infants; infant-exposure reduction remained lower (52 to 78 per 100,000). Varying passive maternal protection from 90 to 270 days changed direct pregnancy Tdap 5-year reductions from 9% to 12% and infant-exposure reduction from 57% to 59% (<span style="color:#5DADE2;">eTable 17</span>).

Because the profile set included available levers, implementation-dependent modifiers, and hypothetical product targets, ordering diagnostics were not interpreted as policy rankings.

## Discussion

This decision analytical modeling study provides a decision-support insight: for infant pertussis protection, additional childhood coverage, pregnancy Tdap, adult and close-contact strategies, PEP, resistance-guided management, and future vaccine targets should not be treated as interchangeable. They act through different mechanisms and require different endpoints: routine-program timeliness, direct newborn protection, infant exposure reduction, contact management, resistant-strain control, and transmission-blocking performance. Across 10 illustrative profiles, routine childhood vaccination remained foundational, but larger modeled reductions were associated with routine timeliness, reduced infant exposure, improved onward-transmission blocking, or resistant-strain management. This aligns with evidence that post-pandemic resurgence, waning aP protection, and incomplete transmission blocking make infant exposure reduction a central policy question.^1,5,6,9-13^

The strategy taxonomy is central to interpretation. Pregnancy Tdap scale-up represented direct passive protection and produced modest, consistent infant benefit, consistent with maternal vaccination studies.^26,27^ The infant-exposure composite produced larger reductions, but those reductions reflected adult boosting and contact assumptions as well as pregnancy Tdap. Targeted high-risk PEP had smaller average benefit and should be read as outbreak or contact-management support, consistent with guidance prioritizing household contacts, infants, and high-risk settings.^30,31^ Routine childhood vaccination remains foundational; the coverage-floor findings concern marginal gains after current programs are represented and do not argue against timely infant-series completion or catch-up vaccination.

The model also clarifies why transmission blocking matters. A symptom-protective aP-like profile reduced modeled infant cases compared with no vaccination, but stronger infection- and transmission-blocking profiles reduced residual infant burden and total infections further. The high-transmission-blocking profile is not a recommendation for an available vaccine or evidence of programmatic superiority; it quantifies how much infant protection could depend on blocking onward transmission rather than only preventing symptoms.^9,13,28,29^

Macrolide resistance changed management-related outcomes but did not overturn the main scenario comparisons. Resistance-guided management was associated with lower resistant infections, but its value depended on testing reach, timely detection, alternative-drug availability, PEP implementation, adherence, and resistant-strain fitness, several of which were reduced-form scenario parameters. Recent MRBP reports support treating resistance as a modifier of strategy value and uncertainty; where MRBP is plausible, vaccine strategy assessment should be paired with isolate or sequencing surveillance, susceptibility reporting, and explicit PEP assumptions.^14-21,30,31^

These findings are not implementation recommendations. Local decisions require surveillance quality, feasibility, cost, equity, acceptability, household contact structure, diagnostic capacity, and resistance testing infrastructure. The model identifies mechanisms that merit priority assessment: maintaining routine childhood vaccination, improving infant exposure reduction, developing vaccines with stronger transmission-blocking properties, and strengthening resistance-informed management where MRBP is plausible.

### Limitations

This study has limitations. First, infant incidence was not directly calibrated; the primary estimand was within-profile relative change, and absolute infant-burden estimates should not be interpreted as national forecasts. Second, across-profile IQRs are heterogeneity summaries, and sensitivity envelopes do not include full structural, contact-matrix, implementation, or resistance-fitness uncertainty. Third, strategy profiles are simplified proxies, not complete country-specific programs; the model does not represent adherence, contact tracing, stochastic fadeout, or individual-level heterogeneity. Fourth, high-transmission-blocking vaccine profiles are hypothetical, and exploratory burden translations did not include costs or decision thresholds.

## Conclusions

In this decision analytical modeling study, model-informed infant pertussis prioritization favored routine-timeliness improvement, infant exposure reduction, improved transmission blocking, or resistance-sensitive management over marginal coverage floors in already high-coverage settings. Relative changes are the primary interpretable quantities; absolute country-specific infant rates are conditional diagnostics, not national forecasts or policy rankings.

## Supplement

**Supplement 1.** eMethods (full model equations, country-profile construction, calibration methods, scenario definitions, resistance hindcast plausibility checks, parameter identifiability classification), eReferences, <span style="color:#5DADE2;">eFigures 1-8</span>, and <span style="color:#5DADE2;">eTables 1-29</span>.

## Article Information

**Previous Presentation:** None.

**Corresponding Author:** Tianmu Chen, PhD, State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine Laboratory, National Innovation Platform for Industry-Education Integration in Vaccine Research, School of Public Health, Xiamen University, Xiamen, China (chentianmu@xmu.edu.cn).

**Author Contributions:** Kangguo Li and Tianmu Chen had full access to all the data in the study and take responsibility for the integrity of the data and the accuracy of the data analysis. Kangguo Li conducted and is responsible for the data analysis. Concept and design: Kangguo Li. Acquisition, analysis, or interpretation of data: Yulun Xie, Yunzhi Zenghuang, Tao Chen, Sha Chen, and Yue He. Drafting of the manuscript: Kangguo Li and Yulun Xie. Critical revision of the manuscript for important intellectual content: Kangguo Li. Statistical analysis: Kangguo Li. Administrative, technical, or material support: Kangguo Li and Tianmu Chen. Supervision: Tianmu Chen.

**Reporting Guideline:** Relevant non-cost elements of CHEERS 2022 were used for decision-model transparency only; this study was not a cost-effectiveness analysis. WHO immunization-modeling guidance was also followed. Model equations, parameter classification, calibration diagnostics, and sensitivity analyses are provided in the Supplement.

**Conflict of Interest Disclosures:** The authors have no conflicts of interest to disclose.

**Funding/Support:** This work was supported by the National Natural Science Foundation of China (825B2104 to Kangguo Li), and the National Key Research and Development Program of China (2024YFC2311404 to Tianmu Chen).

**Role of the Funder/Sponsor:** The funders had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.

**Data Sharing Statement:** Processed inputs, model code, configuration files, and generated outputs are publicly available without access restrictions at https://github.com/xmusphlkg/pertussis_transmission_analysis. An archived release identifier (tag, commit hash, or DOI) will be cited in the final submission. No individual-level participant data were used or are available.

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
30. Centers for Disease Control and Prevention. Treatment of pertussis. Accessed May 25, 2026. https://www.cdc.gov/pertussis/hcp/clinical-care/index.html
31. Centers for Disease Control and Prevention. Postexposure antimicrobial prophylaxis. Accessed May 25, 2026. https://www.cdc.gov/pertussis/php/postexposure-prophylaxis/index.html
32. Centers for Disease Control and Prevention. 2025 Provisional Pertussis Surveillance Report. 2026. Accessed May 23, 2026. https://www.cdc.gov/pertussis/media/pdfs/2026/02/363295-A_FS_PertussisSurveillanceReport_011626_508pass.pdf
33. UK Health Security Agency. Laboratory confirmed cases of pertussis in England: annual report for 2024. Accessed May 23, 2026. https://www.gov.uk/government/publications/pertussis-laboratory-confirmed-cases-reported-in-england-2024/laboratory-confirmed-cases-of-pertussis-in-england-annual-report-for-2024
34. European Centre for Disease Prevention and Control. Pertussis. In: ECDC. Annual epidemiological report for 2024. Stockholm: ECDC; 2026. Accessed May 23, 2026. https://www.ecdc.europa.eu/en/publications-data/pertussis-annual-epidemiological-report-2024
35. Australian Centre for Disease Control. Whooping cough (pertussis). Accessed May 23, 2026. https://www.cdc.gov.au/diseases/whooping-cough-pertussis

## Tables

**Table 1. Post Hoc Infant or Age-Pattern Checks for Interpreting the Modeled Infant Endpoint.**

| Profile | External infant or age-specific check | Model comparison | Interpretation |
| --- | --- | --- | --- |
| United States | Infants younger than 1 y were 12.4% of 2025 provisional reported cases. | Model-implied reported infant share was 14.7%. | Closest agreement among available checks; supports relative-change use, not absolute burden forecasting. |
| United Kingdom | England infants younger than 1 y were 6.0% of 2024 laboratory-confirmed cases. | Model-implied United Kingdom reported infant share was 19.8%. | Model overrepresented infant share compared with external age distribution. |
| Sweden | EU/EEA 2024 infant notification rate was 318.5 per 100,000; infant case share was 4.8%. | Sweden modeled infant endpoint was 408.9 per 100,000 infants; model-implied reported infant share was 15.6%. | Incidence scale was broadly comparable, but infant share was overrepresented. |
| Australia | 2024 notifications were school-age dominated, with ages 5-14 y comprising 57.0% of cases. | Model-implied reported infant share was 23.5%. | Poor age-pattern agreement; absolute infant rate should be interpreted cautiously. |
| Brazil | No comparable public infant or age-specific comparison target retained. | No direct external comparison. | Absolute infant rate is descriptive only. |
| China | No comparable public infant or age-specific comparison target retained. | No direct external comparison. | Absolute infant rate is descriptive only. |
| Japan | No comparable public infant or age-specific comparison target retained. | No direct external comparison. | Absolute infant rate is descriptive only. |
| New Zealand | No comparable public infant or age-specific comparison target retained. | No direct external comparison. | Absolute infant rate is descriptive only. |
| South Africa | No comparable public infant or age-specific comparison target retained. | No direct external comparison. | Absolute infant rate is descriptive only. |
| Thailand | No comparable public infant or age-specific comparison target retained. | No direct external comparison. | Absolute infant rate is descriptive only. |

Sources: Public surveillance summaries cited in references 32-35.

## Figure Legends

**Figure 1. Calibration, Country-Profile Heterogeneity, and Baseline Infant Burden.** (A) WHO regional reported pertussis incidence for context, not global representativeness. (B) Country profile dimensions. (C) Saved-horizon annualized modeled reported incidence vs recent observed mean reported incidence; this scale diagnostic is not the calibration-window likelihood target. Dashed line indicates equality and color indicates resistant infection fraction. (D) Baseline all infections, reported cases, and infant cases per 100,000 on log scale. Infant rates are descriptive model diagnostics, not national forecasts.

**Figure 2. Vaccine Transmission-Blocking Properties and Infant-Burden Reduction.** (A) VE_sus, VE_sym, VE_inf, and VE_dur values for 5 vaccine profiles. (B) Infant-case burden by vaccine profile and country. (C) Vaccine-history origin decomposition by profile. (D) All-infection burden by vaccine profile and country. Panels B and D show profile points, across-profile medians, and empirical heterogeneity intervals.

**Figure 3. Macrolide Resistance as a Management and Uncertainty Modifier.** (A) Country-timeline resistant-fraction dynamics under neutral-fitness stress-test assumptions. (B) Fitness-dependent resistant-fraction stress tests for resistant-strain relative fitness multiplier, fR, values from 0.85 to 1.15. (C) Infant burden across resistance-mechanism scenarios. (D) End-period resistant fraction by fR and VE_inf. (E) Infant disease burden by fR and VE_inf on log10 scale. (F) Transmission-blocking benefit by country at 3 fitness levels. Neutral-fitness panels are mechanistic stress tests, not base-case replacement forecasts.

**Figure 4. Prioritization of Strategy Profiles for Infant Pertussis Protection.** Strategy profiles are grouped by decision domain: foundational comparator, routine-program marginal levers, direct infant-protection lever, exposure-reduction adjuncts, management modifiers, hypothetical product targets, and combined stress-test profile. (A) Across-profile distribution of within-country infant-case reduction vs current practice, with profile points, medians, and empirical intervals; these are heterogeneity summaries, not uncertainty intervals. (B) Within-country percentage infant-case reduction vs current practice; cell text gives point estimates, with conditional beta-grid interval audit data retained in the repository output. (C) Median burden across infant cases, reported cases, and all infections. (D) Baseline infant case incidence with conditional beta-grid intervals. Conditional intervals are not confidence intervals or full structural or implementation uncertainty.
