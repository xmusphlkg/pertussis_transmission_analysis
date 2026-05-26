# Infant Pertussis Prevention, Vaccine Transmission Blocking, and Macrolide Resistance

**Article type:** Original Investigation

**Study type:** Decision Analytical Model

**Target journal:** JAMA Network Open

**Authors:** Kangguo Li, Yulun Xie, Yunzhi Zenghuang, Tao Chen, Sha Chen, Yue He, Tianmu Chen

**Affiliations:** State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine Laboratory, National Innovation Platform for Industry-Education Integration in Vaccine Research, School of Public Health, Xiamen University, Xiamen, China

**Main text word count:** 2723

## Key Points

**Question:** Which mechanisms were associated with lower modeled infant pertussis outcomes across illustrative country profiles?

**Findings:** In this decision analytical model of 10 illustrative country profiles, infant symptomatic cases were lower with improved routine timeliness, infant-exposure reduction, and stronger transmission-blocking assumptions; pregnancy Tdap scale-up showed smaller consistent reductions. Resistance-guided management substantially reduced modeled resistant infections, with more variable infant-case effects, whereas coverage-floor-only changes showed little infant-case reduction where routine coverage was already high.

**Meaning:** Planning should evaluate timeliness, maternal protection, exposure reduction, resistance-guided management, and transmission-blocking vaccine targets as distinct mechanisms.

## Abstract

**Importance:** Severe pertussis morbidity and mortality remain concentrated in young infants, but candidate strategies differ in whether they provide direct protection, reduce infant exposure, block onward transmission, or modify macrolide-resistant *Bordetella pertussis* management.

**Objective:** To compare pertussis scenario domains for infant protection across program levers, adjuncts, management modifiers, and product targets.

**Design:** Deterministic age-structured decision analytical transmission model with a 15-year burn-in and 26-year saved horizon beginning January 1, 2025.

**Setting:** Ten illustrative country profiles using evidence accessed through May 9, 2026.

**Participants:** No individual participants; analyses used population-level country profiles.

**Exposures:** Currently actionable program levers, implementation-dependent adjuncts, resistance-management modifiers, and hypothetical transmission-blocking product-target or stress-test profiles.

**Main Outcomes and Measures:** Primary estimand: within-profile relative change in annualized modeled infant symptomatic cases vs current practice. Descriptive outcomes included infant incidence, infections, reported cases, resistant infections, resistant fraction, and deaths.

**Results:** Infant incidence was not directly calibrated; absolute infant rates were descriptive diagnostics. Calibration-window mean absolute percentage error for reported cases was 5.5% (across-profile interquartile range [IQR], 3.9%-7.8%), but aggregate fit did not validate infant incidence or age-specific burden. Coverage-floor-only changes showed little modeled infant-case change (median reduction, -1%; IQR, -5% to -1%), whereas routine-timeliness improvement lowered modeled infant cases in all 10 profiles (35%; IQR, 31%-51%). Pregnancy Tdap scale-up showed smaller consistent reductions (12%; IQR, 10%-14%). The infant-exposure composite and targeted high-risk postexposure prophylaxis (PEP) were associated with median reductions of 45% (IQR, 25%-77%) and 5%, respectively. Resistance-guided management lowered annualized resistant infections among 9 nonzero-resistance profiles (median reduction, 97%; IQR, 62%-100%), with implementation-sensitive infant-case changes. Hypothetical transmission-blocking and combined stress-test profiles showed larger reductions but were product-target or stress-test analyses.

**Conclusions and Relevance:** In this model, infant pertussis outcomes were most favorably associated with routine timeliness, reduced infant exposure, or stronger transmission blocking. Because infant incidence was not directly calibrated and several scenarios were hypothetical or implementation dependent, findings should be interpreted as conditional within-profile comparisons rather than forecasts or policy rankings.

## Introduction

Pertussis prevention programs are built on routine childhood vaccination, but severe disease remains concentrated in young infants who are not yet fully vaccinated.^1-3^ Infant protection depends on pregnancy vaccination, household or caregiver exposure, adolescent and adult transmission, treatment and postexposure prophylaxis (PEP), and broader circulation.^4-6^ These pathways are not interchangeable.

