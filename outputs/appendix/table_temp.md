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
| Vaccine-mechanism profile | No vaccine | $VE_{sus}$=0.00; $VE_{sym}$=0.00; $VE_{inf}$=0.00; $VE_{dur}$=0.00 | Null counterfactual with all vaccine-effect parameters set to zero; no external efficacy claim. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | No vaccine protection. | Figure 2A and eTables 14 and 27. |
| Vaccine-mechanism profile | Current aP profile | $VE_{sus}$=0.15; $VE_{sym}$=0.85; $VE_{inf}$=0.25; $VE_{dur}$=0.00 | Acellular-pertussis-like disease protection, asymptomatic-transmission structure, incomplete infection blocking, and waning informed by the WHO vaccine framework [1], transmission evidence [5,6], and duration-of-protection studies [7-9]. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | aP-like disease protection with moderate infection/transmission blocking. The high $VE_{sym}$ value is literature-supported for disease protection, while $VE_{sus}$, $VE_{inf}$, and $VE_{dur}$ are a mechanistic decomposition of that evidence rather than directly observed surveillance parameters. $VE_{inf}$ = 0.25 represents a population-average residual transmission-blocking assumption across recently and distantly vaccinated individuals. | Figure 2A and eTables 14 and 27. |
| Vaccine-mechanism profile | Infection-blocking | $VE_{sus}$=0.70; $VE_{sym}$=0.85; $VE_{inf}$=0.40; $VE_{dur}$=0.10 | Mechanistic scenario above the population-average aP profile, bounded by vaccine-framework assumptions [1], transmission evidence [5,6], and waning studies [7-9], then checked against vaccine-pipeline interpretation in eTable 27. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | Stronger reduction in susceptibility to infection. $VE_{inf}$ = 0.40 represents a plausible upper mechanism bound for recently boosted or more infection-blocking protection, not a direct empirical estimate for current aP products. | Figure 2A and eTables 14 and 27. |
| Vaccine-mechanism profile | Transmission-blocking | $VE_{sus}$=0.30; $VE_{sym}$=0.85; $VE_{inf}$=0.55; $VE_{dur}$=0.30 | Improved-transmission-blocking scenario informed by the WHO vaccine framework [1], aP/wP transmission evidence [5,6], waning studies [7-9], and product-target reasoning in eTable 27; not a licensed product estimate. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | Strong reduction in onward infectiousness and duration. Represents an improved aP formulation or wP-like transmission blocking. | Figure 2A and eTables 14 and 27. |
| Vaccine-mechanism profile | Upper-bound transmission-blocking | $VE_{sus}$=0.80; $VE_{sym}$=0.90; $VE_{inf}$=0.65; $VE_{dur}$=0.40 | Upper-bound high-transmission-blocking product-target profile; represented as a hypothetical mechanism profile using vaccine-framework assumptions [1], transmission evidence [5,6], waning studies [7-9], and pipeline mapping in eTable 27. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | Strong infection, symptom, and transmission protection. Represents an upper-bound high-transmission-blocking pertussis vaccine profile with mucosal immunity induction (e.g. live-attenuated nasal or outer membrane vesicle platforms). | Figure 2A and eTables 14 and 27. |
| Macrolide-resistance scenario | Country timeline | target resistant fraction=0.30; importation resistant fraction=0.30; anchor rate/y=2.00; country timeline=Yes; $f_R$=1.00; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Country-specific resistance anchors combined clinical guidance [21,22] with country reports from China [23,24], Australia [25], Japan [26], the Americas [27], and regional MRBP evidence [28,29]; raw evidence is tabulated in eTable 6 and parameter rationale in eTable 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Country-specific macrolide resistance prevalence from data/raw/country_resistance_timeline.csv. The prevalence anchors are data-derived. $f_R$ = 1.00 is an epidemiologically motivated neutral baseline, not a directly measured strain-fitness estimate: China MRBP rose from 36% (2016) to near-fixation (>99%, 2024), and related MRBP lineages were reported internationally without clear transmission disadvantage. The fitness grid and fitness sensitivity scenarios explore the full range [0.70-1.25]. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | Low | target resistant fraction=0.05; importation resistant fraction=0.05; anchor rate/y=2.00; country timeline=No; $f_R$=1.00; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Fixed prevalence stress-test anchored to observed low-prevalence settings and conservative imported-risk assumptions [21,27-29]; see eTables 3, 6, and 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Low macrolide resistance prevalence with fitness-neutral strain. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | Moderate | target resistant fraction=0.30; importation resistant fraction=0.30; anchor rate/y=2.00; country timeline=No; $f_R$=1.00; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Fixed prevalence stress-test spanning plausible intermediate resistance pressure, using clinical guidance [21,22], China and Australia reports [23-25], Japan and Americas reports [26,27], and regional MRBP evidence [28,29]; see eTables 3, 6, and 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Moderate macrolide resistance prevalence with fitness-neutral strain. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | High | target resistant fraction=0.70; importation resistant fraction=0.70; anchor rate/y=2.00; country timeline=No; $f_R$=1.00; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Fixed prevalence stress-test motivated by high-prevalence MRBP reports in China [23,24], Japan [26], and regional evidence [28,29]; see eTables 3, 6, and 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | High macrolide resistance prevalence with fitness-neutral strain. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | Very high | target resistant fraction=0.95; importation resistant fraction=0.95; anchor rate/y=2.00; country timeline=No; $f_R$=1.00; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Upper prevalence stress-test motivated by near-fixation observations in China and high-prevalence Japanese clusters [23,24,26]; see eTables 3, 6, and 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Very high macrolide resistance prevalence with fitness-neutral strain. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | Country timeline with fitness cost | target resistant fraction=0.30; importation resistant fraction=0.30; anchor rate/y=2.00; country timeline=Yes; $f_R$=0.85; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Counterfactual fitness-cost sensitivity retained to bound traditional resistance-cost assumptions against observed MRBP expansion in China [23,24], Australia [25], Japan and the Americas [26,27], and regional reports [28,29]. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Country-timeline resistance with moderate fitness cost (15%). Retained as a sensitivity scenario representing the traditional assumption that ribosomal mutations impose a growth penalty. Recent rapid expansion makes a large persistent cost less plausible, but this scenario is included to bound the optimistic end of resistance projections. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | Country timeline with fitness advantage | target resistant fraction=0.30; importation resistant fraction=0.30; anchor rate/y=2.00; country timeline=Yes; $f_R$=1.10; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Fitness-advantage sensitivity motivated by rapid MRBP expansion and international spread in China [23,24], Australia [25], Japan and the Americas [26,27], and regional reports [28,29], without a demonstrated transmission penalty. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Country-timeline resistance with fitness advantage (10%). The MT28-ptxP3 MRBP clone has been reported with resistance and vaccine-antigen lineages in rapidly expanding outbreaks. This scenario tests whether a modest fitness advantage materially changes long-term resistance burden projections; the 10% value is a stress-test assumption, not a measured relative-fitness estimate. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | High resistance with fitness advantage | target resistant fraction=0.70; importation resistant fraction=0.70; anchor rate/y=2.00; country timeline=No; $f_R$=1.15; resistant treatment effect=0.10; resistant PEP effectiveness=0.10 | Worst-case stress test combining high starting resistance with a fitness-advantaged strain; rationale summarized in eTable 28 and resistance evidence from China [23,24], Japan [26], and regional MRBP reports [28,29]. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | High resistance prevalence with fitness advantage (15%). Worst-case scenario combining high initial resistance with a fitness-advantaged strain, representing the upper bound of resistant infection burden. Motivated by genomic reports of co-selection between resistance and vaccine-antigen lineages; retained as a stress-test assumption rather than a directly estimated fitness value. | eTables 3, 6, 13, and 28. |
| Intervention strategy scenario | Current practice | Baseline comparator; Reference scenario | Country-specific schedule and coverage inputs from WHO/UNICEF and national records [1,14], with standard treatment/PEP assumptions from CDC guidance [20]. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Current vaccination and standard macrolide treatment. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Higher child coverage | Current-program modification; Marginal coverage-change scenario | Scenario modification of country routine childhood coverage using country schedule and coverage inputs [1,14]; not a new efficacy estimate. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Increase routine childhood vaccine coverage in the existing program. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Adolescent booster | Current-program modification; Booster-program scenario | Scenario modification of booster timing/coverage using country schedule inputs and pertussis vaccine guidance [1,14]. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Add a school-age or adolescent booster. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Household/adult transmission-reduction composite proxy | Household/adult transmission-reduction composite proxy; Implementation-dependent composite scenario | Household/adult transmission-reduction composite proxy informed by maternal-program evidence for the direct antibody component [10-12] and infant-specific effectiveness estimates [36,37]; not a maternal-immunization-only effect estimate; decomposed in eTable 17. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Represent a composite transmission-reduction proxy combining direct infant antibody protection, recent reproductive-age adult boosting, and cocooning. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Direct maternal antibody only | Household/adult proxy component diagnostic; Component diagnostic, not standalone policy | Component diagnostic based on maternal-program evidence [10-12] and infant-specific effectiveness estimates [36,37], not a standalone policy estimate. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Isolate direct infant protection from transplacental antibody transfer. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Reproductive-age adult boosting only | Household/adult proxy component diagnostic; Component diagnostic, not standalone policy | Component diagnostic separating adult boosting from direct infant antibody and cocooning effects; informed by maternal-program interpretation [10-12] and infant-specific estimates [36,37]. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Isolate recent reproductive-age adult boosting that lowers infection and transmission risk in young adults. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Cocooning only | Household/adult proxy component diagnostic; Component diagnostic, not standalone policy | Component diagnostic for household/contact reduction, interpreted with maternal-program evidence [10-12] and infant-protection estimates [36,37]. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Isolate reduced mother-infant or household-to-infant transmission. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Resistance-guided treatment | Resistance-management scenario; Implementation-dependent management scenario | Resistance-aware testing, treatment, and PEP scenario translated from CDC treatment/PEP and antibiotic-resistance guidance [20,21]. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Use resistance-aware testing, alternative treatment, and restored PEP effectiveness for resistant infections. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Upper-bound vaccine | Hypothetical product-target vaccine; Product target, not available policy | Hypothetical product-target scenario interpreted through the WHO vaccine framework [1], transmission evidence [5,6], waning studies [7-9], and vaccine-pipeline mapping in eTable 27. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Represent an improved high-transmission-blocking pertussis vaccine profile. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Combined strategy | Composite stress test; Mechanistic upper-bound package, not policy package | Composite stress test combining the cited household/adult proxy, adolescent-booster, resistance-guided, and transmission-blocking assumptions; not a single externally validated package. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Combine transmission-blocking vaccine assumptions, the household/adult proxy, adolescent boosting, and resistance-guided management. | eTables 4, 15-20, 22, and 25. |
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
| Exploratory uncertainty and robustness diagnostics | Sensitivity screens and robustness diagnostics | 48-run Latin-hypercube screening; 128 selected-parameter joint scenario-ranking samples; temporal, infant-contact, maternal-duration, treatment/PEP, event-scale, and stochastic toy diagnostics. | Designed as robustness diagnostics following immunization-model reporting guidance [35], using parameter ranges documented in eTables 5, 10, 16-18, 21, 23, 25, and 28. | Diagnostics are not full posterior or decision analyses; they support scenario-ranking and structural-robustness interpretation. | Quantifies which assumptions threaten interpretation of infant-burden and scenario-ranking conclusions. | eTables 16-26. |
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

