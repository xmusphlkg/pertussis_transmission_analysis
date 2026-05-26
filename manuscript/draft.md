# Optimizing Infant Pertussis Prevention Across Vaccination and Resistance-Management Strategies

**Article type:** Original Investigation

**Study type:** Decision Analytical Model

**Authors:** Kangguo Li, Yulun Xie, Yunzhi Zenghuang, Tao Chen, Sha Chen, Yue He, Tianmu Chen

**Affiliations:** State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine Laboratory, National Innovation Platform for Industry-Education Integration in Vaccine Research, School of Public Health, Xiamen University, Xiamen, China

**Main text word count:** 2853

## Key Points

**Question:** How did modeled infant pertussis outcomes differ across vaccination, exposure-reduction, and resistance-management scenario groups?

**Findings:** In this decision analytical model of 10 illustrative country profiles, improved routine timeliness and infant-exposure reduction resulted in lower modeled infant symptomatic cases than current practice. Resistance-guided management reduced modeled resistant infections under specified assumptions, while transmission-blocking vaccine profiles were interpreted as future product targets.

**Meaning:** Infant pertussis planning should distinguish timeliness, maternal protection, exposure reduction, resistance management, and transmission blocking rather than treating these mechanisms as interchangeable.

## Abstract

**Importance:** Severe pertussis morbidity and mortality remain concentrated in young infants, but candidate strategies differ in whether they provide direct protection, reduce infant exposure, block onward transmission, or modify macrolide-resistant *Bordetella pertussis* management.

**Objective:** To compare vaccination, exposure-reduction, and resistance-management mechanisms for modeled infant protection while separating program levers, resistance-management modifiers, and future product targets or stress tests.

**Design, Setting, and Participants:** Deterministic age-structured decision analytical transmission model with a 15-year burn-in and 26-year saved horizon beginning January 1, 2025, with 5- and 10-year horizon sensitivities. Ten illustrative country profiles used evidence accessed through May 9, 2026. No individual participants were included; analyses used population-level inputs.

**Exposures:** Three interpretive tiers: currently implementable or near-implementable program levers; resistance-management modifiers; and future product targets or stress tests.

**Main Outcomes and Measures:** Primary estimand: within-profile relative change in annualized modeled infant symptomatic cases vs current practice. Descriptive outcomes included modeled infant incidence, infections, reported cases, resistant infections, and resistant fraction.

**Results:** Infant incidence was not directly calibrated; absolute infant rates were descriptive diagnostics. Calibration-window mean absolute percentage error for reported cases was 5.5% (IQR, 3.9%-7.8%), but aggregate fit did not validate infant incidence or age-specific burden. External age-pattern checks were mixed, but reweighting or filtering profiles by age-pattern agreement did not change qualitative mechanism separation. Within the program-lever tier, the nominal coverage floor without timeliness improvement did not evaluate routine vaccination versus no vaccination and showed little modeled infant-case change (median reduction, -1%; IQR, -5% to -1%), whereas routine-timeliness improvement lowered modeled infant cases in all 10 profiles (median reduction, 35%; IQR, 31%-51%). Pregnancy Tdap scale-up and infant-exposure composite resulted in median reductions of 12% and 45% (IQR, 25%-77%); targeted high-risk PEP had smaller modeled changes. Under specified resistance-guided management assumptions, modeled annualized resistant infections were lower among 9 nonzero-resistance profiles (median reduction, 97%; IQR, 62%-100%), with implementation-sensitive modeled infant-case changes. Transmission-blocking and combined profiles were interpreted only as future product targets or stress tests.

**Conclusions and Relevance:** In this model, relative modeled infant pertussis case changes supported mechanism separation across implementable levers, resistance-management assumptions, and future product targets. Because infant incidence was not directly calibrated and several scenarios were hypothetical or implementation dependent, findings should not be interpreted as forecasts or policy rankings.

## Introduction

Pertussis prevention programs are built on routine childhood vaccination, but severe disease remains concentrated in young infants who are not yet fully vaccinated.^1-3^ Infant protection depends on pregnancy vaccination, household or caregiver exposure, adolescent and adult transmission, treatment and postexposure prophylaxis (PEP), and broader circulation.^4-6^ These pathways are not interchangeable.