Post-pandemic pertussis resurgence has reinforced this scenario-comparison problem. High childhood coverage remains essential, yet acellular pertussis (aP) vaccines prevent symptomatic disease more reliably than infection or onward transmission, and protection against infection wanes over time.^7-13^ A model that represents vaccine effectiveness as a single composite parameter may therefore overstate the value of strategies that prevent symptoms but do little to reduce infant exposure, or understate the value of vaccines and program designs that reduce transmission.

Macrolide-resistant *Bordetella pertussis* (MRBP) adds a management and interpretation challenge. Reports from China, the Americas, Australia, Japan, and global genomic analyses indicate that resistant lineages can expand and spread internationally.^14-21^ Resistance affects the expected value of treatment and PEP, but it should be interpreted as a modifier of vaccination strategy comparisons rather than as a replacement for the infant-protection question.

The practical decision space is therefore broader than whether to add more doses. We used an age-structured decision analytical transmission model to compare infant-protection scenario domains across 10 illustrative country settings. We compared additional childhood coverage, pregnancy Tdap, adult and close-contact strategies, PEP, resistance-guided management, and future vaccine product targets as noninterchangeable scenario classes. The study was not a formal optimization, national forecast, or country-specific policy ranking.

## Methods

### Study Design and Decision Frame

This deterministic transmission-modeling study synthesized demographic, surveillance, immunization, contact, treatment, and resistance evidence in a common age-structured pertussis framework. Current practice was each profile's routine vaccination schedule and standard macrolide treatment/PEP assumptions. The analysis compared predefined strategy profiles and did not estimate cost-effectiveness or implementation feasibility. Institutional review board review and informed consent were not required because only public or aggregate population-level data were used. Relevant non-cost CHEERS 2022 elements and WHO immunization-modeling guidance informed reporting.^22,23^

Ten purposively selected profiles were analyzed: Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, the United Kingdom, and the United States. They were chosen to span program, surveillance, contact, and resistance contrasts, not to estimate global or regional averages. Inputs included population denominators, immunization records, contact matrices, surveillance intervals, pregnancy-vaccination evidence, and resistance evidence accessed through May 9, 2026.^24-27^ Selection rationale and data-quality dimensions are reported in <span style="color:#5DADE2;">eTable 1</span>.

The 2025 start date aligned vaccination, resistance, and surveillance inputs after the post-pandemic resurgence period. The 26-year saved horizon, corresponding to January 1, 2025, through December 31, 2050, was used to compare post-rebalancing scenario behavior over a policy-relevant vaccine-development and program-planning period, not to forecast calendar-year incidence. Country medians were unweighted.

### Model and Calibration

The model tracked 8 age groups, macrolide-sensitive and macrolide-resistant strains, and susceptible vaccine-origin histories reflecting maternal protection and recent or waned dose histories. Four vaccine mechanisms were represented separately: reduced susceptibility to infection (VE_sus), symptoms given infection (VE_sym), onward infectiousness (VE_inf), and infectious duration (VE_dur). Immunity followed an SIRWS structure with immune boosting and waning.^7,8^ Transmission used country-specific contact matrices, seasonality, demography, vaccination maintenance, importation, COVID-19 contact reductions, treatment, and PEP. <span style="color:#5DADE2;">eTable 2</span> provides equations and provenance.

Calibration targeted reported pertussis case counts over the 6 most recent observed calendar years, except South Africa, where 3 overlapping years were available. The retained fit minimized a negative-binomial reporting-interval likelihood plus penalties for age-specific reporting probabilities outside broad prior bounds. Diagnostics included observed-vs-modeled intervals, fit scores, mean absolute percentage errors, peak timing, and reporting probabilities (<span style="color:#5DADE2;">eFigure 2B and 2D</span> and <span style="color:#5DADE2;">eTables 7 and 12</span>). Consistent age-specific incidence series were unavailable across all profiles, so infant incidence was not directly calibrated.

Aggregate reported cases cannot separately identify transmission, reporting, waning, strain fitness, and age mixing. The principal calibration fitted the country-specific sensitive-strain transmission coefficient and reporting multiplier, with age-specific reporting probabilities constrained by broad bounds; seasonal amplitude, importation rate, and resistant-importation fraction were bounded nuisance parameters in the full-vector alternative calibration. Demography, contacts, schedules, waning/boosting, natural history, baseline vaccine effects, treatment/PEP settings, and initial resistance anchors were fixed unless varied in sensitivity analyses. Intervention coverage, vaccine-mechanism profiles, resistance fitness, and management assumptions were scenario-defined. Calibrated profiles were therefore interpreted as scenario-consistent representations rather than uniquely identified national histories.

