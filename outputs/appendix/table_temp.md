## eTables

### eTable 1. Country-profile selection rationale and resistance anchors.

| Country | WHO region | Program profile | Resistance anchor | Data quality | Reason for inclusion |
| --- | --- | --- | --- | --- | --- |
| Australia | Western Pacific | aP vaccine; DTP3 92.66%; 6 routine doses; adolescent booster; maternal 20-32w | 4.30% (2024) | High | High recent reported incidence; measured low but detectable resistance; mature maternal and booster program. |
| Brazil | Americas | wP vaccine; DTP3 88.91%; 5 routine doses; no adolescent booster; maternal 20-32w | 1.00% (2025) | Moderate | Large Americas profile with wP schedule, maternal program, and detected resistant cases without national fraction. |
| China | Western Pacific | aP vaccine; DTP3 98.80%; 4 routine doses; no adolescent booster; no routine maternal program | 99.70% (2024) | High | Large population, marked post-pandemic resurgence, and near-complete measured macrolide resistance anchor. |
| Japan | Western Pacific | aP vaccine; DTP3 98.62%; 4 routine doses; no adolescent booster; no routine maternal program | 82.70% (2025) | High | Western Pacific resurgence and high measured resistance in 2024-2025 reports. |
| New Zealand | Western Pacific | aP vaccine; DTP3 87.91%; 5 routine doses; adolescent booster; maternal 16-26w | 1.00% (2025) | Moderate | Small high-income profile with maternal and adolescent programs and emerging resistance concern. |
| South Africa | African | aP vaccine; DTP3 73.90%; 6 routine doses; adolescent booster; maternal 26-34w | 2.00% (2025) | Moderate | African-region profile with shorter overlapping calibration window and contrasting demography. |
| Sweden | European | aP vaccine; DTP3 95.00%; 5 routine doses; adolescent booster; maternal 16-36w | 1.00% (2025) | High | European profile with high-quality surveillance and booster program contrast. |
| Thailand | South-East Asia | wP vaccine; DTP3 89.22%; 5 routine doses; no adolescent booster | 1.00% (2025) | Moderate | South-East Asian low reported-incidence profile with wP schedule and low maternal coverage. |
| United Kingdom | European | aP vaccine; DTP3 91.70%; 4 routine doses; no adolescent booster; maternal 16-32w | 0.30% (2024) | High | European maternal-program profile with established pregnancy vaccination and surveillance data. |
| United States | Americas | aP vaccine; DTP3 94.00%; 6 routine doses; adolescent booster; maternal 27-36w | 0.00% (2015) | High | Large Americas profile with adolescent and maternal Tdap program and low reported resistance. |

<div style="page-break-after: always;"></div>

### eTable 2. Study parameter-design matrix for scenario, sensitivity, and uncertainty analyses.

| Analysis component | Design level | Parameter settings | Source/provenance | Fixed or conditioned assumptions | Primary role | Detailed location |
| --- | --- | --- | --- | --- | --- | --- |
| Country profiles and calibration | Ten calibrated country profiles | Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, United Kingdom, and United States; country-specific demography, contact matrices, vaccination schedules and coverage, seasonality, surveillance intervals, resistance anchors, calibrated $beta_{S}$, and reporting multipliers. | Population denominators [13], schedule and coverage records [14], contact matrices [15-17], reported-case intervals [18], treatment and PEP assumptions [19,20], resistance guidance [21,22], and country resistance reports [23,24], [25], [26], [27], [28,29]; calibrated $beta_{S}$ and reporting multipliers are model-estimated from reported-case intervals. | Common deterministic ODE structure, age partition, natural-history defaults, 15-year burn-in, and 2025-2050 saved horizon. | Defines calibrated current-practice comparators and cross-country heterogeneity. | eTables 1, 5, 7, 9, and 12. |
| Vaccine-mechanism profile | No vaccine | $VE_{sus}$=0.00; $VE_{sym}$=0.00; $VE_{inf}$=0.00; $VE_{dur}$=0.00 | Null counterfactual with all vaccine-effect parameters set to zero; no external efficacy claim. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | No vaccine protection. | Figure 2A and eTables 14 and 22. |
| Vaccine-mechanism profile | Current aP profile | $VE_{sus}$=0.15; $VE_{sym}$=0.85; $VE_{inf}$=0.25; $VE_{dur}$=0.00 | Acellular-pertussis-like disease protection, asymptomatic-transmission structure, incomplete infection blocking, and waning informed by the WHO vaccine framework [1], transmission evidence [5,6], and duration-of-protection studies [7-9]. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | aP-like disease protection with moderate infection/transmission blocking. The high $VE_{sym}$ value is literature-supported for disease protection, while $VE_{sus}$, $VE_{inf}$, and $VE_{dur}$ are a mechanistic decomposition of that evidence rather than directly observed surveillance parameters. $VE_{inf}$ = 0.25 represents a population-average residual transmission-blocking assumption across recently and distantly vaccinated individuals. | Figure 2A and eTables 14 and 22. |
| Vaccine-mechanism profile | Infection-blocking | $VE_{sus}$=0.70; $VE_{sym}$=0.85; $VE_{inf}$=0.40; $VE_{dur}$=0.10 | Mechanistic scenario above the population-average aP profile, bounded by vaccine-framework assumptions [1], transmission evidence [5,6], and waning studies [7-9], then checked against vaccine-pipeline interpretation in eTable 22. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | Stronger reduction in susceptibility to infection. $VE_{inf}$ = 0.40 represents a plausible upper mechanism bound for recently boosted or more infection-blocking protection, not a direct empirical estimate for current aP products. | Figure 2A and eTables 14 and 22. |
| Vaccine-mechanism profile | Transmission-blocking | $VE_{sus}$=0.30; $VE_{sym}$=0.85; $VE_{inf}$=0.55; $VE_{dur}$=0.30 | Improved-transmission-blocking scenario informed by the WHO vaccine framework [1], aP/wP transmission evidence [5,6], waning studies [7-9], and product-target reasoning in eTable 22; not a licensed product estimate. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | Strong reduction in onward infectiousness and duration. Represents an improved aP formulation or wP-like transmission blocking. | Figure 2A and eTables 14 and 22. |
| Vaccine-mechanism profile | Upper-bound transmission-blocking | $VE_{sus}$=0.80; $VE_{sym}$=0.90; $VE_{inf}$=0.65; $VE_{dur}$=0.40 | Upper-bound high-transmission-blocking product-target profile; represented as a hypothetical mechanism profile using vaccine-framework assumptions [1], transmission evidence [5,6], waning studies [7-9], and pipeline mapping in eTable 22. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | Strong infection, symptom, and transmission protection. Represents an upper-bound high-transmission-blocking pertussis vaccine profile with mucosal immunity induction (e.g. live-attenuated nasal or outer membrane vesicle platforms). | Figure 2A and eTables 14 and 22. |
| Macrolide-resistance scenario | Country timeline | target resistant fraction=0.30; importation resistant fraction=0.30; anchor rate/y=2.00; country timeline=Yes; $f_R$=1.00; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Country-specific resistance anchors combined clinical guidance [21,22] with country reports from China [23,24], Australia [25], Japan [26], the Americas [27], and regional MRBP evidence [28,29]; raw evidence is tabulated in eTable 6 and parameter rationale in eTable 23. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Country-specific macrolide resistance prevalence from data/raw/country_resistance_timeline.csv. The prevalence anchors are data-derived. $f_R$ = 1.00 is an epidemiologically motivated neutral baseline, not a directly measured strain-fitness estimate: China MRBP rose from 36% (2016) to near-fixation (>99%, 2024), and related MRBP lineages were reported internationally without clear transmission disadvantage. The fitness grid and fitness sensitivity scenarios explore the full range [0.70-1.25]. | eTables 3, 6, 13, and 23. |
| Macrolide-resistance scenario | Low | target resistant fraction=0.05; importation resistant fraction=0.05; anchor rate/y=2.00; country timeline=No; $f_R$=1.00; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Fixed prevalence stress-test anchored to observed low-prevalence settings and conservative imported-risk assumptions [21,27-29]; see eTables 3, 6, and 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Low macrolide resistance prevalence with fitness-neutral strain. | eTables 3, 6, 13, and 23. |
| Macrolide-resistance scenario | Moderate | target resistant fraction=0.30; importation resistant fraction=0.30; anchor rate/y=2.00; country timeline=No; $f_R$=1.00; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Fixed prevalence stress-test spanning plausible intermediate resistance pressure, using clinical guidance [21,22], China and Australia reports [23-25], Japan and Americas reports [26,27], and regional MRBP evidence [28,29]; see eTables 3, 6, and 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Moderate macrolide resistance prevalence with fitness-neutral strain. | eTables 3, 6, 13, and 23. |
| Macrolide-resistance scenario | High | target resistant fraction=0.70; importation resistant fraction=0.70; anchor rate/y=2.00; country timeline=No; $f_R$=1.00; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Fixed prevalence stress-test motivated by high-prevalence MRBP reports in China [23,24], Japan [26], and regional evidence [28,29]; see eTables 3, 6, and 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | High macrolide resistance prevalence with fitness-neutral strain. | eTables 3, 6, 13, and 23. |
| Macrolide-resistance scenario | Very high | target resistant fraction=0.95; importation resistant fraction=0.95; anchor rate/y=2.00; country timeline=No; $f_R$=1.00; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Upper prevalence stress-test motivated by near-fixation observations in China and high-prevalence Japanese clusters [23,24,26]; see eTables 3, 6, and 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Very high macrolide resistance prevalence with fitness-neutral strain. | eTables 3, 6, 13, and 23. |
| Macrolide-resistance scenario | Country timeline with fitness cost | target resistant fraction=0.30; importation resistant fraction=0.30; anchor rate/y=2.00; country timeline=Yes; $f_R$=0.85; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Counterfactual fitness-cost sensitivity retained to bound traditional resistance-cost assumptions against observed MRBP expansion in China [23,24], Australia [25], Japan and the Americas [26,27], and regional reports [28,29]. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Country-timeline resistance with moderate fitness cost (15%). Retained as a sensitivity scenario representing the traditional assumption that ribosomal mutations impose a growth penalty. Recent rapid expansion makes a large persistent cost less plausible, but this scenario is included to bound the optimistic end of resistance projections. | eTables 3, 6, 13, and 23. |
| Macrolide-resistance scenario | Country timeline with fitness advantage | target resistant fraction=0.30; importation resistant fraction=0.30; anchor rate/y=2.00; country timeline=Yes; $f_R$=1.10; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Fitness-advantage sensitivity motivated by rapid MRBP expansion and international spread in China [23,24], Australia [25], Japan and the Americas [26,27], and regional reports [28,29], without a demonstrated transmission penalty. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Country-timeline resistance with fitness advantage (10%). The MT28-ptxP3 MRBP clone has been reported with resistance and vaccine-antigen lineages in rapidly expanding outbreaks. This scenario tests whether a modest fitness advantage materially changes long-term resistance burden projections; the 10% value is a stress-test assumption, not a measured relative-fitness estimate. | eTables 3, 6, 13, and 23. |
| Macrolide-resistance scenario | High resistance with fitness advantage | target resistant fraction=0.70; importation resistant fraction=0.70; anchor rate/y=2.00; country timeline=No; $f_R$=1.15; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Worst-case stress test combining high starting resistance with a fitness-advantaged strain; rationale summarized in eTable 23 and resistance evidence from China [23,24], Japan [26], and regional MRBP reports [28,29]. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | High resistance prevalence with fitness advantage (15%). Worst-case scenario combining high initial resistance with a fitness-advantaged strain, representing the upper bound of resistant infection burden. Motivated by genomic reports of co-selection between resistance and vaccine-antigen lineages; retained as a stress-test assumption rather than a directly estimated fitness value. | eTables 3, 6, 13, and 23. |
| Intervention strategy scenario | Current practice | Baseline comparator; Reference scenario | Country-specific schedule and coverage inputs from WHO/UNICEF and national records [1,14], with standard treatment/PEP assumptions from CDC guidance [20]. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Current vaccination and standard macrolide treatment. | eTables 4 and 15-17, and eFigure 9. |
| Intervention strategy scenario | Coverage-floor-only scenario | Current-program modification; Coverage-floor-only scenario among high-coverage programs | Scenario modification of country routine childhood coverage using floor targets and country schedule inputs [1,14]; not a new efficacy estimate. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Raise routine infant and childhood vaccine coverage without lowering countries that already exceed the scenario floor, and without changing dose timeliness. | eTables 4 and 15-17, and eFigure 9. |
| Intervention strategy scenario | Adolescent booster | Current-program modification; Booster-program scenario | Scenario modification of booster timing/coverage using country schedule inputs and pertussis vaccine guidance [1,14]. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Add or scale up a school-age/adolescent booster while retaining the current aP-like mechanism. | eTables 4 and 15-17, and eFigure 9. |
| Intervention strategy scenario | Pregnancy Tdap scale-up | Pregnancy Tdap infant-protection strategy; Guideline-aligned vaccination scenario | Pregnancy Tdap scale-up scenario informed by maternal-program evidence [10-12], WHO vaccine position-paper guidance [1], and infant-specific effectiveness estimates [36,37]. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Scale up Tdap during pregnancy for direct early-infant protection through passive antibody transfer. | eTables 4 and 15-17, and eFigure 9. |
| Intervention strategy scenario | Close-contact adult adjunct | Close-contact adult infant-protection strategy; Adjunct strategy, not replacement | Close-contact adult immunization/contact-reduction adjunct interpreted as an implementation-dependent infant-exposure reduction proxy rather than a standalone replacement for pregnancy Tdap. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Represent Tdap-up-to-date close adult contacts and caregivers around infants as a conservative adult immunization/contact-reduction adjunct. | eTables 4 and 15-17, and eFigure 9. |
| Intervention strategy scenario | Infant-exposure reduction strategy | Infant-exposure reduction strategy; Implementation-dependent composite strategy | Infant-exposure reduction strategy combining pregnancy Tdap scale-up and a close-contact adult adjunct; not a maternal-immunization-only effect estimate; decomposed in eTable 15. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Represent a consensus-aligned composite infant-exposure reduction strategy combining pregnancy Tdap scale-up and close-contact adult adjuncts. | eTables 4 and 15-17, and eFigure 9. |
| Intervention strategy scenario | Targeted high-risk PEP | Exposure-management scenario; Guideline-aligned management scenario | Targeted PEP scenario translated from CDC guidance prioritizing household contacts, infants, and high-risk infant settings [20]. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Improve PEP reach among household contacts, infants, and high-risk infant settings. | eTables 4 and 15-17, and eFigure 9. |
| Intervention strategy scenario | Direct maternal antibody only | Infant-exposure strategy component diagnostic; Component diagnostic, not standalone policy | Component diagnostic based on maternal-program evidence [10-12] and infant-specific effectiveness estimates [36,37], not a standalone policy estimate. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Isolate direct infant protection from transplacental antibody transfer. | eTables 4 and 15-17, and eFigure 9. |
| Intervention strategy scenario | Reproductive-age adult boosting only | Infant-exposure strategy component diagnostic; Component diagnostic, not standalone policy | Component diagnostic separating adult boosting from direct infant antibody and contact-reduction effects; informed by maternal-program interpretation [10-12] and infant-specific estimates [36,37]. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Isolate recent reproductive-age adult boosting that lowers infection and transmission risk in young adults. | eTables 4 and 15-17, and eFigure 9. |
| Intervention strategy scenario | Contact reduction only | Infant-exposure strategy component diagnostic; Component diagnostic, not standalone policy | Component diagnostic for household/contact reduction, interpreted with maternal-program evidence [10-12] and infant-protection estimates [36,37]. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Isolate reduced household-to-infant transmission from close-contact assumptions. | eTables 4 and 15-17, and eFigure 9. |
| Intervention strategy scenario | Resistance-guided treatment | Resistance-management scenario; Implementation-dependent management scenario | Resistance-aware testing, treatment, and PEP scenario translated from CDC treatment/PEP and antibiotic-resistance guidance [20,21]. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Use resistance-aware testing, alternative treatment, and restored PEP effectiveness for resistant infections. | eTables 4 and 15-17, and eFigure 9. |
| Intervention strategy scenario | High-transmission-blocking vaccine target | High-transmission-blocking vaccine target; Product target, not available policy | Hypothetical product-target scenario interpreted through the WHO vaccine framework [1], transmission evidence [5,6], waning studies [7-9], and vaccine-pipeline mapping in eTable 22. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Represent an improved high-transmission-blocking pertussis vaccine profile. | eTables 4 and 15-17, and eFigure 9. |
| Intervention strategy scenario | Combined strategy | Combined stress-test profile; Mechanistic upper-bound package, not policy package | Composite stress test combining pregnancy Tdap-based infant protection, close-contact adult adjuncts, adolescent boosting, targeted PEP, resistance-guided management, and transmission-blocking assumptions; not a single externally validated package. | Strategies are grouped by decision domain rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Combine transmission-blocking vaccine assumptions, pregnancy Tdap-based infant protection, close-contact adjuncts, adolescent boosting, targeted PEP, and resistance-guided management. | eTables 4 and 15-17, and eFigure 9. |
| Observation and reporting sensitivity | Medium | overall multiplier=1.00; age multipliers=No; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | High | overall multiplier=1.50; age multipliers=No; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Low | overall multiplier=0.50; age multipliers=No; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Age-biased | age multipliers=Yes; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Time-varying | overall multiplier=1.00; age multipliers=No; time variation=Yes | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Infant high, adult very low | age multipliers=Yes; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Infant moderate, adult minimal | age multipliers=Yes; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Enhanced surveillance | age multipliers=Yes; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Adult-focused improvement | age multipliers=Yes; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | China passive system | age multipliers=Yes; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Vaccine-resistance interaction grids | $VE_{inf}$-only grid and continuous $f_R$ x $VE_{inf}$ grid | $f_R$ values 0.70-1.25; $VE_{inf}$ values 0.05-0.55; $VE_{inf}$-only thresholds also vary resistance prevalence anchors and resistant importation fraction. | Grid bounds combine vaccine-framework and transmission uncertainty [1], [5,6], waning uncertainty [7-9], resistance guidance [21,22], and country resistance evidence [23,24], [25], [26], [27], [28,29]; summarized in eTables 11 and 14. | $VE_{sus}$ and $VE_{dur}$ held at grid-baseline values for $VE_{inf}$-only thresholds; country profiles remain calibrated. | Identifies transmission-blocking thresholds and shows how resistant fitness modifies vaccine benefit. | Figure 3D-F and eTables 11 and 14. |
| Exploratory uncertainty and robustness diagnostics | Sensitivity screens and robustness diagnostics | 48-run Latin-hypercube screening; 128 selected-parameter joint strategy-ordering samples; routine timeliness, temporal, infant-contact, maternal-duration, treatment/PEP, event-scale, and stochastic toy diagnostics. | Designed as robustness diagnostics following immunization-model reporting guidance [35], using parameter ranges documented in retained eTables and summarized graphically in eFigure 9. | Diagnostics are not full posterior or decision analyses; they support strategy-ordering and structural-robustness interpretation. | Quantifies which assumptions threaten interpretation of infant-burden and strategy-ordering conclusions. | eTables 16-21 and eFigure 9. |
| Conditional beta-grid interval analysis | Adaptive $log(beta_{S})$ quadrature | $beta_{S}$ posterior dimension and negative-binomial stochastic overlay scaled to the analysis horizon; pre-specified tail, effective-grid-size, and maximum-mass checks. | Conditional uncertainty workflow follows the model-reporting distinction between calibrated identifiable parameters and fixed nuisance assumptions [35]; priors and fixed nuisance settings are in eTable 10. | Reporting multiplier, vaccine nuisance parameters, infectious durations, asymptomatic infectiousness, resistance fitness, and resistance anchors fixed at calibrated, literature-informed, or pre-specified baseline values. | Provides conditional uncertainty intervals for selected main-text summaries without claiming full joint structural uncertainty. | eTable 10 and beta-grid quality outputs retained in repository CSV files. |