Post-pandemic pertussis resurgence has reinforced this scenario-comparison problem. High childhood coverage remains essential, yet acellular pertussis (aP) vaccines prevent symptomatic disease more reliably than infection or onward transmission, and protection against infection wanes over time.^7-13^ A model that represents vaccine effectiveness as a single composite parameter may therefore overstate the value of strategies that prevent symptoms but do little to reduce infant exposure, or understate the value of vaccines and program designs that reduce transmission.

Macrolide-resistant *Bordetella pertussis* (MRBP) adds a management and interpretation challenge. Reports from China, the Americas, Australia, Japan, and global genomic analyses indicate that resistant lineages can expand and spread internationally.^14-21^ Resistance affects the expected value of treatment and PEP, but it should be interpreted as a modifier of vaccination strategy comparisons rather than as a replacement for the infant-protection question.

We used an age-structured decision analytical model to compare infant-protection mechanisms across vaccination, exposure-reduction, and resistance-management scenarios in 10 profiles grouped as program levers, resistance-management modifiers, and future product targets or stress tests. The goal was mechanism separation.

## Methods

### Study Design and Decision Frame

This deterministic transmission-modeling study synthesized demographic, surveillance, immunization, contact, treatment, and resistance evidence in a common age-structured pertussis framework. Current practice was each profile's routine vaccination schedule and standard macrolide treatment/PEP assumptions. The analysis compared predefined strategy profiles and did not estimate cost-effectiveness or implementation feasibility. Review board approval and consent were not required because analyses used public or aggregate population-level data. Relevant non-cost CHEERS 2022 elements and WHO immunization-modeling guidance informed reporting.^22,23^

Ten purposively selected profiles were analyzed: Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, the United Kingdom, and the United States. They spanned aP and wP schedules, dose counts, adolescent and pregnancy Tdap programs, reported-incidence and surveillance-quality contrasts, demographic and contact patterns, and resistance anchors from near-zero to near-fixation, not global or regional averages. Inputs included population denominators, immunization records, contact matrices, surveillance intervals, pregnancy-vaccination evidence, and resistance evidence accessed through May 9, 2026.^24-27^

The 2025 start date aligned vaccination, resistance, and surveillance inputs after post-pandemic resurgence. The 26-year horizon (January 1, 2025-December 31, 2050) compared post-rebalancing behavior over vaccine-development and program-planning timelines; 5- and 10-year windows tested near-term horizon sensitivity. Medians were unweighted across illustrative profiles, not population-weighted or global estimates.

### Model and Calibration

The model tracked 8 age groups, macrolide-sensitive and macrolide-resistant strains, and susceptible vaccine-origin histories reflecting maternal protection and recent or waned dose histories. Four vaccine mechanisms were represented separately: reduced susceptibility to infection (VE_sus), symptoms given infection (VE_sym), onward infectiousness (VE_inf), and infectious duration (VE_dur). Immunity followed an SIRWS structure with immune boosting and waning.^7,8^ Transmission used country-specific contact matrices, seasonality, demography, vaccination maintenance, importation, COVID-19 contact reductions, treatment, and PEP. <span style="color:#5DADE2;">eTable 2</span> provides equations and provenance.

Calibration targeted reported pertussis case counts over the 6 most recent observed calendar years, except South Africa, where 3 overlapping years were available. The retained fit minimized a negative-binomial reporting-interval likelihood plus penalties for age-specific reporting probabilities outside broad prior bounds. Diagnostics included observed-vs-modeled intervals, fit scores, mean absolute percentage errors, peak timing, and reporting probabilities (<span style="color:#5DADE2;">eFigure 2B and 2D</span> and <span style="color:#5DADE2;">eTables 7 and 12</span>). Consistent age-specific incidence series were unavailable across all profiles, so infant incidence was not directly calibrated.