### eTable 4. Intervention strategy definitions, modified control levers, and interpretive status.

| Strategy | Scenario category | Interpretive status | Scenario definition | Modified control levers | Interpretation note |
| --- | --- | --- | --- | --- | --- |
| Current practice | Baseline comparator | Reference scenario | Current vaccination and standard macrolide treatment. | Country-specific vaccine schedule and coverage; standard macrolide treatment and PEP assumptions. | Comparator for relative reductions. |
| Higher child coverage | Current-program modification | Marginal coverage-change scenario | Increase routine childhood vaccine coverage in the existing program. | Coverage updates: 3-11 mo 0.82, 1-4 y 0.96, 5-9 y 0.94. | Tests marginal gains in high-coverage profiles; not evidence against maintaining routine childhood vaccination. |
| Adolescent booster | Current-program modification | Booster-program scenario | Add a school-age or adolescent booster. | Coverage update: 10-17 y 0.90; $VE_{inf}$ retained at 0.25. | Program-extension scenario using the current aP-like mechanism rather than a new product profile. |
| Household/adult transmission-reduction composite proxy | Household/adult transmission-reduction composite proxy | Implementation-dependent composite scenario | Represent a composite transmission-reduction proxy combining direct infant antibody protection, recent reproductive-age adult boosting, and cocooning. | Infant maternal-protection coverage: 0-2 m 0.72 and 3-11 m 0.78; 18-39 y recent-boosting proxy 0.55; maternal $VE_{sus}$ 0.55 and $VE_{sym}$ 0.92; maternal protection duration 180 d; young-adult-to-infant contact reduction 30%. | Composite proxy, not maternal immunization alone or passive antibody protection alone; eTable 17 decomposes direct antibody, adult boosting, and cocooning components. |
| Direct maternal antibody only | Household/adult proxy component diagnostic | Component diagnostic, not standalone policy | Isolate direct infant protection from transplacental antibody transfer. | Infant maternal-protection coverage: 0-2 m 0.72 and 3-11 m 0.78; maternal $VE_{sus}$ 0.55 and $VE_{sym}$ 0.92; maternal protection duration 180 d. | Excludes adult boosting and cocooning to decompose the household/adult proxy. |
| Reproductive-age adult boosting only | Household/adult proxy component diagnostic | Component diagnostic, not standalone policy | Isolate recent reproductive-age adult boosting that lowers infection and transmission risk in young adults. | Coverage update: 18-39 y recent-boosting proxy 0.55. | Excludes direct infant antibody protection and cocooning. |
| Cocooning only | Household/adult proxy component diagnostic | Component diagnostic, not standalone policy | Isolate reduced mother-infant or household-to-infant transmission. | Young-adult-to-infant contact reduction 30% for 0-2 mo and 3-11 mo targets. | Excludes direct infant antibody protection and adult boosting. |
| Resistance-guided treatment | Resistance-management scenario | Implementation-dependent management scenario | Use resistance-aware testing, alternative treatment, and restored PEP effectiveness for resistant infections. | Resistant infection updates: infectious-duration reduction 0.45 and infectiousness reduction 0.35; symptomatic treatment rate 0.07; resistant-strain PEP effectiveness 0.45. | Depends on testing reach, uptake, treatment selection, and PEP implementation; near-term sensitivity is in eTable 16. |
| Upper-bound vaccine | Hypothetical product-target vaccine | Product target, not available policy | Represent an improved high-transmission-blocking pertussis vaccine profile. | Uses Upper-bound transmission-blocking vaccine profile: $VE_{sus}$ 0.80, $VE_{sym}$ 0.90, $VE_{inf}$ 0.65, $VE_{dur}$ 0.40. | Mechanistic upper-bound profile motivated by candidate mucosal or high-transmission-blocking platforms; pipeline mapping is in eTable 27. |
| Combined strategy | Composite stress test | Mechanistic upper-bound package, not policy package | Combine transmission-blocking vaccine assumptions, the household/adult proxy, adolescent boosting, and resistance-guided management. | Uses Transmission-blocking vaccine profile; infant maternal-protection coverage 0.72/0.84; 10-17 y coverage 0.90; 18-39 y boosting proxy 0.55; maternal $VE_{sus}$ 0.55 and $VE_{sym}$ 0.92; maternal protection duration 180 d; young-adult-to-infant contact reduction 30%; resistance-guided treatment and resistant-strain PEP updates. | Stress-test scenario for combined mechanisms; not an externally validated implementation package. |

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

| Scenario | Importation | Treatment differential | PEP differential | $f_R$ | Median end resistant fraction | IQR end resistant fraction | Median infant cases per 100k | Median resistant infections per 100k | Interpretation |
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
| Comparator threshold | Pregnancy Tdap plus adult-household package | 0.00 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.40 | 10/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Resistance-guided treatment | 0.00 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.35 | 10/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Pregnancy Tdap plus adult-household package | 0.50 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.50 | 8/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Resistance-guided treatment | 0.50 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.45 | 8/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Pregnancy Tdap plus adult-household package | 1.00 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.50 | 8/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Resistance-guided treatment | 1.00 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.40 | 7/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | 25% reduction vs $VE_{inf}$ 0.20 | 0.50 | Cross-country median reduction on the $VE_{inf}$-only grid at 50% starting resistance prevalence. | 0.40 | 6/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | 50% reduction vs $VE_{inf}$ 0.20 | 0.50 | Cross-country median reduction on the $VE_{inf}$-only grid at 50% starting resistance prevalence. | 0.50 | 6/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | 75% reduction vs $VE_{inf}$ 0.20 | 0.50 | Cross-country median reduction on the $VE_{inf}$-only grid at 50% starting resistance prevalence. | Not reached | 0/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |

<div style="page-break-after: always;"></div>

### eTable 15. Intervention outcome summaries by country and strategy.

| Country | Strategy | Total infections | Reported cases | Infant cases | Resistant infections | Infant-case reduction | Infection reduction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | Adolescent booster | 23,966,520.52 | 397,164.11 | 186,347.93 | 22,458,655.95 | 0.00 | 0.00 |
| Australia | Combined strategy | 16,819,690.19 | 230,224.86 | 80,243.90 | 3,956,132.37 | 0.57 | 0.30 |
| Australia | Current practice | 23,960,486.82 | 397,054.15 | 186,312.27 | 22,453,720.74 | 0.00 | 0.00 |
| Australia | Higher child coverage | 23,969,487.00 | 400,506.62 | 194,248.51 | 22,464,802.44 | -0.04 | 0.00 |
| Australia | Reproductive-age adult boosting only | 23,752,319.16 | 389,293.33 | 183,270.62 | 22,386,250.99 | 0.02 | 0.01 |
| Australia | Cocooning only | 23,928,385.43 | 392,693.72 | 177,934.94 | 22,415,235.13 | 0.04 | 0.00 |
| Australia | Direct maternal antibody only | 23,921,315.55 | 390,398.85 | 181,234.00 | 22,410,926.09 | 0.03 | 0.00 |
| Australia | Household/adult transmission-reduction composite proxy | 23,675,597.16 | 378,358.65 | 170,242.12 | 22,296,022.63 | 0.09 | 0.01 |
| Australia | Upper-bound vaccine | 15,821,823.62 | 218,041.89 | 85,197.09 | 14,464,045.44 | 0.54 | 0.34 |
| Australia | Resistance-guided treatment | 22,500,651.17 | 355,791.31 | 154,493.05 | 9,225,083.32 | 0.17 | 0.06 |
| Brazil | Adolescent booster | 602,744.40 | 9,296.84 | 2,382.83 | 8,589.80 | 0.79 | 0.79 |
| Brazil | Combined strategy | 42,932.91 | 644.45 | 163.62 | 381.27 | 0.99 | 0.98 |
| Brazil | Current practice | 2,857,035.12 | 45,073.32 | 11,159.72 | 128,561.16 | 0.00 | 0.00 |
| Brazil | Higher child coverage | 3,325,917.37 | 52,941.15 | 13,283.18 | 183,034.58 | -0.19 | -0.16 |
| Brazil | Reproductive-age adult boosting only | 453,363.74 | 7,039.61 | 1,781.79 | 5,934.54 | 0.84 | 0.84 |
| Brazil | Cocooning only | 2,663,557.14 | 41,675.55 | 9,784.04 | 109,398.53 | 0.12 | 0.07 |
| Brazil | Direct maternal antibody only | 2,842,792.77 | 44,347.15 | 10,658.45 | 126,560.25 | 0.04 | 0.00 |
| Brazil | Household/adult transmission-reduction composite proxy | 434,650.88 | 6,624.98 | 1,550.93 | 5,616.25 | 0.86 | 0.85 |
| Brazil | Upper-bound vaccine | 47,709.79 | 714.95 | 191.94 | 494.46 | 0.98 | 0.98 |
| Brazil | Resistance-guided treatment | 1,210,079.53 | 19,025.82 | 4,683.11 | 4,247.47 | 0.58 | 0.58 |
| China | Adolescent booster | 125,333,078.73 | 5,112,085.33 | 440,662.32 | 125,292,573.44 | 0.23 | 0.25 |
| China | Combined strategy | 541,572.33 | 20,907.41 | 1,534.52 | 539,655.26 | 1.00 | 1.00 |
| China | Current practice | 167,252,430.53 | 6,968,485.05 | 569,957.79 | 167,206,617.14 | 0.00 | 0.00 |
| China | Higher child coverage | 169,414,032.05 | 7,091,319.59 | 591,163.53 | 169,368,342.46 | -0.04 | -0.01 |
| China | Reproductive-age adult boosting only | 96,534,368.32 | 3,909,680.09 | 329,167.31 | 96,493,658.93 | 0.42 | 0.42 |
| China | Cocooning only | 165,002,764.81 | 6,844,512.53 | 531,592.76 | 164,956,882.20 | 0.07 | 0.01 |
| China | Direct maternal antibody only | 165,714,985.43 | 6,832,176.58 | 517,132.48 | 165,668,810.07 | 0.09 | 0.01 |
| China | Household/adult transmission-reduction composite proxy | 94,088,007.58 | 3,755,399.24 | 278,730.04 | 94,046,982.16 | 0.51 | 0.44 |
| China | Upper-bound vaccine | 1,058,436.85 | 41,111.78 | 3,262.59 | 1,055,469.54 | 0.99 | 0.99 |
| China | Resistance-guided treatment | 88,167,875.60 | 3,653,708.96 | 289,133.47 | 66,058,859.81 | 0.49 | 0.47 |
| Japan | Adolescent booster | 26,399,997.31 | 409,534.26 | 79,542.58 | 26,073,172.85 | 0.04 | 0.04 |
| Japan | Combined strategy | 247,708.07 | 3,421.33 | 519.53 | 175,260.10 | 0.99 | 0.99 |
| Japan | Current practice | 27,536,156.22 | 432,979.22 | 82,781.93 | 27,192,103.53 | 0.00 | 0.00 |
| Japan | Higher child coverage | 27,628,577.24 | 436,428.68 | 84,440.80 | 27,284,666.98 | -0.02 | 0.00 |
| Japan | Reproductive-age adult boosting only | 20,696,340.23 | 313,174.10 | 60,339.58 | 20,381,993.00 | 0.27 | 0.25 |
| Japan | Cocooning only | 27,463,589.83 | 428,555.73 | 77,752.79 | 27,118,246.91 | 0.06 | 0.00 |
| Japan | Direct maternal antibody only | 27,518,667.93 | 425,353.22 | 75,148.10 | 27,171,172.35 | 0.09 | 0.00 |
| Japan | Household/adult transmission-reduction composite proxy | 20,586,367.98 | 304,114.26 | 51,503.98 | 20,267,630.36 | 0.38 | 0.25 |
| Japan | Upper-bound vaccine | 6,518,698.92 | 94,532.03 | 16,498.52 | 6,305,541.58 | 0.80 | 0.76 |
| Japan | Resistance-guided treatment | 19,934,391.77 | 309,054.42 | 56,462.66 | 10,455,747.99 | 0.32 | 0.28 |
| New Zealand | Adolescent booster | 3,334,592.80 | 51,174.24 | 21,601.17 | 2,965,841.27 | 0.00 | 0.00 |
| New Zealand | Combined strategy | 1,713,367.27 | 22,245.34 | 7,212.92 | 10,597.50 | 0.67 | 0.49 |
| New Zealand | Current practice | 3,327,226.30 | 51,035.99 | 21,540.81 | 2,957,053.86 | 0.00 | 0.00 |
| New Zealand | Higher child coverage | 3,343,222.65 | 51,731.26 | 22,261.50 | 2,975,962.44 | -0.03 | 0.00 |
| New Zealand | Reproductive-age adult boosting only | 3,201,603.32 | 48,192.38 | 20,352.94 | 2,836,850.23 | 0.06 | 0.04 |
| New Zealand | Cocooning only | 3,320,009.10 | 50,484.90 | 20,550.28 | 2,948,114.44 | 0.05 | 0.00 |
| New Zealand | Direct maternal antibody only | 3,314,904.59 | 49,906.36 | 20,441.69 | 2,941,449.87 | 0.05 | 0.00 |
| New Zealand | Household/adult transmission-reduction composite proxy | 3,182,266.59 | 46,631.10 | 18,456.00 | 2,812,645.41 | 0.14 | 0.04 |
| New Zealand | Upper-bound vaccine | 1,588,469.19 | 20,199.63 | 7,460.05 | 1,268,590.81 | 0.65 | 0.52 |
| New Zealand | Resistance-guided treatment | 2,882,500.81 | 42,854.95 | 17,072.85 | 66,174.25 | 0.21 | 0.13 |
| South Africa | Adolescent booster | 304,955.70 | 4,608.94 | 1,737.07 | 11,965.43 | 0.87 | 0.87 |
| South Africa | Combined strategy | 12,223.56 | 172.61 | 56.79 | 216.21 | 1.00 | 0.99 |
| South Africa | Current practice | 2,361,482.23 | 36,341.05 | 13,237.19 | 844,077.97 | 0.00 | 0.00 |
| South Africa | Higher child coverage | 1,313,792.31 | 19,283.91 | 6,802.93 | 215,178.87 | 0.49 | 0.44 |
| South Africa | Reproductive-age adult boosting only | 683,009.62 | 10,458.82 | 3,825.72 | 57,452.58 | 0.71 | 0.71 |
| South Africa | Cocooning only | 2,214,782.46 | 33,793.88 | 11,734.15 | 731,192.82 | 0.11 | 0.06 |
| South Africa | Direct maternal antibody only | 1,689,769.91 | 24,912.21 | 7,897.80 | 389,794.32 | 0.40 | 0.28 |
| South Africa | Household/adult transmission-reduction composite proxy | 399,182.06 | 5,806.76 | 1,767.59 | 19,276.67 | 0.87 | 0.83 |
| South Africa | Upper-bound vaccine | 12,739.68 | 196.51 | 80.65 | 264.63 | 0.99 | 0.99 |
| South Africa | Resistance-guided treatment | 1,033,313.78 | 15,928.86 | 5,765.30 | 4,075.04 | 0.56 | 0.56 |
| Sweden | Adolescent booster | 2,458,581.93 | 35,587.59 | 10,274.65 | 1,905,994.92 | 0.00 | 0.00 |
| Sweden | Combined strategy | 11,458.08 | 148.62 | 36.75 | 80.59 | 1.00 | 1.00 |
| Sweden | Current practice | 2,457,347.47 | 35,566.76 | 10,269.61 | 1,904,827.80 | 0.00 | 0.00 |
| Sweden | Higher child coverage | 2,452,570.65 | 35,670.55 | 10,741.03 | 1,901,571.38 | -0.05 | 0.00 |
| Sweden | Reproductive-age adult boosting only | 2,066,576.85 | 29,410.73 | 8,536.19 | 1,532,946.67 | 0.17 | 0.16 |
| Sweden | Cocooning only | 2,436,397.21 | 34,979.05 | 9,651.63 | 1,882,020.76 | 0.06 | 0.01 |
| Sweden | Direct maternal antibody only | 2,405,170.24 | 34,260.83 | 9,780.06 | 1,848,623.04 | 0.05 | 0.02 |
| Sweden | Household/adult transmission-reduction composite proxy | 2,005,662.23 | 27,869.83 | 7,654.42 | 1,466,275.57 | 0.25 | 0.18 |
| Sweden | Upper-bound vaccine | 4,890.67 | 63.17 | 17.94 | 51.74 | 1.00 | 1.00 |
| Sweden | Resistance-guided treatment | 1,867,827.57 | 26,633.48 | 7,389.05 | 4,134.35 | 0.28 | 0.24 |
| Thailand | Adolescent booster | 182,096.28 | 2,587.69 | 599.04 | 2,363.67 | 0.70 | 0.71 |
| Thailand | Combined strategy | 16,855.01 | 229.81 | 48.73 | 149.92 | 0.98 | 0.97 |
| Thailand | Current practice | 625,450.99 | 9,062.47 | 2,021.24 | 15,328.16 | 0.00 | 0.00 |
| Thailand | Higher child coverage | 685,943.78 | 9,996.39 | 2,196.99 | 18,360.60 | -0.09 | -0.10 |
| Thailand | Reproductive-age adult boosting only | 126,845.03 | 1,807.68 | 417.02 | 1,522.16 | 0.79 | 0.80 |
| Thailand | Cocooning only | 591,098.57 | 8,502.00 | 1,800.26 | 13,773.05 | 0.11 | 0.05 |
| Thailand | Direct maternal antibody only | 598,599.04 | 8,522.30 | 1,720.61 | 14,068.36 | 0.15 | 0.04 |
| Thailand | Household/adult transmission-reduction composite proxy | 121,082.24 | 1,684.39 | 335.57 | 1,439.42 | 0.83 | 0.81 |
| Thailand | Upper-bound vaccine | 21,247.19 | 293.52 | 71.03 | 220.87 | 0.96 | 0.97 |
| Thailand | Resistance-guided treatment | 302,678.37 | 4,378.97 | 974.15 | 1,332.42 | 0.52 | 0.52 |
| United Kingdom | Adolescent booster | 35,175,229.60 | 489,997.76 | 223,760.52 | 30,048,901.77 | -0.01 | -0.01 |
| United Kingdom | Combined strategy | 11,306,692.47 | 130,676.98 | 45,485.54 | 7,606.31 | 0.80 | 0.68 |
| United Kingdom | Current practice | 34,942,169.45 | 486,413.80 | 222,136.10 | 29,651,102.24 | 0.00 | 0.00 |
| United Kingdom | Higher child coverage | 35,350,285.20 | 496,880.91 | 231,279.64 | 30,100,290.27 | -0.04 | -0.01 |
| United Kingdom | Reproductive-age adult boosting only | 31,197,677.72 | 420,247.33 | 191,569.66 | 26,014,468.60 | 0.14 | 0.11 |
| United Kingdom | Cocooning only | 34,780,242.49 | 479,260.24 | 209,399.82 | 29,459,945.61 | 0.06 | 0.00 |
| United Kingdom | Direct maternal antibody only | 34,711,709.46 | 474,328.16 | 209,825.96 | 29,354,770.40 | 0.06 | 0.01 |
| United Kingdom | Household/adult transmission-reduction composite proxy | 31,000,822.62 | 406,275.49 | 171,971.22 | 25,731,085.90 | 0.23 | 0.11 |
| United Kingdom | Upper-bound vaccine | 16,464,931.51 | 195,407.74 | 76,400.90 | 11,599,813.56 | 0.66 | 0.53 |
| United Kingdom | Resistance-guided treatment | 29,633,755.75 | 402,358.81 | 173,155.67 | 63,958.26 | 0.22 | 0.15 |
| United States | Adolescent booster | 7,661,498.97 | 121,586.88 | 30,005.20 | 0 | -0.03 | -0.03 |
| United States | Combined strategy | 82,443.12 | 1,270.25 | 311.49 | 0 | 0.99 | 0.99 |
| United States | Current practice | 7,418,543.46 | 117,714.81 | 29,055.37 | 0 | 0.00 | 0.00 |
| United States | Higher child coverage | 7,408,708.69 | 118,230.40 | 30,437.15 | 0 | -0.05 | 0.00 |
| United States | Reproductive-age adult boosting only | 2,427,767.61 | 38,088.61 | 9,481.58 | 0 | 0.67 | 0.67 |
| United States | Cocooning only | 7,088,890.21 | 111,562.31 | 26,177.44 | 0 | 0.10 | 0.04 |
| United States | Direct maternal antibody only | 6,756,544.33 | 105,618.01 | 25,791.32 | 0 | 0.11 | 0.09 |
| United States | Household/adult transmission-reduction composite proxy | 2,173,243.74 | 33,360.20 | 7,819.61 | 0 | 0.73 | 0.71 |
| United States | Upper-bound vaccine | 56,444.49 | 868.80 | 243.84 | 0 | 0.99 | 0.99 |
| United States | Resistance-guided treatment | 3,646,164.58 | 57,613.23 | 14,132.36 | 0 | 0.51 | 0.51 |