<div style="page-break-after: always;"></div>

### eTable 3. Macrolide-resistance initialization, importation, and fitness assumptions.

| Scenario | Target resistant fraction | Importation resistant fraction | Anchor rate per year | Country timeline | $f_R$ | Description |
| --- | --- | --- | --- | --- | --- | --- |
| Country timeline | 0.30 | 0.30 | 2.00 | Yes | 1.00 | Country-specific macrolide resistance prevalence from data/raw/country_resistance_timeline.csv. The prevalence anchors are data-derived. $f_R$ = 1.00 is an epidemiologically motivated neutral baseline, not a directly measured strain-fitness estimate: China MRBP rose from 36% (2016) to near-fixation (>99%, 2024), and related MRBP lineages were reported internationally without clear transmission disadvantage. The fitness grid and fitness sensitivity scenarios explore the full range [0.70-1.25]. |
| Low | 0.05 | 0.05 | 2.00 | No | 1.00 | Low macrolide resistance prevalence with fitness-neutral strain. |
| Moderate | 0.30 | 0.30 | 2.00 | No | 1.00 | Moderate macrolide resistance prevalence with fitness-neutral strain. |
| High | 0.70 | 0.70 | 2.00 | No | 1.00 | High macrolide resistance prevalence with fitness-neutral strain. |
| Very high | 0.95 | 0.95 | 2.00 | No | 1.00 | Very high macrolide resistance prevalence with fitness-neutral strain. |
| Country timeline with fitness cost | 0.30 | 0.30 | 2.00 | Yes | 0.85 | Country-timeline resistance with moderate fitness cost (15%). Retained as a sensitivity scenario representing the traditional assumption that ribosomal mutations impose a growth penalty. Recent rapid expansion makes a large persistent cost less plausible, but this scenario is included to bound the optimistic end of resistance projections. |
| Country timeline with fitness advantage | 0.30 | 0.30 | 2.00 | Yes | 1.10 | Country-timeline resistance with fitness advantage (10%). The MT28-ptxP3 MRBP clone has been reported with resistance and vaccine-antigen lineages in rapidly expanding outbreaks. This scenario tests whether a modest fitness advantage materially changes long-term resistance burden projections; the 10% value is a stress-test assumption, not a measured relative-fitness estimate. |
| High resistance with fitness advantage | 0.70 | 0.70 | 2.00 | No | 1.15 | High resistance prevalence with fitness advantage (15%). Worst-case scenario combining high initial resistance with a fitness-advantaged strain, representing the upper bound of resistant infection burden. Motivated by genomic reports of co-selection between resistance and vaccine-antigen lineages; retained as a stress-test assumption rather than a directly estimated fitness value. |

<div style="page-break-after: always;"></div>

### eTable 4. Intervention strategy definitions, modified control levers, and decision domain.

| Strategy | Scenario category | Interpretive status | Scenario definition | Modified control levers | Interpretation note |
| --- | --- | --- | --- | --- | --- |
| Current practice | Baseline comparator | Reference scenario | Current vaccination and standard macrolide treatment. | Country-specific vaccine schedule and coverage; standard macrolide treatment and PEP assumptions. | Comparator for relative reductions. |
| Coverage-floor-only scenario | Current-program modification | Coverage-floor-only scenario among high-coverage programs | Raise routine infant and childhood vaccine coverage without lowering countries that already exceed the scenario floor, and without changing dose timeliness. | Coverage floor updates: 3-11 mo at least 0.82, 1-4 y at least 0.96, 5-9 y at least 0.94. | Tests marginal gains in high-coverage profiles; not evidence against maintaining routine childhood vaccination. |
| Adolescent booster | Current-program modification | Booster-program scenario | Add or scale up a school-age/adolescent booster while retaining the current aP-like mechanism. | Coverage floor update: 10-17 y at least 0.90; $VE_{inf}$ retained at 0.25. | Program-extension scenario using the current aP-like mechanism rather than a new product profile. |
| Pregnancy Tdap scale-up | Pregnancy Tdap infant-protection strategy | Guideline-aligned vaccination scenario | Scale up Tdap during pregnancy for direct early-infant protection through passive antibody transfer. | Coverage floor update: 0-2 mo maternal-protection entry at least 0.75; maternal $VE_{sus}$ 0.55 and $VE_{sym}$ 0.92; maternal protection duration 180 d. | Models direct pregnancy Tdap protection for newborns and avoids changing routine infant DTaP coverage. |
| Close-contact adult adjunct | Close-contact adult infant-protection strategy | Adjunct strategy, not replacement | Represent Tdap-up-to-date close adult contacts and caregivers around infants as a conservative adult immunization/contact-reduction adjunct. | Coverage floor update: 18-39 y at least 0.55; young-adult-to-infant contact reduction 15%. | The contact-reduction component alone is treated as difficult to implement and insufficient as a replacement for pregnancy Tdap. |
| Infant-exposure reduction strategy | Infant-exposure reduction strategy | Implementation-dependent composite strategy | Represent a consensus-aligned composite infant-exposure reduction strategy combining pregnancy Tdap scale-up and close-contact adult adjuncts. | Coverage floor updates: 0-2 mo maternal-protection entry at least 0.75 and 18-39 y at least 0.55; maternal $VE_{sus}$ 0.55 and $VE_{sym}$ 0.92; maternal protection duration 180 d; young-adult-to-infant contact reduction 15%. | Composite proxy, not maternal immunization alone or passive antibody protection alone; eTable 15 decomposes pregnancy Tdap, adult boosting, and contact-reduction components. |
| Targeted high-risk PEP | Exposure-management scenario | Guideline-aligned management scenario | Improve PEP reach among household contacts, infants, and high-risk infant settings. | PEP coverage among eligible household/high-risk contacts increased to 0.45. | Represents targeted PEP among guideline-prioritized contacts, not broad community prophylaxis. |
| Direct maternal antibody only | Infant-exposure strategy component diagnostic | Component diagnostic, not standalone policy | Isolate direct infant protection from transplacental antibody transfer. | Coverage floor update: 0-2 mo maternal-protection entry at least 0.75; maternal $VE_{sus}$ 0.55 and $VE_{sym}$ 0.92; maternal protection duration 180 d. | Excludes adult boosting and contact reduction to decompose the infant-exposure reduction strategy. |
| Reproductive-age adult boosting only | Infant-exposure strategy component diagnostic | Component diagnostic, not standalone policy | Isolate recent reproductive-age adult boosting that lowers infection and transmission risk in young adults. | Coverage floor update: 18-39 y recent-boosting proxy at least 0.55. | Excludes direct infant antibody protection and contact reduction. |
| Contact reduction only | Infant-exposure strategy component diagnostic | Component diagnostic, not standalone policy | Isolate reduced household-to-infant transmission from close-contact assumptions. | Young-adult-to-infant contact reduction 15% for 0-2 mo and 3-11 mo targets. | Excludes direct infant antibody protection and adult boosting. |
| Resistance-guided treatment | Resistance-management scenario | Implementation-dependent management scenario | Use resistance-aware testing, alternative treatment, and restored PEP effectiveness for resistant infections. | Resistant infection updates: infectious-duration reduction 0.45 and infectiousness reduction 0.35; symptomatic treatment rate 0.07; resistant-strain PEP effectiveness 0.45. | Depends on testing reach, uptake, treatment selection, and PEP implementation; near-term sensitivity is in eTable 16. |
| High-transmission-blocking vaccine target | High-transmission-blocking vaccine target | Product target, not available policy | Represent an improved high-transmission-blocking pertussis vaccine profile. | Uses Upper-bound transmission-blocking vaccine profile: $VE_{sus}$ 0.80, $VE_{sym}$ 0.90, $VE_{inf}$ 0.65, $VE_{dur}$ 0.40. | Mechanistic upper-bound profile motivated by candidate mucosal or high-transmission-blocking platforms; pipeline mapping is in eTable 22. |
| Combined strategy | Combined stress-test profile | Mechanistic upper-bound package, not policy package | Combine transmission-blocking vaccine assumptions, pregnancy Tdap-based infant protection, close-contact adjuncts, adolescent boosting, targeted PEP, and resistance-guided management. | Uses Transmission-blocking vaccine profile; coverage targets for 0-2 mo maternal protection 0.75, 10-17 y 0.90, and 18-39 y 0.55; maternal $VE_{sus}$ 0.55 and $VE_{sym}$ 0.92; maternal protection duration 180 d; young-adult-to-infant contact reduction 15%; targeted PEP coverage 0.45; resistance-guided treatment and resistant-strain PEP updates. | Stress-test scenario for combined mechanisms; not an externally validated implementation package. |

