# Optimization of Infant Pertussis Prevention and Resistance-Management Strategies

**Article type:** Original Investigation

**Study type:** Decision Analytical Model

**Authors:** Kangguo Li, Yulun Xie, Yunzhi Zenghuang, Tao Chen, Sha Chen, Yue He, Tianmu Chen

**Affiliations:** State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine Laboratory, National Innovation Platform for Industry-Education Integration in Vaccine Research, School of Public Health, Xiamen University, Xiamen, China

**Main text word count:** 2877

## Key Points

**Question:** Which vaccination, exposure-reduction, and resistance-management strategy profiles optimized modeled infant pertussis outcomes under predefined decision constraints?

**Findings:** In this decision analytical model of 10 illustrative country profiles, program-constrained optimization most often selected infant-exposure reduction or routine timeliness as infant-case-minimizing profiles. Resistance-guided management was non-dominated when resistant infections were included as a secondary objective, and future product-target analyses favored profiles with stronger transmission-blocking assumptions.

**Meaning:** Infant pertussis prevention priorities may differ by feasibility constraint, resistance context, and the relative value assigned to infant cases vs resistant infections.

## Abstract

**Importance:** Severe pertussis morbidity and mortality remain concentrated in young infants, but candidate strategies differ in whether they provide direct protection, reduce infant exposure, block onward transmission, or modify macrolide-resistant *Bordetella pertussis* management.

**Objective:** To identify optimized and non-dominated infant pertussis prevention strategy profiles across vaccination, exposure-reduction, resistance-management, and future transmission-blocking vaccine scenarios.

**Design, Setting, and Participants:** Deterministic age-structured decision analytical transmission model with a 15-year burn-in and 26-year saved horizon beginning January 1, 2025, with 5- and 10-year horizon sensitivities. Ten illustrative country profiles used evidence accessed through May 9, 2026. Analyses used population-level inputs.

**Exposures:** Predefined strategy profiles evaluated under 3 optimization constraints: program-only options, program plus resistance-management options, and future product-target options.

**Main Outcomes and Measures:** Primary optimization objective: minimize annualized modeled infant symptomatic cases vs current practice. Secondary outcomes included modeled resistant infections, all infections, reported cases, non-dominated status, and regret.

**Results:** Infant incidence was not directly calibrated. Calibration-window mean absolute percentage error for reported cases was 5.5% (IQR, 3.9%-7.8%). Under program-only constraints, the infant-case-minimizing profile was infant-exposure reduction in 5 profiles, routine timeliness in 4, and adolescent booster scale-up in 1. Infant-exposure reduction and routine timeliness were non-dominated in 8 and 7 profiles, respectively, when implementation intensity was included as an ordinal feasibility proxy. Under program plus resistance-management constraints, the same profiles minimized infant cases, while resistance-guided management became non-dominated in 9 profiles and reduced median resistant infections by 94%. Future product-target analyses favored profiles with stronger transmission-blocking assumptions. In selected-parameter regret analysis, routine timeliness had the lowest mean regret under program-only and program plus resistance constraints; the combined future stress-test profile had the lowest regret under future product-target constraints.

**Conclusions and Relevance:** In this model, constrained outcome optimization favored different strategy profiles depending on implementability and resistance objectives. Because infant incidence was not directly calibrated and no costs, equity weights, or decision thresholds were modeled, findings should be interpreted as constrained strategy-optimization results, not direct incidence forecasts or cost-effectiveness conclusions.

## Introduction

Pertussis prevention programs are built on routine childhood vaccination, but severe disease remains concentrated in young infants who are not yet fully vaccinated.^1-3^ Infant protection depends on pregnancy vaccination, household or caregiver exposure, adolescent and adult transmission, treatment and postexposure prophylaxis (PEP), and broader circulation.^4-6^ These pathways are not interchangeable.

Post-pandemic pertussis resurgence has reinforced this strategy-optimization problem. High childhood coverage remains essential, yet acellular pertussis (aP) vaccines prevent symptomatic disease more reliably than infection or onward transmission, and protection against infection wanes over time.^7-13^

Macrolide-resistant *Bordetella pertussis* (MRBP) adds a management and interpretation challenge. Reports from China, the Americas, Australia, Japan, and global genomic analyses indicate that resistant lineages can expand and spread internationally.^14-21^ Resistance affects the expected value of treatment and PEP, but it should be interpreted as a modifier of vaccination strategy comparisons rather than as a replacement for the infant-protection question.