Aggregate reported cases cannot separately identify transmission, reporting, waning, strain fitness, and age mixing. The principal calibration fitted the country-specific sensitive-strain transmission coefficient and reporting multiplier, with age-specific reporting probabilities constrained by broad bounds; seasonal amplitude, importation rate, and resistant-importation fraction were bounded nuisance parameters in the full-vector alternative calibration. Demography, contacts, schedules, waning/boosting, natural history, baseline vaccine effects, treatment/PEP settings, and initial resistance anchors were fixed unless varied in sensitivity analyses. Because strategies were compared within the same calibrated profile against current practice, ordering was interpreted as a conditional mechanism contrast despite non-identifiability.

### Infant Endpoint Validation and Interpretability

Because comparable infant incidence or age-specific surveillance targets were unavailable across all profiles, the infant endpoint was used only for within-profile scenario comparison. The primary outcome is relative modeled infant-case change conditional on specified modeling and implementation assumptions. Absolute modeled infant incidence was not used for burden inference. IQRs across illustrative profiles summarize empirical heterogeneity, not uncertainty intervals.

Endpoint plausibility was evaluated with 2 age-pattern diagnostics: public age-distribution summaries vs modeled reported age shares in 4 profiles, and scenario-group ordering reweighted or pass-filtered by agreement. The pass-filter defined acceptable agreement as a country age-pattern weight of at least 0.50 after scaling each external-vs-modeled absolute difference by its prespecified tolerance. These diagnostics tested ordering robustness; they did not externally calibrate infant incidence.

### Strategy Profiles

Strategy profiles were grouped into 3 interpretive tiers (<span style="color:#5DADE2;">Table 1</span> and <span style="color:#5DADE2;">eTable 4</span>). Tier 1 included currently implementable or near-implementable program levers: current practice, nominal coverage floor without timeliness improvement, routine timeliness, adolescent booster scale-up, pregnancy Tdap scale-up, close-contact adult adjuncts, infant-exposure reduction, and targeted high-risk PEP. Tier 2 included resistance-management modifiers: resistance-guided treatment and resistant-strain PEP assumptions. Tier 3 included future product targets and stress tests: infection-blocking, transmission-blocking, high-transmission-blocking vaccine profiles, and combined scenarios.^28,29^

The nominal coverage floor without timeliness improvement raised low infant and childhood coverage values to floors without changing dose timeliness. A routine-timeliness sensitivity accelerated movement toward age-appropriate vaccine-origin targets. Adolescent booster scale-up preserved the current aP-like mechanism. Pregnancy Tdap scale-up increased birth-entry passive protection. The close-contact adult adjunct represented improved Tdap-up-to-date status among close adult contacts and conservative adult-to-infant contact reduction. The infant-exposure composite combined pregnancy Tdap, close-contact adult protection, and reproductive-age adult boosting. Targeted high-risk PEP increased reach for household contacts, infants, and high-risk infant settings. The combined profile was a stress test.

Resistance-guided management was a reduced-form composite rather than a specific diagnostic platform: rapid molecular testing, culture/susceptibility testing, sequencing, or empiric alternative therapy could map to earlier MRBP recognition and resistance-appropriate contact management (<span style="color:#5DADE2;">eTable 25</span>). It raised the symptomatic treatment transition from 0.025 to 0.065 per day, shortened treated resistant infectious duration by 45%, lowered resistant infectiousness by 35%, and restored resistant-strain PEP effectiveness from 0.10 to 0.45 while household-contact PEP coverage stayed 0.30. Testing availability, turnaround time, antibiotic choice, adherence, and PEP delivery were folded into implementation-sensitivity parameters.

Because tiers differed in implementability, results were interpreted by tier and mechanism rather than as a ranking or formal optimization.^23^

The primary estimand was within-profile relative change in annualized modeled infant symptomatic cases over the 26-year saved horizon. Secondary outcomes included all infections, reported cases, resistant infections, and resistant fraction. Modeled infant incidence was treated as a descriptive internal diagnostic. Relative change was calculated as 1 - Z/Z0, where Z was the strategy outcome and Z0 was current practice.

### Sensitivity Analysis

