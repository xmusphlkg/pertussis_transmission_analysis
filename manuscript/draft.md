# Transmission-Blocking Pertussis Vaccines, Macrolide Resistance, and Intervention Prioritization

**Article type:** Original Investigation; Decision Analytical Model

**Target journal:** JAMA Network Open

**Authors:** Kangguo Li, [coauthors to be added]

**Affiliations:** [Affiliations to be added]

## Key Points

**Question:** How do vaccine transmission-blocking effects and macrolide resistance interact to shape pertussis burden and intervention prioritization across heterogeneous national settings?

**Findings:** In this decision analytical model across 10 country profiles, an acellular pertussis-like vaccine reduced infant cases by 53.1% (IQR, 51.3% to 55.2%) vs no vaccination, while infection-blocking and next-generation profiles produced larger reductions (66.2% and 74.1%, respectively). Bayesian posterior predictive analysis estimated current-profile infant incidence at 9,029 per 100,000 (95% CrI, 130 to 20,757). Resistance-guided treatment, next-generation vaccines, and combined strategies outperformed higher child coverage alone, with the combined strategy reducing infant cases by 53.0% (IQR, 48.9% to 54.0%) vs current practice.

**Meaning:** Pertussis control assessments should distinguish clinical protection from transmission blocking and include resistance-aware management outcomes.

## Abstract

**Importance:** Pertussis persists despite acellular vaccine programs, and macrolide-resistant *Bordetella pertussis* has been reported in multiple settings. Decision models should distinguish symptom protection from transmission blocking.

**Objective:** To evaluate how vaccine mechanisms, macrolide resistance, and intervention strategies influence pertussis burden.

**Design, Setting, and Data Sources:** This decision analytical model used a deterministic age-structured pertussis transmission model with 8 age groups, 2 strain classes, maternal and dose-history states, country-specific contacts, vaccination profiles, seasonality, reported-case calibration, and Bayesian posterior predictive uncertainty analysis. Ten country profiles were modeled. Main simulations used a 60-year burn-in and a 26-year analysis beginning January 1, 2025.

**Exposures:** Vaccine mechanisms, initial resistant prevalence, child coverage, adolescent boosting, maternal immunization, resistance-guided treatment, next-generation vaccine properties, and combined strategies.

**Main Outcomes and Measures:** Annualized infant cases, all infections, reported cases, resistant infections, resistant fraction, and relative reductions vs comparators.

**Results:** Baseline annualized infant case incidence ranged from 4,539 in South Africa to 11,775 in China; all-infection incidence ranged from 5,867 to 7,822 per 100,000. Bayesian posterior predictive analysis estimated current-profile infant incidence at 9,029 per 100,000 (95% CrI, 130 to 20,757) and end-period resistant fraction near fixation (median 100%). Starting resistant fractions had a median of 99.3% (IQR, 99.2% to 99.6%) under country-timeline anchoring. Compared with no vaccination, the symptom-protective profile reduced infant cases by 53.1% (IQR, 51.3% to 55.2%) and total infections by 11.5% (IQR, 9.3% to 12.7%). The next-generation profile reduced infant cases by 74.1% (IQR, 69.3% to 75.0%) and resistant infections by 28.8% (IQR, 22.1% to 31.9%). Median infant-case reductions vs current practice were −2.6% for higher child coverage, 3.8% for maternal immunization, 34.0% for resistance-guided treatment, 42.8% for next-generation vaccination, and 53.0% for the combined strategy.

**Conclusions and Relevance:** In this model, intervention rankings depended on vaccine transmission-blocking effects and resistance-aware treatment. The combined strategy (next-generation vaccine + resistance-guided treatment + maternal immunization) achieved the largest infant-case reductions (53.0%), while resistance-guided treatment alone provided meaningful benefit (34.0%). Pertussis decision analyses should include infant burden, total transmission, and resistant infections as distinct outcomes.

## Introduction

Pertussis remains a public health problem in countries with mature vaccination programs. Acellular pertussis vaccines reduce severe clinical disease, but multiple lines of epidemiologic, immunologic, and experimental evidence suggest that protection wanes and that prevention of colonization or onward transmission may be incomplete.1-9 These features complicate interpretation of reported pertussis trends because surveillance captures only a fraction of infections, especially in adolescents and adults, while infants remain at greatest risk of severe outcomes.10-13