<div style="page-break-after: always;"></div>

### eTable 5. Baseline parameter values, admissible ranges, and evidence provenance.

| Parameter | Description | Baseline value | Range | Unit | Source or assumption | Sensitivity |
| --- | --- | --- | --- | --- | --- | --- |
| simulation.end_time | Simulation analysis horizon | 9,495.00 | see config/model_settings.yaml sensitivity_parameters | days | Analysis design | No |
| simulation.burn_in_years | Pre-analysis burn-in horizon | 15.00 | see config/model_settings.yaml sensitivity_parameters | years | Analysis design | No |
| transmission.beta_S | Transmission rate for macrolide-sensitive pertussis | 0.01 | see config/model_settings.yaml sensitivity_parameters | per contact day | Calibrated to reported pertussis incidence | No |
| transmission.relative_infectiousness_asymptomatic | Relative infectiousness of asymptomatic infection | 0.35 | see config/model_settings.yaml sensitivity_parameters | ratio | Literature-informed assumption | Yes |
| transmission.multi_year_period_years | Target/diagnostic inter-epidemic period | 4.00 | see config/model_settings.yaml sensitivity_parameters | years | Pertussis cycle-model evidence | No |
| transmission.multi_year_amplitude | Weak multi-year phase-locking amplitude | 0.00 | see config/model_settings.yaml sensitivity_parameters | ratio | Model-structure assumption | Yes |
| natural_history.latent_duration | Latent period duration | 8.00 | see config/model_settings.yaml sensitivity_parameters | days | CDC clinical guidance | No |
| natural_history.infectious_duration_symptomatic | Symptomatic infectious duration | 21.00 | see config/model_settings.yaml sensitivity_parameters | days | CDC clinical guidance | Yes |
| natural_history.infectious_duration_asymptomatic | Asymptomatic infectious duration | 14.00 | see config/model_settings.yaml sensitivity_parameters | days | Literature-informed assumption | Yes |
| natural_history.recovered_immunity_duration | Duration of post-infection protection | 3,285.00 | see config/model_settings.yaml sensitivity_parameters (reciprocal of rates.waning_natural) | days | CDC clinical guidance and cycle-model evidence | Yes |
| natural_history.vaccine_protection_duration | Duration of vaccine-derived protection proxy | 1,825.00 | see config/model_settings.yaml sensitivity_parameters (reciprocal of rates.waning_vaccine) | days | aP waning literature | Yes |
| treatment.treatment_rate_symptomatic | Daily transition from symptomatic infection to treatment | 0.03 | see config/model_settings.yaml sensitivity_parameters | per day | CDC guidance plus implementation assumption | Yes |
| PEP.coverage_household_contacts | Dynamic PEP coverage ceiling among close contacts | 0.30 | see config/model_settings.yaml sensitivity_parameters | proportion | CDC guidance plus implementation assumption | Yes |

<div style="page-break-after: always;"></div>

### eTable 6. Country-specific macrolide-resistance evidence used for resistance anchoring.

| Country | Year | Sample size | Resistance estimate | Evidence class | Source | Note |
| --- | --- | --- | --- | --- | --- | --- |
| Australia | 2024 | 188 | 4.30% (1.90%-8.20%) | Measured national genomic surveillance fraction | https://doi.org/10.1016/j.lanmic.2025.101286 | Nationwide Australian tNGS study of 2024-positive respiratory specimens estimated macrolide resistance at 8/188 (4.30%). |
| Brazil | 2025 | Not publicly reported; model anchor | 1.00% (0.00%-5.00%) | Low detected model anchor | https://www.paho.org/en/news/26-8-2025-paho-calls-strengthened-vaccination-and-surveillance-amid-spread-antibiotic | No public denominator located; conservative low anchor retained pending surveillance. |
| China | 2016 | 11 | 36.40% (28.00%-45.00%) | Measured regional isolate fraction | https://wwwnc.cdc.gov/eid/article/30/1/22-1588_article | Shanghai isolate series; 4/11 selected 2016 isolates were macrolide resistant. |
| China | 2022 | 72 | 97.20% (94.00%-99.00%) | Measured regional isolate fraction | https://wwwnc.cdc.gov/eid/article/30/1/22-1588_article | Shanghai isolate series; 70/72 selected 2022 isolates were macrolide resistant. |
| China | 2024 | 394 | 99.70% (98.60%-100.00%) | Measured multicenter isolate fraction | https://www.sciencedirect.com/science/article/pii/S2666606525001658 | Five sentinel hospitals in China during 2024; 393/394 isolates displayed high-level azithromycin resistance. |
| Japan | 2024 | 8 | 87.50% (47.30%-99.70%) | Measured regional case series fraction | https://www.sciencedirect.com/science/article/pii/S1341321X26000140 | Osaka case series, August 2024-January 2025; 7/8 analyzed B. pertussis strains were macrolide resistant. |
| Japan | 2025 | 52 | 82.70% (69.70%-91.80%) | Measured multicenter isolate fraction | https://www.mdpi.com/2227-9059/14/1/167 | Japanese children at six clinics, March-August 2025; 43/52 sequenced B. pertussis isolates carried the A2047G mutation associated with macrolide resistance. |
| New Zealand | 1995 | 88 | 0.00% (0.00%-4.10%) | Measured historical national isolate fraction | https://pubmed.ncbi.nlm.nih.gov/9579709/ | ESR national reference laboratory series from 1991-1995: 88 strains tested, with erythromycin MICs 0.12-0.50 mg/L. A later meta-analysis tabulates this study as 0/88 resistant isolates. |
| New Zealand | 2025 | Not publicly reported; model anchor | 1.00% (0.00%-5.00%) | Low detected model anchor | https://www.tewhatuora.govt.nz/for-health-professionals/clinical-guidance/communicable-disease-control-manual/pertussis | No public denominator located; conservative low anchor retained pending surveillance. |
| South Africa | 2025 | Not publicly reported; model anchor | 2.00% (0.50%-5.00%) | Global-surveillance extrapolation | https://www.cdc.gov/pertussis/hcp/antibiotic-resistance/index.html; https://www.mdpi.com/2079-6382/11/11/1570 | No country-specific denominator located; conservative low extrapolated anchor retained pending surveillance. |
| Sweden | 2025 | Not publicly reported; model anchor | 1.00% (0.00%-5.00%) | Low imported model anchor | https://www.folkhalsomyndigheten.se/contentassets/975cc036216b48a39b7bf34319d4ecee/pertussis-surveillance-sweden-23rd-annual-report.pdf | No public denominator located; conservative low anchor retained pending surveillance. |
| Thailand | 2025 | Not publicly reported; model anchor | 1.00% (0.00%-5.00%) | Low imported model anchor | https://www.cdc.gov/pertussis/hcp/antibiotic-resistance/index.html | No public denominator located; conservative low anchor retained pending surveillance. |
| United Kingdom | 2009 | 583 | 0.00% (0.00%-0.60%) | Measured historical national isolate fraction | https://researchportal.ukhsa.gov.uk/en/publications/antimicrobial-susceptibility-testing-of-historical-and-recent-cli/ | UK enhanced-surveillance isolates collected from 2001-2009: all 583 isolates were fully susceptible to erythromycin, clarithromycin, and azithromycin. |
| United Kingdom | 2024 | 661 | 0.30% (0.00%-1.10%) | Measured national surveillance fraction | https://www.postersessiononline.eu/173580348_eu/congresos/UKHSA2025/aula/-P_58_UKHSA2025.pdf | UKHSA national reference laboratory poster: 661 B. pertussis isolates received from June 2023 to November 2024, with 2 predicted and phenotypically confirmed macrolide-resistant isolates. |
| United States | 1997 | 47 | 2.10% (0.10%-11.30%) | Measured regional isolate fraction | https://pubmed.ncbi.nlm.nih.gov/9350776/ | Intermountain West pediatric isolates recovered from January 1985 to June 1997; 1/47 was erythromycin resistant (MIC 32 ug/mL). |
| United States | 2015 | 1,208 | 0.00% (0.00%-0.30%) | Measured multistate surveillance fraction | https://www.walshmedicalmedia.com/conference-abstracts-files/2155-9597.C1.016-015.pdf | CDC surveillance abstract: 1208 B. pertussis isolates collected from 2011-2015 across 7 enhanced-surveillance states, 2 outbreak states, and 6 sporadic-state settings were susceptible to erythromycin and azithromycin; 54 DNA NPS extracts had no A2047G mutation. |

<div style="page-break-after: always;"></div>

### eTable 7. Calibration acceptance, fitted parameters, and interval-level fit diagnostics.

| Country | Period | Accepted | Fit status | Calibrated beta | Observed incidence per 100k | Modeled incidence per 100k | Model/observed ratio | Intervals | Observed reports | Modeled reports | MAPE | Observed peak year | Modeled peak year | Peak timing error, y | Peak magnitude ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | Overall | Yes | Calibrated to reported cases | 0.02 | 61.49 | 61.76 | 1.00 | 65 | 88,963.00 | 88,963.00 | 1.76 | 2024 | 2025 | 1.00 | 0.93 |
| Australia | Pandemic/NPI | Yes | Calibrated to reported cases | 0.02 | 61.49 | 61.76 | 1.00 | 12 | 540.00 | 1.78 | 1.00 |  |  |  |  |
| Australia | Post-pandemic | Yes | Calibrated to reported cases | 0.02 | 61.49 | 61.76 | 1.00 | 53 | 88,423.00 | 88,961.22 | 1.93 |  |  |  |  |
| Brazil | Overall | Yes | Calibrated to reported cases | 0.01 | 1.00 | 0.97 | 0.98 | 64 | 11,275.00 | 11,275.00 | 8.54 | 2024 | 2021 | -3.00 | 0.17 |
| Brazil | Pandemic/NPI | Yes | Calibrated to reported cases | 0.01 | 1.00 | 0.97 | 0.98 | 12 | 159.00 | 2,152.14 | 15.79 |  |  |  |  |
| Brazil | Post-pandemic | Yes | Calibrated to reported cases | 0.01 | 1.00 | 0.97 | 0.98 | 52 | 11,116.00 | 9,122.86 | 6.87 |  |  |  |  |
| China | Overall | Yes | Calibrated to reported cases | 0.01 | 7.04 | 7.27 | 1.03 | 81 | 640,783.00 | 675,181.24 | 3.94 | 2024 | 2025 | 1.00 | 0.57 |
| China | Pandemic/NPI | Yes | Calibrated to reported cases | 0.01 | 7.04 | 7.27 | 1.03 | 24 | 14,156.00 | 8,456.86 | 0.67 |  |  |  |  |
| China | Post-pandemic | Yes | Calibrated to reported cases | 0.01 | 7.04 | 7.27 | 1.03 | 57 | 626,627.00 | 666,724.39 | 5.32 |  |  |  |  |
| Japan | Overall | Yes | Calibrated to reported cases | 0.01 | 12.57 | 14.29 | 1.14 | 276 | 82,325.00 | 82,325.00 | 4.79 | 2025 | 2025 | 0.00 | 0.45 |
| Japan | Pandemic/NPI | Yes | Calibrated to reported cases | 0.01 | 12.57 | 14.29 | 1.14 | 52 | 563.00 | 914.22 | 1.16 |  |  |  |  |
| Japan | Post-pandemic | Yes | Calibrated to reported cases | 0.01 | 12.57 | 14.29 | 1.14 | 224 | 81,762.00 | 81,410.78 | 5.63 |  |  |  |  |
| New Zealand | Overall | Yes | Calibrated to reported cases | 0.01 | 19.15 | 19.23 | 1.00 | 64 | 5,324.00 | 5,324.00 | 3.88 | 2024 | 2026 | 2.00 | 0.69 |
| New Zealand | Pandemic/NPI | Yes | Calibrated to reported cases | 0.01 | 19.15 | 19.23 | 1.00 | 12 | 62.00 | 213.14 | 3.69 |  |  |  |  |
| New Zealand | Post-pandemic | Yes | Calibrated to reported cases | 0.01 | 19.15 | 19.23 | 1.00 | 52 | 5,262.00 | 5,110.86 | 3.93 |  |  |  |  |
| South Africa | Overall | Yes | Calibrated to reported cases | 0.01 | 2.28 | 2.14 | 0.94 | 32 | 3,883.00 | 3,883.00 | 1.17 | 2025 | 2023 | -2.00 | 0.60 |
| South Africa | Post-pandemic | Yes | Calibrated to reported cases | 0.01 | 2.28 | 2.14 | 0.94 | 32 | 3,883.00 | 3,883.00 | 1.17 |  |  |  |  |
| Sweden | Overall | Yes | Calibrated to reported cases | 0.01 | 6.30 | 6.52 | 1.04 | 64 | 3,562.00 | 3,562.00 | 10.47 | 2024 | 2025 | 1.00 | 0.24 |
| Sweden | Pandemic/NPI | Yes | Calibrated to reported cases | 0.01 | 6.30 | 6.52 | 1.04 | 12 | 11.00 | 588.67 | 37.06 |  |  |  |  |
| Sweden | Post-pandemic | Yes | Calibrated to reported cases | 0.01 | 6.30 | 6.52 | 1.04 | 52 | 3,551.00 | 2,973.33 | 5.41 |  |  |  |  |
| Thailand | Overall | Yes | Calibrated to reported cases | 0.01 | 0.46 | 0.48 | 1.04 | 72 | 1,982.00 | 1,982.00 | 7.04 | 2024 | 2024 | 0.00 | 0.22 |
| Thailand | Pandemic/NPI | Yes | Calibrated to reported cases | 0.01 | 0.46 | 0.48 | 1.04 | 24 | 30.00 | 434.09 | 11.70 |  |  |  |  |
| Thailand | Post-pandemic | Yes | Calibrated to reported cases | 0.01 | 0.46 | 0.48 | 1.04 | 48 | 1,952.00 | 1,547.91 | 5.60 |  |  |  |  |
| United Kingdom | Overall | Yes | Calibrated to reported cases | 0.01 | 9.55 | 9.92 | 1.04 | 273 | 34,581.00 | 34,581.00 | 8.09 | 2024 | 2024 | 0.00 | 0.21 |
| United Kingdom | Pandemic/NPI | Yes | Calibrated to reported cases | 0.01 | 9.55 | 9.92 | 1.04 | 104 | 1,812.00 | 8,068.10 | 13.38 |  |  |  |  |
| United Kingdom | Post-pandemic | Yes | Calibrated to reported cases | 0.01 | 9.55 | 9.92 | 1.04 | 169 | 32,769.00 | 26,512.90 | 4.73 |  |  |  |  |
| United States | Overall | Yes | Calibrated to reported cases | 0.01 | 1.39 | 1.41 | 1.01 | 278 | 25,679.00 | 25,679.00 | 6.11 | 2024 | 2021 | -3.00 | 0.22 |
| United States | Pandemic/NPI | Yes | Calibrated to reported cases | 0.01 | 1.39 | 1.41 | 1.01 | 51 | 510.00 | 4,909.29 | 18.16 |  |  |  |  |
| United States | Post-pandemic | Yes | Calibrated to reported cases | 0.01 | 1.39 | 1.41 | 1.01 | 227 | 25,169.00 | 20,769.71 | 3.40 |  |  |  |  |

