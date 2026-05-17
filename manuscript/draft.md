# Vaccine Transmission Blocking, Macrolide Resistance, and Pertussis Intervention Prioritization: A Decision Analytical Model

**Article type:** Original Investigation; Decision Analytical Model

**Target journal:** JAMA Network Open

**Authors:** Kangguo Li, [coauthors to be added]

**Affiliations:** [Affiliations to be added]

## Key Points

**Question:** How do vaccine transmission-blocking effects and macrolide resistance jointly alter projected pertussis infant burden and intervention rankings across heterogeneous national settings?

**Findings:** In this decision analytical model spanning 10 country profiles, resistance-guided treatment reduced infant cases by 50.8% (IQR, 35.7%–62.7%) and maternal immunization by 59.9% (IQR, 27.7%–83.1%) vs current practice, whereas higher child coverage alone produced minimal additional benefit (−4.1%). The symptom-protective acellular pertussis-like profile reduced infant cases by 84.6% (IQR, 75.0%–96.8%) vs no vaccination; profiles with stronger transmission blocking approached near-elimination in the deterministic model.

**Meaning:** Pertussis decision models should distinguish clinical protection from transmission blocking and incorporate resistance-aware treatment assumptions; intervention rankings shift substantially when these mechanisms are modeled explicitly.

## Abstract

**Importance:** Pertussis persists despite high acellular vaccine coverage, and macrolide-resistant *Bordetella pertussis* (MRBP) has spread rapidly across multiple continents since 2020, reaching near-fixation in China and high prevalence in Japan. Decision models that conflate symptom protection with transmission blocking may misrepresent intervention value.

**Objective:** To evaluate how vaccine transmission-blocking mechanisms, macrolide resistance prevalence, and combined intervention strategies influence projected pertussis infant burden and intervention prioritization.

**Design, Setting, and Data Sources:** A deterministic age-structured pertussis transmission model with 8 age groups, 2 strain classes (macrolide-sensitive and macrolide-resistant), explicit maternal and dose-history immunity states, country-specific contact matrices, and probabilistic sensitivity analysis. Ten country profiles spanning 5 WHO regions were modeled using United Nations population data, WHO/UNICEF immunization records, Prem social contact matrices, and resistance evidence through 2025. Simulations used a 15-year burn-in and a 26-year analysis horizon beginning January 1, 2025, aligned with UN World Population Prospects 2024 projections through 2050.

**Exposures:** Vaccine mechanism profiles (symptom-protective, infection-blocking, transmission-blocking, and next-generation), initial macrolide resistance prevalence (country-specific timelines and fixed scenarios), and intervention strategies (higher child coverage, adolescent boosting, maternal immunization, resistance-guided treatment, next-generation vaccination, and a combined strategy).

**Main Outcomes and Measures:** Annualized infant symptomatic cases per 100,000 infants, all infections per 100,000 persons, reported cases, resistant infections, resistant fraction, and relative reductions vs comparators.

**Results:** Baseline annualized infant case incidence ranged from 17 per 100,000 (United Kingdom) to 1,648 (China); resistant fractions under country-timeline anchoring had a median of 1.0% (IQR, 1.0%–3.7%). Compared with no vaccination, the symptom-protective profile reduced infant cases by 84.6% (IQR, 75.0%–96.8%); the infection-blocking profile by 99.9% (IQR, 96.5%–100.0%); and the next-generation profile by 100.0% (IQR, 99.8%–100.0%). Median infant-case reductions vs current practice were −4.1% for higher child coverage, 59.9% for maternal immunization, 50.8% for resistance-guided treatment, 99.1% for next-generation vaccination, and 99.3% for the combined strategy. The near-elimination under infection-blocking and next-generation profiles reflects the deterministic model's herd-immunity threshold behavior and should be interpreted as upper-bound product-profile projections.

**Conclusions and Relevance:** In this decision analytical model, intervention rankings depended on vaccine transmission-blocking properties and resistance-aware treatment. Pertussis decision analyses should report infant burden, total transmission, and resistant infections as distinct outcomes and should distinguish clinical protection from effects on onward transmission.