Macrolides are standard first-line agents for pertussis treatment and postexposure prophylaxis, but macrolide-resistant *B pertussis* has become a practical concern. Reports from China, Japan, Australia, the Americas, and other settings indicate that resistance prevalence is geographically heterogeneous and may change rapidly.14-20 Resistance can reduce the expected effect of treatment and prophylaxis, making it important to consider antimicrobial susceptibility alongside vaccine mechanism.

Most policy-facing summaries of pertussis vaccination emphasize disease prevention, but control decisions also depend on transmission, infant protection, reporting, treatment, and resistance. We therefore developed a decision analytical transmission model to compare vaccine mechanism assumptions, macrolide resistance scenarios, and intervention strategies across 10 country profiles. The primary aim was to identify how transmission-blocking vaccine effects and resistance-aware management alter projected infant cases, total infections, reported cases, and resistant infections.

## Methods

### Study Design

This study used a deterministic, age-structured compartmental model of pertussis transmission. The model was designed as a decision analytical model because it synthesized demographic, surveillance, immunization, contact, treatment, and resistance evidence from multiple sources and compared consequences of alternative decision options. The analysis followed relevant non-cost elements of the CHEERS 2022 reporting framework for model-based decision studies. Because the model used aggregated public data and simulated populations, institutional review board review and informed consent were not applicable; this should be confirmed by the submitting institution.

### Country Profiles and Data Sources

Nine national profiles were analyzed: Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, the United Kingdom, and the United States. The set was purposive rather than globally representative and was selected to span Western Pacific, South-East Asian, European, Americas, and African settings; different population sizes; contrasting booster and maternal immunization program signatures; heterogeneous reported incidence; and both measured and conservative low resistance anchors. Population denominators came from United Nations World Population Prospects; immunization and schedule inputs came from WHO/UNICEF and national schedule extracts; social contact matrices were based on Prem/contactdata matrices aggregated to the 8 model age groups; and all available harmonized surveillance reporting intervals were used for reported incidence, seasonality, and calibration. Resistance anchors used the latest admissible country-specific evidence through 2025.

### Model Structure

The model tracked 8 age groups: 0 to 2 months, 3 to 11 months, 1 to 4 years, 5 to 9 years, 10 to 17 years, 18 to 39 years, 40 to 64 years, and 65 years or older. Infections were divided into macrolide-sensitive and macrolide-resistant strains. Susceptible individuals retained origin histories corresponding to unvaccinated status, maternal protection, 1-dose recent or waned protection, 2-dose recent or waned protection, and 3-or-more-dose recent or waned protection. Exposed, infectious, and treated states retained these origins so vaccine effects on susceptibility, symptom probability, infectiousness, and infectious duration could act on infection source history rather than on a single aggregate vaccinated state.

Transmission was driven by country-specific contact matrices, annual seasonality, demographic aging and birth turnover, routine vaccination maintenance, importation, and strain-specific treatment and prophylaxis effects. Country-level calibration targeted recent reported-case intervals using accepted calibration artifacts; production scenario runs then retained the configured 60-year burn-in and 30-year 2026-start analysis horizon. The main outcomes were annualized infant symptomatic cases per 100,000 infants, all infections per 100,000 persons, reported cases per 100,000 persons, resistant infections, resistant fraction, and relative reduction vs the relevant comparator.

### Scenarios

Vaccine scenarios contrasted no vaccine, an acellular pertussis-like symptom-protective profile, stronger infection blocking, stronger transmission blocking, and next-generation protection. In the notation used here, VE_sus denotes protection against infection through reduced susceptibility, whereas VE_inf denotes reduced onward infectiousness among infected vaccine-history origins. Resistance scenarios used either country-specific resistance timelines or fixed low, moderate, high, and very high resistant prevalence. A 7-by-7 interaction grid varied vaccine reduction in infectiousness and initial resistant prevalence, and a continuous fitness_R grid evaluated resistant strains with equal or higher transmissibility than sensitive strains. Intervention strategies represented current practice, higher child coverage, adolescent boosting, maternal immunization, resistance-guided treatment, next-generation vaccination, and a combined strategy. Reporting-rate, Bayesian posterior predictive, and global sensitivity analyses evaluated observation uncertainty and parameter influence.

## Results