We used an age-structured decision analytical model to identify optimized and non-dominated infant-protection strategy profiles across vaccination, exposure-reduction, resistance-management, and future product-target scenarios in 10 illustrative country profiles.

## Methods

### Study Design and Decision Frame

This deterministic transmission-modeling study synthesized demographic, surveillance, immunization, contact, treatment, and resistance evidence in a common age-structured pertussis framework. Current practice was each profile's routine vaccination schedule and standard macrolide treatment/PEP assumptions. The analysis evaluated predefined strategy profiles as a constrained outcome-optimization problem and did not estimate cost-effectiveness, costs, utilities, or budget impact. Review board approval and consent were not required because analyses used public or aggregate population-level data. Relevant non-cost CHEERS 2022 elements and WHO immunization-modeling guidance informed reporting.^22,23^

Ten purposively selected profiles were analyzed: Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, the United Kingdom, and the United States. They spanned vaccination schedules, adolescent and pregnancy Tdap programs, surveillance-quality contrasts, contact patterns, and resistance anchors from near-zero to near-fixation, not global or regional averages. Inputs included population, immunization, contact, surveillance, pregnancy-vaccination, and resistance evidence accessed through May 9, 2026.^24-27^

The 2025 start date aligned vaccination, resistance, and surveillance inputs after post-pandemic resurgence. The 26-year horizon (January 1, 2025-December 31, 2050) compared post-rebalancing behavior over vaccine-development and planning timelines; 5- and 10-year windows tested near-term sensitivity. Medians were unweighted across illustrative profiles, not population-weighted or global estimates.

### Model and Calibration

The model tracked 8 age groups, macrolide-sensitive and macrolide-resistant strains, and susceptible vaccine-origin histories reflecting maternal protection and recent or waned dose histories. Four vaccine mechanisms were represented separately: reduced susceptibility to infection (VE_sus), symptoms given infection (VE_sym), onward infectiousness (VE_inf), and infectious duration (VE_dur). Immunity followed an SIRWS structure with immune boosting and waning.^7,8^ Transmission used country-specific contact matrices, seasonality, demography, vaccination maintenance, importation, COVID-19 contact reductions, treatment, and PEP. Supplementary Methods provide equations, and <span style="color:#5DADE2;">eTable 2</span> maps analysis components to parameter settings and provenance.

Calibration targeted reported pertussis case counts over the 6 most recent observed calendar years, except South Africa, where 3 overlapping years were available. The retained fit minimized a negative-binomial reporting-interval likelihood plus penalties for age-specific reporting probabilities outside broad prior bounds. Diagnostics included observed-vs-modeled intervals, fit scores, mean absolute percentage errors, peak timing, and reporting probabilities (<span style="color:#5DADE2;">eFigure 2B and 2D</span> and <span style="color:#5DADE2;">eTables 7 and 12</span>). Consistent age-specific incidence series were unavailable across all profiles, so infant incidence was not directly calibrated.

Aggregate reported cases cannot separately identify transmission, reporting, waning, strain fitness, and age mixing. The principal calibration fitted the country-specific sensitive-strain transmission coefficient and reporting multiplier, with other poorly identified quantities fixed or bounded unless varied in sensitivity analyses. Because strategies were compared within the same calibrated profile against current practice, ordering was interpreted as conditional despite non-identifiability.

### Infant Endpoint Validation and Interpretability

Because comparable infant incidence or age-specific surveillance targets were unavailable across all profiles, the infant endpoint was used only for within-profile scenario comparison. The primary outcome was relative modeled infant-case change conditional on specified assumptions; absolute modeled infant incidence was not used for burden inference. IQRs across illustrative profiles summarize empirical heterogeneity, not uncertainty intervals.

Endpoint plausibility was evaluated with 2 age-pattern diagnostics: public age-distribution summaries vs modeled reported age shares in 4 profiles, and scenario-group ordering reweighted or pass-filtered by agreement. The pass-filter defined acceptable agreement as a country age-pattern weight of at least 0.50 after scaling each external-vs-modeled absolute difference by its prespecified tolerance. These diagnostics tested ordering robustness; they did not externally calibrate infant incidence.

### Strategy Profiles