Uncertainty was organized into parameter, structural, data, and scenario layers. Sensitivity analyses mapped to these layers through vaccine-mechanism thresholds, reporting, infant contacts, treatment/PEP implementation, temporal windows, timeliness mechanisms, and scenario ordering. Conditional beta-grid intervals propagated only transmission-rate uncertainty with nuisance parameters fixed, and Latin-hypercube analyses were deterministic sensitivity envelopes. Because infant incidence, scenario reach, and structural assumptions were not jointly identifiable from available surveillance, the model supported qualitative strategy-group comparisons, not effect-size estimation.

## Results

### Endpoint Validation and Baseline Infant Cases

Across the 10 calibrated profiles, current-practice modeled annual infant case incidence ranged from 16 per 100,000 infants in Thailand to 2393 in Australia (<span style="color:#5DADE2;">Figure 1D</span>). This absolute range is an internal descriptive diagnostic. The fitted reported-case calibration-window target had mean absolute percentage error of 5.5% (IQR across illustrative profiles, 3.9%-7.8%; range, 1.2%-10.5%), with median absolute peak-timing error of 1 year (<span style="color:#5DADE2;">eTable 7</span>). Infant incidence was not directly calibrated.

Baseline profiles differed in resistance and surveillance scale. Starting resistant fractions ranged from 0% in the United States to 99.7% in China, with high starting resistance in Japan and lower but nonzero anchors elsewhere. Saved-horizon reported incidence under current practice ranged from less than 1 to 52 reported cases per 100,000 population per year, while all-infection incidence exceeded reported incidence in every profile.

External age-pattern checks for 4 profiles, not calibration targets, were mixed (<span style="color:#5DADE2;">Supplementary Methods</span>). Agreement was closest for the United States (12.4% provisional vs 14.7% modeled infant case share) and moderate for Sweden/EU/EEA despite a higher modeled infant share (15.6% vs 4.8%). The United Kingdom was less consistent (6.0% in England vs 19.8% modeled), and Australia was least consistent on the school-age check (57.0% observed aged 5-14 years vs 31.4% modeled aged 5-17 years).^32-35^ Using the 0.50 age-pattern weight threshold retained Sweden and the United States and excluded Australia and the United Kingdom. Aggregate calibration fit did not validate infant incidence or age-specific burden.

### Tier 1: Program Levers and Adjuncts

Within currently implementable or near-implementable program levers (<span style="color:#5DADE2;">Figure 4A-4C</span>), the nominal coverage floor without timeliness improvement showed little modeled infant-case change (median reduction across illustrative profiles, -1%; IQR, -5% to -1%), and adolescent booster scale-up was heterogeneous, with a small median reduction across illustrative profiles and wide variation (2%; IQR, 0%-58%).

**Interpretation of the nominal coverage-floor scenario.** This scenario should not be interpreted as reducing the value of routine childhood vaccination. It evaluated marginal nominal coverage increases in mostly high-coverage profiles, without changing dose timeliness or vaccine effects on infection and transmission. Small negative estimates arose when the coverage floor moved susceptible mass into vaccine-origin states within broad age bins; with waning and immune boosting, this could slightly increase infant force of infection. In contrast, routine timeliness improvement lowered modeled infant cases in all 10 profiles (median reduction, 35%; IQR, 31%-51%) (<span style="color:#5DADE2;">eFigure 9A</span>).

Pregnancy Tdap scale-up had a 12% median modeled infant-case reduction across illustrative profiles (IQR, 10%-14%). The close-contact adult adjunct had a 37% median reduction, driven mainly by adult boosting. The infant-exposure composite had a 45% median reduction (IQR, 25%-77%) and combined direct passive protection, close-contact adult protection, and reproductive-age adult boosting (<span style="color:#5DADE2;">eFigure 7C</span>). Targeted high-risk PEP had a 5% median reduction.

Country-level heterogeneity was greater for program levers acting through older-age transmission. The nominal coverage-floor scenario showed lower modeled infant cases in 1 of 10 profiles; adolescent boosting showed reductions in 5. Routine timeliness, pregnancy Tdap scale-up, close-contact adult adjuncts, and infant-exposure reduction showed lower modeled infant cases in all profiles. Infant-exposure reduction yielded 38% lower median modeled reported cases and 35% lower all infections across illustrative profiles.

### Tier 2: Resistance-Management Modifiers