<div style="page-break-after: always;"></div>

### eTable 16. Near-term implementation sensitivity for resistance-guided treatment and resistant-strain PEP assumptions.

| Scenario | Guided-treatment uptake | PEP restored | PEP reach multiplier | Median infant-case reduction vs current, 5 y | IQR reduction | Countries with positive reduction | Median infant cases per 100k | Implementation note |
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

| Sensitivity dimension | Strategy | Setting | Median infant cases per 100k, 5 y | IQR infant cases per 100k, 5 y | Median infant-case reduction vs current, 5 y | IQR reduction | Countries with positive reduction | Countries | Interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Infant contact multiplier | Current practice | 0.75 | 145.76 | 31.54-453.90 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Current practice | 1.00 | 170.55 | 38.93-525.80 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Current practice | 1.25 | 198.33 | 47.55-589.00 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Current practice | 1.50 | 228.29 | 57.08-642.80 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Household/adult transmission-reduction composite proxy | 0.75 | 93.37 | 6.95-311.50 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Household/adult transmission-reduction composite proxy | 1.00 | 108.18 | 8.93-354.80 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Household/adult transmission-reduction composite proxy | 1.25 | 121.51 | 11.54-397.10 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Household/adult transmission-reduction composite proxy | 1.50 | 138.47 | 14.86-442.40 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Maternal passive-protection duration | Current practice | 90.00 | 141.57 | 37.86-444.70 | 0.00 | 0.00-0.00 | 0 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Direct maternal antibody only | 90.00 | 138.54 | 34.17-434.90 | 0.03 | 0.01-0.06 | 8 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Household/adult transmission-reduction composite proxy | 90.00 | 64.77 | 8.73-339.50 | 0.55 | 0.22-0.81 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Current practice | 180.00 | 140.65 | 37.49-440.30 | 0.00 | 0.00-0.00 | 0 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Direct maternal antibody only | 180.00 | 134.82 | 33.02-424.30 | 0.04 | 0.02-0.09 | 9 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Household/adult transmission-reduction composite proxy | 180.00 | 63.45 | 8.38-331.50 | 0.56 | 0.23-0.81 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Current practice | 270.00 | 140.14 | 37.36-438.40 | 0.00 | 0.00-0.00 | 0 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Direct maternal antibody only | 270.00 | 133.68 | 32.55-419.80 | 0.04 | 0.03-0.10 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Household/adult transmission-reduction composite proxy | 270.00 | 62.39 | 8.24-327.80 | 0.57 | 0.23-0.82 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |

<div style="page-break-after: always;"></div>

### eTable 18. Higher child-coverage mechanism diagnostics.

| Diagnostic | Country, age group, or scenario | Current infant cases per 100k | Higher child coverage infant cases per 100k | Relative change or share | Largest increase age group | Age-shift IQR | Countries | Interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Country infant-burden change | Australia | 2,574.20 | 2,679.06 | -0.04 | 1-4 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | Brazil | 21.13 | 24.92 | -0.18 | 18-39 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | China | 293.87 | 302.70 | -0.03 | 40-64 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | Japan | 450.16 | 458.70 | -0.02 | 40-64 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | New Zealand | 1,532.79 | 1,581.91 | -0.03 | 18-39 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | South Africa | 47.80 | 24.54 | 0.49 | 0-2 mo |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | Sweden | 421.19 | 439.26 | -0.04 | 3-11 mo |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | Thailand | 17.11 | 18.45 | -0.08 | 40-64 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | United Kingdom | 1,272.16 | 1,325.01 | -0.04 | 18-39 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | United States | 31.34 | 32.88 | -0.05 | 18-39 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Age-shift summary | Adolescent 10 17y |  |  | 0.00 |  | 0.00 to 0.01 | 7 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 1-4 y |  |  | 0.01 |  | 0.00 to 0.02 | 8 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 5-9 y |  |  | 0.01 |  | 0.00 to 0.02 | 7 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 65+ y |  |  | 0.00 |  | 0.00 to 0.01 | 7 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 0-2 mo |  |  | 0.01 |  | 0.00 to 0.02 | 8 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 3-11 mo |  |  | 0.01 |  | 0.01 to 0.02 | 9 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 40-64 y |  |  | 0.00 |  | 0.00 to 0.01 | 7 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 18-39 y |  |  | 0.00 |  | 0.00 to 0.01 | 8 | Median age-specific infection change under higher child coverage. |
| Vaccine-history origin share | Current practice |  |  | 0.46 |  |  | 10 | Median vaccinated-origin infant infection share; source CSV retains dose-specific shares. |
| Vaccine-history origin share | Higher child coverage |  |  | 0.43 |  |  | 10 | Median vaccinated-origin infant infection share; source CSV retains dose-specific shares. |

<div style="page-break-after: always;"></div>

### eTable 19. Intervention scenario-ordering sensitivity to analysis-window choice.

| Analysis window | Scenario | Median order position | Countries ordered first | Median infant-case reduction |
| --- | --- | --- | --- | --- |
| 2025-2029 | Combined strategy | 1.00 | 6 | 0.99 |
| 2025-2029 | Upper-bound vaccine | 2.00 | 3 | 0.98 |
| 2025-2029 | Household/adult transmission-reduction composite proxy | 3.00 | 0 | 0.58 |
| 2025-2029 | Adolescent booster | 4.00 | 1 | 0.22 |
| 2025-2029 | Resistance-guided treatment | 5.00 | 0 | 0.16 |
| 2025-2029 | Current practice | 6.00 | 0 | 0.00 |
| 2025-2029 | Higher child coverage | 6.00 | 0 | -0.04 |
| 2025-2034 | Combined strategy | 1.00 | 8 | 0.99 |
| 2025-2034 | Upper-bound vaccine | 2.00 | 2 | 0.98 |
| 2025-2034 | Household/adult transmission-reduction composite proxy | 3.50 | 0 | 0.49 |
| 2025-2034 | Resistance-guided treatment | 4.00 | 0 | 0.44 |
| 2025-2034 | Adolescent booster | 5.00 | 0 | 0.04 |
| 2025-2034 | Current practice | 6.00 | 0 | 0.00 |
| 2025-2034 | Higher child coverage | 7.00 | 0 | -0.04 |
| 2025-2039 | Combined strategy | 1.00 | 8 | 0.99 |
| 2025-2039 | Upper-bound vaccine | 2.00 | 2 | 0.98 |
| 2025-2039 | Household/adult transmission-reduction composite proxy | 3.50 | 0 | 0.41 |
| 2025-2039 | Resistance-guided treatment | 4.00 | 0 | 0.39 |
| 2025-2039 | Adolescent booster | 5.00 | 0 | 0.01 |
| 2025-2039 | Current practice | 6.00 | 0 | 0.00 |
| 2025-2039 | Higher child coverage | 7.00 | 0 | -0.04 |
| 2025-2050 full horizon | Combined strategy | 1.00 | 8 | 0.99 |
| 2025-2050 full horizon | Upper-bound vaccine | 2.00 | 2 | 0.98 |
| 2025-2050 full horizon | Household/adult transmission-reduction composite proxy | 3.50 | 0 | 0.43 |
| 2025-2050 full horizon | Resistance-guided treatment | 4.00 | 0 | 0.41 |
| 2025-2050 full horizon | Adolescent booster | 5.00 | 0 | 0.02 |
| 2025-2050 full horizon | Current practice | 6.00 | 0 | 0.00 |
| 2025-2050 full horizon | Higher child coverage | 7.00 | 0 | -0.04 |
| 2030-2050 excluding initial transient | Combined strategy | 1.00 | 8 | 0.99 |
| 2030-2050 excluding initial transient | Upper-bound vaccine | 2.00 | 2 | 0.97 |
| 2030-2050 excluding initial transient | Resistance-guided treatment | 3.00 | 0 | 0.43 |
| 2030-2050 excluding initial transient | Household/adult transmission-reduction composite proxy | 4.00 | 0 | 0.38 |
| 2030-2050 excluding initial transient | Adolescent booster | 5.50 | 0 | 0.00 |
| 2030-2050 excluding initial transient | Current practice | 5.50 | 0 | 0.00 |
| 2030-2050 excluding initial transient | Higher child coverage | 7.00 | 0 | -0.04 |

<div style="page-break-after: always;"></div>

### eTable 20. Cross-diagnostic intervention scenario-ordering stability across countries, analysis windows, and infant age strata.

| Scenario | Full-horizon median order position | Countries ordered first | Countries ordered top 2 | Window cells ordered first | Window cells ordered top 2 | Age-window cells ordered first | Age-window cells ordered top 2 | Age-window cells with reduction | Median age-window reduction | Interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combined strategy | 1.00 | 8 | 10 | 38 | 48 | 78 | 97 | 98 | 0.99 | Most stable lowest-burden scenario across country, horizon, and infant-age diagnostics. |
| Upper-bound vaccine | 2.00 | 2 | 10 | 11 | 49 | 19 | 95 | 98 | 0.98 | Often near the lowest modeled burden, but not consistently ordered first. |
| Household/adult transmission-reduction composite proxy | 3.50 | 0 | 0 | 0 | 1 | 1 | 4 | 94 | 0.53 | Usually lower burden than current practice, but ordering is horizon- and age-stratum-dependent. |
| Adolescent booster | 5.00 | 0 | 0 | 1 | 1 | 1 | 2 | 70 | 0.03 | Usually lower burden than current practice, but ordering is horizon- and age-stratum-dependent. |
| Higher child coverage | 7.00 | 0 | 0 | 0 | 0 | 1 | 1 | 20 | -0.04 | Low-benefit or unstable scenario in these deterministic diagnostics. |
| Current practice | 6.00 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0.00 | Low-benefit or unstable scenario in these deterministic diagnostics. |
| Resistance-guided treatment | 4.00 | 0 | 0 | 0 | 0 | 0 | 0 | 92 | 0.39 | Usually lower burden than current practice, but ordering is horizon- and age-stratum-dependent. |