### Baseline Country Heterogeneity

The calibrated country profiles produced wide variation in projected burden under current acellular pertussis-like vaccination and country-specific resistance anchors. Annualized infant case incidence ranged from 4,539 per 100,000 in South Africa to 11,775 in China, while all-infection incidence ranged from 5,867 to 7,822 per 100,000. Reported incidence ranged from 98 to 145 per 100,000, reflecting both transmission differences and age-specific observation assumptions. Resistant fractions under country-timeline anchoring had a median of 99.3% (IQR, 99.2% to 99.6%) at the start of the analysis period and reached near-fixation (median 100%) by the end, consistent with the neutral-fitness baseline assumption and the observed rapid spread of macrolide-resistant *B pertussis* in China, Japan, and other settings.

### Vaccine Mechanism Scenarios

Compared with no vaccination, the symptom-protective acellular pertussis-like profile reduced infant cases by 53.1% (IQR, 51.3% to 55.2%) and total infections by 11.5% (IQR, 9.3% to 12.7%). Scenarios with stronger infection blocking produced larger reductions: the infection-blocking profile reduced infant cases by 66.2% (IQR, 62.5% to 66.8%) and total infections by 22.6% (IQR, 17.6% to 25.3%). The next-generation profile reduced infant cases by 74.1% (IQR, 69.3% to 75.0%) and resistant infections by 28.8% (IQR, 22.1% to 31.9%), indicating that vaccine effects on infectiousness can influence both clinical and resistance-related outcomes.

### Macrolide Resistance and Transmission Blocking

Fixed resistance scenarios showed that resistant infection burden and resistant fraction were sensitive to initial resistance prevalence, importation, and resistant-strain fitness. Median annualized infant case incidence under the low-resistance scenario was 211.2 (IQR, 20.6 to 301.4); resistant fractions were 11.0% (IQR, 3.8% to 29.5%) in the high-resistance scenario and 42.2% (IQR, 5.9% to 76.9%) in the very-high-resistance scenario. In the continuous fitness stress test, the median effect was 97.7% (IQR, 90.9% to 99.5%) higher end-period resistant fraction when fitness_R increased from 0.70 to 1.25. Across the VE_inf-resistance grid, increasing vaccine reduction in infectiousness from 0.0% to 75.0% reduced infant cases by 98.7% (IQR, 80.7% to 99.6%), supporting the importance of transmission-blocking effects when resistance threatens treatment and prophylaxis performance.

### Intervention Prioritization

Intervention rankings were heterogeneous across countries. Higher child coverage alone had a median infant-case effect of −2.6% (IQR, −3.9% to −1.9%) vs current practice, whereas maternal immunization reduced infant cases by 3.8% (IQR, 3.1% to 4.3%), resistance-guided treatment by 34.0% (IQR, 32.3% to 36.1%), next-generation vaccination by 42.8% (IQR, 36.5% to 46.1%), and the combined strategy by 53.0% (IQR, 48.9% to 54.0%). The largest absolute screening correlations with infant cases were waning_rate_natural (r=0.54), infectious_duration_asymptomatic (r=0.52), fitness_R (r=0.51).

## Discussion

In this decision analytical model, pertussis control conclusions changed when vaccines were allowed to differ in protection against infection, symptoms, infectiousness, and duration. A symptom-protective acellular pertussis-like profile substantially reduced infant cases compared with no vaccination, but profiles with stronger transmission blocking produced larger reductions in total infections and resistant infections. This distinction matters because transmission outcomes affect population-level recurrence, infant exposure risk, and the frequency of infections for which treatment and prophylaxis may be compromised by macrolide resistance.

The findings also suggest that intervention choices should not be evaluated only through routine child coverage. In several modeled settings, adolescent boosting, maternal immunization, resistance-guided treatment, next-generation vaccine assumptions, and combined strategies produced larger median infant-case reductions than higher child coverage alone. This does not imply that routine coverage is unimportant; rather, in high-coverage profiles, marginal increases in child coverage may be less influential than interventions that alter transmission among older age groups, protect the youngest infants directly, or restore treatment effectiveness for resistant infections.