<div style="page-break-after: always;"></div>

### eTable 8. Model-derived outcomes and summary definitions.

| Quantity | Definition | Denominator or reference population | Primary use |
| --- | --- | --- | --- |
| Total infections | Symptomatic plus asymptomatic incident infections integrated over the analysis interval; treated infections are counted at infection onset, not as a separate new infection. | Mean total population over the interval. | Overall transmission burden. |
| Reported cases | Symptomatic incident infections multiplied by age-specific reporting probabilities and integrated over the analysis interval. | Mean total population over the interval. | Calibration target and surveillance-comparable burden. |
| Infant cases | Symptomatic incident infections in the 0-2 month and 3-11 month age groups. | Mean population in the two infant age groups. | Primary severe-risk outcome. |
| Resistant infections | Total incident infections attributed to the macrolide-resistant strain. | Mean total population over the interval. | Resistance burden and treatment relevance. |
| Resistant fraction | For interval summaries, resistant incident infections divided by all incident infections; for start/end strain dynamics, resistant active exposed, infectious, and treated compartments divided by all active strain-specific compartments. | Total infections or active infected compartments, depending on summary. | Strain-composition diagnostic. |
| PEP-averted cases | Difference between pre-PEP and post-PEP symptomatic infection flows under the same state trajectory. | Not a population-normalized compartment count unless explicitly annualized. | Diagnostic estimate of prophylaxis effect. |
| Relative reduction | 1 - Z/Z0, where Z is the scenario outcome and Z0 is the comparator outcome. | Scenario-specific comparator. | Cross-scenario intervention comparison. |

<div style="page-break-after: always;"></div>

### eTable 9. Core model settings and implementation choices.

| Aspect | Setting | Value |
| --- | --- | --- |
| Model class | Deterministic age-structured compartmental ODE | Two strain classes, country-specific demographics, vaccination histories, and treatment states are explicit; PEP modifies the force of infection and is retained as an averted-case diagnostic. |
| Age structure | Eight model age groups | 0-2 months, 3-11 months, 1-4 years, 5-9 years, 10-17 years, 18-39 years, 40-64 years, and 65 years or older. |
| Strain structure | Two strain classes | Macrolide-sensitive and macrolide-resistant strains are simulated separately. |
| Vaccine-history structure | Explicit origin states | Unvaccinated, maternally protected, dose-1 recent/waned, dose-2 recent/waned, and dose-3-plus recent/waned states retain distinct effects. |
| Burn-in and horizon | Long burn-in plus analysis window | Fifteen-year burn-in followed by saved analysis from 1 January 2025 through 31 December 2050; summary files report this as approximately 26.01 years. |
| Time scale | Daily rates with weekly saved output | All state equations are evaluated in days, and output is stored every 7 days for downstream summaries. |
| Numerical solver | Adaptive Runge-Kutta integration | RK45 with relative tolerance 1e-5 and absolute tolerance 1e-7. |
| Seasonality | Annual cosine forcing | Annual cosine forcing is used by default; an optional 4-year diagnostic term is available when surveillance peaks support multi-year recurrence. |
| Demography | WPP trajectory-driven age turnover | Births and aging are driven by UN World Population Prospects 2024 annual trajectories with gentle nudging toward target age profiles; a fixed-profile fallback is retained for tests. |
| Observation model | Age-specific reporting probabilities | Reported cases are symptomatic infections multiplied by age-specific reporting probabilities; diagnosis rates and PEP-detection proxies are separate parameters. |
| Calibration target | Reported surveillance intervals | Country-specific $beta_{S}$ is selected using a negative-binomial reported-case likelihood, and retained fits must match observed annualized reported incidence within the configured tolerance. |
| Resistance anchoring | Evidence-based initialization | Country-specific anchors use the latest admissible evidence at the 2025 analysis anchor; low-level resistant importation prevents deterministic extinction. |
| Sensitivity screening | Latin-hypercube screening | Forty-eight parameter sets were used for Pearson, Spearman, and PRCC screening correlations, separate from posterior inference. |
| Bayesian uncertainty | Conditional beta-grid interval analysis with pre-specified checks | A negative-binomial reported-case likelihood and literature-informed priors define a conditional $beta_{S}$ interval analysis; weakly identifiable nuisance parameters are fixed at calibrated, literature-informed, or pre-specified baseline values, and intervals are retained only when beta-grid tail and quadrature-resolution checks pass. |
| Resistance fitness stress test | Continuous $f_R$ grid | Macrolide-resistant strain fitness is varied from 0.70 to 1.25 and crossed with vaccine infectiousness-effect assumptions. |

<div style="page-break-after: always;"></div>

### eTable 10. Bayesian uncertainty priors and fixed nuisance settings for the conditional beta-grid interval analysis.

| Parameter | Prior | Interpretation |
| --- | --- | --- |
| $log(beta_{S})$ | $Normal(log(beta_{S,cal}), 0.80^2)$ | Transmission-rate uncertainty |
| $log(m_{rep})$ | $Normal(log(m_{rep,cal}), 0.80^2)$ | Surveillance/reporting uncertainty |
| $VE_{sus}$ | $Beta(mu=0.45, sigma=0.05)$ | Literature-informed decomposition parameter for reduced susceptibility after aP vaccination. Aggregate studies support high disease protection and waning protection, but do not directly identify this component from surveillance data; the posterior is constrained to [0.30, 0.60] as a modeling range. |
| $VE_{inf}$ | $Beta(mu=0.25, sigma=0.05)$ | Literature-informed decomposition parameter for reduced onward infectiousness among vaccinated infections. It is motivated by aP transmission-blocking evidence and waning studies, but the exact component is not directly measured in country surveillance; range [0.12, 0.38] spans weak-to-moderate residual transmission blocking. |
| $VE_{dur}$ | $Beta(mu=0.10, sigma=0.10)$ | Mechanistic duration-shortening proxy fixed at the prior mean during the conditional beta-grid analysis; treated as a vaccine-scenario assumption rather than a directly estimated literature parameter. |
| $rho_{asym}$ | $Beta(mu=0.45, sigma=0.10)$ | Relative infectiousness of asymptomatic/subclinical infections compared to symptomatic cases. The exact ratio is weakly identified and not directly available from routine surveillance; range [0.20, 0.70] spans minimal subclinical transmission to near-equal infectiousness. |
| $D_{sym}$ | $log(D_{sym}) ~ Normal(log(D_{sym,0}), 0.15^2)$ | Clinical natural-history nuisance parameter centered on the CDC-aligned 21-day symptomatic infectious window; uncertainty range captures plausible variation around the clinical anchor. |
| $D_{asym}$ | $log(D_{asym}) ~ Normal(log(D_{asym,0}), 0.20^2)$ | Modeling assumption centered on a shorter mild/asymptomatic infectious window than symptomatic pertussis; uncertainty range retained because this duration is not directly measured. |
| $f_R$ | $Normal(1.00, 0.12^2)$ on $[0.70, 1.25]$ | Epidemiologically motivated prior centered on fitness-neutral (1.00), because MRBP reached near-fixation in China within 8 years and spread internationally without clear transmission disadvantage. This is not a direct measured relative-fitness estimate; SD of 0.12 allows modest fitness costs or advantages. |
| $p_R$ | Fixed country timeline; floor SD 0.03 | Resistance prevalence is FIXED at the country-calibrated value during MCMC (not sampled). The country_resistance_timeline.csv provides well-constrained estimates for most countries. This eliminates a major source of multimodality without losing scientific information. |
| $VE^{mat}_{sus}$ | $Beta(mu=0.55, sigma=0.12)$ | Prior for maternal antibody protection against infant infection. Centered on 0.55 using maternal Tdap effectiveness evidence for confirmed pertussis in infants younger than 2 months [36], which combines infection prevention and disease prevention. The infection-blocking component is a decomposed model assumption guided by maternal immunization effectiveness studies [10,12]. SD of 0.12 allows exploration of [0.30, 0.80]. |
| $VE^{mat}_{sym}$ | $Beta(mu=0.92, sigma=0.05)$ | Prior for maternal antibody protection against symptomatic disease given infection. High confidence based on consistent estimates of VE against hospitalization (>90%) across US, UK, and Argentina studies [10,36,37]. Narrow SD reflects strong evidence consensus. |

<div style="page-break-after: always;"></div>

### eTable 11. Condensed macrolide-resistant fitness and vaccine infectiousness grid definition.

| Dimension | Grid values | Selected contrasts | Interpretation |
| --- | --- | --- | --- |
| Resistant-strain relative fitness | 0.70, 0.80, 0.85, 0.90, 0.95, 0.98, 1.00, 1.02, 1.05, 1.10, 1.15, 1.20, 1.25 | 0.85, 1.00, and 1.15 emphasized in the main text. | Values below 1.00 impose a resistant-strain transmission penalty; values above 1.00 impose a transmission advantage. |
| Vaccine infectiousness effect, $VE_{inf}$ | 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55 | 0.05 to 0.55 range used for Figure 3E/F surfaces. | $VE_{inf}$ reduces onward infectiousness among infected vaccine-history origins; it is not an infection-acquisition endpoint. |
| Crossed grid | 13 fitness values x 11 $VE_{inf}$ values | 143 simulated combinations retained in repository source table. | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. $VE_{inf}$ is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around $f_R$ = 1.00 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.00. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. $VE_{inf}$ axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |

<div style="page-break-after: always;"></div>

### eTable 12. Fitted age-specific reporting probabilities and prior bounds.