### Interpretability of the Infant Endpoint

Because comparable infant incidence or age-specific surveillance targets were unavailable across all profiles, the infant endpoint was used for within-profile scenario comparison only. The model should not be used to infer country-specific infant incidence, infant deaths, or national policy rankings. Absolute infant incidence estimates are internal diagnostics, not forecasts. Across-profile IQRs summarize empirical heterogeneity, not uncertainty intervals. Baseline incidence, sensitivity envelopes, and post hoc age-pattern checks made endpoint uncertainty visible.

### Strategy Profiles

Strategy profiles were grouped by decision domain (<span style="color:#5DADE2;">Table 1</span> and <span style="color:#5DADE2;">eTable 4</span>). Routine-program levers included current practice, a coverage-floor-only scenario, and adolescent booster scale-up. Infant-protection levers separated pregnancy Tdap scale-up, a close-contact adult immunization/contact-reduction adjunct, and an infant-exposure composite with component diagnostics. Management modifiers included targeted high-risk PEP and resistance-guided treatment. Product-target profiles compared current aP-like vaccination with infection-blocking, transmission-blocking, and hypothetical high-transmission-blocking vaccine profiles.^28,29^

The coverage-floor-only scenario raised low infant and childhood coverage values to floors without changing dose timeliness. A routine-timeliness sensitivity accelerated movement toward age-appropriate vaccine-origin targets. Adolescent booster scale-up preserved the current aP-like mechanism. Pregnancy Tdap scale-up increased birth-entry passive protection. The close-contact adult adjunct represented improved Tdap-up-to-date status among close adult contacts and conservative adult-to-infant contact reduction. The infant-exposure composite combined pregnancy Tdap, close-contact adult protection, and reproductive-age adult boosting. Targeted high-risk PEP increased reach for household contacts, infants, and high-risk infant settings. The combined profile was a stress test.

Resistance-guided management was a reduced-form proxy for rapid MRBP recognition among symptomatic cases plus resistance-appropriate contact management, consistent with CDC guidance.^16,30,31^ It increased the symptomatic treatment transition from 0.025 to 0.065 per day and represented effective alternative therapy as 45% shorter infectious duration and 35% lower infectiousness for treated resistant infections. Resistant-strain PEP effectiveness was restored from 0.10 to 0.45 while baseline household-contact coverage stayed 0.30. Testing coverage, turnaround time, antibiotic choice, and adherence were folded into treatment, PEP, and implementation-sensitivity parameters.

Resistance analyses were tiered into country-specific starting-composition baselines, mechanistic stress tests varying resistant prevalence and fitness, and implementation-dependent resistance-management scenarios. Because the profile set mixed available program levers, implementation-dependent adjuncts, management modifiers, and hypothetical product targets, the results were interpreted as conditional scenario comparisons rather than a definitive ranking or formal optimization.^23^

The primary estimand was within-profile relative reduction in annualized infant symptomatic cases over the 26-year saved horizon. Secondary outcomes included all infections, reported cases, resistant infections, resistant fraction, deaths, and infant deaths where available. Absolute modeled infant incidence was treated as a descriptive internal diagnostic. Relative reduction was calculated as 1 - Z/Z0, where Z was the strategy outcome and Z0 was current practice.

### Sensitivity Analysis

Sensitivity analyses evaluated vaccine-mechanism thresholds, resistance fitness, reporting, treatment/PEP implementation, infant contacts, maternal protection duration, temporal windows, timeliness mechanisms, scenario ordering, stochastic contact clustering, burden translation, and vaccine-pipeline mapping. A post hoc external age-pattern diagnostic used the 4 profiles with public age-distribution checks to weight or filter scenario-class ordering by age-pattern agreement. Conditional beta-grid intervals propagated transmission-rate uncertainty with nuisance parameters fixed; they are not confidence intervals and do not jointly propagate structural, contact-matrix, resistance-fitness, or implementation uncertainty. Selected-parameter Latin-hypercube analyses were deterministic sensitivity envelopes. The model therefore supported qualitative scenario-domain comparisons, not precise numerical estimates.