Resistance-management modifiers were reduced-form testing, treatment, and resistant-strain PEP assumptions, not standalone vaccination policies (<span style="color:#5DADE2;">Figure 3A-3F</span> and <span style="color:#5DADE2;">eTable 25</span>). Under the specified resistance-guided composite, modeled annualized resistant infections declined from a median across illustrative profiles of 574 to 2 per 100,000; among 9 nonzero-resistance profiles, the median relative reduction across illustrative profiles was 97% (IQR, 62%-100%). Modeled infant-case effects were implementation-sensitive.

Resistance stress tests showed strong dependence on strain fitness and treatment/PEP differentials: the median end resistant fraction reached 99.7% under neutral-fitness country-timeline assumptions, 12% after equalizing PEP effectiveness, 1% after equalizing both treatment and PEP effects, and less than 0.1% with a resistant-strain relative fitness multiplier, fR, of 0.85 (<span style="color:#5DADE2;">eTable 13</span>). Higher VE_inf lowered modeled infant cases across fitness assumptions, but resistant fraction remained fitness-dependent.

Near-term implementation sweeps varied guided-treatment uptake, resistant-strain PEP restoration, and PEP reach; partial uptake with restored PEP showed median modeled infant-case changes ranging from -16% to 16%. Large resistant-infection reductions could coexist with variable infant-case effects because case treatment and contact PEP changed strain competition and resistant-source timing more directly than all-strain infant exposure.

### Tier 3: Future Product Targets and Stress Tests

Vaccine profiles with stronger infection or transmission effects yielded progressively lower modeled infant-case and population infection outcomes (<span style="color:#5DADE2;">Figure 2A, 2B, and 2D</span>). Compared with no vaccination, the symptom-protective aP-like profile yielded an 82% simulated infant-case reduction, while infection-blocking, transmission-blocking, and high-transmission-blocking profiles yielded lower residual modeled cases. Threshold analyses showed that VE_inf values near 0.35 to 0.50 were needed to cross selected infant-case reduction or comparator thresholds when other vaccine mechanisms were held fixed (<span style="color:#5DADE2;">eTable 14</span>).

The vaccine-history decomposition showed that residual infections under the current aP-like profile were concentrated in waned and unvaccinated histories, with smaller shares from maternal or partial-dose histories. Profiles with reduced susceptibility, infectiousness, or infectious duration shifted both modeled infant cases and all infections downward. High-transmission-blocking vaccine and combined stress-test profiles showed median modeled infant-case reductions across illustrative profiles of 97% or higher, but these were product-target and stress-test results, not available policy options.

### Robustness

In the selected-parameter sensitivity envelope (128 Latin-hypercube parameter sets by 10 profiles), the combined stress-test and high-transmission-blocking product-target profiles had the lowest or second-lowest modeled infant-case rates in 100% and 99.6% of country-sample observations, respectively. Infant-exposure reduction had a median third order position and a 3% to 80% reduction envelope, while nominal coverage-floor and adolescent booster scale-up had median reductions near 0% (<span style="color:#5DADE2;">eFigure 9E</span>).

The primary endpoint robustness check addressed the mixed age-pattern validation results. Reweighting the 4 external-check profiles by age-pattern agreement did not change qualitative mechanism grouping. A stricter pass-filter retained Sweden and the United States, excluding Australia and the United Kingdom; qualitative grouping again remained stable, with only an exact-order swap between the high-transmission-blocking product-target and combined stress-test classes within Tier 3 (<span style="color:#5DADE2;">eFigure 9F</span>). These ordering diagnostics were scenario-comparison checks only.

Near-term 5- and 10-year windows retained the broad grouping: product-target and stress-test profiles lowest, infant-exposure reduction ahead of routine marginal levers, and nominal coverage floor near the bottom (<span style="color:#5DADE2;">eFigure 9B</span>). In infant-contact sensitivity analyses, increasing child, adolescent, and adult sources into infant target groups from 0.75 to 1.50 changed current-practice 5-year median modeled infant cases across illustrative profiles from 120 to 186 cases per 100,000 infants; infant-exposure reduction remained lower (52 to 78 per 100,000). Varying passive maternal protection from 90 to 270 days changed direct pregnancy Tdap 5-year reductions from 9% to 12% and infant-exposure reduction from 57% to 59% (<span style="color:#5DADE2;">eTable 17</span>).