<div style="page-break-after: always;"></div>

### eTable 21. Near-term temporal assumption sensitivity for burn-in duration and COVID-19 NPI contact-shock assumptions.

| Temporal dimension | Scenario | Countries | Burn-in years | NPI reduction scale | Median infant cases per 100k, 5 y | IQR infant cases per 100k, 5 y | Median all infections per 100k, 5 y | Median end resistant fraction, 5 y | Implementation note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Burn-in | Burnin 10y | 10 | 10.00 | 1.00 | 52.11 | 33.67-983.20 | 135.77 | 0.39 | Near-term current-practice run varying pre-analysis burn-in duration. |
| Burn-in | Burnin 15y | 10 | 15.00 | 1.00 | 170.55 | 38.93-525.80 | 354.02 | 0.10 | Near-term current-practice run varying pre-analysis burn-in duration. |
| Burn-in | Burnin 30y | 10 | 30.00 | 1.00 | 336.36 | 33.89-737.30 | 659.21 | 0.16 | Near-term current-practice run varying pre-analysis burn-in duration. |
| NPI contact shock | NPI country profile | 1 | 15.00 | 1.00 | 547.24 | 547.20-547.20 | 680.06 | 0.44 | Near-term current-practice run varying COVID-19 NPI contact-reduction assumptions for countries with explicit NPI periods. |
| NPI contact shock | Half NPI contact shock | 1 | 15.00 | 0.50 | 228.62 | 228.60-228.60 | 297.34 | 0.19 | Near-term current-practice run varying COVID-19 NPI contact-reduction assumptions for countries with explicit NPI periods. |
| NPI contact shock | No NPI contact shock | 1 | 15.00 |  | 2,996.53 | 2997.00-2997.00 | 3,855.37 | 0.99 | Near-term current-practice run varying COVID-19 NPI contact-reduction assumptions for countries with explicit NPI periods. |

<div style="page-break-after: always;"></div>

### eTable 22. Infant age-stratified intervention outcomes summarized by analysis window.

| Analysis window | Infant age stratum | Scenario | Median infant cases per 100k/y | IQR infant cases per 100k/y | Median infant-case reduction | Median order position | Countries with positive reduction | Countries |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-2029 | 0-2 mo | Adolescent booster | 216.76 | 19.86-710.47 | 0.22 | 4.00 | 8 | 10 |
| 2025-2029 | 0-2 mo | Combined strategy | 1.22 | 0.39-228.24 | 0.99 | 1.00 | 9 | 10 |
| 2025-2029 | 0-2 mo | Current practice | 251.75 | 55.89-778.79 | 0.00 | 6.00 | 0 | 10 |
| 2025-2029 | 0-2 mo | Higher child coverage | 243.44 | 46.04-794.16 | -0.04 | 6.00 | 4 | 10 |
| 2025-2029 | 0-2 mo | Household/adult transmission-reduction composite proxy | 116.94 | 9.75-387.59 | 0.69 | 3.00 | 9 | 10 |
| 2025-2029 | 0-2 mo | Upper-bound vaccine | 1.86 | 0.58-394.23 | 0.98 | 2.00 | 9 | 10 |
| 2025-2029 | 0-2 mo | Resistance-guided treatment | 300.27 | 28.15-1277.41 | 0.16 | 5.00 | 6 | 10 |
| 2025-2029 | 3-11 mo | Adolescent booster | 131.36 | 12.44-420.80 | 0.22 | 4.00 | 8 | 10 |
| 2025-2029 | 3-11 mo | Combined strategy | 1.06 | 0.34-197.02 | 0.99 | 1.00 | 9 | 10 |
| 2025-2029 | 3-11 mo | Current practice | 151.05 | 34.92-460.92 | 0.00 | 6.00 | 0 | 10 |
| 2025-2029 | 3-11 mo | Higher child coverage | 153.54 | 29.73-484.36 | -0.05 | 6.00 | 2 | 10 |
| 2025-2029 | 3-11 mo | Household/adult transmission-reduction composite proxy | 104.51 | 8.74-344.25 | 0.53 | 3.00 | 9 | 10 |
| 2025-2029 | 3-11 mo | Upper-bound vaccine | 0.95 | 0.34-225.86 | 0.98 | 2.00 | 9 | 10 |
| 2025-2029 | 3-11 mo | Resistance-guided treatment | 181.55 | 17.60-792.07 | 0.16 | 5.00 | 6 | 10 |
| 2025-2034 | 0-2 mo | Adolescent booster | 338.57 | 18.99-1673.59 | 0.04 | 5.00 | 8 | 10 |
| 2025-2034 | 0-2 mo | Combined strategy | 1.24 | 0.39-231.34 | 0.99 | 1.00 | 10 | 10 |
| 2025-2034 | 0-2 mo | Current practice | 511.04 | 50.61-1634.66 | 0.00 | 6.00 | 0 | 10 |
| 2025-2034 | 0-2 mo | Higher child coverage | 510.72 | 41.79-1674.02 | -0.01 | 7.00 | 3 | 10 |
| 2025-2034 | 0-2 mo | Household/adult transmission-reduction composite proxy | 185.76 | 8.93-945.75 | 0.64 | 3.00 | 10 | 10 |
| 2025-2034 | 0-2 mo | Upper-bound vaccine | 1.88 | 0.59-426.52 | 0.98 | 2.00 | 10 | 10 |
| 2025-2034 | 0-2 mo | Resistance-guided treatment | 313.02 | 26.23-1216.01 | 0.44 | 4.00 | 10 | 10 |
| 2025-2034 | 3-11 mo | Adolescent booster | 203.80 | 11.89-1021.35 | 0.04 | 5.00 | 8 | 10 |
| 2025-2034 | 3-11 mo | Combined strategy | 1.07 | 0.34-199.71 | 0.99 | 1.00 | 10 | 10 |
| 2025-2034 | 3-11 mo | Current practice | 299.73 | 31.62-997.65 | 0.00 | 6.00 | 0 | 10 |
| 2025-2034 | 3-11 mo | Higher child coverage | 312.64 | 27.54-1053.36 | -0.06 | 7.00 | 1 | 10 |
| 2025-2034 | 3-11 mo | Household/adult transmission-reduction composite proxy | 165.79 | 8.01-827.27 | 0.43 | 4.00 | 9 | 10 |
| 2025-2034 | 3-11 mo | Upper-bound vaccine | 0.96 | 0.34-243.92 | 0.98 | 2.00 | 10 | 10 |
| 2025-2034 | 3-11 mo | Resistance-guided treatment | 189.16 | 16.40-755.85 | 0.44 | 3.50 | 10 | 10 |
| 2025-2039 | 0-2 mo | Adolescent booster | 477.00 | 18.62-1410.22 | 0.01 | 5.00 | 7 | 10 |
| 2025-2039 | 0-2 mo | Combined strategy | 1.26 | 0.39-228.26 | 0.99 | 1.00 | 10 | 10 |
| 2025-2039 | 0-2 mo | Current practice | 575.77 | 48.77-1396.48 | 0.00 | 6.00 | 0 | 10 |
| 2025-2039 | 0-2 mo | Higher child coverage | 578.45 | 39.75-1421.38 | -0.02 | 7.00 | 2 | 10 |
| 2025-2039 | 0-2 mo | Household/adult transmission-reduction composite proxy | 250.02 | 8.48-844.31 | 0.59 | 3.00 | 10 | 10 |
| 2025-2039 | 0-2 mo | Upper-bound vaccine | 1.93 | 0.60-578.40 | 0.98 | 2.00 | 10 | 10 |
| 2025-2039 | 0-2 mo | Resistance-guided treatment | 316.40 | 25.07-1202.80 | 0.39 | 4.00 | 10 | 10 |
| 2025-2039 | 3-11 mo | Adolescent booster | 273.74 | 11.66-871.35 | 0.01 | 5.00 | 7 | 10 |
| 2025-2039 | 3-11 mo | Combined strategy | 1.09 | 0.34-197.11 | 0.99 | 1.00 | 10 | 10 |
| 2025-2039 | 3-11 mo | Current practice | 331.74 | 30.47-862.03 | 0.00 | 6.00 | 0 | 10 |
| 2025-2039 | 3-11 mo | Higher child coverage | 342.03 | 26.01-908.50 | -0.05 | 7.00 | 1 | 10 |
| 2025-2039 | 3-11 mo | Household/adult transmission-reduction composite proxy | 222.26 | 7.60-739.68 | 0.34 | 4.00 | 9 | 10 |
| 2025-2039 | 3-11 mo | Upper-bound vaccine | 0.99 | 0.35-329.04 | 0.98 | 2.00 | 10 | 10 |
| 2025-2039 | 3-11 mo | Resistance-guided treatment | 191.09 | 15.67-748.59 | 0.39 | 3.50 | 10 | 10 |
| 2025-2050 full horizon | 0-2 mo | Adolescent booster | 476.70 | 18.33-1562.19 | 0.02 | 5.00 | 7 | 10 |
| 2025-2050 full horizon | 0-2 mo | Combined strategy | 1.29 | 0.39-224.55 | 0.99 | 1.00 | 10 | 10 |
| 2025-2050 full horizon | 0-2 mo | Current practice | 533.56 | 51.01-1553.11 | 0.00 | 6.00 | 0 | 10 |
| 2025-2050 full horizon | 0-2 mo | Higher child coverage | 535.23 | 39.44-1578.04 | -0.01 | 7.00 | 2 | 10 |
| 2025-2050 full horizon | 0-2 mo | Household/adult transmission-reduction composite proxy | 239.15 | 8.03-926.98 | 0.60 | 3.00 | 10 | 10 |
| 2025-2050 full horizon | 0-2 mo | Upper-bound vaccine | 2.02 | 0.62-558.68 | 0.97 | 2.00 | 10 | 10 |
| 2025-2050 full horizon | 0-2 mo | Resistance-guided treatment | 328.91 | 24.21-1195.71 | 0.41 | 4.00 | 10 | 10 |
| 2025-2050 full horizon | 3-11 mo | Adolescent booster | 285.64 | 11.47-960.65 | 0.02 | 5.00 | 7 | 10 |
| 2025-2050 full horizon | 3-11 mo | Combined strategy | 1.12 | 0.34-193.90 | 0.99 | 1.00 | 10 | 10 |
| 2025-2050 full horizon | 3-11 mo | Current practice | 317.27 | 31.89-955.28 | 0.00 | 6.00 | 0 | 10 |
| 2025-2050 full horizon | 3-11 mo | Higher child coverage | 333.42 | 24.74-1000.90 | -0.05 | 7.00 | 1 | 10 |
| 2025-2050 full horizon | 3-11 mo | Household/adult transmission-reduction composite proxy | 212.80 | 7.20-812.66 | 0.36 | 4.00 | 9 | 10 |
| 2025-2050 full horizon | 3-11 mo | Upper-bound vaccine | 1.03 | 0.36-317.72 | 0.98 | 2.00 | 10 | 10 |
| 2025-2050 full horizon | 3-11 mo | Resistance-guided treatment | 198.17 | 15.13-744.42 | 0.41 | 3.00 | 10 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Adolescent booster | 537.01 | 17.96-1754.89 | 0.00 | 5.50 | 5 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Combined strategy | 1.31 | 0.40-223.74 | 0.99 | 1.00 | 10 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Current practice | 596.70 | 49.91-1735.95 | 0.00 | 6.00 | 0 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Higher child coverage | 601.07 | 37.89-1752.63 | 0.00 | 7.00 | 3 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Household/adult transmission-reduction composite proxy | 267.88 | 7.62-1048.77 | 0.56 | 3.00 | 10 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Upper-bound vaccine | 2.06 | 0.63-596.03 | 0.97 | 2.00 | 10 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Resistance-guided treatment | 335.77 | 23.30-1177.25 | 0.43 | 4.00 | 10 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Adolescent booster | 312.58 | 11.24-1082.77 | 0.00 | 5.00 | 5 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Combined strategy | 1.14 | 0.34-193.21 | 0.99 | 1.00 | 10 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Current practice | 334.60 | 31.21-1077.98 | 0.00 | 5.50 | 0 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Higher child coverage | 345.10 | 23.48-1126.47 | -0.04 | 7.00 | 1 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Household/adult transmission-reduction composite proxy | 238.27 | 6.83-918.65 | 0.31 | 4.00 | 9 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Upper-bound vaccine | 1.05 | 0.37-338.60 | 0.97 | 2.00 | 10 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Resistance-guided treatment | 193.81 | 14.56-737.82 | 0.43 | 3.00 | 10 | 10 |