## Results

### Calibration and Baseline Infant Cases

Across the 10 calibrated profiles, current-practice modeled annual infant case incidence ranged from approximately 16 per 100,000 infants in Thailand to 2393 in Australia (<span style="color:#5DADE2;">Figure 1D</span>). This absolute range is an internal descriptive diagnostic, not a national burden forecast. The fitted reported-case calibration-window target had mean absolute percentage error of 5.5% (across-profile interquartile range [IQR], 3.9%-7.8%; range, 1.2%-10.5%), with median absolute peak-timing error of 1 year (<span style="color:#5DADE2;">eTable 7</span>). Infant incidence was not directly calibrated.

Baseline profiles differed in resistance composition and surveillance scale. Starting resistant fractions ranged from 0% in the United States to 99.7% in China, with high starting resistance in Japan and lower but nonzero anchors elsewhere. Saved-horizon reported incidence under current practice ranged from less than 1 to approximately 52 reported cases per 100,000 population per year, while all-infection incidence exceeded reported incidence in every profile.

Post hoc age-pattern checks for 4 profiles, not calibration targets, were mixed (<span style="color:#5DADE2;">Supplementary Methods</span>). Agreement was closest for the United States, where infants were 12.4% of provisional reported cases vs a model-implied reported infant share of 14.7%. Modeled infant shares were higher than observed in England and Sweden/EU/EEA comparisons; Australia showed the least agreement.^32-35^ Aggregate calibration fit did not validate infant incidence or age-specific burden. Therefore, country-specific infant-rate estimates, especially for profiles with poor age-pattern agreement, should not be used for national burden inference.

### Scenario-Domain Comparisons

Strategy profiles showed separation by decision domain (<span style="color:#5DADE2;">Figure 4A-4C</span>). The coverage-floor-only scenario showed little modeled infant-case change (median reduction, -1%; across-profile IQR, -5% to -1%), and adolescent booster scale-up was heterogeneous, with a small median reduction and wide across-profile variation (median, 2%; across-profile IQR, 0%-58%). This diagnostic evaluated marginal gains above current programs and should not be interpreted as evidence against maintaining or improving timely routine childhood vaccination.

Mechanistically, the small negative coverage-floor-only estimates were not reporting artifacts and did not compare routine vaccination with no vaccination. They arose because the coverage floor moved susceptible mass into vaccine-origin states within broad age bins, while the aP-like mechanism reduced symptoms more than infection or onward transmission. With waning and immune boosting, this could lower symptomatic infection in children without proportionately reducing circulation and slightly increase infant force of infection. When routine improvement was represented as faster movement toward age-appropriate vaccine-origin targets rather than coverage-floor-only changes, modeled infant cases were lower in all 10 profiles (median reduction, 35%; across-profile IQR, 31%-51%) (<span style="color:#5DADE2;">eFigure 9A</span>).

Pregnancy Tdap scale-up was associated with a median 12% infant-case reduction (across-profile IQR, 10%-14%). The close-contact adult adjunct was associated with a median 37% reduction, driven mainly by adult boosting. The infant-exposure composite was associated with a median 45% reduction (across-profile IQR, 25%-77%) and combined direct passive protection, close-contact adult protection, and reproductive-age adult boosting; component medians were 12%, 35%, and 3%, respectively (<span style="color:#5DADE2;">eFigure 7C</span>). Targeted high-risk PEP was associated with a median 5% reduction. Resistance-guided management lowered annualized resistant infections from a median of 574 to 2 per 100,000 population; among 9 profiles with nonzero current resistant infections, the median relative reduction was 97% (across-profile IQR, 62%-100%). Infant-case reductions were more variable across implementation sensitivities. High-transmission-blocking vaccine and combined stress-test profiles showed median infant-case reductions of 97% or higher but were product-target and stress-test results, not available policy options.

Country-level heterogeneity was greater for strategies acting through older-age transmission. The coverage-floor-only scenario showed lower modeled infant cases in 1 of 10 profiles; adolescent boosting showed reductions in 5. Routine timeliness, pregnancy Tdap scale-up, close-contact adult adjuncts, infant-exposure reduction, resistance-guided management, high-transmission-blocking vaccine targets, and combined stress-test profiles showed lower modeled infant cases in all profiles. Infant-exposure reduction was associated with 38% lower modeled median reported cases and 35% lower all infections.