| Country | 0-2 mo | 3-11 mo | 1-9 y | 5-17 y | 18+ y | Prior bounds | Prior evidence class |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | 0.51 | 0.43 | 0.18 | 0.11 | 0.03 | 0-2 mo: $p_{rep}=0.60$ $[0.30, 0.75]$<br>3-11 mo: $p_{rep}=0.50$ $[0.25, 0.70]$<br>1-4 y: $p_{rep}=0.25$ $[0.10, 0.50]$<br>5-9 y: $p_{rep}=0.18$ $[0.08, 0.40]$<br>10-17 y: $p_{rep}=0.08$ $[0.04, 0.20]$<br>18-39 y: $p_{rep}=0.05$ $[0.01, 0.12]$<br>40-64 y: $p_{rep}=0.03$ $[0.01, 0.10]$<br>65+ y: $p_{rep}=0.04$ $[0.01, 0.12]$ | Serology proxy |
| Brazil | 0.58 | 0.48 | 0.21 | 0.13 | 0.04 | 0-2 mo: $p_{rep}=0.60$ $[0.20, 0.70]$<br>3-11 mo: $p_{rep}=0.50$ $[0.18, 0.65]$<br>1-4 y: $p_{rep}=0.25$ $[0.05, 0.40]$<br>5-9 y: $p_{rep}=0.18$ $[0.04, 0.30]$<br>10-17 y: $p_{rep}=0.08$ $[0.03, 0.15]$<br>18-39 y: $p_{rep}=0.05$ $[0.00, 0.08]$<br>40-64 y: $p_{rep}=0.03$ $[0.00, 0.06]$<br>65+ y: $p_{rep}=0.04$ $[0.00, 0.08]$ | Passive surveillance proxy |
| China | 0.60 | 0.50 | 0.21 | 0.13 | 0.04 | 0-2 mo: $p_{rep}=0.60$ $[0.20, 0.70]$<br>3-11 mo: $p_{rep}=0.50$ $[0.20, 0.65]$<br>1-4 y: $p_{rep}=0.25$ $[0.05, 0.40]$<br>5-9 y: $p_{rep}=0.18$ $[0.04, 0.30]$<br>10-17 y: $p_{rep}=0.08$ $[0.03, 0.15]$<br>18-39 y: $p_{rep}=0.05$ $[0.00, 0.08]$<br>40-64 y: $p_{rep}=0.03$ $[0.00, 0.06]$<br>65+ y: $p_{rep}=0.04$ $[0.00, 0.08]$ | Active surveillance proxy |
| Japan | 0.60 | 0.50 | 0.21 | 0.13 | 0.04 | 0-2 mo: $p_{rep}=0.60$ $[0.25, 0.70]$<br>3-11 mo: $p_{rep}=0.50$ $[0.20, 0.65]$<br>1-4 y: $p_{rep}=0.25$ $[0.08, 0.45]$<br>5-9 y: $p_{rep}=0.18$ $[0.06, 0.35]$<br>10-17 y: $p_{rep}=0.08$ $[0.03, 0.15]$<br>18-39 y: $p_{rep}=0.05$ $[0.01, 0.08]$<br>40-64 y: $p_{rep}=0.03$ $[0.01, 0.06]$<br>65+ y: $p_{rep}=0.04$ $[0.01, 0.08]$ | Laboratory surveillance proxy |
| New Zealand | 0.59 | 0.49 | 0.21 | 0.13 | 0.04 | 0-2 mo: $p_{rep}=0.60$ $[0.30, 0.75]$<br>3-11 mo: $p_{rep}=0.50$ $[0.25, 0.70]$<br>1-4 y: $p_{rep}=0.25$ $[0.10, 0.50]$<br>5-9 y: $p_{rep}=0.18$ $[0.08, 0.40]$<br>10-17 y: $p_{rep}=0.08$ $[0.04, 0.18]$<br>18-39 y: $p_{rep}=0.05$ $[0.01, 0.10]$<br>40-64 y: $p_{rep}=0.03$ $[0.01, 0.08]$<br>65+ y: $p_{rep}=0.04$ $[0.01, 0.10]$ | High income underreporting proxy |
| South Africa | 0.60 | 0.50 | 0.22 | 0.13 | 0.04 | 0-2 mo: $p_{rep}=0.60$ $[0.20, 0.70]$<br>3-11 mo: $p_{rep}=0.50$ $[0.18, 0.65]$<br>1-4 y: $p_{rep}=0.25$ $[0.05, 0.40]$<br>5-9 y: $p_{rep}=0.18$ $[0.04, 0.30]$<br>10-17 y: $p_{rep}=0.08$ $[0.03, 0.15]$<br>18-39 y: $p_{rep}=0.05$ $[0.00, 0.08]$<br>40-64 y: $p_{rep}=0.03$ $[0.00, 0.06]$<br>65+ y: $p_{rep}=0.04$ $[0.00, 0.08]$ | Passive notification proxy |
| Sweden | 0.62 | 0.51 | 0.22 | 0.13 | 0.04 | 0-2 mo: $p_{rep}=0.60$ $[0.40, 0.80]$<br>3-11 mo: $p_{rep}=0.50$ $[0.35, 0.75]$<br>1-4 y: $p_{rep}=0.25$ $[0.25, 0.60]$<br>5-9 y: $p_{rep}=0.18$ $[0.14, 0.50]$<br>10-17 y: $p_{rep}=0.08$ $[0.08, 0.25]$<br>18-39 y: $p_{rep}=0.05$ $[0.02, 0.12]$<br>40-64 y: $p_{rep}=0.03$ $[0.01, 0.10]$<br>65+ y: $p_{rep}=0.04$ $[0.02, 0.12]$ | Direct preschool anchor |
| Thailand | 0.61 | 0.51 | 0.22 | 0.13 | 0.04 | 0-2 mo: $p_{rep}=0.60$ $[0.20, 0.70]$<br>3-11 mo: $p_{rep}=0.50$ $[0.18, 0.65]$<br>1-4 y: $p_{rep}=0.25$ $[0.05, 0.40]$<br>5-9 y: $p_{rep}=0.18$ $[0.04, 0.30]$<br>10-17 y: $p_{rep}=0.08$ $[0.03, 0.15]$<br>18-39 y: $p_{rep}=0.05$ $[0.00, 0.08]$<br>40-64 y: $p_{rep}=0.03$ $[0.00, 0.06]$<br>65+ y: $p_{rep}=0.04$ $[0.00, 0.08]$ | Passive surveillance proxy |
| United Kingdom | 0.57 | 0.47 | 0.20 | 0.12 | 0.04 | 0-2 mo: $p_{rep}=0.60$ $[0.30, 0.75]$<br>3-11 mo: $p_{rep}=0.50$ $[0.25, 0.70]$<br>1-4 y: $p_{rep}=0.25$ $[0.10, 0.45]$<br>5-9 y: $p_{rep}=0.18$ $[0.08, 0.35]$<br>10-17 y: $p_{rep}=0.08$ $[0.04, 0.20]$<br>18-39 y: $p_{rep}=0.05$ $[0.01, 0.10]$<br>40-64 y: $p_{rep}=0.03$ $[0.01, 0.08]$<br>65+ y: $p_{rep}=0.04$ $[0.01, 0.10]$ | Notification efficiency low |
| United States | 0.62 | 0.51 | 0.22 | 0.13 | 0.04 | 0-2 mo: $p_{rep}=0.60$ $[0.30, 0.75]$<br>3-11 mo: $p_{rep}=0.50$ $[0.25, 0.70]$<br>1-4 y: $p_{rep}=0.25$ $[0.10, 0.50]$<br>5-9 y: $p_{rep}=0.18$ $[0.08, 0.40]$<br>10-17 y: $p_{rep}=0.08$ $[0.04, 0.18]$<br>18-39 y: $p_{rep}=0.05$ $[0.01, 0.10]$<br>40-64 y: $p_{rep}=0.03$ $[0.01, 0.08]$<br>65+ y: $p_{rep}=0.04$ $[0.01, 0.10]$ | Capture recapture proxy |

<div style="page-break-after: always;"></div>

### eTable 13. Macrolide-resistance mechanism decomposition across importation, treatment, PEP, and fitness assumptions.

| Scenario | Importation | Treatment differential | PEP differential | $f_R$ | Median end resistant fraction | Across-profile IQR end resistant fraction | Median infant cases per 100k | Median resistant infections per 100k | Interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Full baseline mechanism | Yes | Yes | Yes | 1.00 | 1.00 | 0.28-1.00 | 357.53 | 596.21 | Full baseline mechanism: country anchor, resistant importation, strain-specific treatment and PEP, neutral fitness. |
| No resistant importation | No | Yes | Yes | 1.00 | 0.98 | 0.25-1.00 | 352.84 | 579.92 | Tests dependence on ongoing resistant-strain importation after the analysis-start anchor. |
| Equal treatment effect | Yes | No | Yes | 1.00 | 0.99 | 0.06-1.00 | 327.98 | 525.11 | Tests treatment-mediated selection by making resistant treatment effects equal to sensitive-strain effects. |
| Equal PEP effect | Yes | Yes | No | 1.00 | 0.12 | 0.05-0.38 | 276.63 | 28.44 | Tests PEP-mediated selection by making resistant PEP effectiveness equal to sensitive-strain PEP effectiveness. |
| No treatment or PEP differential | Yes | No | No | 1.00 | 0.01 | 0.01-0.04 | 266.87 | 5.88 | Tests neutral strain competition under importation when treatment and PEP do not favor resistant strains. |
| Fitness-cost stress test | Yes | Yes | Yes | 0.85 | 0.00 | 0.00-0.00 | 246.81 | 0.17 | Fitness-cost stress test retaining baseline importation and management assumptions. |

<div style="page-break-after: always;"></div>

### eTable 14. Vaccine infectiousness-effect threshold diagnostics.

| Threshold type | Fitness or comparator | Resistance prevalence | Target or comparator basis | Minimum $VE_{inf}$ | Countries | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Reduction target | $f_R$=0.85 |  | 25.00% | 0.40 | 6/10 | Threshold reached on the simulated $VE_{inf}$ grid. |
| Reduction target | $f_R$=0.85 |  | 50.00% | 0.50 | 5/10 | Threshold reached on the simulated $VE_{inf}$ grid. |
| Reduction target | $f_R$=0.85 |  | 75.00% | Not reached through 0.55 | 4/10 | Threshold not reached on the simulated grid. |
| Reduction target | $f_R$=1.00 |  | 25.00% | 0.40 | 6/10 | Threshold reached on the simulated $VE_{inf}$ grid. |
| Reduction target | $f_R$=1.00 |  | 50.00% | 0.55 | 6/10 | Threshold reached on the simulated $VE_{inf}$ grid. |
| Reduction target | $f_R$=1.00 |  | 75.00% | Not reached through 0.55 | 4/10 | Threshold not reached on the simulated grid. |
| Reduction target | $f_R$=1.10 |  | 25.00% | 0.50 | 7/10 | Threshold reached on the simulated $VE_{inf}$ grid. |
| Reduction target | $f_R$=1.10 |  | 50.00% | Not reached through 0.55 | 4/10 | Threshold not reached on the simulated grid. |
| Reduction target | $f_R$=1.10 |  | 75.00% | Not reached through 0.55 | 1/10 | Threshold not reached on the simulated grid. |
| Reduction target | $f_R$=1.15 |  | 25.00% | 0.55 | 8/10 | Threshold reached on the simulated $VE_{inf}$ grid. |
| Reduction target | $f_R$=1.15 |  | 50.00% | Not reached through 0.55 | 2/10 | Threshold not reached on the simulated grid. |
| Reduction target | $f_R$=1.15 |  | 75.00% | Not reached through 0.55 | 1/10 | Threshold not reached on the simulated grid. |
| Comparator threshold | Infant exposure reduction strategy | 0.00 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.40 | 10/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Resistance-guided treatment | 0.00 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.35 | 10/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Infant exposure reduction strategy | 0.50 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.50 | 8/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Resistance-guided treatment | 0.50 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.50 | 9/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Infant exposure reduction strategy | 1.00 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.50 | 8/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Resistance-guided treatment | 1.00 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.50 | 9/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | 25% reduction vs $VE_{inf}$ 0.20 | 0.50 | Median across evaluated profiles on the $VE_{inf}$-only grid at 50% starting resistance prevalence. | 0.40 | 6/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | 50% reduction vs $VE_{inf}$ 0.20 | 0.50 | Median across evaluated profiles on the $VE_{inf}$-only grid at 50% starting resistance prevalence. | 0.50 | 6/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | 75% reduction vs $VE_{inf}$ 0.20 | 0.50 | Median across evaluated profiles on the $VE_{inf}$-only grid at 50% starting resistance prevalence. | Not reached | 0/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |

<div style="page-break-after: always;"></div>

### eTable 15. Intervention outcome summaries by country and strategy.