This analysis has limitations. It is a deterministic compartmental model and does not explicitly represent stochastic extinction, household clustering, or superspreading. The Bayesian posterior predictive analysis propagates parameter and observation uncertainty through the deterministic model, but it should not be interpreted as an individual-based transmission reconstruction. Country profiles combine measured inputs, processed surveillance summaries, and explicit assumptions; therefore, cross-country contrasts should be interpreted as conditional scenario comparisons under a harmonized model rather than definitive national forecasts. Reporting probabilities are literature-informed and calibrated pragmatically, but direct age- and country-specific reporting fractions remain sparse. Resistance anchors are heterogeneous in recency and certainty, and fixed resistance and fitness-grid scenarios should be read as stress tests rather than forecasts of clonal spread. Finally, the model does not include costs, quality-adjusted life-years, or formal cost-effectiveness thresholds, so the results inform epidemiologic prioritization rather than economic adoption decisions.

## Conclusions

Across 10 country profiles, vaccine transmission blocking and macrolide resistance materially shaped pertussis burden and intervention rankings. Decision analyses for pertussis should report infant burden, total infections, reported cases, and resistant infections, and should distinguish clinical protection from effects on onward transmission.

## Figure Legends

**Figure 1. Global context, country selection, and baseline heterogeneity.** Reported pertussis incidence, country selection characteristics, model-data reported-incidence anchors, baseline burden metrics, resistance trajectories, and epidemic recurrence diagnostics across the 10 country profiles.

**Figure 2. Vaccine mechanism scenarios.** Infant cases, relative infant-case reductions, trade-offs between total infection and infant-case reductions, and resistant infection reductions under no vaccine, symptom-protective, infection-blocking, transmission-blocking, and next-generation vaccine profiles.

**Figure 3. Macrolide resistance and vaccine transmission blocking.** Resistant fraction trajectories, infant burden under resistance scenarios, median infant burden across the VE_inf-resistance grid, and country-specific benefits of high vaccine transmission blocking.

**Figure 4. Intervention prioritization.** Infant-case reductions, infection-burden trade-offs, median intervention effects across outcomes, and the relationship between starting resistance and benefit from resistance-guided treatment.

## Supplement

**Supplement 1.** eMethods, eReferences, eFigures 1-12, and eTables 1-11.

The supplement includes full model equations, country-profile construction, calibration methods, scenario definitions, sensitivity analyses, data provenance, calibration diagnostics, model architecture, contact matrix reconstruction, and generated tables aligned with the analysis pipeline.

## Article Information

**Accepted for Presentation:** [To be added if applicable]

**Corresponding Author:** [Name, degree, postal address, email]

**Author Contributions:** [Author name] had full access to all data and code in the study and takes responsibility for the integrity of the data and the accuracy of the analysis. Concept and design: [to be completed]. Acquisition, analysis, or interpretation of data: [to be completed]. Drafting of the manuscript: [to be completed]. Critical revision of the manuscript for important intellectual content: [to be completed]. Statistical analysis: [to be completed]. Administrative, technical, or material support: [to be completed]. Supervision: [to be completed].

**Conflict of Interest Disclosures:** [To be completed.]

**Funding/Support:** [To be completed.]

**Role of the Funder/Sponsor:** [To be completed.]

**Data Sharing Statement:** Publicly available processed inputs, model code, configuration files, and generated outputs will be shared in a repository at [repository URL/DOI to be added]. No individual-level participant data were used.

**Additional Contributions:** [To be completed.]

**Use of Artificial Intelligence:** Drafting and code-assistance tools were used to help organize manuscript text and implementation checks. The authors reviewed and edited all content and are responsible for the final manuscript. [Revise to match journal and institutional disclosure requirements.]

## References