### Mechanistic Drivers

Vaccine profiles with stronger infection or transmission effects yielded progressively lower infant-case and population infection outcomes (<span style="color:#5DADE2;">Figure 2A, 2B, and 2D</span>). Compared with no vaccination, the symptom-protective aP-like profile was associated with an 82% simulated infant-case reduction, while infection-blocking, transmission-blocking, and high-transmission-blocking profiles were associated with lower residual cases. Threshold analyses showed that VE_inf values near 0.35 to 0.50 were needed to cross selected infant-case reduction or comparator thresholds when other vaccine mechanisms were held fixed (<span style="color:#5DADE2;">eTable 14</span>).

The vaccine-history decomposition showed that residual infections under the current aP-like profile were concentrated in waned and unvaccinated histories, with smaller shares from maternal or partial-dose histories. Profiles with reduced susceptibility, infectiousness, or infectious duration shifted both modeled infant cases and all infections downward. Transmission-blocking profiles were also associated with lower modeled reported cases and resistant infections.

### Macrolide Resistance as a Modifier

Resistance analyses included starting-composition baselines, mechanistic stress tests, and implementation-dependent management scenarios (<span style="color:#5DADE2;">Figure 3A-3F</span>). In stress tests with country-timeline anchors plus strain-specific treatment and PEP differentials, the median end resistant fraction reached 99.7% from 1.0%; equalizing PEP effectiveness lowered it to 12%, equalizing both treatment and PEP effects lowered it to 1%, and imposing a resistant-strain relative fitness multiplier, fR, of 0.85 lowered it to less than 0.1% (<span style="color:#5DADE2;">eTable 13</span>). Higher VE_inf was associated with lower modeled infant cases across fitness assumptions, but resistant fraction remained highly dependent on resistant-strain fitness.

Near-term implementation sweeps varied guided-treatment uptake, resistant-strain PEP restoration, and PEP reach; partial uptake with restored PEP showed median infant-case changes ranging from -16% to 16%. Large resistant-infection reductions could coexist with variable infant-case effects because case treatment and contact PEP changed strain competition and resistant-source timing more directly than all-strain infant exposure. Scenarios without restored PEP effectiveness showed larger apparent median infant-case reductions in some settings.

### Robustness

In the selected-parameter sensitivity envelope (128 Latin-hypercube parameter sets by 10 profiles), the combined stress-test and high-transmission-blocking product-target profiles had the lowest or second-lowest modeled infant-case rates in 100% and 99.6% of country-sample observations, respectively. Infant-exposure reduction had a median third order position and a 3% to 80% reduction envelope, while coverage-floor-only and adolescent booster scale-up had median reductions near 0% (<span style="color:#5DADE2;">eFigure 9E</span>). External age-pattern weighting across the 4 profiles with public age checks did not change the qualitative scenario-tier ordering; a stricter pass-filter changed only the order within the top transmission-blocking or combined tier (<span style="color:#5DADE2;">eFigure 9F</span>). These ordering diagnostics were scenario-comparison checks only.

In infant-contact sensitivity analyses, increasing child, adolescent, and adult sources into infant target groups from 0.75 to 1.50 changed current-practice 5-year median modeled infant cases from 120 to 186 cases per 100,000 infants; infant-exposure reduction remained lower (52 to 78 per 100,000). Varying passive maternal protection from 90 to 270 days changed direct pregnancy Tdap 5-year reductions from 9% to 12% and infant-exposure reduction from 57% to 59% (<span style="color:#5DADE2;">eTable 17</span>).

Because the profile set included available levers, implementation-dependent modifiers, and hypothetical product targets, ordering diagnostics were not interpreted as policy rankings.

## Discussion

This decision analytical model provides a mechanism-based comparison of infant pertussis prevention scenarios. Additional childhood coverage, pregnancy Tdap, adult and close-contact strategies, PEP, resistance-guided management, and future vaccine targets should not be treated as interchangeable. They act through different mechanisms: routine-program timeliness, newborn protection, infant exposure reduction, contact management, resistant-strain control, and transmission-blocking performance. Across 10 illustrative profiles, routine childhood vaccination remained foundational, but lower modeled infant symptomatic cases were associated with routine timeliness, reduced infant exposure, improved onward-transmission blocking, or resistant-strain management. This aligns with evidence that post-pandemic resurgence, waning aP protection, and incomplete transmission blocking make infant exposure reduction central.^1,5,6,9-13^