## Introduction

Pertussis has resurged globally in the post-pandemic period, with China reporting a 65-fold increase in cases between 2023 and 2024, Japan recording over 60,000 cases in the first 7 months of 2025 (a 10-fold increase over 2024), and South Korea reporting a greater than 20-fold increase.^1-5^ These outbreaks occurred despite high primary vaccination coverage (94%–97% DTP3), underscoring that acellular pertussis (aP) vaccines, while effective against severe disease, provide incomplete and waning protection against infection and onward transmission.^6-12^

The distinction between clinical protection and transmission blocking has become operationally important. Nonhuman primate studies demonstrate that aP-vaccinated animals develop reduced symptoms but remain colonized and transmit *B pertussis* to naive contacts.^8^ Epidemiologic modeling and meta-analyses confirm that aP-derived protection against infection wanes substantially within 3 to 5 years, while protection against severe disease persists longer.^9-12^ This mechanistic gap means that high routine coverage may reduce disease burden without proportionally reducing circulation, leaving infants—who are too young for complete vaccination—exposed through household and community transmission from older age groups.

Simultaneously, macrolide-resistant *B pertussis* (MRBP) has emerged as a global concern. The MT28-ptxP3 clone carrying the 23S rRNA A2047G mutation escalated from less than 50% prevalence in China before 2020 to near-complete fixation (>99%) by 2024, and has since spread to Japan, Australia, the Americas, and Europe.^13-20^ Genomic surveillance confirms that resistance escalated mechanistically through the A2047G mutation and is linked to vaccine-driven genomic evolution including ptxP3 dominance and pertactin deficiency.^17,18^ This rapid global dissemination without apparent fitness cost challenges the assumption that resistant strains carry a transmission disadvantage and raises the prospect that macrolide treatment and postexposure prophylaxis (PEP)—standard first-line interventions—may become progressively less effective.

Most pertussis policy models report vaccine effectiveness as a single composite endpoint and do not explicitly model how transmission-blocking properties interact with antimicrobial resistance to shape intervention value. We developed a decision analytical transmission model to address this gap. The model compares vaccine mechanism assumptions, macrolide resistance scenarios, and intervention strategies across 10 country profiles, with the primary aim of identifying how transmission-blocking vaccine effects and resistance-aware management alter projected infant cases, total infections, and resistant infections.

## Methods

### Study Design and Decision Context

This study used a deterministic, age-structured compartmental model of pertussis transmission designed as a decision analytical model. The model synthesized demographic, surveillance, immunization, contact, treatment, and resistance evidence from multiple sources and compared consequences of alternative decision options under a unified mechanistic framework. The model does not predict specific national future epidemics; rather, it compares how vaccine transmission-blocking effects and resistance-aware management alter projected infant burden and intervention rankings. The analysis followed relevant non-cost elements of the Consolidated Health Economic Evaluation Reporting Standards (CHEERS) 2022 reporting framework and the WHO 2025 guidance for using modelling for immunization decision-making.^21,22^ Because the model used aggregated public data and simulated populations, institutional review board review was not applicable.

### Country Profiles and Data Sources

Ten national profiles were analyzed: Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, the United Kingdom, and the United States. The set was purposive rather than globally representative, selected to span 5 WHO regions (Western Pacific, South-East Asian, European, Americas, and African), contrasting population sizes, heterogeneous booster and maternal immunization program signatures, varied reported incidence levels, and both measured high-resistance and conservative low-resistance anchors. Population denominators came from United Nations World Population Prospects 2024; immunization inputs from WHO/UNICEF Joint Reporting Form and national schedule records; social contact matrices from Prem et al aggregated to 8 model age groups with population-weighted reciprocity correction; and resistance anchors from the latest admissible country-specific evidence through 2025.^23-26^

### Model Structure