1. World Health Organization. Pertussis vaccines: WHO position paper, August 2015. Weekly Epidemiological Record. 2015;90:433-458.
2. Wearing HJ, Rohani P. Estimating the duration of pertussis immunity using epidemiological signatures. PLoS Pathog. 2009;5:e1000647. doi:10.1371/journal.ppat.1000647
3. Lavine JS, King AA, Bjornstad ON. Natural immune boosting in pertussis dynamics and the potential for long-term vaccine failure. Proc Natl Acad Sci U S A. 2011;108:7259-7264. doi:10.1073/pnas.1014394108
4. Domenech de Celles M, Magpantay FMG, King AA, Rohani P. The impact of past vaccination coverage and immunity on pertussis resurgence. Sci Transl Med. 2018;10:eaaj1748. doi:10.1126/scitranslmed.aaj1748
5. Althouse BM, Scarpino SV. Asymptomatic transmission and the resurgence of *Bordetella pertussis*. BMC Med. 2015;13:146. doi:10.1186/s12916-015-0382-8
6. Warfel JM, Zimmerman LI, Merkel TJ. Acellular pertussis vaccines protect against disease but fail to prevent infection and transmission in a nonhuman primate model. Proc Natl Acad Sci U S A. 2014;111:787-792. doi:10.1073/pnas.1314688110
7. McGirr A, Fisman DN. Duration of pertussis immunity after DTaP immunization: a meta-analysis. Pediatrics. 2015;135:331-343. doi:10.1542/peds.2014-1729
8. Chit A, Zivaripiran H, Shin T, Lee JKH, Tomovici A, Macina D. Acellular pertussis vaccines effectiveness over time: a systematic review, meta-analysis and modeling study. PLoS One. 2018;13:e0197970. doi:10.1371/journal.pone.0197970
9. Klein NP, Bartlett J, Rowhani-Rahbar A, Fireman B, Baxter R. Waning protection after fifth dose of acellular pertussis vaccine in children. N Engl J Med. 2012;367:1012-1019. doi:10.1056/NEJMoa1200850
10. Amirthalingam G, Andrews N, Campbell H, Ribeiro S, Kara E, Donegan K. Effectiveness of maternal pertussis vaccination in England: an observational study. Lancet. 2014;384:1521-1528. doi:10.1016/S0140-6736(14)60686-3
11. Baxter R, Bartlett J, Fireman B, Lewis E, Klein NP. Effectiveness of vaccination during pregnancy to prevent infant pertussis. Pediatrics. 2017;139:e20164091. doi:10.1542/peds.2016-4091
12. Clarkson JA, Fine PEM. The efficiency of measles and pertussis notification in England and Wales. Int J Epidemiol. 1985;14:153-168. doi:10.1093/ije/14.1.153
13. Crowcroft NS, Johnson C, Chen C, Li Y, Marchand-Austin A, Bolotin S. Under-reporting of pertussis in Ontario: a Canadian Immunization Research Network study using capture-recapture. PLoS One. 2018;13:e0195984. doi:10.1371/journal.pone.0195984
14. Centers for Disease Control and Prevention. Treatment of pertussis and postexposure antimicrobial prophylaxis. Accessed May 9, 2026. https://www.cdc.gov/pertussis/hcp/clinical-care/index.html
15. Centers for Disease Control and Prevention. Antibiotic-resistant *Bordetella pertussis*. Accessed May 9, 2026. https://www.cdc.gov/pertussis/hcp/antibiotic-resistance/index.html
16. Fu P, Zhou J, Yang C, Nijati Y, Zhou L, Jiang W. Molecular evolution and increasing macrolide resistance of *Bordetella pertussis*, Shanghai, China, 2016-2022. Emerg Infect Dis. 2024;30:117-127. doi:10.3201/eid3001.221588
17. Cai J, Liu Q, Chen B, Jiang Y, Zeng X, Huang J. Waning immunity, prevailing non-vaccine type ptxP3 and macrolide-resistant strains in the 2024 pertussis outbreak in China: a multicentre cross-sectional descriptive study. Lancet Reg Health West Pac. 2025;60:101628. doi:10.1016/j.lanwpc.2025.101628
18. Fong W, Rockett RJ, Tam KKG, Nguyen T, Sim EM, Tay E. Characterisation of *Bordetella pertussis* virulence and macrolide resistance in Australia by targeted culture-independent sequencing: a genomic epidemiology study. Lancet Microbe. 2026;7:101286. doi:10.1016/j.lanmic.2025.101286
19. United Nations Department of Economic and Social Affairs, Population Division. World Population Prospects 2024. Accessed May 9, 2026. https://population.un.org/wpp/
20. Prem K, Cook AR, Jit M. Projecting social contact matrices in 152 countries using contact surveys and demographic data. PLoS Comput Biol. 2017;13:e1005697. doi:10.1371/journal.pcbi.1005697
21. Husereau D, Drummond M, Augustovski F, et al. Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) statement: updated reporting guidance for health economic evaluations. BMJ. 2022;376:e067975. doi:10.1136/bmj-2021-067975