Strategy profiles were assigned to decision domains used in the optimization constraints (<span style="color:#5DADE2;">Table 1</span> and <span style="color:#5DADE2;">eTable 4</span>). Program-only options included current practice, nominal coverage floor without timeliness improvement, routine timeliness, adolescent booster scale-up, pregnancy Tdap scale-up, close-contact adult adjuncts, infant-exposure reduction, and targeted high-risk PEP. Resistance-management options added resistance-guided treatment and resistant-strain PEP assumptions. Future product-target options included infection-blocking, transmission-blocking, high-transmission-blocking vaccine profiles, and combined scenarios.^28,29^

The nominal coverage floor raised low infant and childhood coverage values without changing dose timeliness. A supplementary program-portfolio factorial layered routine timeliness, infant-exposure reduction, targeted PEP, and resistance-guided management to test feasible combinations separately from primary predefined-profile optimization. The combined future profile was a stress test.

Resistance-guided management was a reduced-form composite rather than a specific diagnostic platform (<span style="color:#5DADE2;">eTable 16</span>). It represented earlier MRBP recognition, shorter treated resistant infectious duration, lower resistant infectiousness, and restored resistant-strain PEP effectiveness, with testing, treatment, adherence, and delivery uncertainty folded into implementation-sensitivity parameters.

### Optimization Objective and Constraints

We defined optimization as identifying strategy profiles that minimized annualized modeled infant symptomatic cases, with secondary consideration of resistant infections, implementation intensity, and robustness. This was constrained outcome optimization, not cost-effectiveness analysis. Program-only optimization allowed current or near-current program levers. Program plus resistance-management optimization added resistance-guided management. Future product-target optimization added transmission-blocking vaccine assumptions and the combined future stress-test profile.

Dominance was assessed within each country and constraint: a strategy was dominated if another allowed strategy had at least as large an infant-case reduction, at least as large a resistant-infection reduction, and no greater implementation-intensity score, with improvement in at least 1 dimension. Preferred profiles minimized infant cases under each constraint; non-dominated sets defined decision frontiers rather than a single recommendation. Implementation-intensity scores were prespecified ordinal categories based on the number and operational complexity of added components, with the rubric and sensitivity checks in the Supplement; they were not interpreted as costs.

The primary estimand was within-profile relative change in annualized modeled infant symptomatic cases over the 26-year saved horizon. Secondary outcomes included all infections, reported cases, resistant infections, and resistant fraction. Modeled infant incidence was treated as a descriptive internal diagnostic. Relative change was calculated as 1 - Z/Z0, where Z was the strategy outcome and Z0 was current practice.

### Sensitivity Analysis

Sensitivity analyses addressed vaccine-mechanism thresholds, reporting, infant contacts, treatment/PEP implementation, temporal windows, timeliness mechanisms, scenario ordering, and regret. Minimum-regret analyses calculated excess modeled infant cases vs the best allowed strategy in the same country-sample draw; standardized regret divided this excess by current-practice modeled infant cases. Resistance-management tradeoffs used lambda-weighted benefit scores, in which higher values favored larger infant-case and resistant-infection reductions, and epsilon constraints on resistant-infection reduction. Conditional beta-grid intervals propagated only transmission-rate uncertainty, and Latin-hypercube analyses were deterministic sensitivity envelopes. Because infant incidence, scenario reach, and structural assumptions were not jointly identifiable, optimization results were interpreted as conditional prioritization, not effect-size estimation.

## Results

### Endpoint Validation and Baseline Infant Cases

Across the 10 calibrated profiles, current-practice modeled annual infant case incidence ranged from 16 per 100,000 infants in Thailand to 2393 in Australia (<span style="color:#5DADE2;">Figure 1D</span>), an internal descriptive diagnostic. The fitted reported-case calibration-window target had mean absolute percentage error of 5.5% (IQR, 3.9%-7.8%), with median absolute peak-timing error of 1 year (<span style="color:#5DADE2;">eTable 7</span>). Infant incidence was not directly calibrated.

Baseline profiles differed in resistance and surveillance scale. Starting resistant fractions ranged from 0% in the United States to 99.7% in China, with high starting resistance in Japan and lower but nonzero anchors elsewhere. Saved-horizon reported incidence under current practice ranged from less than 1 to 52 reported cases per 100,000 population per year, while all-infection incidence exceeded reported incidence in every profile.

External age-pattern checks for 4 profiles, not calibration targets, were mixed (<span style="color:#5DADE2;">Supplementary Methods</span>). Agreement was closest for the United States and moderate for Sweden/EU/EEA; the United Kingdom and Australia were less consistent.^32-35^ Sweden and the United States were interpreted as externally supported, Australia and the United Kingdom as externally discordant, and the remaining 6 profiles as not externally assessed. Aggregate calibration fit did not validate infant incidence or age-specific burden.