The model tracked 8 age groups (0–2 months, 3–11 months, 1–4 years, 5–9 years, 10–17 years, 18–39 years, 40–64 years, and ≥65 years), chosen to separate the maternal protection window, primary immunization series, school-age booster period, adolescent waning period, reproductive-age adults (primary infant contact source), and elderly populations with distinct clinical presentation. Infections were divided into macrolide-sensitive and macrolide-resistant strains. Susceptible individuals retained origin histories (unvaccinated, maternally protected, 1-dose recent/waned, 2-dose recent/waned, 3-or-more-dose recent/waned), so that four vaccine mechanism parameters—VE_sus (reduced susceptibility to infection), VE_sym (reduced symptomatic disease), VE_inf (reduced onward infectiousness), and VE_dur (reduced infectious duration)—could act on infection source history rather than on a single aggregate vaccinated state. The resulting state space comprised 73 compartments per age group (584 total state variables).

Transmission was driven by country-specific contact matrices, annual seasonality, demographic aging and birth turnover, routine vaccination maintenance, low-level importation, and strain-specific treatment effects. The force of infection incorporated postexposure prophylaxis as a prevalence-triggered modifier with strain-specific effectiveness, so that macrolide resistance directly reduced PEP benefit without requiring a separate prophylaxis compartment.

### Vaccine Mechanism Scenarios

Five vaccine profiles were compared: no vaccine; symptom-protective (aP-like: VE_sus=0.15, VE_sym=0.85, VE_inf=0.25, VE_dur=0.00); infection-blocking (VE_sus=0.70, VE_inf=0.40); transmission-blocking (VE_inf=0.55, VE_dur=0.30); and next-generation (VE_sus=0.80, VE_sym=0.90, VE_inf=0.65, VE_dur=0.40). The aP-like VE_inf of 0.25 represents the time-averaged population effect accounting for rapid waning from initial approximately 50%–60% to less than 10% within 3–5 years post-vaccination.^8-12^ The next-generation profile represents mucosal immunity-inducing platforms (live-attenuated nasal or outer membrane vesicle vaccines) currently in preclinical and early clinical development.^27^

### Resistance Scenarios and Fitness Assumptions

Resistance scenarios used either country-specific timelines (anchored to the latest evidence: China >99% in 2024, Japan 83%–88% in 2024–2025, Australia 4.3% in 2024) or fixed low (5%), moderate (30%), high (70%), and very high (95%) resistant prevalence. The baseline fitness assumption was neutral (fitness_R = 1.00), reflecting the observed rapid fixation of MRBP in China within 8 years and intercontinental spread without apparent transmission disadvantage.^14-18^ A continuous fitness grid (fitness_R = 0.70–1.25) evaluated the sensitivity of resistance dynamics and infant burden to this assumption. Resistance hindcast validation against observed trajectories in China, Japan, and Australia assessed model plausibility.

### Intervention Strategies

Seven strategies were compared against current practice: higher child coverage (+10 percentage points), adolescent boosting, maternal immunization (decomposed into direct antibody protection, adult boosting, and cocooning components), resistance-guided treatment (alternative antibiotics restoring treatment effectiveness for resistant infections), next-generation vaccination, and a combined strategy (next-generation vaccine + resistance-guided treatment + maternal immunization). Reporting-rate sensitivity analyses perturbed only the observation layer without altering treatment-driven resistance selection pressure.

### Uncertainty and Sensitivity Analysis

Probabilistic sensitivity analysis used Latin hypercube sampling (48 parameter sets) varying vaccine effects, immunity waning, transmission, treatment, PEP, resistance fitness, and reporting. Parameter-outcome associations were summarized using Pearson correlations. A Bayesian posterior predictive analysis using adaptive Metropolis MCMC was conducted; convergence was assessed using rank-normalized split-R̂ (<1.05) and bulk effective sample size (>100). If convergence criteria were not met, probabilistic sensitivity intervals from Latin hypercube sampling were reported instead of Bayesian credible intervals.

## Results

### Baseline Country Heterogeneity