| Country | Strategy | Total infections | Reported cases | Infant cases | Resistant infections | Infant-case reduction | Infection reduction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | Adolescent booster | 23,966,520.52 | 397,164.11 | 186,347.93 | 22,458,655.95 | 0.00 | 0.00 |
| Australia | Close-contact adult adjunct | 23,740,397.57 | 387,251.81 | 179,290.07 | 22,370,693.18 | 0.04 | 0.01 |
| Australia | Combined strategy | 16,393,944.68 | 221,600.83 | 74,496.88 | 11,420,864.74 | 0.60 | 0.32 |
| Australia | Current practice | 23,960,486.82 | 397,054.15 | 186,312.27 | 22,453,720.74 | 0.00 | 0.00 |
| Australia | Coverage-floor-only scenario | 23,985,714.89 | 398,454.72 | 186,703.58 | 22,474,991.43 | 0.00 | 0.00 |
| Australia | Reproductive-age adult boosting only | 23,752,319.16 | 389,293.33 | 183,270.62 | 22,386,250.99 | 0.02 | 0.01 |
| Australia | Contact reduction only | 23,943,354.74 | 394,859.90 | 182,121.73 | 22,433,642.28 | 0.02 | 0.00 |
| Australia | Direct maternal antibody only | 23,938,406.52 | 386,794.12 | 168,744.46 | 22,415,690.31 | 0.09 | 0.00 |
| Australia | Infant-exposure reduction strategy | 23,710,560.64 | 377,212.77 | 162,306.18 | 22,323,018.83 | 0.13 | 0.01 |
| Australia | High-transmission-blocking vaccine target | 15,821,823.62 | 218,041.89 | 85,197.09 | 14,464,045.44 | 0.54 | 0.34 |
| Australia | Pregnancy Tdap scale-up | 23,938,406.52 | 386,794.12 | 168,744.46 | 22,415,690.31 | 0.09 | 0.00 |
| Australia | Resistance-guided treatment | 22,500,651.17 | 355,791.31 | 154,493.05 | 9,225,083.32 | 0.17 | 0.06 |
| Australia | Targeted high-risk PEP | 23,797,925.81 | 391,983.98 | 181,518.44 | 22,930,595.96 | 0.03 | 0.01 |
| Brazil | Adolescent booster | 602,744.40 | 9,296.84 | 2,382.83 | 8,589.80 | 0.79 | 0.79 |
| Brazil | Close-contact adult adjunct | 444,705.88 | 6,879.51 | 1,700.60 | 5,787.68 | 0.85 | 0.84 |
| Brazil | Combined strategy | 43,120.17 | 648.31 | 165.25 | 382.77 | 0.99 | 0.98 |
| Brazil | Current practice | 2,857,035.12 | 45,073.32 | 11,159.72 | 128,561.16 | 0.00 | 0.00 |
| Brazil | Coverage-floor-only scenario | 3,270,276.50 | 52,009.17 | 12,799.39 | 175,774.31 | -0.15 | -0.14 |
| Brazil | Reproductive-age adult boosting only | 453,363.74 | 7,039.61 | 1,781.79 | 5,934.54 | 0.84 | 0.84 |
| Brazil | Contact reduction only | 2,758,234.38 | 43,335.13 | 10,452.48 | 118,514.65 | 0.06 | 0.03 |
| Brazil | Direct maternal antibody only | 2,740,546.84 | 42,631.55 | 9,795.25 | 116,164.42 | 0.12 | 0.04 |
| Brazil | Infant-exposure reduction strategy | 432,961.72 | 6,604.57 | 1,515.08 | 5,589.73 | 0.86 | 0.85 |
| Brazil | High-transmission-blocking vaccine target | 47,709.79 | 714.95 | 191.94 | 494.46 | 0.98 | 0.98 |
| Brazil | Pregnancy Tdap scale-up | 2,740,546.84 | 42,631.55 | 9,795.25 | 116,164.42 | 0.12 | 0.04 |
| Brazil | Resistance-guided treatment | 1,210,079.53 | 19,025.82 | 4,683.11 | 4,247.47 | 0.58 | 0.58 |
| Brazil | Targeted high-risk PEP | 2,599,684.69 | 40,976.27 | 10,132.61 | 141,074.25 | 0.09 | 0.09 |
| China | Adolescent booster | 125,333,078.73 | 5,112,085.33 | 440,662.32 | 125,292,573.44 | 0.23 | 0.25 |
| China | Close-contact adult adjunct | 95,841,592.82 | 3,873,866.05 | 318,503.59 | 95,800,856.01 | 0.44 | 0.43 |
| China | Combined strategy | 543,185.16 | 20,997.15 | 1,546.93 | 541,261.71 | 1.00 | 1.00 |
| China | Current practice | 167,252,430.53 | 6,968,485.05 | 569,957.79 | 167,206,617.14 | 0.00 | 0.00 |
| China | Coverage-floor-only scenario | 168,890,119.25 | 7,067,870.01 | 577,171.98 | 168,844,471.86 | -0.01 | -0.01 |
| China | Reproductive-age adult boosting only | 96,534,368.32 | 3,909,680.09 | 329,167.31 | 96,493,658.93 | 0.42 | 0.42 |
| China | Contact reduction only | 166,132,148.48 | 6,906,612.41 | 550,689.20 | 166,086,299.58 | 0.03 | 0.01 |
| China | Direct maternal antibody only | 164,793,655.63 | 6,790,880.87 | 489,315.17 | 164,747,524.74 | 0.14 | 0.01 |
| China | Infant-exposure reduction strategy | 94,204,281.27 | 3,766,980.10 | 272,927.72 | 94,163,297.87 | 0.52 | 0.44 |
| China | High-transmission-blocking vaccine target | 1,058,436.85 | 41,111.78 | 3,262.59 | 1,055,469.54 | 0.99 | 0.99 |
| China | Pregnancy Tdap scale-up | 164,793,655.63 | 6,790,880.87 | 489,315.17 | 164,747,524.74 | 0.14 | 0.01 |
| China | Resistance-guided treatment | 88,167,875.60 | 3,653,708.96 | 289,133.47 | 66,058,859.81 | 0.49 | 0.47 |
| China | Targeted high-risk PEP | 167,752,006.90 | 7,005,650.08 | 572,223.09 | 167,718,956.70 | 0.00 | 0.00 |
| Japan | Adolescent booster | 26,399,997.31 | 409,534.26 | 79,542.58 | 26,073,172.85 | 0.04 | 0.04 |
| Japan | Close-contact adult adjunct | 20,642,816.95 | 311,225.21 | 58,525.43 | 20,327,926.32 | 0.29 | 0.25 |
| Japan | Combined strategy | 247,740.65 | 3,429.41 | 529.03 | 175,418.42 | 0.99 | 0.99 |
| Japan | Current practice | 27,536,156.22 | 432,979.22 | 82,781.93 | 27,192,103.53 | 0.00 | 0.00 |
| Japan | Coverage-floor-only scenario | 27,602,864.30 | 435,588.18 | 83,103.58 | 27,258,985.43 | 0.00 | 0.00 |
| Japan | Reproductive-age adult boosting only | 20,696,340.23 | 313,174.10 | 60,339.58 | 20,381,993.00 | 0.27 | 0.25 |
| Japan | Contact reduction only | 27,507,598.28 | 430,890.72 | 80,289.28 | 27,162,851.52 | 0.03 | 0.00 |
| Japan | Direct maternal antibody only | 27,470,043.48 | 423,450.81 | 71,804.29 | 27,122,438.03 | 0.13 | 0.00 |
| Japan | Infant-exposure reduction strategy | 20,540,846.23 | 303,684.07 | 50,638.58 | 20,222,907.91 | 0.39 | 0.25 |
| Japan | High-transmission-blocking vaccine target | 6,518,698.92 | 94,532.03 | 16,498.52 | 6,305,541.58 | 0.80 | 0.76 |
| Japan | Pregnancy Tdap scale-up | 27,470,043.48 | 423,450.81 | 71,804.29 | 27,122,438.03 | 0.13 | 0.00 |
| Japan | Resistance-guided treatment | 19,934,391.77 | 309,054.42 | 56,462.66 | 10,455,747.99 | 0.32 | 0.28 |
| Japan | Targeted high-risk PEP | 27,016,463.52 | 424,453.51 | 80,916.47 | 26,796,354.41 | 0.02 | 0.02 |
| New Zealand | Adolescent booster | 3,334,592.80 | 51,174.24 | 21,601.17 | 2,965,841.27 | 0.00 | 0.00 |
| New Zealand | Close-contact adult adjunct | 3,198,195.00 | 47,944.62 | 19,907.75 | 2,832,704.78 | 0.08 | 0.04 |
| New Zealand | Combined strategy | 1,563,529.10 | 20,197.61 | 6,464.09 | 55,736.37 | 0.70 | 0.53 |
| New Zealand | Current practice | 3,327,226.30 | 51,035.99 | 21,540.81 | 2,957,053.86 | 0.00 | 0.00 |
| New Zealand | Coverage-floor-only scenario | 3,345,654.69 | 51,651.22 | 21,739.90 | 2,978,054.72 | -0.01 | -0.01 |
| New Zealand | Reproductive-age adult boosting only | 3,201,603.32 | 48,192.38 | 20,352.94 | 2,836,850.23 | 0.06 | 0.04 |
| New Zealand | Contact reduction only | 3,323,333.55 | 50,755.23 | 21,042.81 | 2,952,290.17 | 0.02 | 0.00 |
| New Zealand | Direct maternal antibody only | 3,320,252.22 | 49,759.21 | 19,403.72 | 2,945,610.78 | 0.10 | 0.00 |
| New Zealand | Infant-exposure reduction strategy | 3,192,102.00 | 46,770.62 | 17,935.76 | 2,822,054.90 | 0.17 | 0.04 |
| New Zealand | High-transmission-blocking vaccine target | 1,588,469.19 | 20,199.63 | 7,460.05 | 1,268,590.81 | 0.65 | 0.52 |
| New Zealand | Pregnancy Tdap scale-up | 3,320,252.22 | 49,759.21 | 19,403.72 | 2,945,610.78 | 0.10 | 0.00 |
| New Zealand | Resistance-guided treatment | 2,882,500.81 | 42,854.95 | 17,072.85 | 66,174.25 | 0.21 | 0.13 |
| New Zealand | Targeted high-risk PEP | 3,091,033.32 | 47,052.65 | 19,667.33 | 2,898,369.47 | 0.09 | 0.07 |
| South Africa | Adolescent booster | 304,955.70 | 4,608.94 | 1,737.07 | 11,965.43 | 0.87 | 0.87 |
| South Africa | Close-contact adult adjunct | 652,418.15 | 9,948.67 | 3,558.56 | 52,048.48 | 0.73 | 0.72 |
| South Africa | Combined strategy | 13,120.52 | 193.23 | 69.11 | 229.76 | 0.99 | 0.99 |
| South Africa | Current practice | 2,361,482.23 | 36,341.05 | 13,237.19 | 844,077.97 | 0.00 | 0.00 |
| South Africa | Coverage-floor-only scenario | 1,313,792.31 | 19,283.91 | 6,802.93 | 215,178.87 | 0.49 | 0.44 |
| South Africa | Reproductive-age adult boosting only | 683,009.62 | 10,458.82 | 3,825.72 | 57,452.58 | 0.71 | 0.71 |
| South Africa | Contact reduction only | 2,286,280.86 | 35,034.69 | 12,464.47 | 785,482.80 | 0.06 | 0.03 |
| South Africa | Direct maternal antibody only | 2,226,958.68 | 33,492.35 | 11,019.00 | 731,907.94 | 0.17 | 0.06 |
| South Africa | Infant-exposure reduction strategy | 602,289.40 | 8,976.53 | 2,899.62 | 43,630.18 | 0.78 | 0.74 |
| South Africa | High-transmission-blocking vaccine target | 12,739.68 | 196.51 | 80.65 | 264.63 | 0.99 | 0.99 |
| South Africa | Pregnancy Tdap scale-up | 2,226,958.68 | 33,492.35 | 11,019.00 | 731,907.94 | 0.17 | 0.06 |
| South Africa | Resistance-guided treatment | 1,033,313.78 | 15,928.86 | 5,765.30 | 4,075.04 | 0.56 | 0.56 |
| South Africa | Targeted high-risk PEP | 2,368,764.28 | 36,377.60 | 13,230.57 | 1,171,391.37 | 0.00 | 0.00 |
| Sweden | Adolescent booster | 2,458,581.93 | 35,587.59 | 10,274.65 | 1,905,994.92 | 0.00 | 0.00 |
| Sweden | Close-contact adult adjunct | 2,057,985.20 | 29,174.59 | 8,287.44 | 1,523,466.26 | 0.19 | 0.16 |
| Sweden | Combined strategy | 11,638.42 | 151.21 | 36.57 | 81.53 | 1.00 | 1.00 |
| Sweden | Current practice | 2,457,347.47 | 35,566.76 | 10,269.61 | 1,904,827.80 | 0.00 | 0.00 |
| Sweden | Coverage-floor-only scenario | 2,476,305.93 | 35,970.68 | 10,365.38 | 1,924,554.21 | -0.01 | -0.01 |
| Sweden | Reproductive-age adult boosting only | 2,066,576.85 | 29,410.73 | 8,536.19 | 1,532,946.67 | 0.17 | 0.16 |
| Sweden | Contact reduction only | 2,447,146.64 | 35,276.55 | 9,960.71 | 1,893,702.67 | 0.03 | 0.00 |
| Sweden | Direct maternal antibody only | 2,441,121.53 | 34,707.98 | 9,202.27 | 1,883,633.42 | 0.10 | 0.01 |
| Sweden | Infant-exposure reduction strategy | 2,045,168.86 | 28,489.23 | 7,428.85 | 1,505,648.49 | 0.28 | 0.17 |
| Sweden | High-transmission-blocking vaccine target | 4,890.67 | 63.17 | 17.94 | 51.74 | 1.00 | 1.00 |
| Sweden | Pregnancy Tdap scale-up | 2,441,121.53 | 34,707.98 | 9,202.27 | 1,883,633.42 | 0.10 | 0.01 |
| Sweden | Resistance-guided treatment | 1,867,827.57 | 26,633.48 | 7,389.05 | 4,134.35 | 0.28 | 0.24 |
| Sweden | Targeted high-risk PEP | 2,452,128.54 | 35,403.33 | 10,181.15 | 2,089,545.09 | 0.01 | 0.00 |
| Thailand | Adolescent booster | 182,096.28 | 2,587.69 | 599.04 | 2,363.67 | 0.70 | 0.71 |
| Thailand | Close-contact adult adjunct | 125,269.31 | 1,779.31 | 401.20 | 1,499.49 | 0.80 | 0.80 |
| Thailand | Combined strategy | 16,913.77 | 231.27 | 51.06 | 150.35 | 0.97 | 0.97 |
| Thailand | Current practice | 625,450.99 | 9,062.47 | 2,021.24 | 15,328.16 | 0.00 | 0.00 |
| Thailand | Coverage-floor-only scenario | 685,943.78 | 9,996.39 | 2,196.99 | 18,360.60 | -0.09 | -0.10 |
| Thailand | Reproductive-age adult boosting only | 126,845.03 | 1,807.68 | 417.02 | 1,522.16 | 0.79 | 0.80 |
| Thailand | Contact reduction only | 606,622.58 | 8,757.48 | 1,903.93 | 14,460.64 | 0.06 | 0.03 |
| Thailand | Direct maternal antibody only | 594,570.87 | 8,455.32 | 1,684.58 | 13,890.18 | 0.17 | 0.05 |
| Thailand | Infant-exposure reduction strategy | 122,056.09 | 1,701.06 | 342.56 | 1,453.36 | 0.83 | 0.80 |
| Thailand | High-transmission-blocking vaccine target | 21,247.19 | 293.52 | 71.03 | 220.87 | 0.96 | 0.97 |
| Thailand | Pregnancy Tdap scale-up | 594,570.87 | 8,455.32 | 1,684.58 | 13,890.18 | 0.17 | 0.05 |
| Thailand | Resistance-guided treatment | 302,678.37 | 4,378.97 | 974.15 | 1,332.42 | 0.52 | 0.52 |
| Thailand | Targeted high-risk PEP | 584,529.63 | 8,468.64 | 1,888.43 | 15,612.73 | 0.07 | 0.07 |
| United Kingdom | Adolescent booster | 35,175,229.60 | 489,997.76 | 223,760.52 | 30,048,901.77 | -0.01 | -0.01 |
| United Kingdom | Close-contact adult adjunct | 31,128,207.08 | 417,359.08 | 186,432.79 | 25,932,619.89 | 0.16 | 0.11 |
| United Kingdom | Combined strategy | 10,065,525.57 | 116,330.17 | 40,438.20 | 9,674.07 | 0.82 | 0.71 |
| United Kingdom | Current practice | 34,942,169.45 | 486,413.80 | 222,136.10 | 29,651,102.24 | 0.00 | 0.00 |
| United Kingdom | Coverage-floor-only scenario | 35,391,583.51 | 496,339.53 | 225,810.02 | 30,141,664.02 | -0.02 | -0.01 |
| United Kingdom | Reproductive-age adult boosting only | 31,197,677.72 | 420,247.33 | 191,569.66 | 26,014,468.60 | 0.14 | 0.11 |
| United Kingdom | Contact reduction only | 34,862,692.86 | 482,852.09 | 215,764.39 | 29,557,968.74 | 0.03 | 0.00 |
| United Kingdom | Direct maternal antibody only | 34,809,743.64 | 473,618.23 | 199,287.52 | 29,452,271.41 | 0.10 | 0.00 |
| United Kingdom | Infant-exposure reduction strategy | 31,024,215.72 | 406,769.43 | 167,333.76 | 25,764,668.96 | 0.25 | 0.11 |
| United Kingdom | High-transmission-blocking vaccine target | 16,464,931.51 | 195,407.74 | 76,400.90 | 11,599,813.56 | 0.66 | 0.53 |
| United Kingdom | Pregnancy Tdap scale-up | 34,809,743.64 | 473,618.23 | 199,287.52 | 29,452,271.41 | 0.10 | 0.00 |
| United Kingdom | Resistance-guided treatment | 29,633,755.75 | 402,358.81 | 173,155.67 | 63,958.26 | 0.22 | 0.15 |
| United Kingdom | Targeted high-risk PEP | 31,719,466.84 | 439,757.65 | 199,837.61 | 28,713,843.70 | 0.10 | 0.09 |
| United States | Adolescent booster | 7,661,498.97 | 121,586.88 | 30,005.20 | 0 | -0.03 | -0.03 |
| United States | Close-contact adult adjunct | 2,342,472.81 | 36,608.91 | 8,899.66 | 0 | 0.69 | 0.68 |
| United States | Combined strategy | 83,153.56 | 1,282.70 | 305.80 | 0 | 0.99 | 0.99 |
| United States | Current practice | 7,418,543.46 | 117,714.81 | 29,055.37 | 0 | 0.00 | 0.00 |
| United States | Coverage-floor-only scenario | 7,848,636.15 | 125,131.05 | 30,779.84 | 0 | -0.06 | -0.06 |
| United States | Reproductive-age adult boosting only | 2,427,767.61 | 38,088.61 | 9,481.58 | 0 | 0.67 | 0.67 |
| United States | Contact reduction only | 7,256,068.89 | 114,665.39 | 27,607.15 | 0 | 0.05 | 0.02 |
| United States | Direct maternal antibody only | 7,201,601.50 | 112,388.06 | 25,448.07 | 0 | 0.12 | 0.03 |
| United States | Infant-exposure reduction strategy | 2,230,969.08 | 34,303.12 | 7,648.95 | 0 | 0.74 | 0.70 |
| United States | High-transmission-blocking vaccine target | 56,444.49 | 868.80 | 243.84 | 0 | 0.99 | 0.99 |
| United States | Pregnancy Tdap scale-up | 7,201,601.50 | 112,388.06 | 25,448.07 | 0 | 0.12 | 0.03 |
| United States | Resistance-guided treatment | 3,646,164.58 | 57,613.23 | 14,132.36 | 0 | 0.51 | 0.51 |
| United States | Targeted high-risk PEP | 6,534,876.77 | 103,648.52 | 25,561.06 | 0 | 0.12 | 0.12 |