The strategy taxonomy is central to interpretation. Pregnancy Tdap scale-up represented direct passive protection and was associated with modest, consistent infant-case reductions, consistent with maternal vaccination studies.^26,27^ The infant-exposure composite showed larger reductions, but reflected adult boosting and contact assumptions as well as pregnancy Tdap. Targeted high-risk PEP had smaller average reduction and should be read as outbreak or contact-management support.^30,31^ The coverage-floor-only findings should not be interpreted as evidence against childhood vaccination; they indicate that marginal increases in nominal coverage, without improved timeliness or stronger transmission blocking, may be insufficient to reduce modeled infant exposure in already high-coverage settings.

The model also clarifies why transmission blocking matters. A symptom-protective aP-like profile was associated with lower modeled infant cases compared with no vaccination, but stronger infection- and transmission-blocking profiles were associated with still lower residual modeled infant cases and total infections. The high-transmission-blocking profile is not a recommendation for an available vaccine or evidence of programmatic superiority; it quantifies how much infant protection could depend on blocking onward transmission rather than only preventing symptoms.^9,13,28,29^

Macrolide resistance changed management-related outcomes but did not overturn the main scenario comparisons. Resistance-guided management was associated with lower resistant infections, but its value depended on testing reach, timely detection, alternative-drug availability, PEP implementation, adherence, and resistant-strain fitness, several of which were reduced-form scenario parameters. Recent MRBP reports support treating resistance as a modifier of strategy value and uncertainty; where MRBP is plausible, vaccine strategy assessment should be paired with isolate or sequencing surveillance, susceptibility reporting, and explicit PEP assumptions.^14-21,30,31^

These findings are not implementation recommendations. Local decisions require surveillance quality, feasibility, cost, equity, acceptability, household contact structure, diagnostic capacity, and resistance testing infrastructure. The model identifies mechanisms for separate assessment: maintaining routine childhood vaccination, improving infant exposure reduction, developing vaccines with stronger transmission-blocking properties, and strengthening resistance-informed management where MRBP is plausible.

### Limitations

This study has limitations. First, infant incidence was not directly calibrated; the primary estimand was within-profile relative change, and absolute modeled infant-case estimates should not be interpreted as national forecasts. Scenario comparisons involving infant outcomes are less secure where post hoc age-pattern agreement was poor. Second, across-profile IQRs are heterogeneity summaries, and sensitivity envelopes do not include full structural, contact-matrix, implementation, or resistance-fitness uncertainty. Third, strategy profiles are simplified proxies, not complete country-specific programs; the model does not represent adherence, contact tracing, stochastic fadeout, or individual heterogeneity. Fourth, high-transmission-blocking vaccine profiles are hypothetical, and burden translations did not include costs or decision thresholds.

## Conclusions

In this decision analytical modeling study, modeled infant pertussis outcomes were lower in scenario domains that improved routine timeliness, reduced infant exposure, or strengthened transmission blocking; resistance-guided management substantially reduced modeled resistant infections under specified assumptions, with more variable infant-case effects. Relative changes are the primary interpretable quantities; absolute country-specific infant rates are conditional diagnostics, not national forecasts or policy rankings.

## Supplement

**Supplement 1.** eMethods (full model equations, country-profile construction, calibration methods, scenario definitions, resistance hindcast plausibility checks, parameter identifiability classification), eReferences, <span style="color:#5DADE2;">eFigures 1-9</span>, and <span style="color:#5DADE2;">eTables 1-24</span>.

## Article Information

**Previous Presentation:** None.

**Corresponding Author:** Tianmu Chen, PhD, State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine Laboratory, National Innovation Platform for Industry-Education Integration in Vaccine Research, School of Public Health, Xiamen University, Xiamen, China (chentianmu@xmu.edu.cn).