The 10 calibrated country profiles produced wide variation in projected burden under current aP-like vaccination and country-specific resistance anchors (Figure 1). Annualized infant case incidence ranged from 4,539 per 100,000 infants in South Africa to 11,775 in China, while all-infection incidence ranged from 5,867 to 7,822 per 100,000 persons. Reported incidence ranged from 98 to 145 per 100,000, reflecting both transmission differences and age-specific reporting assumptions. Under the neutral-fitness country-timeline scenario, resistant fractions had a median of 99.3% (IQR, 99.2%–99.6%) at the start of the analysis period and reached near-fixation by the end, consistent with the observed rapid spread of MRBP in China and Japan and the neutral-fitness baseline assumption.

### Vaccine Mechanism Scenarios

Vaccine profiles with stronger transmission-blocking properties produced progressively larger reductions in both infant cases and total infections (Figure 2). Compared with no vaccination, the symptom-protective aP-like profile reduced infant cases by 53.1% (IQR, 51.3%–55.2%) and total infections by 11.5% (IQR, 9.3%–12.7%). The infection-blocking profile reduced infant cases by 66.2% (IQR, 62.5%–66.8%) and total infections by 22.6% (IQR, 17.6%–25.3%). The next-generation profile achieved the largest reductions: infant cases by 74.1% (IQR, 69.3%–75.0%) and resistant infections by 28.8% (IQR, 22.1%–31.9%). The gap between infant-case reduction and total-infection reduction widened as VE_inf increased, indicating that transmission-blocking effects propagate beyond direct protection to reduce population-level circulation.

### Macrolide Resistance and Transmission-Blocking Interaction

Resistant infection burden was sensitive to initial resistance prevalence, importation, and resistant-strain fitness (Figure 3). Under the neutral-fitness assumption, resistance reached near-fixation within 2–3 years regardless of starting prevalence. Even with a moderate fitness cost (fitness_R = 0.85), resistance exceeded 90% within 3 years; fitness advantages accelerated convergence to near-complete dominance within 1 year. Across the VE_inf–resistance grid, increasing vaccine reduction in infectiousness from 0% to 75% reduced infant cases by 98.7% (IQR, 80.7%–99.6%), demonstrating that transmission-blocking vaccines retain substantial value even when macrolide treatment is compromised by resistance. The benefit of transmission blocking was robust across fitness assumptions and heterogeneous across epidemiological settings.

### Intervention Prioritization

Intervention rankings were heterogeneous across countries but showed consistent patterns (Figure 4). Higher child coverage alone had a median infant-case effect of −2.6% (IQR, −3.9% to −1.9%) vs current practice, indicating minimal marginal benefit in already high-coverage settings. Maternal immunization reduced infant cases by 3.8% (IQR, 3.1%–4.3%), with the direct antibody protection component contributing the largest share. Resistance-guided treatment produced a median reduction of 34.0% (IQR, 32.3%–36.1%), with benefit scaling with starting resistance prevalence. Next-generation vaccination reduced infant cases by 42.8% (IQR, 36.5%–46.1%). The combined strategy achieved the largest reduction: 53.0% (IQR, 48.9%–54.0%). The largest absolute screening correlations with infant cases were waning rate of natural immunity (r = 0.54), asymptomatic infectious duration (r = 0.52), and resistance fitness (r = 0.51), indicating that immunity dynamics and resistance assumptions are the primary drivers of outcome uncertainty.

[NOTE: All quantitative results in this section are from a prior model run and must be regenerated from the current frozen configuration before submission.]

## Discussion

This decision analytical model demonstrates that pertussis control conclusions change materially when vaccines are allowed to differ in their effects on infection, symptoms, infectiousness, and duration, and when macrolide resistance is incorporated into treatment and prophylaxis assumptions. Three principal findings emerge.

First, the distinction between clinical protection and transmission blocking has quantifiable consequences for projected infant burden. A symptom-protective aP-like profile substantially reduced infant cases compared with no vaccination (53.1%), but profiles with stronger transmission blocking produced progressively larger reductions in both infant cases and total infections. This finding is consistent with the nonhuman primate evidence that aP vaccination prevents disease but not colonization or transmission,^8^ and with epidemiologic observations that pertussis circulation persists in highly vaccinated populations.^1-5^ The implication is that policy models reporting only composite vaccine effectiveness may underestimate the potential benefit of next-generation vaccines designed to induce mucosal immunity and reduce transmission.^27^