<div style="page-break-after: always;"></div>

### eTable 16. Near-term implementation sensitivity for resistance-guided treatment and resistant-strain PEP assumptions.

| Scenario | Guided-treatment uptake | PEP restored | PEP reach multiplier | Median infant-case reduction vs current, 5 y | Across-profile IQR reduction | Countries with positive reduction | Median infant cases per 100k | Implementation note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Current near-term practice | 0.00 | Baseline | 1.00 | 0.00 | 0.00-0.00 | 0 | 170.55 | Current macrolide treatment and baseline resistant-strain PEP effectiveness. |
| 25% guided treatment; PEP restored | 0.25 | Yes | 1.00 | -0.11 | -0.21-0.19 | 4 | 204.44 | Quarter uptake of resistance-guided treatment with partial restoration of resistant-strain PEP effectiveness. |
| 50% guided treatment; PEP restored | 0.50 | Yes | 1.00 | -0.16 | -0.35-0.30 | 4 | 226.84 | Half uptake of resistance-guided treatment with partial restoration of resistant-strain PEP effectiveness. |
| 75% guided treatment; PEP restored | 0.75 | Yes | 1.00 | -0.01 | -0.65-0.40 | 5 | 217.75 | Three-quarter uptake of resistance-guided treatment with partial restoration of resistant-strain PEP effectiveness. |
| 100% guided treatment; PEP restored | 1.00 | Yes | 1.00 | 0.16 | -0.68-0.50 | 6 | 204.12 | Full resistance-guided treatment scenario used in the main analysis. |
| 50% guided treatment; no PEP restoration | 0.50 | No | 1.00 | 0.27 | 0.01-0.33 | 8 | 166.62 | Half uptake of resistance-guided treatment; resistant-strain PEP effectiveness remains at baseline. |
| 100% guided treatment; no PEP restoration | 1.00 | No | 1.00 | 0.48 | -0.33-0.50 | 6 | 169.13 | Full treatment restoration but no restoration of resistant-strain PEP effectiveness. |
| 50% guided treatment; low PEP reach | 0.50 | Yes | 0.50 | 0.15 | -0.23-0.27 | 7 | 193.74 | Half uptake and half baseline PEP reach, approximating delayed activation, lower adherence, or household-only reach. |

<div style="page-break-after: always;"></div>

### eTable 17. Infant-contact and maternal passive-protection sensitivity diagnostics.

| Sensitivity dimension | Strategy | Setting | Median infant cases per 100k, 5 y | Across-profile IQR infant cases per 100k, 5 y | Median infant-case reduction vs current, 5 y | Across-profile IQR reduction | Countries with positive reduction | Countries | Interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Infant contact multiplier | Current practice | 0.75 | 120.10 | 30.00-383.60 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Current practice | 1.00 | 140.19 | 37.22-441.10 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Current practice | 1.25 | 162.38 | 45.51-499.90 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Current practice | 1.50 | 185.96 | 55.00-563.10 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Infant-exposure reduction strategy | 0.75 | 51.98 | 7.46-276.70 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Infant-exposure reduction strategy | 1.00 | 59.88 | 9.64-315.90 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Infant-exposure reduction strategy | 1.25 | 68.62 | 12.48-355.20 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Infant-exposure reduction strategy | 1.50 | 78.01 | 16.22-395.70 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Maternal passive-protection duration | Current practice | 90.00 | 140.19 | 37.22-441.10 | 0.00 | 0.00-0.00 | 0 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Direct maternal antibody only | 90.00 | 127.99 | 33.51-406.70 | 0.09 | 0.07-0.12 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Infant-exposure reduction strategy | 90.00 | 61.37 | 10.09-324.40 | 0.57 | 0.23-0.74 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Current practice | 180.00 | 139.26 | 36.88-435.00 | 0.00 | 0.00-0.00 | 0 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Direct maternal antibody only | 180.00 | 124.12 | 32.34-392.70 | 0.11 | 0.09-0.15 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Infant-exposure reduction strategy | 180.00 | 59.88 | 9.64-315.90 | 0.58 | 0.25-0.75 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Current practice | 270.00 | 139.08 | 36.69-433.80 | 0.00 | 0.00-0.00 | 0 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Direct maternal antibody only | 270.00 | 122.23 | 31.78-387.20 | 0.12 | 0.10-0.16 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Infant-exposure reduction strategy | 270.00 | 58.50 | 9.47-311.10 | 0.59 | 0.26-0.76 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |

<div style="page-break-after: always;"></div>

### eTable 18. Near-term temporal assumption sensitivity for burn-in duration and COVID-19 NPI contact-shock assumptions.

| Temporal dimension | Scenario | Countries | Burn-in years | NPI reduction scale | Median infant cases per 100k, 5 y | Across-profile IQR infant cases per 100k, 5 y | Median all infections per 100k, 5 y | Median end resistant fraction, 5 y | Implementation note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Burn-in | Burnin 10y | 10 | 10.00 | 1.00 | 52.11 | 33.67-983.20 | 135.77 | 0.39 | Near-term current-practice run varying pre-analysis burn-in duration. |
| Burn-in | Burnin 15y | 10 | 15.00 | 1.00 | 170.55 | 38.93-525.80 | 354.02 | 0.10 | Near-term current-practice run varying pre-analysis burn-in duration. |
| Burn-in | Burnin 30y | 10 | 30.00 | 1.00 | 336.36 | 33.89-737.30 | 659.21 | 0.16 | Near-term current-practice run varying pre-analysis burn-in duration. |
| NPI contact shock | NPI country profile | 1 | 15.00 | 1.00 | 547.24 | 547.20-547.20 | 680.06 | 0.44 | Near-term current-practice run varying COVID-19 NPI contact-reduction assumptions for countries with explicit NPI periods. |
| NPI contact shock | Half NPI contact shock | 1 | 15.00 | 0.50 | 228.62 | 228.60-228.60 | 297.34 | 0.19 | Near-term current-practice run varying COVID-19 NPI contact-reduction assumptions for countries with explicit NPI periods. |
| NPI contact shock | No NPI contact shock | 1 | 15.00 |  | 2,996.53 | 2997.00-2997.00 | 3,855.37 | 0.99 | Near-term current-practice run varying COVID-19 NPI contact-reduction assumptions for countries with explicit NPI periods. |

<div style="page-break-after: always;"></div>

### eTable 19. Deterministic event-scale diagnostics for stochastic-interpretation sensitivity.

| Scenario | Countries | Median annual infant cases | Minimum annual infant cases | Median infant cases per 100k/y | Low-event countries | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Adolescent booster | 10 | 991.91 | 23.03 | 310.43 | Thailand | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Close-contact adult adjunct | 10 | 553.70 | 15.42 | 230.44 | Thailand | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Combined strategy | 10 | 16.05 | 1.41 | 1.10 | Sweden; South Africa; Thailand; Brazil; United States; Japan | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Current practice | 10 | 972.49 | 77.70 | 341.40 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Coverage-floor-only scenario | 10 | 1,009.46 | 84.45 | 345.04 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Infant-exposure reduction strategy | 10 | 491.75 | 13.17 | 198.75 | Thailand | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| High-transmission-blocking vaccine target | 10 | 67.40 | 0.69 | 1.14 | Sweden; South Africa; Thailand; Brazil; United States | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Pregnancy Tdap scale-up | 10 | 862.08 | 64.76 | 300.77 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Resistance-guided treatment | 10 | 599.78 | 37.45 | 216.58 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Targeted high-risk PEP | 10 | 869.32 | 72.59 | 340.18 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |

<div style="page-break-after: always;"></div>

### eTable 20. Limitation-to-diagnostic map and residual interpretation.