**Author Contributions:** Kangguo Li and Tianmu Chen had full access to all the data in the study and take responsibility for the integrity of the data and the accuracy of the data analysis. Kangguo Li conducted and is responsible for the data analysis. Concept and design: Kangguo Li and Tianmu Chen. Acquisition, analysis, or interpretation of data: Kangguo Li, Yulun Xie, Yunzhi Zenghuang, Tao Chen, Sha Chen, Yue He, and Tianmu Chen. Drafting of the manuscript: Kangguo Li and Yulun Xie. Critical revision of the manuscript for important intellectual content: all authors. Statistical analysis: Kangguo Li. Administrative, technical, or material support: Kangguo Li and Tianmu Chen. Supervision: Tianmu Chen.

**Reporting Guideline:** Relevant non-cost elements of CHEERS 2022 were used for decision-model transparency only; this study was not a cost-effectiveness analysis. WHO immunization-modeling guidance was also followed. Model equations, parameter classification, calibration diagnostics, and sensitivity analyses are provided in the Supplement.

**Conflict of Interest Disclosures:** The authors have no conflicts of interest to disclose.

**Funding/Support:** This work was supported by the National Natural Science Foundation of China (825B2104 to Kangguo Li), and the National Key Research and Development Program of China (2024YFC2311404 to Tianmu Chen).

**Role of the Funder/Sponsor:** The funders had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.

**Data Sharing Statement:** Processed inputs, model code, configuration files, and generated outputs are publicly available without access restrictions at https://github.com/xmusphlkg/pertussis_transmission_analysis (commit 5958e27afc3d6ad0bc56bf47c8d7f8ec6971d352). No individual-level participant data were used or are available.

**Additional Contributions:** None.

**Use of Artificial Intelligence:** OpenAI Codex (GPT-5; OpenAI; used in May 2026) was used for language organization, code assistance, and implementation checks. It was not used to generate data, make autonomous analytic decisions, or replace author verification. The authors reviewed and edited all AI-assisted content and take full responsibility for the integrity of the final manuscript.

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
19. Komatsu S, Nakanishi N, Matsubara K, et al. Molecular analysis of emerging MT27 macrolide-resistant *Bordetella pertussis*, Kobe, Japan, 2025. *Emerg Infect Dis*. 2026;32(1):150-153. doi:10.3201/eid3201.250890
20. Obara T, Kano K, Yorifuji T, et al. Localized outbreak of macrolide-resistant pertussis in infants, Japan, March-May 2025. *Emerg Infect Dis*. 2026;32(1):158-161. doi:10.3201/eid3201.250824
21. Zhang H, Kang Z, Zhang Y, et al. Evolutionary dynamics and global spread of macrolide-resistant *Bordetella pertussis* during the post-pandemic pertussis resurgence. *J Infect*. 2026;92(4):106718. doi:10.1016/j.jinf.2026.106718
22. Husereau D, Drummond M, Augustovski F, et al. Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) statement. *BMJ*. 2022;376:e067975. doi:10.1136/bmj-2021-067975
23. World Health Organization. Guidance for using modelling for immunization decision-making. Geneva: World Health Organization; 2025. Accessed May 9, 2026. https://iris.who.int/handle/10665/385083
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

**Table 1. Strategy Scenario Domains and Main Modeling Assumptions.**