### Optimization Under Program-Only Constraints

Under program-only constraints (<span style="color:#5DADE2;">Figure 4A and 4B</span>), the infant-case-minimizing profile was infant-exposure reduction in 5 country profiles, routine timeliness in 4, and adolescent booster scale-up in 1. With implementation intensity included in the dominance rule, infant-exposure reduction was non-dominated in 8 profiles and routine timeliness in 7; current practice also remained non-dominated as the lowest-intensity reference but was not infant-case minimizing. The nominal coverage floor without timeliness improvement showed little modeled infant-case change (median reduction across illustrative profiles, -1%; IQR, -5% to -1%).

**Interpretation of the nominal coverage-floor scenario.** This scenario evaluated marginal nominal coverage increases in mostly high-coverage profiles, without timeliness improvement or transmission blocking; it was not evidence against routine vaccination. Routine timeliness lowered modeled infant cases in all 10 profiles (median reduction, 35%; IQR, 31%-51%) (<span style="color:#5DADE2;">eFigure 9A</span>).

Pregnancy Tdap scale-up had a 12% median modeled infant-case reduction across illustrative profiles (IQR, 10%-14%). The close-contact adult adjunct had a 37% median reduction, driven mainly by adult boosting. The infant-exposure composite had a 45% median reduction (IQR, 25%-77%) and combined direct passive protection, close-contact adult protection, and reproductive-age adult boosting (<span style="color:#5DADE2;">eFigure 7C</span>). Targeted high-risk PEP had a 5% median reduction.

Program levers acting through older-age transmission were more heterogeneous. Infant-exposure reduction yielded 38% lower median modeled reported cases and 35% lower all infections across illustrative profiles.

### Optimization With Resistance Management

Adding resistance-guided management did not change the primary infant-case-minimizing profile in any country: program plus resistance-management optimization still selected infant-exposure reduction in 5 profiles, routine timeliness in 4, and adolescent booster scale-up in 1 (<span style="color:#5DADE2;">Figure 4A</span>). However, resistance-guided management became non-dominated in 9 profiles because it substantially reduced resistant infections while not always minimizing all-strain infant cases. Under the specified resistance-guided composite, modeled annualized resistant infections declined from a median across illustrative profiles of 574 to 2 per 100,000; the median resistant-infection reduction was 94% across all profiles and 97% (IQR, 62%-100%) among 9 nonzero-resistance profiles (<span style="color:#5DADE2;">Figure 4B</span>).

Resistance stress tests showed strong dependence on strain fitness and treatment/PEP differentials: the median end resistant fraction was 99.7% under neutral-fitness country-timeline assumptions, 1% after equalizing both treatment and PEP effects, and less than 0.1% with resistant-strain relative fitness, fR, of 0.85 (<span style="color:#5DADE2;">eFigure 10A and 10B</span>). Higher VE_inf lowered modeled infant cases across fitness assumptions.

A consolidated resistance-management decomposition separated long-horizon selection mechanisms (treatment differential, PEP differential, both combined, fitness, and importation) from near-term implementation levers (testing/treatment uptake, resistant-strain PEP restoration, and PEP reach) (<span style="color:#5DADE2;">eFigure 10A-C</span>). Partial uptake with restored PEP showed median modeled infant-case changes ranging from -16% to 16%. Large resistant-infection reductions could coexist with variable infant-case effects because case treatment and contact PEP changed strain competition and resistant-source timing more directly than all-strain infant exposure.

In preference-threshold analyses, resistance-guided management entered the preferred set in 6 profiles when resistant-infection reduction received modest additional weight; in 3 profiles, it required near-dominant weighting of resistant-infection outcomes, and it was never preferred in the United States, where baseline resistant infections were zero (<span style="color:#5DADE2;">Figure 4C</span> and <span style="color:#5DADE2;">eFigure 10D</span>). With at least 50% resistant-infection reduction required, resistance-guided management was preferred in 6 profiles, with median standardized infant-case regret of 8.1%.

The supplementary program-portfolio factorial ranked a layered timeliness, infant-exposure, targeted PEP, and resistance-management package lowest for modeled infant cases in all 10 profiles, with a median 83% infant-case reduction (IQR, 65%-94%) (<span style="color:#5DADE2;">eFigure 11A</span>). Because this package combined multiple implementation-dependent assumptions, it tested layering logic rather than defining a primary preferred strategy.