| Limitation domain | Added or existing diagnostic | Supplement location | Residual interpretation |
| --- | --- | --- | --- |
| Infant outcomes without direct age-specific calibration | Overall calibration fit, fitted reporting gradients, infant contact sensitivity, event-scale diagnostics, and routine-timeliness, infant-age/window, and external age-pattern weighted ordering diagnostics. | Supplementary Methods, eTables 7, 12, 17, and 19, and eFigure 9 | Infant estimates are conditional model outputs; age-pattern weighting is a partial external consistency diagnostic, not full recalibration. |
| Strategy-profile ordering under selected-parameter sensitivity | Country-level order positions, analysis-window order positions, infant-age/window order positions, strategy-ordering summary, Figure 4B conditional-interval audit data, and selected-parameter deterministic strategy-ordering diagnostics. | eTable 15 and eFigure 9 | Order-position probabilities are conditional on the selected epidemiologic sensitivity ranges and do not include costs, feasibility, or equity weights. |
| Deterministic dynamics without stochastic extinction or superspreading | Event-scale diagnostics identify low-event cells where deterministic persistence assumptions matter most; a small individual stochastic toy model illustrates contact-clustering sensitivity. | eTables 19 and 21 | Near-zero burdens and low-event cells should be read as deterministic thresholds, not stochastic elimination probabilities. |
| No explicit household clustering, contact tracing, or adherence model | Resistance-guided treatment implementation sensitivity, infant contact-matrix sensitivity, maternal package component decomposition, and individual stochastic contact-clustering illustration. | eTables 16, 17, 21, and 24, and eFigure 9 | Age-structured proxy diagnostics do not replace household or contact-tracing simulations. |
| Macrolide-resistant strain dynamics depend on fitness and management assumptions | Resistance mechanism decomposition, fitness grids, hindcast plausibility checks, treatment/PEP implementation sensitivity, vaccine-infectiousness thresholds, and resistance-parameter justification. | eTables 13, 14, 16, and 23, and eFigure 9 | Resistance trajectories remain stress tests of selection mechanisms rather than unconditional replacement predictions. |
| No costs, utility weights, feasibility, or equity weights | Exploratory burden translation from model deaths and symptomatic cases, with hospitalization imputed from transparent scenario assumptions. | Repository health-utility output tables | This is not a formal cost-effectiveness analysis; the model still does not include costs, decision thresholds, discounting, feasibility constraints, or equity weights. |
| In-development vaccine products cannot be treated as available policies | Pipeline-to-mechanism mapping for intranasal BPZE1, OMV-based platforms, genetically detoxified recombinant aP vaccines, and new multicomponent aP candidates. | eTable 22 | Candidate products were represented through mechanism profiles and sensitivity ranges, not product-specific policy scenarios. |

<div style="page-break-after: always;"></div>

### eTable 21. Individual stochastic contact-clustering toy model key diagnostics (100 replicates, synthetic population 1,500, target R=1.08; structural sensitivity only).

| Country | Contact structure | Pr(extinct <=3) | Pr(outbreak >=20 infections) | Total infections, median (2.5%-97.5% replicate range) | Infant infections (mean; Pr any; Q95) | Mean household clusters |
| --- | --- | --- | --- | --- | --- | --- |
| Australia | Homogeneous all contacts | 0.69 | 0.17 | 1.00 (1.00-200.92) | mean 0.01; Pr(any) 0.01; Q95 0.00 | 19.02 |
| Australia | Setting clustered | 0.66 | 0.06 | 2.00 (1.00-67.05) | mean 0.04; Pr(any) 0.04; Q95 0.00 | 4.71 |
| Australia | Setting clustered high household | 0.71 | 0.09 | 1.00 (1.00-31.10) | mean 0.08; Pr(any) 0.08; Q95 1.00 | 3.43 |
| China | Homogeneous all contacts | 0.66 | 0.14 | 1.00 (1.00-118.25) | mean 0.00; Pr(any) 0.00; Q95 0.00 | 14.22 |
| China | Setting clustered | 0.68 | 0.05 | 2.00 (1.00-33.10) | mean 0.07; Pr(any) 0.07; Q95 1.00 | 3.37 |
| China | Setting clustered high household | 0.75 | 0.04 | 2.00 (1.00-21.52) | mean 0.10; Pr(any) 0.10; Q95 1.00 | 2.50 |
| Japan | Homogeneous all contacts | 0.72 | 0.12 | 1.00 (1.00-131.75) | mean 0.00; Pr(any) 0.00; Q95 0.00 | 14.29 |
| Japan | Setting clustered | 0.64 | 0.14 | 2.00 (1.00-68.52) | mean 0.11; Pr(any) 0.11; Q95 1.00 | 6.66 |
| Japan | Setting clustered high household | 0.68 | 0.05 | 2.00 (1.00-20.52) | mean 0.09; Pr(any) 0.09; Q95 1.00 | 2.97 |
| South Africa | Homogeneous all contacts | 0.54 | 0.29 | 2.00 (1.00-195.67) | mean 0.08; Pr(any) 0.06; Q95 1.00 | 23.51 |
| South Africa | Setting clustered | 0.76 | 0.07 | 1.00 (1.00-42.30) | mean 0.01; Pr(any) 0.01; Q95 0.00 | 3.41 |
| South Africa | Setting clustered high household | 0.75 | 0.00 | 1.00 (1.00-10.52) | mean 0.09; Pr(any) 0.09; Q95 1.00 | 1.90 |
| United States | Homogeneous all contacts | 0.70 | 0.14 | 2.00 (1.00-85.12) | mean 0.00; Pr(any) 0.00; Q95 0.00 | 11.84 |
| United States | Setting clustered | 0.73 | 0.06 | 2.00 (1.00-37.57) | mean 0.06; Pr(any) 0.06; Q95 1.00 | 3.36 |
| United States | Setting clustered high household | 0.74 | 0.03 | 1.00 (1.00-19.05) | mean 0.08; Pr(any) 0.07; Q95 1.00 | 2.39 |

<div style="page-break-after: always;"></div>

### eTable 22. Vaccine-pipeline mechanism mapping to modeled scenario profiles.

| Candidate/platform | Development status | Transmission-relevant signal | Model use | Evidence source |
| --- | --- | --- | --- | --- |
| BPZE1 intranasal live attenuated | Phase 2b adult/challenge evidence; school-age trial registered. | Mucosal immunity and colonization reduction; closest to the high-transmission-blocking target. | Upper-bound transmission-blocking profile plus $VE_{inf}$ sensitivity; no product-specific efficacy assigned. | Keech et al [38]; Gbesemete et al [39]; ClinicalTrials.gov NCT03942406, NCT05461131, NCT05116241. |
| OMV or OMV-adjuvanted platforms | Preclinical/translational evidence; no late-stage pertussis efficacy trial identified. | Broader antigenic and Th1/Th17 responses; possible effects on susceptibility, infectiousness, or duration. | Covered by infection-/transmission-blocking profiles and $VE_{inf}$/$VE_{dur}$ ranges. | Locati et al [40]; related OMV literature cited therein. |
| Recombinant PT acellular boosters | Licensed recombinant boosters reported in Asia; Pertagen2x phase II/III registered. | Potentially stronger or more durable antibody response; not primarily mucosal transmission blocking. | Mapped to adolescent booster, current aP, infection-blocking, or waning-duration sensitivity. | BioNet pertussis product information; ClinicalTrials.gov NCT05193734. |
| New multi-component acellular combinations | CanSino DTcP phase 3 active-not-recruiting; other products remain platform-specific. | Relevant to clinical protection and possibly infection blocking; limited direct carriage evidence. | Covered by current aP and infection-blocking profiles; no separate product scenario. | ClinicalTrials.gov NCT05951725. |

<div style="page-break-after: always;"></div>

### eTable 23. Macrolide-resistance parameter justification and expected direction of bias.

| Parameter group | Baseline value | Explored range or scenarios | Source or anchor | Rationale | Expected direction of bias | Residual caveat |
| --- | --- | --- | --- | --- | --- | --- |
| Country-specific starting resistant fraction | Latest admissible country timeline anchor; fixed scenarios also used 5%, 30%, 70%, and 95% | Country timeline; fixed low, moderate, high, and very-high resistance scenarios | Country resistance timeline assembled from China, Japan, Australia, Americas, Europe, and low-anchor surveillance reports through the evidence lock | Separates observed or conservative starting strain composition from subsequent modeled selection dynamics. | Higher starting resistant fraction increases resistant burden and the apparent value of resistance-guided management; lower anchors delay resistant dominance. | Resistance sampling is heterogeneous across countries and years; anchors are not a globally representative surveillance system. |
| Resistant-strain relative fitness (fitness_R) | 1.00 (fitness neutral) | 0.70-1.25 grid and selected-parameter sensitivity range; selected narrative contrasts at 0.85, 1.00, and 1.15 | Rapid MRBP expansion and international spread without a demonstrated transmission penalty; local evidence note in manuscript_notes/resistance_fitness_evidence.md | Avoids assuming a persistent fitness cost when epidemiologic trajectories in China, Japan, and Australia do not rule out neutral or above-neutral fitness. | Lower fitness reduces projected resistant fraction and resistant-guided treatment benefit; higher fitness accelerates replacement and increases resistant burden. | Fitness is represented as one transmission scalar and may vary with vaccine history, treatment pressure, strain background, and host immunity. |
| Sensitive-strain treatment effect | Infectious-duration reduction 0.20; infectiousness reduction 0.15 | Treatment implementation and resistance-mechanism decomposition scenarios | CDC pertussis treatment/PEP guidance and model scenario assumptions | Represents early macrolide benefit for susceptible infections without assuming treatment fully blocks transmission. | Stronger sensitive-strain treatment benefit increases selection pressure favoring resistant strains; weaker benefit reduces modeled treatment-mediated selection. | Real-world treatment effect depends on timing, diagnosis, adherence, and clinical practice, none of which are explicitly modeled as individual pathways. |
| Resistant-strain treatment effect under standard macrolide practice | Infectious-duration reduction 0.10; infectiousness reduction 0.05 | Equalized treatment counterfactual; resistance-guided treatment alternative | Resistance-aware scenario assumption informed by macrolide resistance biology and treatment guidance | Allows resistant infections to receive less benefit from standard macrolide management while testing whether that differential drives replacement. | Lower resistant treatment benefit increases resistant burden and infant cases; equalizing treatment effects lowers selection for resistance. | The model does not identify strain-specific treatment effect from patient-level outcome data. |
| Postexposure prophylaxis (PEP) coverage | Household-contact coverage 0.30 | 0.05-0.60 in sensitivity analysis and selected-parameter sensitivity multiplier; implementation scenarios vary PEP reach | CDC/PAHO-style public health PEP guidance translated into scenario coverage assumptions | Represents partial household/contact implementation rather than universal prophylaxis. | Higher PEP reach amplifies any strain-specific PEP effectiveness differential; lower PEP reach weakens PEP-mediated selection and management benefit. | PEP targeting, timing, adherence, and contact tracing are not explicit household processes in the deterministic model. |
| PEP effectiveness by strain | Sensitive 0.70; resistant 0.10 under standard macrolide PEP | Resistant PEP effectiveness 0.00-0.50; equalized PEP and treatment+PEP decomposition scenarios | Macrolide-resistance mechanism, clinical guidance, and resistance-management scenario assumptions | Tests whether strain-specific prophylaxis failure can plausibly create selection pressure under standard macrolide PEP. | A larger sensitive-resistant PEP gap favors resistant strains; equalized PEP effectiveness markedly lowers projected end resistant fraction. | PEP effectiveness is not estimated from strain-specific household trial data; results are stress tests conditional on PEP reach and timing. |
| Resistance-guided management scenario | Symptomatic treatment rate 0.07; resistant infectious-duration reduction 0.45; resistant infectiousness reduction 0.35; resistant PEP effectiveness 0.45 | Treatment/PEP implementation scenarios and selected-parameter sensitivity uptake multiplier | CDC resistance-aware treatment guidance translated into a testing-and-alternative-treatment scenario | Represents improved recognition of resistance and use of effective alternatives or restored prophylaxis effectiveness. | Higher uptake or restored PEP effectiveness increases projected benefit; low testing reach and uptake reduce or delay benefit. | Testing availability, turnaround time, clinician suspicion, drug tolerability, and adherence are not modeled explicitly. |
| Resistant importation | Low-level importation enabled; default rate 0.20 per 100,000 persons/year with country/scenario resistant fraction | Resistance mechanism decomposition separates ongoing importation from fitness and treatment/PEP differentials | Persistence/reintroduction assumption anchored to observed international spread | Prevents deterministic extinction of rare resistant strains while allowing decomposition of whether importation alone drives high end fractions. | Higher importation affects persistence and timing; mechanism decomposition suggests it is not the main driver of near-complete replacement in the main runs. | Importation is smooth and low-level rather than a stochastic travel- or outbreak-linked process. |

<div style="page-break-after: always;"></div>

### eTable 24. Strategy domains, decision role, and interpretation of model assumptions.

| Strategy domain or assumption | Evidence strength | Decision role | How this should affect scenario-comparison interpretation |
| --- | --- | --- | --- |
| Routine childhood vaccination | Strong programmatic evidence, but marginal gains are constrained when coverage is already high. | Foundational comparator and maintenance priority. | Small modeled marginal gains should not be interpreted as evidence against sustaining high routine coverage. |
| Pregnancy Tdap scale-up | Stronger evidence for direct early-infant protection than for indirect adult-transmission effects. | Direct infant-protection lever. | Provides modest, consistent direct protection; should be separated from broader infant-exposure composites. |
| Infant-exposure reduction composite and components | More implementation dependent than pregnancy Tdap; sensitive to adult-boosting and contact assumptions. | Mechanistic exposure-reduction bundle, not a single practical intervention. | The composite combined direct passive protection, close-contact adult protection, and reproductive-age adult boosting; median component reductions were 12% for pregnancy Tdap alone, 35% for reproductive-age adult boosting, and 3% for contact reduction alone. |
| Targeted high-risk PEP | Guidance informed, but reach and adherence vary. | Contact-management support for infants and high-risk settings. | Interpreted as an outbreak/contact modifier, not broad population control. |
| Resistance-guided management | Dependent on testing reach, turnaround time, alternative treatment, PEP delivery, and adherence; modeled as symptomatic case treatment plus contact PEP restoration. | Resistance-sensitive management modifier. | Can reduce absolute resistant infections under specified assumptions, but is not a stand-alone policy lever. |
| Vaccine transmission-blocking properties | Evidence is stronger for disease protection than for separate transmission-blocking components. | Product-target and mechanism-comparison domain. | Strategy comparisons should distinguish symptom prevention from infection, infectiousness, and duration effects. |
| Infant incidence endpoint | Not directly calibrated across all profiles. | Relative-change comparative estimand, not national forecast. | Supports broad scenario-comparison patterns rather than precise country-specific absolute rates. |

<div style="page-break-after: always;"></div>