Second, resistance-guided treatment emerged as a high-value intervention (34.0% infant-case reduction) that does not require new vaccine development. This finding reflects the model's explicit representation of how macrolide resistance reduces treatment and PEP effectiveness: when resistance is prevalent, standard macrolide therapy provides diminished benefit, and alternative antibiotics that restore treatment effectiveness produce substantial gains. The benefit scales with starting resistance prevalence, suggesting that settings with documented high MRBP prevalence (China, Japan) would benefit most from resistance-aware clinical management. This aligns with recent public health alerts from PAHO and CDC emphasizing the need for antimicrobial susceptibility testing and alternative treatment protocols.^15,16^

Third, intervention rankings depended on the interaction between vaccine mechanism and resistance. Higher child coverage alone produced minimal additional benefit in already high-coverage profiles (−2.6%), consistent with the theoretical expectation that marginal coverage gains in settings above 90% DTP3 are less influential than interventions targeting transmission routes, infant protection, or treatment effectiveness. The combined strategy achieved the largest reductions by simultaneously addressing transmission (next-generation vaccine), treatment failure (resistance-guided therapy), and direct infant protection (maternal immunization).

These findings should be interpreted in the context of the current global pertussis resurgence. The post-pandemic period has seen unprecedented outbreaks across the Western Pacific, with Japan recording over 60,000 cases in 2025 and genomic surveillance confirming intercontinental spread of macrolide-resistant clones.^3,4,17^ A recent multi-country transmission modeling study similarly identified waning aP immunity and incomplete transmission blocking as key drivers of resurgence, though without explicitly modeling resistance interactions.^28^ Our analysis extends this work by demonstrating that resistance-aware management and transmission-blocking vaccine properties jointly determine intervention value—a finding that becomes increasingly relevant as MRBP prevalence rises globally.

### Limitations

This analysis has several limitations. First, it is a deterministic compartmental model that does not represent stochastic extinction, household clustering, or superspreading; these features may affect outbreak dynamics in small populations. Second, the model uses exponential waning of both natural and vaccine-derived immunity without explicit immune boosting from subclinical re-exposure; sensitivity analyses comparing alternative immunity structures are provided in the supplement. Third, country profiles combine measured inputs, processed surveillance summaries, and explicit assumptions; cross-country contrasts should be interpreted as conditional scenario comparisons under a harmonized model rather than definitive national forecasts. Fourth, reporting probabilities are literature-informed and calibrated pragmatically, but direct age- and country-specific reporting fractions remain sparse; reporting-rate sensitivity analyses perturb only the observation layer and do not alter resistance selection pressure. Fifth, resistance anchors are heterogeneous in recency and certainty; resistance hindcast validation against observed trajectories in China, Japan, and Australia is provided to assess plausibility, but fixed resistance and fitness-grid scenarios should be read as stress tests rather than forecasts. Sixth, the next-generation vaccine profile (VE_sus = 0.80, VE_inf = 0.65) represents an aspirational product target based on mucosal vaccine platforms in early development; results for this profile should be interpreted as upper-bound estimates of what improved transmission blocking could achieve. Finally, the model does not include costs or quality-adjusted life-years, so results inform epidemiologic prioritization rather than economic adoption decisions.

## Conclusions

Across 10 country profiles, vaccine transmission-blocking properties and macrolide resistance materially shaped pertussis burden and intervention rankings. Resistance-guided treatment and next-generation vaccines with stronger transmission blocking produced larger projected infant-case reductions than marginal increases in child coverage alone. Decision analyses for pertussis should report infant burden, total infections, and resistant infections as distinct outcomes, distinguish clinical protection from effects on onward transmission, and incorporate resistance-aware treatment assumptions.

## Figure Legends