### Future Product-Target Mechanism Analysis

Future product-target analyses favored profiles with stronger transmission-blocking assumptions rather than symptom protection alone (<span style="color:#5DADE2;">Figure 4A and 4D</span>). Within this hypothetical domain, the combined future stress-test profile was lowest in 8 profiles and the high-transmission-blocking vaccine target in 2. Across illustrative profiles, these profiles had median infant-case reductions of 99% and 97%, respectively. The transmission-blocking-only target had a median 95% reduction but was dominated by profiles with stronger combined infection, transmission, or management effects.

Vaccine profiles with stronger infection or transmission effects yielded progressively lower modeled infant-case and population infection outcomes (<span style="color:#5DADE2;">Figure 2A, 2B, and 2D</span>). Compared with no vaccination, the symptom-protective aP-like profile yielded an 82% simulated infant-case reduction. Threshold analyses showed that VE_inf values near 0.35 to 0.50 were needed to cross selected infant-case reduction or comparator thresholds when other vaccine mechanisms were held fixed (<span style="color:#5DADE2;">eFigure 10E</span>).

High-transmission-blocking vaccine and combined stress-test profiles had median modeled infant-case reductions of 97% or higher, but these were product-target and stress-test results, not available policy options.

### Robustness, Regret, and Age-Pattern Filtering

In the selected-parameter sensitivity envelope (128 Latin-hypercube parameter sets by 10 profiles), routine timeliness had the lowest mean regret under program-only constraints (10.1 infant cases per 100,000/y; standardized mean regret, 3.9% of current-practice infant cases; best in 71% of country-sample observations) and under program plus resistance-management constraints (11.5 per 100,000/y; standardized mean regret, 4.1%; best in 69%) (<span style="color:#5DADE2;">Figure 4E</span>). Resistance-guided management had higher mean infant-case regret under program plus resistance-management constraints (434.0 per 100,000/y; standardized mean regret, 26.0%) but remained non-dominated for resistant-infection secondary outcomes. Under future product-target constraints, the combined future stress-test profile had lower mean regret than the high-transmission-blocking vaccine target (43.5 vs 103.8 per 100,000/y; standardized mean regret, 1.8% vs 6.9%) and was best in 69% of country-sample observations.

The primary endpoint robustness check addressed mixed age-pattern validation. Reweighting the 4 external-check profiles did not change qualitative optimization grouping. A stricter pass-filter retained Sweden and the United States, excluding Australia and the United Kingdom; grouping again remained stable, with only an exact-order swap between high-transmission-blocking product-target and combined stress-test classes (<span style="color:#5DADE2;">eFigure 9F</span>). These ordering diagnostics were optimization robustness checks only.

Near-term 5- and 10-year windows retained the broad grouping (<span style="color:#5DADE2;">eFigure 9B</span>). Infant-contact and maternal-protection sensitivity analyses changed absolute infant-case levels more than strategy grouping (<span style="color:#5DADE2;">eFigure 11B and 11C</span>).

## Discussion

This decision analytical model used constrained outcome optimization to identify non-dominated infant pertussis prevention strategy profiles across program, resistance-management, and future vaccine-product scenarios. The principal finding was that optimized profiles differed by decision constraint: program-only optimization favored routine timeliness or infant-exposure reduction in most profiles, resistance-inclusive optimization added resistance-guided management as a non-dominated secondary-objective option, and future product-target optimization emphasized the value of onward-transmission blocking.

Program-only scenarios were closest to implementable decisions. Pregnancy Tdap scale-up yielded modest, consistent modeled infant-case reductions, consistent with maternal vaccination studies.^26,27^ The infant-exposure composite showed larger reductions but depended on adult boosting, contact assumptions, and pregnancy Tdap. Targeted high-risk PEP should be read as outbreak or contact-management support.^30,31^ Nominal coverage-floor findings were not evidence against childhood vaccination; they reflected marginal nominal changes without timeliness improvement or stronger transmission blocking.

Resistance-management options changed resistant-infection outcomes but were reduced-form proxies for testing reach, detection, alternative-drug availability, PEP implementation, adherence, and resistant-strain fitness. Decomposition analyses therefore support interpreting the resistance-guided profile as a family of policy levers rather than a single black-box intervention. Recent MRBP reports support treating resistance as a modifier of strategy value and uncertainty; where MRBP is plausible, vaccine strategy assessment should be paired with isolate or sequencing surveillance, susceptibility reporting, and explicit PEP assumptions.^14-21,30,31^