## Discussion

This model compares modeled infant pertussis prevention scenarios by mechanism and implementability tier. Program levers, resistance-management modifiers, and future product targets answered different questions. Routine childhood vaccination remained foundational. Modeled infant symptomatic cases depended on timeliness, maternal protection, exposure reduction, onward-transmission blocking, and resistant-strain management, not nominal coverage alone. This aligns with evidence that post-pandemic resurgence, waning aP protection, and incomplete transmission blocking make infant exposure reduction central.^1,5,6,9-13^

Tier 1 scenarios were closest to implementable program decisions. Pregnancy Tdap scale-up represented direct passive protection and yielded modest, consistent modeled infant-case reductions, consistent with maternal vaccination studies.^26,27^ The infant-exposure composite showed larger reductions, but reflected adult boosting and contact assumptions as well as pregnancy Tdap. Targeted high-risk PEP should be read as outbreak or contact-management support.^30,31^ Nominal coverage-floor findings should not be interpreted as evidence against childhood vaccination; they indicate that marginal increases in nominal coverage, without improved timeliness or stronger transmission blocking, may be insufficient to reduce modeled infant exposure in already high-coverage settings.

Tier 2 resistance-management modifiers changed resistant-infection outcomes under specified assumptions but were reduced-form proxies for testing reach, timely detection, alternative-drug availability, PEP implementation, adherence, and resistant-strain fitness. Recent MRBP reports support treating resistance as a modifier of strategy value and uncertainty; where MRBP is plausible, vaccine strategy assessment should be paired with isolate or sequencing surveillance, susceptibility reporting, and explicit PEP assumptions.^14-21,30,31^

Tier 3 product targets and stress tests clarified why transmission blocking matters. A symptom-protective aP-like profile yielded lower modeled infant cases than no vaccination, but stronger infection- and transmission-blocking profiles lowered residual modeled infant cases and total infections. The high-transmission-blocking profile quantified possible infant protection from blocking onward transmission rather than only preventing symptoms.^9,13,28,29^

Local decisions require surveillance quality, feasibility, cost, equity, acceptability, household contact structure, diagnostic capacity, and resistance testing infrastructure. The model identifies mechanisms for separate assessment within the relevant tier.

### Limitations

This study has limitations. First, infant incidence was not directly calibrated; the primary estimand was within-profile relative modeled change, and absolute modeled infant-case estimates should not be interpreted as national forecasts. Scenario comparisons involving infant outcomes are less secure where external age-pattern agreement was poor, even though the pass-filter robustness check did not change qualitative mechanism grouping. Second, IQRs across illustrative profiles are heterogeneity summaries, and the uncertainty hierarchy was not a full probabilistic ensemble jointly propagating structural, data, parameter, and scenario uncertainty. Third, strategy profiles are simplified proxies, not complete country-specific programs; the model does not represent adherence, contact tracing, stochastic fadeout, or individual heterogeneity. Fourth, the 26-year horizon increases dependence on waning, demography, and resistance assumptions; 5- and 10-year diagnostics supported the same broad mechanism grouping but did not remove long-term uncertainty. Fifth, high-transmission-blocking vaccine profiles are hypothetical, and burden translations did not include costs or decision thresholds.

## Conclusions

Relative modeled infant pertussis case changes supported separation of currently implementable program levers, resistance-management modifiers, and future product targets or stress tests. Relative changes are the primary interpretable quantities; absolute country-specific infant rates are conditional diagnostics.

## Supplement

**Supplement 1.** eMethods (full model equations, country-profile construction, calibration methods, scenario definitions, resistance hindcast plausibility checks, parameter identifiability classification), eReferences, <span style="color:#5DADE2;">eFigures 1-9</span>, and <span style="color:#5DADE2;">eTables 1-25</span>.

**Supplement 2.** Relevant non-cost CHEERS 2022 reporting checklist.

**Supplement 3.** Figure source data manifest and reproducibility file locations.