**Figure 1. Global Context, Country Selection, and Baseline Heterogeneity.** (A) WHO regional reported pertussis incidence, establishing the surveillance backdrop for the 10-country set across 5 WHO regions. (B) Country selection basis showing profile dimensions (WHO region, population size, reported incidence, starting resistant fraction, and programme signature). (C) Model-data reported incidence calibration: observed vs modelled annual reported incidence, with points colored by resistant infection fraction. Dashed line indicates equality. (D) Baseline burden metrics (all infections, reported cases, infant cases per 100,000) by country on log scale, with probabilistic sensitivity intervals when available.

**Figure 2. Vaccine Mechanism Scenarios.** (A) Vaccine scenario parameter matrix showing VE_sus, VE_sym, VE_inf, and VE_dur values for 5 profiles. (B) Infant-case reduction vs no vaccine by country and scenario (forest plot with cross-country median). (C) Infection-source decomposition by vaccine profile, showing how stronger profiles shift the origin composition of infections. (D) Total infection reduction vs infant-case reduction trade-off; points above the diagonal indicate disproportionately stronger infant-case reduction.

**Figure 3. Macrolide Resistance and Vaccine Transmission Blocking.** (A) Resistance takeover dynamics over 5 years by country under country-specific timelines. (B) Fitness-dependent takeover speed (median ± IQR) for fitness_R = 0.85–1.15. (C) Infant burden across resistance scenarios by country. (D) Resistance equilibrium heatmap (fitness × VE_inf). (E) Infant disease burden heatmap (fitness × VE_inf, log10 scale)—anchor panel demonstrating that higher VE_inf reduces infant burden regardless of resistance fitness. (F) Transmission-blocking benefit by country at 3 fitness levels.

**Figure 4. Intervention Prioritization.** (A) Infant-case reduction by intervention and country vs current practice (individual country points with cross-country medians and IQR). (B) Country × strategy heatmap with annotated percentage values. (C) Median intervention effect across outcomes (infant cases, reported cases, all infections), demonstrating consistent rankings across outcome measures. (D) Resistance-guided treatment benefit vs starting resistant fraction, showing that benefit scales with resistance prevalence; or Bayesian posterior predictive intervals when MCMC convergence is achieved.

## Supplement

**Supplement 1.** eMethods (full model equations, country-profile construction, calibration methods, scenario definitions, resistance hindcast validation, parameter identifiability classification), eReferences, eFigures 1–13, and eTables 1–11.

## Article Information

**Accepted for Presentation:** [To be added if applicable]

**Corresponding Author:** [Name, degree, postal address, email]

**Author Contributions:** [Author name] had full access to all data and code in the study and takes responsibility for the integrity of the data and the accuracy of the analysis. Concept and design: [to be completed]. Acquisition, analysis, or interpretation of data: [to be completed]. Drafting of the manuscript: [to be completed]. Critical revision of the manuscript for important intellectual content: [to be completed]. Statistical analysis: [to be completed]. Administrative, technical, or material support: [to be completed]. Supervision: [to be completed].

**Conflict of Interest Disclosures:** [To be completed.]

**Funding/Support:** [To be completed.]

**Role of the Funder/Sponsor:** [To be completed.]

**Data Sharing Statement:** Publicly available processed inputs, model code, configuration files, and generated outputs will be shared in a repository at [repository URL/DOI to be added]. No individual-level participant data were used.

**Additional Contributions:** [To be completed.]

**Use of Artificial Intelligence:** AI-assisted drafting and code-assistance tools (Claude, Anthropic) were used to help organize manuscript text, implement model code, and perform implementation checks. The authors reviewed and edited all content and take full responsibility for the final manuscript.

## References