The supplementary program-portfolio factorial supported layered local planning, but the highest-performing package had the greatest implementation intensity; primary inferences therefore remain based on predefined strategy profiles under explicit feasibility constraints.

Future product targets clarified why transmission blocking matters. A symptom-protective aP-like profile yielded lower modeled infant cases than no vaccination, but stronger infection- and transmission-blocking profiles lowered residual infant cases and total infections.^9,13,28,29^

Policy translation requires surveillance quality, feasibility, cost, equity, acceptability, household contact structure, diagnostic capacity, resistance testing infrastructure, decision thresholds, and implementation evidence.

### Limitations

This study has limitations. First, infant incidence was not directly calibrated; the estimand was within-profile relative change, absolute modeled infant-case estimates are not national forecasts, and infant-outcome optimization is less secure where external age-pattern agreement was discordant or unassessed. Second, IQRs across illustrative profiles are heterogeneity summaries, and uncertainty analyses did not jointly propagate structural, data, parameter, and scenario uncertainty. Third, strategy profiles are simplified proxies rather than country-specific programs; adherence, contact tracing, stochastic fadeout, and individual heterogeneity were not modeled. Fourth, the 26-year horizon depends on waning, demography, and resistance assumptions, although 5- and 10-year diagnostics supported the same broad grouping. Fifth, this was constrained outcome optimization rather than economic evaluation; future vaccine profiles were hypothetical, and burden translations excluded costs, equity weights, utilities, budget constraints, and decision thresholds.

## Conclusions

Constrained outcome optimization identified different preferred infant pertussis prevention strategy profiles under program-only, resistance-management, and future product-target constraints. Relative changes and non-dominated status are the primary interpretable quantities; absolute country-specific infant rates are conditional diagnostics.

## Supplement

**Supplement 1.** eMethods (full model equations, country-profile construction, calibration methods, optimization definitions, scenario definitions, resistance hindcast plausibility checks, parameter identifiability classification), eReferences, <span style="color:#5DADE2;">eFigures 1-11</span>, and <span style="color:#5DADE2;">eTables 1-17</span>.

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

**Data Sharing Statement:** Processed inputs, model code, configuration files, generated outputs, figure source data, and reproducibility files are publicly available without access restrictions at https://github.com/xmusphlkg/pertussis_transmission_analysis. The final submission package should be archived with a versioned repository commit or release DOI. No individual-level participant data were used or are available.

**Additional Contributions:** None.

**Use of Artificial Intelligence:** OpenAI Codex coding assistant (GPT-5; OpenAI; API-based Codex interface; used May 2026) was used for code assistance, manuscript-edit implementation, language organization, pipeline execution support, and consistency checks. AI-assisted wording was incorporated only after author review and editing. The tool did not independently generate data, define analytic decisions, select assumptions, or replace author verification. The authors take full responsibility for the integrity and accuracy of the final manuscript.

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

**Table 1. Strategy Optimization Domains and Main Modeling Assumptions.**