## Article Information

**Previous Presentation:** None.

**Corresponding Author:** Tianmu Chen, PhD, State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine Laboratory, National Innovation Platform for Industry-Education Integration in Vaccine Research, School of Public Health, Xiamen University, Xiamen, China (chentianmu@xmu.edu.cn).

**Author Contributions:** Kangguo Li and Tianmu Chen had full access to all the data in the study and take responsibility for the integrity of the data and the accuracy of the data analysis. Kangguo Li conducted and is responsible for the data analysis. Concept and design: Kangguo Li and Tianmu Chen. Acquisition, analysis, or interpretation of data: Kangguo Li, Yulun Xie, Yunzhi Zenghuang, Tao Chen, Sha Chen, Yue He, and Tianmu Chen. Drafting of the manuscript: Kangguo Li and Yulun Xie. Critical revision of the manuscript for important intellectual content: all authors. Statistical analysis: Kangguo Li. Administrative, technical, or material support: Kangguo Li and Tianmu Chen. Supervision: Tianmu Chen.

**Reporting Guideline:** Relevant non-cost elements of CHEERS 2022 were used for decision-model transparency only; this study was not a cost-effectiveness analysis. WHO immunization-modeling guidance was also followed. Model equations, parameter classification, calibration diagnostics, sensitivity analyses, and a reporting checklist are provided in the Supplement.

**Conflict of Interest Disclosures:** The authors have no conflicts of interest to disclose.

**Funding/Support:** This work was supported by the National Natural Science Foundation of China (825B2104 to Kangguo Li), and the National Key Research and Development Program of China (2024YFC2311404 to Tianmu Chen).

**Role of the Funder/Sponsor:** The funders had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.

**Data Sharing Statement:** Processed inputs, model code, configuration files, generated outputs, figure source data, and reproducibility files are publicly available without access restrictions at https://github.com/xmusphlkg/pertussis_transmission_analysis (commit 5958e27afc3d6ad0bc56bf47c8d7f8ec6971d352). No individual-level participant data were used or are available.

**Additional Contributions:** None.

**Use of Artificial Intelligence:** OpenAI Codex coding assistant (GPT-5; OpenAI; API-based Codex interface; used May 2026) was used for code assistance, manuscript-edit implementation, language organization, and consistency checks. AI-assisted wording was incorporated only after author review and editing. The tool was not used to generate data, define analytic decisions, select assumptions, or replace author verification. The authors take full responsibility for the integrity and accuracy of the final manuscript.

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

**Table 1. Strategy Scenario Tiers and Main Modeling Assumptions.**

| Tier | Scenario | Implementable now? | Main assumption changed | Primary intended mechanism | Key caveat |
| --- | --- | ---: | --- | --- | --- |
| Tier 1 program lever | Current practice | Yes | Country-specific vaccination schedule, coverage, treatment, and PEP assumptions retained | Baseline for within-profile relative reductions | Not a no-vaccination counterfactual |
| Tier 1 program lever | Nominal coverage floor without timeliness improvement | Yes/partly | Infant and childhood coverage values below floors raised; countries already above floors unchanged | More nominal routine vaccine-origin coverage | Does not evaluate routine vaccination versus no vaccination; does not improve timeliness or transmission blocking |
| Tier 1 program lever | Timeliness improvement sensitivity | Yes/partly | Faster movement toward age-appropriate infant-series vaccine-origin targets | Earlier direct infant protection | Implementation dependent and modeled as sensitivity analysis |
| Tier 1 program lever | Adolescent booster scale-up | Yes/partly | Adolescent coverage floor raised while current aP-like mechanism retained | Reduced older-child and adolescent contribution to transmission | Indirect infant effects depend on age mixing and aP transmission blocking |
| Tier 1 program lever | Pregnancy Tdap scale-up | Yes | Birth-entry passive-protection target raised to 75% | Direct early-infant passive protection | Country-specific uptake pathways not fully modeled |
| Tier 1 program lever | Infant-exposure composite | Partly | Pregnancy Tdap, close-contact adult protection, reproductive-age adult boosting, and 15% adult-to-infant contact reduction combined | Lower infant exposure from direct and indirect sources | Implementation-dependent composite, not a single program |
| Tier 1 program lever | Targeted high-risk PEP | Yes/partly | PEP reach among eligible household contacts, infants, and high-risk settings raised to 45% | Reduced infection after recognized exposure | Depends on detection, contact tracing, timing, and adherence |
| Tier 2 resistance-management modifier | Resistance-guided management | Partly | Composite of rapid molecular testing, culture/susceptibility testing, sequencing, or empiric alternative therapy; resistant-strain PEP effectiveness restored | Lower resistant-strain transmission under specified management assumptions | Reduced-form proxy for testing, turnaround, uptake, alternative treatment, PEP delivery, and adherence |
| Tier 3 product target or stress test | High-transmission-blocking vaccine | No | Upper-bound vaccine profile: VE_sus 0.80, VE_sym 0.90, VE_inf 0.65, VE_dur 0.40 | Lower susceptibility and onward transmission | Hypothetical product-target scenario |
| Tier 3 product target or stress test | Combined profile | No | Transmission-blocking vaccine assumptions, pregnancy Tdap, adult/contact adjuncts, adolescent boosting, targeted PEP, and resistance-guided management combined | Upper-bound multi-mechanism contrast | Non-implementable scenario-comparison stress test |