1. World Health Organization. Pertussis vaccines: WHO position paper, August 2015. *Wkly Epidemiol Rec*. 2015;90:433-458.
2. Cai J, Liu Q, Chen B, et al. Waning immunity, prevailing non-vaccine type ptxP3 and macrolide-resistant strains in the 2024 pertussis outbreak in China: a multicentre cross-sectional descriptive study. *Lancet Reg Health West Pac*. 2025;60:101628. doi:10.1016/j.lanwpc.2025.101628
3. Pertussis resurgence after the COVID-19 pandemic in four Western Pacific Countries and the USA, highlighting the 2025 outbreak in Japan. *Sci Rep*. 2026. doi:10.1038/s41598-026-47780-4
4. Serial interval and intervention efficiency in pertussis outbreak, South Korea, 2024. *Emerg Infect Dis*. 2026;32(5). doi:10.3201/eid3205.251304
5. Global drivers and implications of pertussis resurgence in the acellular vaccine era. *PubMed*. 2025. PMID:41600951.
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
16. Pan American Health Organization. PAHO calls for strengthened vaccination and surveillance amid spread of antibiotic-resistant pertussis. August 26, 2025. https://www.paho.org/en/news/26-8-2025
17. Genomic surveillance reveals global spread of macrolide-resistant *Bordetella pertussis* linked to vaccine changes. *PubMed*. 2025. PMID:41236009.
18. Fong W, Rockett RJ, Tam KKG, et al. Characterisation of *Bordetella pertussis* virulence and macrolide resistance in Australia by targeted culture-independent sequencing: a genomic epidemiology study. *Lancet Microbe*. 2026;7:101286. doi:10.1016/j.lanmic.2025.101286
19. Komatsu S, Nakanishi N, Matsubara K, et al. Molecular analysis of emerging MT27 macrolide-resistant *Bordetella pertussis*, Kobe, Japan, 2025. *Emerg Infect Dis*. 2026;32:150-153. doi:10.3201/eid3201.250890
20. Localized outbreak of macrolide-resistant pertussis in infants, Japan, March–May 2025. *Emerg Infect Dis*. 2026;32(1). doi:10.3201/eid3201.250824
21. Husereau D, Drummond M, Augustovski F, et al. Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) statement. *BMJ*. 2022;376:e067975. doi:10.1136/bmj-2021-067975
22. World Health Organization. Guidance for using modelling for immunization decision-making. Geneva: WHO; 2025.
23. United Nations Department of Economic and Social Affairs, Population Division. World Population Prospects 2024. Accessed May 9, 2026. https://population.un.org/wpp/
24. Prem K, Cook AR, Jit M. Projecting social contact matrices in 152 countries using contact surveys and demographic data. *PLoS Comput Biol*. 2017;13:e1005697. doi:10.1371/journal.pcbi.1005697
25. Amirthalingam G, Andrews N, Campbell H, et al. Effectiveness of maternal pertussis vaccination in England: an observational study. *Lancet*. 2014;384:1521-1528. doi:10.1016/S0140-6736(14)60686-3
26. Baxter R, Bartlett J, Fireman B, Lewis E, Klein NP. Effectiveness of vaccination during pregnancy to prevent infant pertussis. *Pediatrics*. 2017;139:e20164091. doi:10.1542/peds.2016-4091
27. New life into pertussis prevention. *Nat Microbiol*. 2025. doi:10.1038/s41564-025-02169-3
28. Identifying drivers of pertussis disease resurgence: pilot study final report. *medRxiv*. 2025. doi:10.1101/2025.05.22.25328117
29. Centers for Disease Control and Prevention. Treatment of pertussis and postexposure antimicrobial prophylaxis. Accessed May 9, 2026. https://www.cdc.gov/pertussis/hcp/clinical-care/index.html
30. Clarkson JA, Fine PEM. The efficiency of measles and pertussis notification in England and Wales. *Int J Epidemiol*. 1985;14:153-168. doi:10.1093/ije/14.1.153
31. Crowcroft NS, Johnson C, Chen C, et al. Under-reporting of pertussis in Ontario. *PLoS One*. 2018;13:e0195984. doi:10.1371/journal.pone.0195984
32. Evolutionary dynamics and global spread of macrolide-resistant *Bordetella pertussis* during the post-pandemic pertussis resurgence. *PubMed*. 2026. PMID:41802571.
33. Innovative adjuvant strategies for next-generation pertussis vaccines. *PMC*. 2025. PMC12351750.
34. Pertussis resurgence: epidemiological trends, pathogenic mechanisms, and preventive strategies. *Front Immunol*. 2025. doi:10.3389/fimmu.2025.1618883