| Decision domain | Scenario | Implementable now? | Main assumption changed | Primary intended mechanism | Key caveat |
| --- | --- | ---: | --- | --- | --- |
| Program-only option | Current practice | Yes | Country-specific vaccination schedule, coverage, treatment, and PEP assumptions retained | Baseline for within-profile relative reductions | Not a no-vaccination counterfactual |
| Program-only option | Nominal coverage floor without timeliness improvement | Yes/partly | Infant and childhood coverage values below floors raised; countries already above floors unchanged | More nominal routine vaccine-origin coverage | Does not evaluate routine vaccination versus no vaccination; does not improve timeliness or transmission blocking |
| Program-only option | Timeliness improvement sensitivity | Yes/partly | Faster movement toward age-appropriate infant-series vaccine-origin targets | Earlier direct infant protection | Implementation dependent and modeled as sensitivity analysis |
| Program-only option | Adolescent booster scale-up | Yes/partly | Adolescent coverage floor raised while current aP-like mechanism retained | Reduced older-child and adolescent contribution to transmission | Indirect infant effects depend on age mixing and aP transmission blocking |
| Program-only option | Pregnancy Tdap scale-up | Yes | Birth-entry passive-protection target raised to 75% | Direct early-infant passive protection | Country-specific uptake pathways not fully modeled |
| Program-only option | Infant-exposure composite | Partly | Pregnancy Tdap, close-contact adult protection, reproductive-age adult boosting, and 15% adult-to-infant contact reduction combined | Lower infant exposure from direct and indirect sources | Implementation-dependent composite, not a single program |
| Program-only option | Targeted high-risk PEP | Yes/partly | PEP reach among eligible household contacts, infants, and high-risk settings raised to 45% | Reduced infection after recognized exposure | Depends on detection, contact tracing, timing, and adherence |
| Resistance-management option | Resistance-guided management | Partly | Composite of rapid molecular testing, culture/susceptibility testing, sequencing, or empiric alternative therapy; resistant-strain PEP effectiveness restored | Lower resistant-strain transmission under specified management assumptions | Reduced-form proxy for testing, turnaround, uptake, alternative treatment, PEP delivery, and adherence |
| Future product target or stress test | High-transmission-blocking vaccine | No | Upper-bound vaccine profile: VE_sus 0.80, VE_sym 0.90, VE_inf 0.65, VE_dur 0.40 | Lower susceptibility and onward transmission | Hypothetical product-target scenario |
| Future product target or stress test | Combined profile | No | Transmission-blocking vaccine assumptions, pregnancy Tdap, adult/contact adjuncts, adolescent boosting, targeted PEP, and resistance-guided management combined | Upper-bound multi-mechanism contrast | Non-implementable future stress test |

Abbreviations: aP, acellular pertussis; PEP, postexposure prophylaxis; VE_dur, vaccine effectiveness against infectious duration; VE_inf, vaccine effectiveness against onward infectiousness; VE_sus, vaccine effectiveness against susceptibility; VE_sym, vaccine effectiveness against symptoms given infection.

## Figure Legends

**Figure 1. Calibration, Country-Profile Heterogeneity, and Baseline Infant Cases.** (A) WHO regional reported pertussis incidence for context, not global representativeness. (B) Country profile dimensions. (C) Saved-horizon annualized modeled reported incidence vs recent observed mean reported incidence; this scale diagnostic is not the calibration-window likelihood target. Dashed line indicates equality and color indicates resistant infection fraction. (D) Baseline all infections, reported cases, and infant cases per 100,000 on log scale. Infant rates are descriptive model diagnostics, not national forecasts.

**Figure 2. Vaccine Transmission-Blocking Properties and Infant-Case Reduction.** (A) VE_sus, VE_sym, VE_inf, and VE_dur values for 5 vaccine profiles. (B) Modeled infant cases by vaccine profile and country. (C) Vaccine-history origin decomposition by profile. (D) All infections by vaccine profile and country. Panels B and D show profile points, medians across illustrative profiles, and empirical heterogeneity intervals.

**Figure 3. Macrolide Resistance as a Management and Uncertainty Modifier.** (A) Country-timeline resistant-fraction dynamics under neutral-fitness stress-test assumptions. (B) Fitness-dependent resistant-fraction stress tests for selected resistant-strain relative fitness multipliers, fR. (C) Modeled infant cases across resistance-mechanism scenarios on log scale. (D) End-period resistant fraction by fR and VE_inf. (E) Modeled infant cases by fR and VE_inf on log10 scale. (F) Transmission-blocking reduction by country at 3 fitness levels. Neutral-fitness panels are mechanistic stress tests, not base-case replacement forecasts.

**Figure 4. Decision-Framework Optimization Results for Infant Pertussis Prevention Strategies.** Strategy profiles are evaluated under constrained outcome optimization, not cost-effectiveness analysis. (A) Country-by-strategy heatmap of infant-case reduction vs current practice; black borders mark non-dominated cells and asterisks mark the infant-case-preferred profile within each constraint. (B) Non-dominated decision frontier in the 2 explicit outcome dimensions; filled points are primary-preferred, open points are non-dominated-only, and size indicates ordinal implementation intensity. (C) Preference-weight curve as resistant-infection reduction received increasing weight relative to infant-case reduction. (D) Multi-outcome heatmap showing median reductions in infant cases, resistant infections, reported cases, and all infections for decision-relevant profiles. (E) Selected-parameter robustness heatmap; color shows mean standardized infant-case regret and text shows Pr(best). Optimization results are conditional model outputs, not direct incidence forecasts or cost-effectiveness conclusions.