<div style="page-break-after: always;"></div>

### eTable 23. Deterministic event-scale diagnostics for stochastic-interpretation sensitivity.

| Scenario | Countries | Median annual infant cases | Minimum annual infant cases | Median infant cases per 100k/y | Low-event countries | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Adolescent booster | 10 | 1,008.97 | 25.55 | 321.21 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Combined strategy | 10 | 17.17 | 1.49 | 1.15 | Sweden; South Africa; Thailand; Brazil; United States; Japan | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Current practice | 10 | 995.63 | 86.07 | 357.53 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Higher child coverage | 10 | 1,037.54 | 92.76 | 370.98 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Household/adult transmission-reduction composite proxy | 10 | 525.21 | 13.79 | 217.70 | Thailand | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Upper-bound vaccine | 10 | 72.95 | 0.72 | 1.21 | Sweden; South Africa; Thailand; Brazil; United States | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Resistance-guided treatment | 10 | 621.01 | 40.52 | 222.51 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |

<div style="page-break-after: always;"></div>

### eTable 24. Limitation-to-diagnostic map and residual interpretation.

| Limitation domain | Added or existing diagnostic | Supplement location | Residual interpretation |
| --- | --- | --- | --- |
| Infant outcomes without direct age-specific calibration | Overall calibration fit, fitted reporting gradients, infant contact sensitivity, age-shift diagnostics, and 0-2 month/3-11 month intervention-window summaries. | eTables 7, 12, 17, 18, and 22 | Infant estimates are conditional model outputs, not externally validated infant forecasts. |
| Intervention scenario ordering under joint parameter uncertainty | Analysis-window order positions, cross-diagnostic scenario-ranking summary, infant-age/window summaries, Figure 4B source data retained as repository CSV, and selected-parameter joint PSA scenario-ranking diagnostics. | eTables 19, 20, 22, and 25 | Order-position probabilities are conditional on the epidemiologic PSA ranges and do not include household/adult proxy implementation heterogeneity, costs, feasibility, or equity weights. |
| Deterministic dynamics without stochastic extinction or superspreading | Event-scale diagnostics identify low-event cells where deterministic persistence assumptions matter most; a small individual stochastic toy model illustrates contact-clustering sensitivity. | eTables 23 and 26 | Near-zero burdens and low-event cells should be read as deterministic thresholds, not stochastic elimination probabilities. |
| No explicit household clustering, contact tracing, or adherence model | Intervention outcome summaries, resistance-guided treatment implementation sensitivity, infant-contact and maternal-duration sensitivity, and individual stochastic contact-clustering illustration. | eTables 15, 16, 17, and 26 | Age-structured proxy diagnostics do not replace household or contact-tracing simulations. |
| Macrolide-resistant strain dynamics depend on fitness and management assumptions | Resistance mechanism decomposition, condensed fitness grid, treatment/PEP implementation sensitivity, vaccine-infectiousness thresholds, and resistance-parameter justification. | eTables 11, 13, 14, 16, and 28 | Resistance trajectories remain stress tests of selection mechanisms rather than unconditional replacement predictions. |
| No costs, quality-adjusted life-years, feasibility, or equity weights | Exploratory QALY-like burden translations are retained as repository outputs rather than submitted appendix tables. | Repository CSV outputs | This is not a formal cost-effectiveness analysis; the submitted model still does not include costs, decision thresholds, discounting, feasibility constraints, or equity weights. |
| In-development vaccine products cannot be treated as available policies | Pipeline-to-mechanism mapping for intranasal BPZE1, OMV-based platforms, genetically detoxified recombinant aP vaccines, and new multicomponent aP candidates. | eTable 27 | Candidate products were represented through mechanism profiles and sensitivity ranges, not product-specific policy scenarios. |

<div style="page-break-after: always;"></div>

### eTable 25. Selected-parameter joint PSA scenario-ranking diagnostics for infant-case intervention ordering.