| Domain | Scenario | Implementable now? | Main assumption changed | Primary intended mechanism | Key caveat |
| --- | --- | ---: | --- | --- | --- |
| Comparator | Current practice | Yes | Country-specific vaccination schedule, coverage, treatment, and PEP assumptions retained | Baseline for within-profile relative reductions | Not a no-vaccination counterfactual |
| Routine program | Coverage-floor-only scenario | Yes/partly | Infant and childhood coverage values below floors raised; countries already above floors unchanged | More nominal routine vaccine-origin coverage | Does not improve timeliness or transmission blocking; not evidence against routine vaccination |
| Routine program | Timeliness improvement sensitivity | Yes/partly | Faster movement toward age-appropriate infant-series vaccine-origin targets | Earlier direct infant protection | Implementation dependent and modeled as sensitivity analysis |
| Routine program | Adolescent booster scale-up | Yes/partly | Adolescent coverage floor raised while current aP-like mechanism retained | Reduced older-child and adolescent contribution to transmission | Indirect infant effects depend on age mixing and aP transmission blocking |
| Pregnancy | Pregnancy Tdap scale-up | Yes | Birth-entry passive-protection target raised to 75% | Direct early-infant passive protection | Country-specific uptake pathways not fully modeled |
| Exposure reduction | Infant-exposure composite | Partly | Pregnancy Tdap, close-contact adult protection, reproductive-age adult boosting, and 15% adult-to-infant contact reduction combined | Lower infant exposure from direct and indirect sources | Implementation-dependent composite, not a single program |
| Contact management | Targeted high-risk PEP | Yes/partly | PEP reach among eligible household contacts, infants, and high-risk settings raised to 45% | Reduced infection after recognized exposure | Depends on detection, contact tracing, timing, and adherence |
| Resistance management | Resistance-guided management | Partly | Symptomatic treatment transition raised; resistant infectious duration and infectiousness lowered; resistant-strain PEP effectiveness restored | Lower resistant-strain transmission under resistance-guided care | Reduced-form proxy for testing, turnaround, alternative treatment, and adherence |
| Product target | High-transmission-blocking vaccine | No | Upper-bound vaccine profile: VE_sus 0.80, VE_sym 0.90, VE_inf 0.65, VE_dur 0.40 | Lower susceptibility and onward transmission | Hypothetical product-target scenario |
| Stress test | Combined profile | No | Transmission-blocking vaccine assumptions, pregnancy Tdap, adult/contact adjuncts, adolescent boosting, targeted PEP, and resistance-guided management combined | Upper-bound multi-mechanism contrast | Non-implementable scenario-comparison stress test |

Abbreviations: aP, acellular pertussis; PEP, postexposure prophylaxis; VE_dur, vaccine effectiveness against infectious duration; VE_inf, vaccine effectiveness against onward infectiousness; VE_sus, vaccine effectiveness against susceptibility; VE_sym, vaccine effectiveness against symptoms given infection.

## Figure Legends

**Figure 1. Calibration, Country-Profile Heterogeneity, and Baseline Infant Cases.** (A) WHO regional reported pertussis incidence for context, not global representativeness. (B) Country profile dimensions. (C) Saved-horizon annualized modeled reported incidence vs recent observed mean reported incidence; this scale diagnostic is not the calibration-window likelihood target. Dashed line indicates equality and color indicates resistant infection fraction. (D) Baseline all infections, reported cases, and infant cases per 100,000 on log scale. Infant rates are descriptive model diagnostics, not national forecasts.

**Figure 2. Vaccine Transmission-Blocking Properties and Infant-Case Reduction.** (A) VE_sus, VE_sym, VE_inf, and VE_dur values for 5 vaccine profiles. (B) Modeled infant cases by vaccine profile and country. (C) Vaccine-history origin decomposition by profile. (D) All infections by vaccine profile and country. Panels B and D show profile points, across-profile medians, and empirical heterogeneity intervals.

**Figure 3. Macrolide Resistance as a Management and Uncertainty Modifier.** (A) Country-timeline resistant-fraction dynamics under neutral-fitness stress-test assumptions. (B) Fitness-dependent resistant-fraction stress tests for resistant-strain relative fitness multiplier, fR, values from 0.85 to 1.15. (C) Modeled infant cases across resistance-mechanism scenarios. (D) End-period resistant fraction by fR and VE_inf. (E) Modeled infant cases by fR and VE_inf on log10 scale. (F) Transmission-blocking reduction by country at 3 fitness levels. Neutral-fitness panels are mechanistic stress tests, not base-case replacement forecasts.

**Figure 4. Scenario-Domain Comparisons for Modeled Infant Pertussis Outcomes.** Strategy profiles are grouped by decision domain: foundational comparator, routine-program marginal levers, direct infant-protection lever, exposure-reduction adjuncts, management modifiers, hypothetical product targets, and combined stress-test profile. (A) Across-profile distribution of within-country infant-case reduction vs current practice, with profile points, medians, and empirical intervals; these are heterogeneity summaries, not uncertainty intervals. (B) Within-country percentage infant-case reduction vs current practice; cell text gives point estimates, with conditional beta-grid interval audit data retained in the repository output. (C) Median outcomes across infant cases, reported cases, and all infections. (D) Baseline infant case incidence with conditional beta-grid intervals. Conditional intervals are not confidence intervals or full structural or implementation uncertainty.