Abbreviations: aP, acellular pertussis; PEP, postexposure prophylaxis; VE_dur, vaccine effectiveness against infectious duration; VE_inf, vaccine effectiveness against onward infectiousness; VE_sus, vaccine effectiveness against susceptibility; VE_sym, vaccine effectiveness against symptoms given infection.

## Figure Legends

**Figure 1. Calibration, Country-Profile Heterogeneity, and Baseline Infant Cases.** (A) WHO regional reported pertussis incidence for context, not global representativeness. (B) Country profile dimensions. (C) Saved-horizon annualized modeled reported incidence vs recent observed mean reported incidence; this scale diagnostic is not the calibration-window likelihood target. Dashed line indicates equality and color indicates resistant infection fraction. (D) Baseline all infections, reported cases, and infant cases per 100,000 on log scale. Infant rates are descriptive model diagnostics, not national forecasts.

**Figure 2. Vaccine Transmission-Blocking Properties and Infant-Case Reduction.** (A) VE_sus, VE_sym, VE_inf, and VE_dur values for 5 vaccine profiles. (B) Modeled infant cases by vaccine profile and country. (C) Vaccine-history origin decomposition by profile. (D) All infections by vaccine profile and country. Panels B and D show profile points, medians across illustrative profiles, and empirical heterogeneity intervals.

**Figure 3. Macrolide Resistance as a Management and Uncertainty Modifier.** (A) Country-timeline resistant-fraction dynamics under neutral-fitness stress-test assumptions. (B) Fitness-dependent resistant-fraction stress tests for resistant-strain relative fitness multiplier, fR, values from 0.85 to 1.15. (C) Modeled infant cases across resistance-mechanism scenarios. (D) End-period resistant fraction by fR and VE_inf. (E) Modeled infant cases by fR and VE_inf on log10 scale. (F) Transmission-blocking reduction by country at 3 fitness levels. Neutral-fitness panels are mechanistic stress tests, not base-case replacement forecasts.

**Figure 4. Three-Tier Scenario Mechanism Comparisons for Modeled Infant Pertussis Outcomes.** Strategy profiles are grouped by interpretive tier: currently implementable or near-implementable program levers, resistance-management modifiers, and future product targets or stress tests. (A) Distribution of within-country infant-case reduction vs current practice, with profile points and medians across illustrative profiles; empirical IQRs or ranges summarize heterogeneity, not uncertainty. (B) Within-country percentage infant-case reduction vs current practice; cell text gives point estimates, with conditional beta-grid interval audit data retained in the repository output. (C) Median outcomes across illustrative profiles for infant cases, reported cases, and all infections. (D) Baseline infant case incidence with conditional beta-grid intervals. The figure juxtaposes tiers for mechanism interpretation, not policy ranking; conditional intervals are not confidence intervals or full structural or implementation uncertainty.