| Strategy | Pr(ordered first) | Pr(top 2) | Pr(within 10% of best) | Mean order position | Median order position | Median infant cases per 100k/y | Q2.5 infant cases per 100k/y | Q97.5 infant cases per 100k/y | Median reduction vs current | PSA samples |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Adolescent booster | 0.00 | 0.00 | 0.00 | 5.36 | 5.00 | 1,245.19 | 0.40 | 5,740.13 | 0.00 | 128 |
| Combined strategy | 0.69 | 1.00 | 0.79 | 1.31 | 1.00 | 390.48 | 0.14 | 3,450.37 | 0.66 | 128 |
| Current practice | 0.00 | 0.00 | 0.00 | 5.59 | 6.00 | 1,246.48 | 0.47 | 5,773.86 | 0.00 | 128 |
| Higher child coverage | 0.00 | 0.00 | 0.00 | 6.58 | 7.00 | 1,256.41 | 0.44 | 5,965.17 | -0.03 | 128 |
| Household/adult transmission-reduction composite proxy | 0.00 | 0.00 | 0.00 | 3.18 | 3.00 | 1,012.63 | 0.32 | 5,449.85 | 0.19 | 128 |
| Upper-bound vaccine | 0.31 | 1.00 | 0.43 | 1.70 | 2.00 | 508.32 | 0.17 | 3,115.39 | 0.59 | 128 |
| Resistance-guided treatment | 0.00 | 0.00 | 0.00 | 4.29 | 4.00 | 1,180.64 | 0.43 | 5,507.19 | 0.06 | 128 |

<div style="page-break-after: always;"></div>

### eTable 26. Individual stochastic contact-clustering toy model key diagnostics (100 replicates, synthetic population 1,500, target R=1.08; structural sensitivity only).

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

### eTable 27. Vaccine-pipeline mechanism mapping to modeled scenario profiles.

| Candidate/platform | Development status | Transmission-relevant signal | Model use | Evidence source |
| --- | --- | --- | --- | --- |
| BPZE1 intranasal live attenuated | Phase 2b adult/challenge evidence; school-age trial registered. | Mucosal immunity and colonization reduction; closest to the high-transmission-blocking target. | Upper-bound transmission-blocking profile plus $VE_{inf}$ sensitivity; no product-specific efficacy assigned. | Keech et al [38]; Gbesemete et al [39]; ClinicalTrials.gov NCT03942406, NCT05461131, NCT05116241. |
| OMV or OMV-adjuvanted platforms | Preclinical/translational evidence; no late-stage pertussis efficacy trial identified. | Broader antigenic and Th1/Th17 responses; possible effects on susceptibility, infectiousness, or duration. | Covered by infection-/transmission-blocking profiles and $VE_{inf}$/$VE_{dur}$ ranges. | Locati et al [40]; related OMV literature cited therein. |
| Recombinant PT acellular boosters | Licensed recombinant boosters reported in Asia; Pertagen2x phase II/III registered. | Potentially stronger or more durable antibody response; not primarily mucosal transmission blocking. | Mapped to adolescent booster, current aP, infection-blocking, or waning-duration sensitivity. | BioNet pertussis product information; ClinicalTrials.gov NCT05193734. |
| New multi-component acellular combinations | CanSino DTcP phase 3 active-not-recruiting; other products remain platform-specific. | Relevant to clinical protection and possibly infection blocking; limited direct carriage evidence. | Covered by current aP and infection-blocking profiles; no separate product scenario. | ClinicalTrials.gov NCT05951725. |

<div style="page-break-after: always;"></div>

### eTable 28. Macrolide-resistance parameter justification and expected direction of bias.

| Parameter group | Baseline value | Explored range or scenarios | Source or anchor | Rationale | Expected direction of bias | Residual caveat |
| --- | --- | --- | --- | --- | --- | --- |
| Country-specific starting resistant fraction | Latest admissible country timeline anchor; fixed scenarios also used 5%, 30%, 70%, and 95% | Country timeline; fixed low, moderate, high, and very-high resistance scenarios | Country resistance timeline assembled from China, Japan, Australia, Americas, Europe, and low-anchor surveillance reports through the evidence lock | Separates observed or conservative starting strain composition from subsequent modeled selection dynamics. | Higher starting resistant fraction increases resistant burden and the apparent value of resistance-guided management; lower anchors delay resistant dominance. | Resistance sampling is heterogeneous across countries and years; anchors are not a globally representative surveillance system. |
| Resistant-strain relative fitness (fitness_R) | 1.00 (fitness neutral) | 0.70-1.25 grid and PSA range; selected narrative contrasts at 0.85, 1.00, and 1.15 | Rapid MRBP expansion and international spread without a demonstrated transmission penalty; local evidence note in manuscript_notes/resistance_fitness_evidence.md | Avoids assuming a persistent fitness cost when epidemiologic trajectories in China, Japan, and Australia do not rule out neutral or above-neutral fitness. | Lower fitness reduces projected resistant fraction and resistant-guided treatment benefit; higher fitness accelerates replacement and increases resistant burden. | Fitness is represented as one transmission scalar and may vary with vaccine history, treatment pressure, strain background, and host immunity. |
| Sensitive-strain treatment effect | Infectious-duration reduction 0.20; infectiousness reduction 0.15 | Treatment implementation and resistance-mechanism decomposition scenarios | CDC pertussis treatment/PEP guidance and model scenario assumptions | Represents early macrolide benefit for susceptible infections without assuming treatment fully blocks transmission. | Stronger sensitive-strain treatment benefit increases selection pressure favoring resistant strains; weaker benefit reduces modeled treatment-mediated selection. | Real-world treatment effect depends on timing, diagnosis, adherence, and clinical practice, none of which are explicitly modeled as individual pathways. |
| Resistant-strain treatment effect under standard macrolide practice | Infectious-duration reduction 0.10; infectiousness reduction 0.05 | Equalized treatment counterfactual; resistance-guided treatment alternative | Resistance-aware scenario assumption informed by macrolide resistance biology and treatment guidance | Allows resistant infections to receive less benefit from standard macrolide management while testing whether that differential drives replacement. | Lower resistant treatment benefit increases resistant burden and infant cases; equalizing treatment effects lowers selection for resistance. | The model does not identify strain-specific treatment effect from patient-level outcome data. |
| Postexposure prophylaxis (PEP) coverage | Household-contact coverage 0.30 | 0.05-0.60 in sensitivity analysis and PSA multiplier; implementation scenarios vary PEP reach | CDC/PAHO-style public health PEP guidance translated into scenario coverage assumptions | Represents partial household/contact implementation rather than universal prophylaxis. | Higher PEP reach amplifies any strain-specific PEP effectiveness differential; lower PEP reach weakens PEP-mediated selection and management benefit. | PEP targeting, timing, adherence, and contact tracing are not explicit household processes in the deterministic model. |
| PEP effectiveness by strain | Sensitive 0.70; resistant 0.10 under standard macrolide PEP | Resistant PEP effectiveness 0.00-0.50; equalized PEP and treatment+PEP decomposition scenarios | Macrolide-resistance mechanism, clinical guidance, and resistance-management scenario assumptions | Tests whether strain-specific prophylaxis failure can plausibly create selection pressure under standard macrolide PEP. | A larger sensitive-resistant PEP gap favors resistant strains; equalized PEP effectiveness markedly lowers projected end resistant fraction. | PEP effectiveness is not estimated from strain-specific household trial data; results are stress tests conditional on PEP reach and timing. |
| Resistance-guided management scenario | Symptomatic treatment rate 0.07; resistant infectious-duration reduction 0.45; resistant infectiousness reduction 0.35; resistant PEP effectiveness 0.45 | Treatment/PEP implementation scenarios and joint PSA uptake multiplier | CDC resistance-aware treatment guidance translated into a testing-and-alternative-treatment scenario | Represents improved recognition of resistance and use of effective alternatives or restored prophylaxis effectiveness. | Higher uptake or restored PEP effectiveness increases projected benefit; low testing reach and uptake reduce or delay benefit. | Testing availability, turnaround time, clinician suspicion, drug tolerability, and adherence are not modeled explicitly. |
| Resistant importation | Low-level importation enabled; default rate 0.20 per 100,000 persons/year with country/scenario resistant fraction | Resistance mechanism decomposition separates ongoing importation from fitness and treatment/PEP differentials | Persistence/reintroduction assumption anchored to observed international spread | Prevents deterministic extinction of rare resistant strains while allowing decomposition of whether importation alone drives high end fractions. | Higher importation affects persistence and timing; mechanism decomposition suggests it is not the main driver of near-complete replacement in the main runs. | Importation is smooth and low-level rather than a stochastic travel- or outbreak-linked process. |

<div style="page-break-after: always;"></div>
