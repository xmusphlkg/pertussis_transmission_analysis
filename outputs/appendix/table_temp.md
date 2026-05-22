## eTables

### eTable 1. Country-profile selection rationale and resistance anchors.

| Country | WHO region | Program profile | Resistance anchor | Data quality | Reason for inclusion |
| --- | --- | --- | --- | --- | --- |
| Australia | Western Pacific | aP vaccine; DTP3 93%; 6 routine doses; adolescent booster; maternal 20-32w | 4.3% (2024) | High | High recent reported incidence; measured low but detectable resistance; mature maternal and booster program. |
| Brazil | Americas | wP vaccine; DTP3 89%; 5 routine doses; no adolescent booster; maternal 20-32w | 1.0% (2025) | Moderate | Large Americas profile with wP schedule, maternal program, and detected resistant cases without national fraction. |
| China | Western Pacific | aP vaccine; DTP3 99%; 4 routine doses; no adolescent booster; no routine maternal program | 99.7% (2024) | High | Large population, marked post-pandemic resurgence, and near-complete measured macrolide resistance anchor. |
| Japan | Western Pacific | aP vaccine; DTP3 99%; 4 routine doses; no adolescent booster; no routine maternal program | 82.7% (2025) | High | Western Pacific resurgence and high measured resistance in 2024-2025 reports. |
| New Zealand | Western Pacific | aP vaccine; DTP3 88%; 5 routine doses; adolescent booster; maternal 16-26w | 1.0% (2025) | Moderate | Small high-income profile with maternal and adolescent programs and emerging resistance concern. |
| South Africa | African | aP vaccine; DTP3 74%; 6 routine doses; adolescent booster; maternal 26-34w | 2.0% (2025) | Moderate | African-region profile with shorter overlapping calibration window and contrasting demography. |
| Sweden | European | aP vaccine; DTP3 95%; 5 routine doses; adolescent booster; maternal 16-36w | 1.0% (2025) | High | European profile with high-quality surveillance and booster program contrast. |
| Thailand | South-East Asia | wP vaccine; DTP3 89%; 5 routine doses; no adolescent booster | 1.0% (2025) | Moderate | South-East Asian low reported-incidence profile with wP schedule and low maternal coverage. |
| United Kingdom | European | aP vaccine; DTP3 92%; 4 routine doses; no adolescent booster; maternal 16-32w | 0.3% (2024) | High | European maternal-program profile with established pregnancy vaccination and surveillance data. |
| United States | Americas | aP vaccine; DTP3 94%; 6 routine doses; adolescent booster; maternal 27-36w | 0.0% (2015) | High | Large Americas profile with adolescent and maternal Tdap program and low reported resistance. |

<div style="page-break-after: always;"></div>

### eTable 2. Study parameter-design matrix for scenario, sensitivity, and uncertainty analyses.

| Analysis component | Design level | Parameter settings | Source/provenance | Fixed or conditioned assumptions | Primary role | Detailed location |
| --- | --- | --- | --- | --- | --- | --- |
| Country profiles and calibration | Ten calibrated country profiles | Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, United Kingdom, and United States; country-specific demography, contact matrices, vaccination schedules and coverage, seasonality, surveillance intervals, resistance anchors, calibrated $beta_{S}$, and reporting multipliers. | Population denominators [13], schedule and coverage records [14], contact matrices [15-17], reported-case intervals [18], treatment and PEP assumptions [19,20], resistance guidance [21,22], and country resistance reports [23,24], [25], [26], [27], [28,29]; calibrated $beta_{S}$ and reporting multipliers are model-estimated from reported-case intervals. | Common deterministic ODE structure, age partition, natural-history defaults, 15-year burn-in, and 2025-2050 saved horizon. | Defines calibrated current-practice comparators and cross-country heterogeneity. | eTables 1, 5, 7, 9, and 12. |
| Vaccine-mechanism profile | No vaccine | $VE_{sus}$=0.0; $VE_{sym}$=0.0; $VE_{inf}$=0.0; $VE_{dur}$=0.0 | Null counterfactual with all vaccine-effect parameters set to zero; no external efficacy claim. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | No vaccine protection. | Figure 2A and eTables 14 and 27. |
| Vaccine-mechanism profile | Current aP profile | $VE_{sus}$=0.15; $VE_{sym}$=0.85; $VE_{inf}$=0.25; $VE_{dur}$=0.0 | Acellular-pertussis-like disease protection, asymptomatic-transmission structure, incomplete infection blocking, and waning informed by the WHO vaccine framework [1], transmission evidence [5,6], and duration-of-protection studies [7-9]. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | aP-like disease protection with moderate infection/transmission blocking. The high $VE_{sym}$ value is literature-supported for disease protection, while $VE_{sus}$, $VE_{inf}$, and $VE_{dur}$ are a mechanistic decomposition of that evidence rather than directly observed surveillance parameters. $VE_{inf}$ = 0.25 represents a population-average residual transmission-blocking assumption across recently and distantly vaccinated individuals. | Figure 2A and eTables 14 and 27. |
| Vaccine-mechanism profile | Infection-blocking | $VE_{sus}$=0.7; $VE_{sym}$=0.85; $VE_{inf}$=0.4; $VE_{dur}$=0.1 | Mechanistic scenario above the population-average aP profile, bounded by vaccine-framework assumptions [1], transmission evidence [5,6], and waning studies [7-9], then checked against vaccine-pipeline interpretation in eTable 27. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | Stronger reduction in susceptibility to infection. $VE_{inf}$ = 0.40 represents a plausible upper mechanism bound for recently boosted or more infection-blocking protection, not a direct empirical estimate for current aP products. | Figure 2A and eTables 14 and 27. |
| Vaccine-mechanism profile | Transmission-blocking | $VE_{sus}$=0.3; $VE_{sym}$=0.85; $VE_{inf}$=0.55; $VE_{dur}$=0.3 | Improved-transmission-blocking scenario informed by the WHO vaccine framework [1], aP/wP transmission evidence [5,6], waning studies [7-9], and product-target reasoning in eTable 27; not a licensed product estimate. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | Strong reduction in onward infectiousness and duration. Represents an improved aP formulation or wP-like transmission blocking. | Figure 2A and eTables 14 and 27. |
| Vaccine-mechanism profile | Upper-bound transmission-blocking | $VE_{sus}$=0.8; $VE_{sym}$=0.9; $VE_{inf}$=0.65; $VE_{dur}$=0.4 | Upper-bound high-transmission-blocking product-target profile; represented as a hypothetical mechanism profile using vaccine-framework assumptions [1], transmission evidence [5,6], waning studies [7-9], and pipeline mapping in eTable 27. | Other natural-history, contact, reporting, and resistance settings held to the scenario-specific country baseline unless explicitly crossed in grid analyses. | Strong infection, symptom, and transmission protection. Represents an upper-bound high-transmission-blocking pertussis vaccine profile with mucosal immunity induction (e.g. live-attenuated nasal or outer membrane vesicle platforms). | Figure 2A and eTables 14 and 27. |
| Macrolide-resistance scenario | Country timeline | target resistant fraction=0.3; importation resistant fraction=0.3; anchor rate/y=2.0; country timeline=Yes; $f_R$=1.0; resistant treatment effect=0.1; resistant PEP effectiveness=0.1 | Country-specific resistance anchors combined clinical guidance [21,22] with country reports from China [23,24], Australia [25], Japan [26], the Americas [27], and regional MRBP evidence [28,29]; raw evidence is tabulated in eTable 6 and parameter rationale in eTable 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Country-specific macrolide resistance prevalence from data/raw/country_resistance_timeline.csv. The prevalence anchors are data-derived. $f_R$ = 1.0 is an epidemiologically motivated neutral baseline, not a directly measured strain-fitness estimate: China MRBP rose from 36% (2016) to near-fixation (>99%, 2024), and related MRBP lineages were reported internationally without clear transmission disadvantage. The fitness grid and fitness sensitivity scenarios explore the full range [0.70-1.25]. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | Low | target resistant fraction=0.05; importation resistant fraction=0.05; anchor rate/y=2.0; country timeline=No; $f_R$=1.0; resistant treatment effect=0.1; resistant PEP effectiveness=0.1 | Fixed prevalence stress-test anchored to observed low-prevalence settings and conservative imported-risk assumptions [21,27-29]; see eTables 3, 6, and 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Low macrolide resistance prevalence with fitness-neutral strain. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | Moderate | target resistant fraction=0.3; importation resistant fraction=0.3; anchor rate/y=2.0; country timeline=No; $f_R$=1.0; resistant treatment effect=0.1; resistant PEP effectiveness=0.1 | Fixed prevalence stress-test spanning plausible intermediate resistance pressure, using clinical guidance [21,22], China and Australia reports [23-25], Japan and Americas reports [26,27], and regional MRBP evidence [28,29]; see eTables 3, 6, and 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Moderate macrolide resistance prevalence with fitness-neutral strain. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | High | target resistant fraction=0.7; importation resistant fraction=0.7; anchor rate/y=2.0; country timeline=No; $f_R$=1.0; resistant treatment effect=0.1; resistant PEP effectiveness=0.1 | Fixed prevalence stress-test motivated by high-prevalence MRBP reports in China [23,24], Japan [26], and regional evidence [28,29]; see eTables 3, 6, and 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | High macrolide resistance prevalence with fitness-neutral strain. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | Very high | target resistant fraction=0.95; importation resistant fraction=0.95; anchor rate/y=2.0; country timeline=No; $f_R$=1.0; resistant treatment effect=0.1; resistant PEP effectiveness=0.1 | Upper prevalence stress-test motivated by near-fixation observations in China and high-prevalence Japanese clusters [23,24,26]; see eTables 3, 6, and 28. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Very high macrolide resistance prevalence with fitness-neutral strain. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | Country timeline with fitness cost | target resistant fraction=0.3; importation resistant fraction=0.3; anchor rate/y=2.0; country timeline=Yes; $f_R$=0.85; resistant treatment effect=0.1; resistant PEP effectiveness=0.1 | Counterfactual fitness-cost sensitivity retained to bound traditional resistance-cost assumptions against observed MRBP expansion in China [23,24], Australia [25], Japan and the Americas [26,27], and regional reports [28,29]. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Country-timeline resistance with moderate fitness cost (15%). Retained as a sensitivity scenario representing the traditional assumption that ribosomal mutations impose a growth penalty. Recent rapid expansion makes a large persistent cost less plausible, but this scenario is included to bound the optimistic end of resistance projections. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | Country timeline with fitness advantage | target resistant fraction=0.3; importation resistant fraction=0.3; anchor rate/y=2.0; country timeline=Yes; $f_R$=1.1; resistant treatment effect=0.1; resistant PEP effectiveness=0.1 | Fitness-advantage sensitivity motivated by rapid MRBP expansion and international spread in China [23,24], Australia [25], Japan and the Americas [26,27], and regional reports [28,29], without a demonstrated transmission penalty. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | Country-timeline resistance with fitness advantage (10%). The MT28-ptxP3 MRBP clone has been reported with resistance and vaccine-antigen lineages in rapidly expanding outbreaks. This scenario tests whether a modest fitness advantage materially changes long-term resistance burden projections; the 10% value is a stress-test assumption, not a measured relative-fitness estimate. | eTables 3, 6, 13, and 28. |
| Macrolide-resistance scenario | High resistance with fitness advantage | target resistant fraction=0.7; importation resistant fraction=0.7; anchor rate/y=2.0; country timeline=No; $f_R$=1.15; resistant treatment effect=0.1; resistant PEP effectiveness=0.1 | Worst-case stress test combining high starting resistance with a fitness-advantaged strain; rationale summarized in eTable 28 and resistance evidence from China [23,24], Japan [26], and regional MRBP reports [28,29]. | Country-timeline anchors use latest admissible evidence through the 2025 analysis anchor; fixed scenarios provide low-to-very-high contrasts. | High resistance prevalence with fitness advantage (15%). Worst-case scenario combining high initial resistance with a fitness-advantaged strain, representing the upper bound of resistant infection burden. Motivated by genomic reports of co-selection between resistance and vaccine-antigen lineages; retained as a stress-test assumption rather than a directly estimated fitness value. | eTables 3, 6, 13, and 28. |
| Intervention strategy scenario | Current practice | Baseline comparator; Reference scenario | Country-specific schedule and coverage inputs from WHO/UNICEF and national records [1,14], with standard treatment/PEP assumptions from CDC guidance [20]. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Current vaccination and standard macrolide treatment. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Higher child coverage | Current-program modification; Marginal coverage-change scenario | Scenario modification of country routine childhood coverage using country schedule and coverage inputs [1,14]; not a new efficacy estimate. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Increase routine childhood vaccine coverage in the existing program. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Adolescent booster | Current-program modification; Booster-program scenario | Scenario modification of booster timing/coverage using country schedule inputs and pertussis vaccine guidance [1,14]. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Add a school-age or adolescent booster. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Maternal-household composite proxy | Maternal-household composite proxy; Implementation-dependent composite scenario | Maternal and household-proxy scenario informed by maternal-program evidence [10-12] and infant-specific effectiveness estimates [36,37]; decomposed in eTable 17. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Represent pregnancy Tdap-based infant protection through direct infant antibody protection, recent maternal/adult boosting, and cocooning. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Direct maternal antibody only | Maternal-household component diagnostic; Component diagnostic, not standalone policy | Component diagnostic based on maternal-program evidence [10-12] and infant-specific effectiveness estimates [36,37], not a standalone policy estimate. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Isolate direct infant protection from transplacental antibody transfer. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Maternal/adult boosting only | Maternal-household component diagnostic; Component diagnostic, not standalone policy | Component diagnostic separating adult boosting from direct infant antibody and cocooning effects; informed by maternal-program interpretation [10-12] and infant-specific estimates [36,37]. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Isolate recent adult or maternal boosting that lowers infection and transmission risk in young adults. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Cocooning only | Maternal-household component diagnostic; Component diagnostic, not standalone policy | Component diagnostic for household/contact reduction, interpreted with maternal-program evidence [10-12] and infant-protection estimates [36,37]. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Isolate reduced mother-infant or household-to-infant transmission. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Resistance-guided treatment | Resistance-management scenario; Implementation-dependent management scenario | Resistance-aware testing, treatment, and PEP scenario translated from CDC treatment/PEP and antibiotic-resistance guidance [20,21]. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Use resistance-aware testing, alternative treatment, and restored PEP effectiveness for resistant infections. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Upper-bound vaccine | Hypothetical product-target vaccine; Product target, not available policy | Hypothetical product-target scenario interpreted through the WHO vaccine framework [1], transmission evidence [5,6], waning studies [7-9], and vaccine-pipeline mapping in eTable 27. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Represent an improved high-transmission-blocking pertussis vaccine profile. | eTables 4, 15-20, 22, and 25. |
| Intervention strategy scenario | Combined strategy | Composite stress test; Mechanistic upper-bound package, not policy package | Composite stress test combining the cited maternal, adolescent-booster, resistance-guided, and transmission-blocking assumptions; not a single externally validated package. | Strategies are grouped by interpretive status rather than treated as directly substitutable policies; costs, feasibility, equity weights, and implementation constraints are not optimized. | Combine transmission-blocking vaccine assumptions, maternal-household protection, adolescent boosting, and resistance-guided management. | eTables 4, 15-20, 22, and 25. |
| Observation and reporting sensitivity | Medium | overall multiplier=1.0; age multipliers=No; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | High | overall multiplier=1.5; age multipliers=No; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Low | overall multiplier=0.5; age multipliers=No; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Age-biased | age multipliers=Yes; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Time-varying | overall multiplier=1.0; age multipliers=No; time variation=Yes | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Infant high, adult very low | age multipliers=Yes; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Infant moderate, adult minimal | age multipliers=Yes; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Enhanced surveillance | age multipliers=Yes; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | Adult-focused improvement | age multipliers=Yes; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Observation and reporting sensitivity | China passive system | age multipliers=Yes; time variation=No | Reporting sensitivities are scenario perturbations around literature-informed reporting priors from notification-efficiency and serology studies [30,31], capture-recapture and cough-serology evidence [32,33], and active surveillance [34]; fitted probabilities are shown in eTable 12. | Reporting scenarios perturb the observation process only; PEP activation uses a separate detection proxy. | Separates surveillance completeness from true transmission and resistant-strain dynamics. | Supplementary Methods and eTables 10 and 12. |
| Vaccine-resistance interaction grids | $VE_{inf}$-only grid and continuous $f_R$ x $VE_{inf}$ grid | $f_R$ values 0.70-1.25; $VE_{inf}$ values 0.05-0.55; $VE_{inf}$-only thresholds also vary resistance prevalence anchors and resistant importation fraction. | Grid bounds combine vaccine-framework and transmission uncertainty [1], [5,6], waning uncertainty [7-9], resistance guidance [21,22], and country resistance evidence [23,24], [25], [26], [27], [28,29]; summarized in eTables 11 and 14. | $VE_{sus}$ and $VE_{dur}$ held at grid-baseline values for $VE_{inf}$-only thresholds; country profiles remain calibrated. | Identifies transmission-blocking thresholds and shows how resistant fitness modifies vaccine benefit. | Figure 3D-F and eTables 11 and 14. |
| Exploratory uncertainty and robustness diagnostics | Sensitivity screens and robustness diagnostics | 48-run Latin-hypercube screening; 128 selected-parameter joint order-stability samples; temporal, infant-contact, maternal-duration, treatment/PEP, event-scale, and stochastic toy diagnostics. | Designed as robustness diagnostics following immunization-model reporting guidance [35], using parameter ranges documented in eTables 5, 10, 16-18, 21, 23, 25, and 28. | Diagnostics are not full posterior or decision analyses; they support scenario-order and structural-robustness interpretation. | Quantifies which assumptions threaten interpretation of infant-burden and intervention-order conclusions. | eTables 16-26. |
| Conditional beta-grid interval analysis | Adaptive $log(beta_{S})$ quadrature | $beta_{S}$ posterior dimension and negative-binomial stochastic overlay scaled to the analysis horizon; pre-specified tail, effective-grid-size, and maximum-mass checks. | Conditional uncertainty workflow follows the model-reporting distinction between calibrated identifiable parameters and fixed nuisance assumptions [35]; priors and fixed nuisance settings are in eTable 10. | Reporting multiplier, vaccine nuisance parameters, infectious durations, asymptomatic infectiousness, resistance fitness, and resistance anchors fixed at calibrated, literature-informed, or pre-specified baseline values. | Provides conditional uncertainty intervals for selected main-text summaries without claiming full joint structural uncertainty. | eTable 10 and beta-grid quality outputs retained in repository CSV files. |

<div style="page-break-after: always;"></div>

### eTable 3. Macrolide-resistance initialization, importation, and fitness assumptions.

| Scenario | Target resistant fraction | Importation resistant fraction | Anchor rate per year | Country timeline | $f_R$ | Description |
| --- | --- | --- | --- | --- | --- | --- |
| Country timeline | 0.3 | 0.3 | 2.000 | Yes | 1.000 | Country-specific macrolide resistance prevalence from data/raw/country_resistance_timeline.csv. The prevalence anchors are data-derived. $f_R$ = 1.0 is an epidemiologically motivated neutral baseline, not a directly measured strain-fitness estimate: China MRBP rose from 36% (2016) to near-fixation (>99%, 2024), and related MRBP lineages were reported internationally without clear transmission disadvantage. The fitness grid and fitness sensitivity scenarios explore the full range [0.70-1.25]. |
| Low | 0.05 | 0.05 | 2.000 | No | 1.000 | Low macrolide resistance prevalence with fitness-neutral strain. |
| Moderate | 0.3 | 0.3 | 2.000 | No | 1.000 | Moderate macrolide resistance prevalence with fitness-neutral strain. |
| High | 0.7 | 0.7 | 2.000 | No | 1.000 | High macrolide resistance prevalence with fitness-neutral strain. |
| Very high | 0.95 | 0.95 | 2.000 | No | 1.000 | Very high macrolide resistance prevalence with fitness-neutral strain. |
| Country timeline with fitness cost | 0.3 | 0.3 | 2.000 | Yes | 0.85 | Country-timeline resistance with moderate fitness cost (15%). Retained as a sensitivity scenario representing the traditional assumption that ribosomal mutations impose a growth penalty. Recent rapid expansion makes a large persistent cost less plausible, but this scenario is included to bound the optimistic end of resistance projections. |
| Country timeline with fitness advantage | 0.3 | 0.3 | 2.000 | Yes | 1.100 | Country-timeline resistance with fitness advantage (10%). The MT28-ptxP3 MRBP clone has been reported with resistance and vaccine-antigen lineages in rapidly expanding outbreaks. This scenario tests whether a modest fitness advantage materially changes long-term resistance burden projections; the 10% value is a stress-test assumption, not a measured relative-fitness estimate. |
| High resistance with fitness advantage | 0.7 | 0.7 | 2.000 | No | 1.150 | High resistance prevalence with fitness advantage (15%). Worst-case scenario combining high initial resistance with a fitness-advantaged strain, representing the upper bound of resistant infection burden. Motivated by genomic reports of co-selection between resistance and vaccine-antigen lineages; retained as a stress-test assumption rather than a directly estimated fitness value. |

<div style="page-break-after: always;"></div>

### eTable 4. Intervention strategy definitions, modified control levers, and interpretive status.

| Strategy | Scenario category | Interpretive status | Scenario definition | Modified control levers | Interpretation note |
| --- | --- | --- | --- | --- | --- |
| Current practice | Baseline comparator | Reference scenario | Current vaccination and standard macrolide treatment. | Country-specific vaccine schedule and coverage; standard macrolide treatment and PEP assumptions. | Comparator for relative reductions. |
| Higher child coverage | Current-program modification | Marginal coverage-change scenario | Increase routine childhood vaccine coverage in the existing program. | Coverage updates: 3-11 mo 0.82, 1-4 y 0.96, 5-9 y 0.94. | Tests marginal gains in high-coverage profiles; not evidence against maintaining routine childhood vaccination. |
| Adolescent booster | Current-program modification | Booster-program scenario | Add a school-age or adolescent booster. | Coverage update: 10-17 y 0.90; $VE_{inf}$ retained at 0.25. | Program-extension scenario using the current aP-like mechanism rather than a new product profile. |
| Maternal-household composite proxy | Maternal-household composite proxy | Implementation-dependent composite scenario | Represent pregnancy Tdap-based infant protection through direct infant antibody protection, recent maternal/adult boosting, and cocooning. | Infant maternal-protection coverage: 0-2 m 0.72 and 3-11 m 0.78; 18-39 y recent-boosting proxy 0.55; maternal $VE_{sus}$ 0.55 and $VE_{sym}$ 0.92; maternal protection duration 180 d; young-adult-to-infant contact reduction 30%. | Composite proxy, not passive antibody protection alone; eTable 17 decomposes direct antibody, adult boosting, and cocooning components. |
| Direct maternal antibody only | Maternal-household component diagnostic | Component diagnostic, not standalone policy | Isolate direct infant protection from transplacental antibody transfer. | Infant maternal-protection coverage: 0-2 m 0.72 and 3-11 m 0.78; maternal $VE_{sus}$ 0.55 and $VE_{sym}$ 0.92; maternal protection duration 180 d. | Excludes adult boosting and cocooning to attribute the composite maternal-household scenario. |
| Maternal/adult boosting only | Maternal-household component diagnostic | Component diagnostic, not standalone policy | Isolate recent adult or maternal boosting that lowers infection and transmission risk in young adults. | Coverage update: 18-39 y recent-boosting proxy 0.55. | Excludes direct infant antibody protection and cocooning. |
| Cocooning only | Maternal-household component diagnostic | Component diagnostic, not standalone policy | Isolate reduced mother-infant or household-to-infant transmission. | Young-adult-to-infant contact reduction 30% for 0-2 mo and 3-11 mo targets. | Excludes direct infant antibody protection and adult boosting. |
| Resistance-guided treatment | Resistance-management scenario | Implementation-dependent management scenario | Use resistance-aware testing, alternative treatment, and restored PEP effectiveness for resistant infections. | Resistant infection updates: infectious-duration reduction 0.45 and infectiousness reduction 0.35; symptomatic treatment rate 0.065; resistant-strain PEP effectiveness 0.45. | Depends on testing reach, uptake, treatment selection, and PEP implementation; near-term sensitivity is in eTable 16. |
| Upper-bound vaccine | Hypothetical product-target vaccine | Product target, not available policy | Represent an improved high-transmission-blocking pertussis vaccine profile. | Uses Upper-bound transmission-blocking vaccine profile: $VE_{sus}$ 0.80, $VE_{sym}$ 0.90, $VE_{inf}$ 0.65, $VE_{dur}$ 0.40. | Mechanistic upper-bound profile motivated by candidate mucosal or high-transmission-blocking platforms; pipeline mapping is in eTable 27. |
| Combined strategy | Composite stress test | Mechanistic upper-bound package, not policy package | Combine transmission-blocking vaccine assumptions, maternal-household protection, adolescent boosting, and resistance-guided management. | Uses Transmission-blocking vaccine profile; infant maternal-protection coverage 0.72/0.84; 10-17 y coverage 0.90; 18-39 y boosting proxy 0.55; maternal $VE_{sus}$ 0.55 and $VE_{sym}$ 0.92; maternal protection duration 180 d; young-adult-to-infant contact reduction 30%; resistance-guided treatment and resistant-strain PEP updates. | Stress-test scenario for combined mechanisms; not an externally validated implementation package. |

<div style="page-break-after: always;"></div>

### eTable 5. Baseline parameter values, admissible ranges, and evidence provenance.

| Parameter | Description | Baseline value | Range | Unit | Source or assumption | Sensitivity |
| --- | --- | --- | --- | --- | --- | --- |
| simulation.end_time | Simulation analysis horizon | 9,495.0 | see config/model_settings.yaml sensitivity_parameters | days | Analysis design | No |
| simulation.burn_in_years | Pre-analysis burn-in horizon | 15.00 | see config/model_settings.yaml sensitivity_parameters | years | Analysis design | No |
| transmission.beta_S | Transmission rate for macrolide-sensitive pertussis | 0.01 | see config/model_settings.yaml sensitivity_parameters | per contact day | Calibrated to reported pertussis incidence | No |
| transmission.relative_infectiousness_asymptomatic | Relative infectiousness of asymptomatic infection | 0.35 | see config/model_settings.yaml sensitivity_parameters | ratio | Literature-informed assumption | Yes |
| transmission.multi_year_period_years | Target/diagnostic inter-epidemic period | 4.000 | see config/model_settings.yaml sensitivity_parameters | years | Pertussis cycle-model evidence | No |
| transmission.multi_year_amplitude | Weak multi-year phase-locking amplitude | 0 | see config/model_settings.yaml sensitivity_parameters | ratio | Model-structure assumption | Yes |
| natural_history.latent_duration | Latent period duration | 8.000 | see config/model_settings.yaml sensitivity_parameters | days | CDC clinical guidance | No |
| natural_history.infectious_duration_symptomatic | Symptomatic infectious duration | 21.00 | see config/model_settings.yaml sensitivity_parameters | days | CDC clinical guidance | Yes |
| natural_history.infectious_duration_asymptomatic | Asymptomatic infectious duration | 14.00 | see config/model_settings.yaml sensitivity_parameters | days | Literature-informed assumption | Yes |
| natural_history.recovered_immunity_duration | Duration of post-infection protection | 3,285.0 | see config/model_settings.yaml sensitivity_parameters (reciprocal of rates.waning_natural) | days | CDC clinical guidance and cycle-model evidence | Yes |
| natural_history.vaccine_protection_duration | Duration of vaccine-derived protection proxy | 1,825.0 | see config/model_settings.yaml sensitivity_parameters (reciprocal of rates.waning_vaccine) | days | aP waning literature | Yes |
| treatment.treatment_rate_symptomatic | Daily transition from symptomatic infection to treatment | 0.025 | see config/model_settings.yaml sensitivity_parameters | per day | CDC guidance plus implementation assumption | Yes |
| PEP.coverage_household_contacts | Dynamic PEP coverage ceiling among close contacts | 0.3 | see config/model_settings.yaml sensitivity_parameters | proportion | CDC guidance plus implementation assumption | Yes |

<div style="page-break-after: always;"></div>

### eTable 6. Country-specific macrolide-resistance evidence used for resistance anchoring.

| Country | Year | Sample size | Resistance estimate | Evidence class | Source | Note |
| --- | --- | --- | --- | --- | --- | --- |
| Australia | 2024 | 188 | 4.3% (1.9%-8.2%) | Measured national genomic surveillance fraction | https://doi.org/10.1016/j.lanmic.2025.101286 | Nationwide Australian tNGS study of 2024-positive respiratory specimens estimated macrolide resistance at 8/188 (4.3%). |
| Brazil | 2025 | Not publicly reported; model anchor | 1.0% (0.0%-5.0%) | Low detected model anchor | https://www.paho.org/en/news/26-8-2025-paho-calls-strengthened-vaccination-and-surveillance-amid-spread-antibiotic | No public denominator located; conservative low anchor retained pending surveillance. |
| China | 2016 | 11 | 36.4% (28.0%-45.0%) | Measured regional isolate fraction | https://wwwnc.cdc.gov/eid/article/30/1/22-1588_article | Shanghai isolate series; 4/11 selected 2016 isolates were macrolide resistant. |
| China | 2022 | 72 | 97.2% (94.0%-99.0%) | Measured regional isolate fraction | https://wwwnc.cdc.gov/eid/article/30/1/22-1588_article | Shanghai isolate series; 70/72 selected 2022 isolates were macrolide resistant. |
| China | 2024 | 394 | 99.7% (98.6%-100.0%) | Measured multicenter isolate fraction | https://www.sciencedirect.com/science/article/pii/S2666606525001658 | Five sentinel hospitals in China during 2024; 393/394 isolates displayed high-level azithromycin resistance. |
| Japan | 2024 | 8 | 87.5% (47.3%-99.7%) | Measured regional case series fraction | https://www.sciencedirect.com/science/article/pii/S1341321X26000140 | Osaka case series, August 2024-January 2025; 7/8 analyzed B. pertussis strains were macrolide resistant. |
| Japan | 2025 | 52 | 82.7% (69.7%-91.8%) | Measured multicenter isolate fraction | https://www.mdpi.com/2227-9059/14/1/167 | Japanese children at six clinics, March-August 2025; 43/52 sequenced B. pertussis isolates carried the A2047G mutation associated with macrolide resistance. |
| New Zealand | 1995 | 88 | 0.0% (0.0%-4.1%) | Measured historical national isolate fraction | https://pubmed.ncbi.nlm.nih.gov/9579709/ | ESR national reference laboratory series from 1991-1995: 88 strains tested, with erythromycin MICs 0.12-0.5 mg/L. A later meta-analysis tabulates this study as 0/88 resistant isolates. |
| New Zealand | 2025 | Not publicly reported; model anchor | 1.0% (0.0%-5.0%) | Low detected model anchor | https://www.tewhatuora.govt.nz/for-health-professionals/clinical-guidance/communicable-disease-control-manual/pertussis | No public denominator located; conservative low anchor retained pending surveillance. |
| South Africa | 2025 | Not publicly reported; model anchor | 2.0% (0.5%-5.0%) | Global-surveillance extrapolation | https://www.cdc.gov/pertussis/hcp/antibiotic-resistance/index.html; https://www.mdpi.com/2079-6382/11/11/1570 | No country-specific denominator located; conservative low extrapolated anchor retained pending surveillance. |
| Sweden | 2025 | Not publicly reported; model anchor | 1.0% (0.0%-5.0%) | Low imported model anchor | https://www.folkhalsomyndigheten.se/contentassets/975cc036216b48a39b7bf34319d4ecee/pertussis-surveillance-sweden-23rd-annual-report.pdf | No public denominator located; conservative low anchor retained pending surveillance. |
| Thailand | 2025 | Not publicly reported; model anchor | 1.0% (0.0%-5.0%) | Low imported model anchor | https://www.cdc.gov/pertussis/hcp/antibiotic-resistance/index.html | No public denominator located; conservative low anchor retained pending surveillance. |
| United Kingdom | 2009 | 583 | 0.0% (0.0%-0.6%) | Measured historical national isolate fraction | https://researchportal.ukhsa.gov.uk/en/publications/antimicrobial-susceptibility-testing-of-historical-and-recent-cli/ | UK enhanced-surveillance isolates collected from 2001-2009: all 583 isolates were fully susceptible to erythromycin, clarithromycin, and azithromycin. |
| United Kingdom | 2024 | 661 | 0.3% (0.0%-1.1%) | Measured national surveillance fraction | https://www.postersessiononline.eu/173580348_eu/congresos/UKHSA2025/aula/-P_58_UKHSA2025.pdf | UKHSA national reference laboratory poster: 661 B. pertussis isolates received from June 2023 to November 2024, with 2 predicted and phenotypically confirmed macrolide-resistant isolates. |
| United States | 1997 | 47 | 2.1% (0.1%-11.3%) | Measured regional isolate fraction | https://pubmed.ncbi.nlm.nih.gov/9350776/ | Intermountain West pediatric isolates recovered from January 1985 to June 1997; 1/47 was erythromycin resistant (MIC 32 ug/mL). |
| United States | 2015 | 1,208 | 0.0% (0.0%-0.3%) | Measured multistate surveillance fraction | https://www.walshmedicalmedia.com/conference-abstracts-files/2155-9597.C1.016-015.pdf | CDC surveillance abstract: 1208 B. pertussis isolates collected from 2011-2015 across 7 enhanced-surveillance states, 2 outbreak states, and 6 sporadic-state settings were susceptible to erythromycin and azithromycin; 54 DNA NPS extracts had no A2047G mutation. |

<div style="page-break-after: always;"></div>

### eTable 7. Calibration acceptance, fitted parameters, and interval-level fit diagnostics.

| Country | Period | Accepted | Fit status | Calibrated beta | Observed incidence per 100k | Modeled incidence per 100k | Model/observed ratio | Intervals | Observed reports | Modeled reports | MAPE | Observed peak year | Modeled peak year | Peak timing error, y | Peak magnitude ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | Overall | Yes | Calibrated to reported cases | 0.0231 | 61.49 | 61.76 | 1.005 | 65 | 88,963.0 | 88,963.0 | 1.761 | 2024 | 2025 | 1.000 | 0.9258 |
| Australia | Pandemic/NPI | Yes | Calibrated to reported cases | 0.0231 | 61.49 | 61.76 | 1.005 | 12 | 540.00 | 1.785 | 0.9964 |  |  |  |  |
| Australia | Post-pandemic | Yes | Calibrated to reported cases | 0.0231 | 61.49 | 61.76 | 1.005 | 53 | 88,423.0 | 88,961.2 | 1.934 |  |  |  |  |
| Brazil | Overall | Yes | Calibrated to reported cases | 0.009043 | 0.9975 | 0.9728 | 0.9752 | 64 | 11,275.0 | 11,275.0 | 8.544 | 2024 | 2021 | -3.000 | 0.1661 |
| Brazil | Pandemic/NPI | Yes | Calibrated to reported cases | 0.009043 | 0.9975 | 0.9728 | 0.9752 | 12 | 159.00 | 2,152.1 | 15.79 |  |  |  |  |
| Brazil | Post-pandemic | Yes | Calibrated to reported cases | 0.009043 | 0.9975 | 0.9728 | 0.9752 | 52 | 11,116.0 | 9,122.9 | 6.871 |  |  |  |  |
| China | Overall | Yes | Calibrated to reported cases | 0.009717 | 7.037 | 7.267 | 1.033 | 81 | 640,783 | 675,181 | 3.939 | 2024 | 2025 | 1.000 | 0.574 |
| China | Pandemic/NPI | Yes | Calibrated to reported cases | 0.009717 | 7.037 | 7.267 | 1.033 | 24 | 14,156.0 | 8,456.9 | 0.6679 |  |  |  |  |
| China | Post-pandemic | Yes | Calibrated to reported cases | 0.009717 | 7.037 | 7.267 | 1.033 | 57 | 626,627 | 666,724 | 5.316 |  |  |  |  |
| Japan | Overall | Yes | Calibrated to reported cases | 0.0119 | 12.57 | 14.29 | 1.137 | 276 | 82,325.0 | 82,325.0 | 4.791 | 2025 | 2025 | 0 | 0.4462 |
| Japan | Pandemic/NPI | Yes | Calibrated to reported cases | 0.0119 | 12.57 | 14.29 | 1.137 | 52 | 563.00 | 914.22 | 1.157 |  |  |  |  |
| Japan | Post-pandemic | Yes | Calibrated to reported cases | 0.0119 | 12.57 | 14.29 | 1.137 | 224 | 81,762.0 | 81,410.8 | 5.635 |  |  |  |  |
| New Zealand | Overall | Yes | Calibrated to reported cases | 0.015 | 19.15 | 19.23 | 1.004 | 64 | 5,324.0 | 5,324.0 | 3.883 | 2024 | 2026 | 2.000 | 0.6944 |
| New Zealand | Pandemic/NPI | Yes | Calibrated to reported cases | 0.015 | 19.15 | 19.23 | 1.004 | 12 | 62.00 | 213.14 | 3.693 |  |  |  |  |
| New Zealand | Post-pandemic | Yes | Calibrated to reported cases | 0.015 | 19.15 | 19.23 | 1.004 | 52 | 5,262.0 | 5,110.9 | 3.926 |  |  |  |  |
| South Africa | Overall | Yes | Calibrated to reported cases | 0.009416 | 2.276 | 2.143 | 0.9415 | 32 | 3,883.0 | 3,883.0 | 1.167 | 2025 | 2023 | -2.000 | 0.5983 |
| South Africa | Post-pandemic | Yes | Calibrated to reported cases | 0.009416 | 2.276 | 2.143 | 0.9415 | 32 | 3,883.0 | 3,883.0 | 1.167 |  |  |  |  |
| Sweden | Overall | Yes | Calibrated to reported cases | 0.01105 | 6.299 | 6.522 | 1.035 | 64 | 3,562.0 | 3,562.0 | 10.47 | 2024 | 2025 | 1.000 | 0.2354 |
| Sweden | Pandemic/NPI | Yes | Calibrated to reported cases | 0.01105 | 6.299 | 6.522 | 1.035 | 12 | 11.00 | 588.67 | 37.06 |  |  |  |  |
| Sweden | Post-pandemic | Yes | Calibrated to reported cases | 0.01105 | 6.299 | 6.522 | 1.035 | 52 | 3,551.0 | 2,973.3 | 5.405 |  |  |  |  |
| Thailand | Overall | Yes | Calibrated to reported cases | 0.009217 | 0.4605 | 0.4797 | 1.042 | 72 | 1,982.0 | 1,982.0 | 7.043 | 2024 | 2024 | 0 | 0.216 |
| Thailand | Pandemic/NPI | Yes | Calibrated to reported cases | 0.009217 | 0.4605 | 0.4797 | 1.042 | 24 | 30.00 | 434.09 | 11.70 |  |  |  |  |
| Thailand | Post-pandemic | Yes | Calibrated to reported cases | 0.009217 | 0.4605 | 0.4797 | 1.042 | 48 | 1,952.0 | 1,547.9 | 5.602 |  |  |  |  |
| United Kingdom | Overall | Yes | Calibrated to reported cases | 0.015 | 9.553 | 9.916 | 1.038 | 273 | 34,581.0 | 34,581.0 | 8.092 | 2024 | 2024 | 0 | 0.2146 |
| United Kingdom | Pandemic/NPI | Yes | Calibrated to reported cases | 0.015 | 9.553 | 9.916 | 1.038 | 104 | 1,812.0 | 8,068.1 | 13.38 |  |  |  |  |
| United Kingdom | Post-pandemic | Yes | Calibrated to reported cases | 0.015 | 9.553 | 9.916 | 1.038 | 169 | 32,769.0 | 26,512.9 | 4.735 |  |  |  |  |
| United States | Overall | Yes | Calibrated to reported cases | 0.009501 | 1.394 | 1.415 | 1.014 | 278 | 25,679.0 | 25,679.0 | 6.108 | 2024 | 2021 | -3.000 | 0.2152 |
| United States | Pandemic/NPI | Yes | Calibrated to reported cases | 0.009501 | 1.394 | 1.415 | 1.014 | 51 | 510.00 | 4,909.3 | 18.16 |  |  |  |  |
| United States | Post-pandemic | Yes | Calibrated to reported cases | 0.009501 | 1.394 | 1.415 | 1.014 | 227 | 25,169.0 | 20,769.7 | 3.400 |  |  |  |  |

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
| $f_R$ | $Normal(1.00, 0.12^2)$ on $[0.70, 1.25]$ | Epidemiologically motivated prior centered on fitness-neutral (1.0), because MRBP reached near-fixation in China within 8 years and spread internationally without clear transmission disadvantage. This is not a direct measured relative-fitness estimate; SD of 0.12 allows modest fitness costs or advantages. |
| $p_R$ | Fixed country timeline; floor SD 0.03 | Resistance prevalence is FIXED at the country-calibrated value during MCMC (not sampled). The country_resistance_timeline.csv provides well-constrained estimates for most countries. This eliminates a major source of multimodality without losing scientific information. |
| $VE^{mat}_{sus}$ | $Beta(mu=0.55, sigma=0.12)$ | Prior for maternal antibody protection against infant infection. Centered on 0.55 using maternal Tdap effectiveness evidence for confirmed pertussis in infants younger than 2 months [36], which combines infection prevention and disease prevention. The infection-blocking component is a decomposed model assumption guided by maternal immunization effectiveness studies [10,12]. SD of 0.12 allows exploration of [0.30, 0.80]. |
| $VE^{mat}_{sym}$ | $Beta(mu=0.92, sigma=0.05)$ | Prior for maternal antibody protection against symptomatic disease given infection. High confidence based on consistent estimates of VE against hospitalization (>90%) across US, UK, and Argentina studies [10,36,37]. Narrow SD reflects strong evidence consensus. |

<div style="page-break-after: always;"></div>

### eTable 11. Condensed macrolide-resistant fitness and vaccine infectiousness grid definition.

| Dimension | Grid values | Selected contrasts | Interpretation |
| --- | --- | --- | --- |
| Resistant-strain relative fitness | 0.70, 0.80, 0.85, 0.90, 0.95, 0.98, 1.00, 1.02, 1.05, 1.10, 1.15, 1.20, 1.25 | 0.85, 1.00, and 1.15 emphasized in the main text. | Values below 1.00 impose a resistant-strain transmission penalty; values above 1.00 impose a transmission advantage. |
| Vaccine infectiousness effect, $VE_{inf}$ | 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55 | 0.05 to 0.55 range used for Figure 3E/F surfaces. | $VE_{inf}$ reduces onward infectiousness among infected vaccine-history origins; it is not an infection-acquisition endpoint. |
| Crossed grid | 13 fitness values x 11 $VE_{inf}$ values | 143 simulated combinations retained in repository source table. | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. $VE_{inf}$ is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around $f_R$ = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. $VE_{inf}$ axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |

<div style="page-break-after: always;"></div>

### eTable 12. Fitted age-specific reporting probabilities and prior bounds.

| Country | 0-2 mo | 3-11 mo | 1-9 y | 5-17 y | 18+ y | Prior bounds | Prior evidence class |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | 0.5146 | 0.4288 | 0.1844 | 0.1115 | 0.0343 | 0-2 mo: $p_{rep}=0.6$ $[0.3, 0.75]$<br>3-11 mo: $p_{rep}=0.5$ $[0.25, 0.7]$<br>1-4 y: $p_{rep}=0.25$ $[0.1, 0.5]$<br>5-9 y: $p_{rep}=0.18$ $[0.08, 0.4]$<br>10-17 y: $p_{rep}=0.08$ $[0.04, 0.2]$<br>18-39 y: $p_{rep}=0.05$ $[0.01, 0.12]$<br>40-64 y: $p_{rep}=0.03$ $[0.005, 0.1]$<br>65+ y: $p_{rep}=0.04$ $[0.01, 0.12]$ | Serology proxy |
| Brazil | 0.5779 | 0.4816 | 0.2071 | 0.1253 | 0.0385 | 0-2 mo: $p_{rep}=0.6$ $[0.2, 0.7]$<br>3-11 mo: $p_{rep}=0.5$ $[0.18, 0.65]$<br>1-4 y: $p_{rep}=0.25$ $[0.05, 0.4]$<br>5-9 y: $p_{rep}=0.18$ $[0.04, 0.3]$<br>10-17 y: $p_{rep}=0.08$ $[0.03, 0.15]$<br>18-39 y: $p_{rep}=0.05$ $[0.003, 0.08]$<br>40-64 y: $p_{rep}=0.03$ $[0.003, 0.06]$<br>65+ y: $p_{rep}=0.04$ $[0.003, 0.08]$ | Passive surveillance proxy |
| China | 0.6 | 0.5 | 0.215 | 0.13 | 0.04 | 0-2 mo: $p_{rep}=0.6$ $[0.2, 0.7]$<br>3-11 mo: $p_{rep}=0.5$ $[0.2, 0.65]$<br>1-4 y: $p_{rep}=0.25$ $[0.05, 0.4]$<br>5-9 y: $p_{rep}=0.18$ $[0.04, 0.3]$<br>10-17 y: $p_{rep}=0.08$ $[0.03, 0.15]$<br>18-39 y: $p_{rep}=0.05$ $[0.003, 0.08]$<br>40-64 y: $p_{rep}=0.03$ $[0.003, 0.06]$<br>65+ y: $p_{rep}=0.04$ $[0.003, 0.08]$ | Active surveillance proxy |
| Japan | 0.5961 | 0.4968 | 0.2136 | 0.1291 | 0.0397 | 0-2 mo: $p_{rep}=0.6$ $[0.25, 0.7]$<br>3-11 mo: $p_{rep}=0.5$ $[0.2, 0.65]$<br>1-4 y: $p_{rep}=0.25$ $[0.08, 0.45]$<br>5-9 y: $p_{rep}=0.18$ $[0.06, 0.35]$<br>10-17 y: $p_{rep}=0.08$ $[0.03, 0.15]$<br>18-39 y: $p_{rep}=0.05$ $[0.005, 0.08]$<br>40-64 y: $p_{rep}=0.03$ $[0.005, 0.06]$<br>65+ y: $p_{rep}=0.04$ $[0.005, 0.08]$ | Laboratory surveillance proxy |
| New Zealand | 0.587 | 0.4892 | 0.2104 | 0.1272 | 0.0391 | 0-2 mo: $p_{rep}=0.6$ $[0.3, 0.75]$<br>3-11 mo: $p_{rep}=0.5$ $[0.25, 0.7]$<br>1-4 y: $p_{rep}=0.25$ $[0.1, 0.5]$<br>5-9 y: $p_{rep}=0.18$ $[0.08, 0.4]$<br>10-17 y: $p_{rep}=0.08$ $[0.04, 0.18]$<br>18-39 y: $p_{rep}=0.05$ $[0.01, 0.1]$<br>40-64 y: $p_{rep}=0.03$ $[0.008, 0.08]$<br>65+ y: $p_{rep}=0.04$ $[0.01, 0.1]$ | High income underreporting proxy |
| South Africa | 0.604 | 0.5033 | 0.2164 | 0.1308 | 0.0403 | 0-2 mo: $p_{rep}=0.6$ $[0.2, 0.7]$<br>3-11 mo: $p_{rep}=0.5$ $[0.18, 0.65]$<br>1-4 y: $p_{rep}=0.25$ $[0.05, 0.4]$<br>5-9 y: $p_{rep}=0.18$ $[0.04, 0.3]$<br>10-17 y: $p_{rep}=0.08$ $[0.03, 0.15]$<br>18-39 y: $p_{rep}=0.05$ $[0.003, 0.08]$<br>40-64 y: $p_{rep}=0.03$ $[0.003, 0.06]$<br>65+ y: $p_{rep}=0.04$ $[0.003, 0.08]$ | Passive notification proxy |
| Sweden | 0.6151 | 0.5126 | 0.2204 | 0.1333 | 0.041 | 0-2 mo: $p_{rep}=0.6$ $[0.4, 0.8]$<br>3-11 mo: $p_{rep}=0.5$ $[0.35, 0.75]$<br>1-4 y: $p_{rep}=0.25$ $[0.25, 0.6]$<br>5-9 y: $p_{rep}=0.18$ $[0.144, 0.5]$<br>10-17 y: $p_{rep}=0.08$ $[0.08, 0.25]$<br>18-39 y: $p_{rep}=0.05$ $[0.02, 0.12]$<br>40-64 y: $p_{rep}=0.03$ $[0.015, 0.1]$<br>65+ y: $p_{rep}=0.04$ $[0.02, 0.12]$ | Direct preschool anchor |
| Thailand | 0.6127 | 0.5106 | 0.2196 | 0.1327 | 0.0408 | 0-2 mo: $p_{rep}=0.6$ $[0.2, 0.7]$<br>3-11 mo: $p_{rep}=0.5$ $[0.18, 0.65]$<br>1-4 y: $p_{rep}=0.25$ $[0.05, 0.4]$<br>5-9 y: $p_{rep}=0.18$ $[0.04, 0.3]$<br>10-17 y: $p_{rep}=0.08$ $[0.03, 0.15]$<br>18-39 y: $p_{rep}=0.05$ $[0.003, 0.08]$<br>40-64 y: $p_{rep}=0.03$ $[0.003, 0.06]$<br>65+ y: $p_{rep}=0.04$ $[0.003, 0.08]$ | Passive surveillance proxy |
| United Kingdom | 0.5679 | 0.4733 | 0.2035 | 0.123 | 0.0379 | 0-2 mo: $p_{rep}=0.6$ $[0.3, 0.75]$<br>3-11 mo: $p_{rep}=0.5$ $[0.25, 0.7]$<br>1-4 y: $p_{rep}=0.25$ $[0.1, 0.45]$<br>5-9 y: $p_{rep}=0.18$ $[0.08, 0.35]$<br>10-17 y: $p_{rep}=0.08$ $[0.04, 0.2]$<br>18-39 y: $p_{rep}=0.05$ $[0.005, 0.1]$<br>40-64 y: $p_{rep}=0.03$ $[0.005, 0.08]$<br>65+ y: $p_{rep}=0.04$ $[0.005, 0.1]$ | Notification efficiency low |
| United States | 0.6177 | 0.5147 | 0.2213 | 0.1338 | 0.0412 | 0-2 mo: $p_{rep}=0.6$ $[0.3, 0.75]$<br>3-11 mo: $p_{rep}=0.5$ $[0.25, 0.7]$<br>1-4 y: $p_{rep}=0.25$ $[0.1, 0.5]$<br>5-9 y: $p_{rep}=0.18$ $[0.08, 0.4]$<br>10-17 y: $p_{rep}=0.08$ $[0.04, 0.18]$<br>18-39 y: $p_{rep}=0.05$ $[0.005, 0.1]$<br>40-64 y: $p_{rep}=0.03$ $[0.005, 0.08]$<br>65+ y: $p_{rep}=0.04$ $[0.005, 0.1]$ | Capture recapture proxy |

<div style="page-break-after: always;"></div>

### eTable 13. Macrolide-resistance mechanism decomposition across importation, treatment, PEP, and fitness assumptions.

| Scenario | Importation | Treatment differential | PEP differential | $f_R$ | Median end resistant fraction | IQR end resistant fraction | Median infant cases per 100k | Median resistant infections per 100k | Interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Full baseline mechanism | Yes | Yes | Yes | 1.000 | 0.9965 | 0.2815-0.9986 | 357.53 | 596.21 | Full baseline mechanism: country anchor, resistant importation, strain-specific treatment and PEP, neutral fitness. |
| No resistant importation | No | Yes | Yes | 1.000 | 0.9795 | 0.2463-0.9976 | 352.84 | 579.92 | Tests dependence on ongoing resistant-strain importation after the analysis-start anchor. |
| Equal treatment effect | Yes | No | Yes | 1.000 | 0.995 | 0.0586-0.9985 | 327.98 | 525.11 | Tests treatment-mediated selection by making resistant treatment effects equal to sensitive-strain effects. |
| Equal PEP effect | Yes | Yes | No | 1.000 | 0.1224 | 0.04585-0.3797 | 276.63 | 28.44 | Tests PEP-mediated selection by making resistant PEP effectiveness equal to sensitive-strain PEP effectiveness. |
| No treatment or PEP differential | Yes | No | No | 1.000 | 0.01 | 0.01-0.03725 | 266.87 | 5.879 | Tests neutral strain competition under importation when treatment and PEP do not favor resistant strains. |
| Fitness-cost stress test | Yes | Yes | Yes | 0.85 | 0.0001373 | 1.909e-05-0.0005749 | 246.81 | 0.1656 | Fitness-cost stress test retaining baseline importation and management assumptions. |

<div style="page-break-after: always;"></div>

### eTable 14. Vaccine infectiousness-effect threshold diagnostics.

| Threshold type | Fitness or comparator | Resistance prevalence | Target or comparator basis | Minimum $VE_{inf}$ | Countries | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Reduction target | $f_R$=0.85 |  | 25% | 0.4 | 6/10 | Threshold reached on the simulated $VE_{inf}$ grid. |
| Reduction target | $f_R$=0.85 |  | 50% | 0.5 | 5/10 | Threshold reached on the simulated $VE_{inf}$ grid. |
| Reduction target | $f_R$=0.85 |  | 75% | Not reached through 0.55 | 4/10 | Threshold not reached on the simulated grid. |
| Reduction target | $f_R$=1.00 |  | 25% | 0.4 | 6/10 | Threshold reached on the simulated $VE_{inf}$ grid. |
| Reduction target | $f_R$=1.00 |  | 50% | 0.55 | 6/10 | Threshold reached on the simulated $VE_{inf}$ grid. |
| Reduction target | $f_R$=1.00 |  | 75% | Not reached through 0.55 | 4/10 | Threshold not reached on the simulated grid. |
| Reduction target | $f_R$=1.10 |  | 25% | 0.5 | 7/10 | Threshold reached on the simulated $VE_{inf}$ grid. |
| Reduction target | $f_R$=1.10 |  | 50% | Not reached through 0.55 | 4/10 | Threshold not reached on the simulated grid. |
| Reduction target | $f_R$=1.10 |  | 75% | Not reached through 0.55 | 1/10 | Threshold not reached on the simulated grid. |
| Reduction target | $f_R$=1.15 |  | 25% | 0.55 | 8/10 | Threshold reached on the simulated $VE_{inf}$ grid. |
| Reduction target | $f_R$=1.15 |  | 50% | Not reached through 0.55 | 2/10 | Threshold not reached on the simulated grid. |
| Reduction target | $f_R$=1.15 |  | 75% | Not reached through 0.55 | 1/10 | Threshold not reached on the simulated grid. |
| Comparator threshold | Pregnancy Tdap plus adult-household package | 0 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.4 | 10/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Resistance-guided treatment | 0 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.35 | 10/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Pregnancy Tdap plus adult-household package | 0.5 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.5 | 8/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Resistance-guided treatment | 0.5 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.45 | 8/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Pregnancy Tdap plus adult-household package | 1.000 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.5 | 8/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | Resistance-guided treatment | 1.000 | $VE_{inf}$-only grid; $VE_{sus}$ and $VE_{dur}$ held at the grid baseline. | 0.4 | 7/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | 25% reduction vs $VE_{inf}$ 0.20 | 0.5 | Cross-country median reduction on the $VE_{inf}$-only grid at 50% starting resistance prevalence. | 0.4 | 6/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | 50% reduction vs $VE_{inf}$ 0.20 | 0.5 | Cross-country median reduction on the $VE_{inf}$-only grid at 50% starting resistance prevalence. | 0.5 | 6/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |
| Comparator threshold | 75% reduction vs $VE_{inf}$ 0.20 | 0.5 | Cross-country median reduction on the $VE_{inf}$-only grid at 50% starting resistance prevalence. | Not reached | 0/10 | Median minimum $VE_{inf}$ needed to meet or exceed the comparator across evaluated countries. |

<div style="page-break-after: always;"></div>

### eTable 15. Intervention outcome summaries by country and strategy.

| Country | Strategy | Total infections | Reported cases | Infant cases | Resistant infections | Infant-case reduction | Infection reduction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | Adolescent booster | 23,966,521 | 397,164 | 186,348 | 22,458,656 | -0.0001914 | -0.0002518 |
| Australia | Combined strategy | 16,819,690 | 230,225 | 80,243.9 | 3,956,132 | 0.5693 | 0.298 |
| Australia | Current practice | 23,960,487 | 397,054 | 186,312 | 22,453,721 | 0 | 0 |
| Australia | Higher child coverage | 23,969,487 | 400,507 | 194,249 | 22,464,802 | -0.0426 | -0.0003756 |
| Australia | Maternal/adult boosting only | 23,752,319 | 389,293 | 183,271 | 22,386,251 | 0.01633 | 0.008688 |
| Australia | Cocooning only | 23,928,385 | 392,694 | 177,935 | 22,415,235 | 0.04496 | 0.00134 |
| Australia | Direct maternal antibody only | 23,921,316 | 390,399 | 181,234 | 22,410,926 | 0.02726 | 0.001635 |
| Australia | Maternal-household composite proxy | 23,675,597 | 378,359 | 170,242 | 22,296,023 | 0.08625 | 0.01189 |
| Australia | Upper-bound vaccine | 15,821,824 | 218,042 | 85,197.1 | 14,464,045 | 0.5427 | 0.3397 |
| Australia | Resistance-guided treatment | 22,500,651 | 355,791 | 154,493 | 9,225,083 | 0.1708 | 0.06093 |
| Brazil | Adolescent booster | 602,744 | 9,296.8 | 2,382.8 | 8,589.8 | 0.7865 | 0.789 |
| Brazil | Combined strategy | 42,932.9 | 644.45 | 163.62 | 381.27 | 0.9853 | 0.985 |
| Brazil | Current practice | 2,857,035 | 45,073.3 | 11,159.7 | 128,561 | 0 | 0 |
| Brazil | Higher child coverage | 3,325,917 | 52,941.1 | 13,283.2 | 183,035 | -0.1903 | -0.1641 |
| Brazil | Maternal/adult boosting only | 453,364 | 7,039.6 | 1,781.8 | 5,934.5 | 0.8403 | 0.8413 |
| Brazil | Cocooning only | 2,663,557 | 41,675.6 | 9,784.0 | 109,399 | 0.1233 | 0.06772 |
| Brazil | Direct maternal antibody only | 2,842,793 | 44,347.1 | 10,658.5 | 126,560 | 0.04492 | 0.004985 |
| Brazil | Maternal-household composite proxy | 434,651 | 6,625.0 | 1,550.9 | 5,616.2 | 0.861 | 0.8479 |
| Brazil | Upper-bound vaccine | 47,709.8 | 714.95 | 191.94 | 494.46 | 0.9828 | 0.9833 |
| Brazil | Resistance-guided treatment | 1,210,080 | 19,025.8 | 4,683.1 | 4,247.5 | 0.5804 | 0.5765 |
| China | Adolescent booster | 125,333,079 | 5,112,085 | 440,662 | 125,292,573 | 0.2269 | 0.2506 |
| China | Combined strategy | 541,572 | 20,907.4 | 1,534.5 | 539,655 | 0.9973 | 0.9968 |
| China | Current practice | 167,252,431 | 6,968,485 | 569,958 | 167,206,617 | 0 | 0 |
| China | Higher child coverage | 169,414,032 | 7,091,320 | 591,164 | 169,368,342 | -0.03721 | -0.01292 |
| China | Maternal/adult boosting only | 96,534,368 | 3,909,680 | 329,167 | 96,493,659 | 0.4225 | 0.4228 |
| China | Cocooning only | 165,002,765 | 6,844,513 | 531,593 | 164,956,882 | 0.06731 | 0.01345 |
| China | Direct maternal antibody only | 165,714,985 | 6,832,177 | 517,132 | 165,668,810 | 0.09268 | 0.009192 |
| China | Maternal-household composite proxy | 94,088,008 | 3,755,399 | 278,730 | 94,046,982 | 0.511 | 0.4374 |
| China | Upper-bound vaccine | 1,058,437 | 41,111.8 | 3,262.6 | 1,055,470 | 0.9943 | 0.9937 |
| China | Resistance-guided treatment | 88,167,876 | 3,653,709 | 289,133 | 66,058,860 | 0.4927 | 0.4728 |
| Japan | Adolescent booster | 26,399,997 | 409,534 | 79,542.6 | 26,073,173 | 0.03913 | 0.04126 |
| Japan | Combined strategy | 247,708 | 3,421.3 | 519.53 | 175,260 | 0.9937 | 0.991 |
| Japan | Current practice | 27,536,156 | 432,979 | 82,781.9 | 27,192,104 | 0 | 0 |
| Japan | Higher child coverage | 27,628,577 | 436,429 | 84,440.8 | 27,284,667 | -0.02004 | -0.003356 |
| Japan | Maternal/adult boosting only | 20,696,340 | 313,174 | 60,339.6 | 20,381,993 | 0.2711 | 0.2484 |
| Japan | Cocooning only | 27,463,590 | 428,556 | 77,752.8 | 27,118,247 | 0.06075 | 0.002635 |
| Japan | Direct maternal antibody only | 27,518,668 | 425,353 | 75,148.1 | 27,171,172 | 0.09222 | 0.0006351 |
| Japan | Maternal-household composite proxy | 20,586,368 | 304,114 | 51,504.0 | 20,267,630 | 0.3778 | 0.2524 |
| Japan | Upper-bound vaccine | 6,518,699 | 94,532.0 | 16,498.5 | 6,305,542 | 0.8007 | 0.7633 |
| Japan | Resistance-guided treatment | 19,934,392 | 309,054 | 56,462.7 | 10,455,748 | 0.3179 | 0.2761 |
| New Zealand | Adolescent booster | 3,334,593 | 51,174.2 | 21,601.2 | 2,965,841 | -0.002802 | -0.002214 |
| New Zealand | Combined strategy | 1,713,367 | 22,245.3 | 7,212.9 | 10,597.5 | 0.6652 | 0.485 |
| New Zealand | Current practice | 3,327,226 | 51,036.0 | 21,540.8 | 2,957,054 | 0 | 0 |
| New Zealand | Higher child coverage | 3,343,223 | 51,731.3 | 22,261.5 | 2,975,962 | -0.03346 | -0.004808 |
| New Zealand | Maternal/adult boosting only | 3,201,603 | 48,192.4 | 20,352.9 | 2,836,850 | 0.05515 | 0.03776 |
| New Zealand | Cocooning only | 3,320,009 | 50,484.9 | 20,550.3 | 2,948,114 | 0.04598 | 0.002169 |
| New Zealand | Direct maternal antibody only | 3,314,905 | 49,906.4 | 20,441.7 | 2,941,450 | 0.05103 | 0.003703 |
| New Zealand | Maternal-household composite proxy | 3,182,267 | 46,631.1 | 18,456.0 | 2,812,645 | 0.1432 | 0.04357 |
| New Zealand | Upper-bound vaccine | 1,588,469 | 20,199.6 | 7,460.0 | 1,268,591 | 0.6537 | 0.5226 |
| New Zealand | Resistance-guided treatment | 2,882,501 | 42,854.9 | 17,072.9 | 66,174.2 | 0.2074 | 0.1337 |
| South Africa | Adolescent booster | 304,956 | 4,608.9 | 1,737.1 | 11,965.4 | 0.8688 | 0.8709 |
| South Africa | Combined strategy | 12,223.6 | 172.61 | 56.79 | 216.21 | 0.9957 | 0.9948 |
| South Africa | Current practice | 2,361,482 | 36,341.1 | 13,237.2 | 844,078 | 0 | 0 |
| South Africa | Higher child coverage | 1,313,792 | 19,283.9 | 6,802.9 | 215,179 | 0.4861 | 0.4437 |
| South Africa | Maternal/adult boosting only | 683,010 | 10,458.8 | 3,825.7 | 57,452.6 | 0.711 | 0.7108 |
| South Africa | Cocooning only | 2,214,782 | 33,793.9 | 11,734.1 | 731,193 | 0.1135 | 0.06212 |
| South Africa | Direct maternal antibody only | 1,689,770 | 24,912.2 | 7,897.8 | 389,794 | 0.4034 | 0.2844 |
| South Africa | Maternal-household composite proxy | 399,182 | 5,806.8 | 1,767.6 | 19,276.7 | 0.8665 | 0.831 |
| South Africa | Upper-bound vaccine | 12,739.7 | 196.51 | 80.65 | 264.63 | 0.9939 | 0.9946 |
| South Africa | Resistance-guided treatment | 1,033,314 | 15,928.9 | 5,765.3 | 4,075.0 | 0.5645 | 0.5624 |
| Sweden | Adolescent booster | 2,458,582 | 35,587.6 | 10,274.6 | 1,905,995 | -0.0004908 | -0.0005024 |
| Sweden | Combined strategy | 11,458.1 | 148.62 | 36.75 | 80.59 | 0.9964 | 0.9953 |
| Sweden | Current practice | 2,457,347 | 35,566.8 | 10,269.6 | 1,904,828 | 0 | 0 |
| Sweden | Higher child coverage | 2,452,571 | 35,670.5 | 10,741.0 | 1,901,571 | -0.0459 | 0.001944 |
| Sweden | Maternal/adult boosting only | 2,066,577 | 29,410.7 | 8,536.2 | 1,532,947 | 0.1688 | 0.159 |
| Sweden | Cocooning only | 2,436,397 | 34,979.1 | 9,651.6 | 1,882,021 | 0.06018 | 0.008526 |
| Sweden | Direct maternal antibody only | 2,405,170 | 34,260.8 | 9,780.1 | 1,848,623 | 0.04767 | 0.02123 |
| Sweden | Maternal-household composite proxy | 2,005,662 | 27,869.8 | 7,654.4 | 1,466,276 | 0.2547 | 0.1838 |
| Sweden | Upper-bound vaccine | 4,890.7 | 63.17 | 17.94 | 51.74 | 0.9983 | 0.998 |
| Sweden | Resistance-guided treatment | 1,867,828 | 26,633.5 | 7,389.1 | 4,134.3 | 0.2805 | 0.2399 |
| Thailand | Adolescent booster | 182,096 | 2,587.7 | 599.04 | 2,363.7 | 0.7036 | 0.7089 |
| Thailand | Combined strategy | 16,855.0 | 229.81 | 48.73 | 149.92 | 0.9759 | 0.9731 |
| Thailand | Current practice | 625,451 | 9,062.5 | 2,021.2 | 15,328.2 | 0 | 0 |
| Thailand | Higher child coverage | 685,944 | 9,996.4 | 2,197.0 | 18,360.6 | -0.08695 | -0.09672 |
| Thailand | Maternal/adult boosting only | 126,845 | 1,807.7 | 417.02 | 1,522.2 | 0.7937 | 0.7972 |
| Thailand | Cocooning only | 591,099 | 8,502.0 | 1,800.3 | 13,773.1 | 0.1093 | 0.05492 |
| Thailand | Direct maternal antibody only | 598,599 | 8,522.3 | 1,720.6 | 14,068.4 | 0.1487 | 0.04293 |
| Thailand | Maternal-household composite proxy | 121,082 | 1,684.4 | 335.57 | 1,439.4 | 0.834 | 0.8064 |
| Thailand | Upper-bound vaccine | 21,247.2 | 293.52 | 71.03 | 220.87 | 0.9649 | 0.966 |
| Thailand | Resistance-guided treatment | 302,678 | 4,379.0 | 974.15 | 1,332.4 | 0.518 | 0.5161 |
| United Kingdom | Adolescent booster | 35,175,230 | 489,998 | 223,761 | 30,048,902 | -0.007313 | -0.00667 |
| United Kingdom | Combined strategy | 11,306,692 | 130,677 | 45,485.5 | 7,606.3 | 0.7952 | 0.6764 |
| United Kingdom | Current practice | 34,942,169 | 486,414 | 222,136 | 29,651,102 | 0 | 0 |
| United Kingdom | Higher child coverage | 35,350,285 | 496,881 | 231,280 | 30,100,290 | -0.04116 | -0.01168 |
| United Kingdom | Maternal/adult boosting only | 31,197,678 | 420,247 | 191,570 | 26,014,469 | 0.1376 | 0.1072 |
| United Kingdom | Cocooning only | 34,780,242 | 479,260 | 209,400 | 29,459,946 | 0.05734 | 0.004634 |
| United Kingdom | Direct maternal antibody only | 34,711,709 | 474,328 | 209,826 | 29,354,770 | 0.05542 | 0.006595 |
| United Kingdom | Maternal-household composite proxy | 31,000,823 | 406,275 | 171,971 | 25,731,086 | 0.2258 | 0.1128 |
| United Kingdom | Upper-bound vaccine | 16,464,932 | 195,408 | 76,400.9 | 11,599,814 | 0.6561 | 0.5288 |
| United Kingdom | Resistance-guided treatment | 29,633,756 | 402,359 | 173,156 | 63,958.3 | 0.2205 | 0.1519 |
| United States | Adolescent booster | 7,661,499 | 121,587 | 30,005.2 | 0 | -0.03269 | -0.03275 |
| United States | Combined strategy | 82,443.1 | 1,270.3 | 311.49 | 0 | 0.9893 | 0.9889 |
| United States | Current practice | 7,418,543 | 117,715 | 29,055.4 | 0 | 0 | 0 |
| United States | Higher child coverage | 7,408,709 | 118,230 | 30,437.2 | 0 | -0.04756 | 0.001326 |
| United States | Maternal/adult boosting only | 2,427,768 | 38,088.6 | 9,481.6 | 0 | 0.6737 | 0.6727 |
| United States | Cocooning only | 7,088,890 | 111,562 | 26,177.4 | 0 | 0.09905 | 0.04444 |
| United States | Direct maternal antibody only | 6,756,544 | 105,618 | 25,791.3 | 0 | 0.1123 | 0.08924 |
| United States | Maternal-household composite proxy | 2,173,244 | 33,360.2 | 7,819.6 | 0 | 0.7309 | 0.7071 |
| United States | Upper-bound vaccine | 56,444.5 | 868.80 | 243.84 | 0 | 0.9916 | 0.9924 |
| United States | Resistance-guided treatment | 3,646,165 | 57,613.2 | 14,132.4 | 0 | 0.5136 | 0.5085 |

<div style="page-break-after: always;"></div>

### eTable 16. Near-term implementation sensitivity for resistance-guided treatment and resistant-strain PEP assumptions.

| Scenario | Guided-treatment uptake | PEP restored | PEP reach multiplier | Median infant-case reduction vs current, 5 y | IQR reduction | Countries with positive reduction | Median infant cases per 100k | Implementation note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Current near-term practice | 0 | Baseline | 1.000 | 0 | 0-0 | 0 | 170.55 | Current macrolide treatment and baseline resistant-strain PEP effectiveness. |
| 25% guided treatment; PEP restored | 0.25 | Yes | 1.000 | -0.1105 | -0.2084-0.1932 | 4 | 204.44 | Quarter uptake of resistance-guided treatment with partial restoration of resistant-strain PEP effectiveness. |
| 50% guided treatment; PEP restored | 0.5 | Yes | 1.000 | -0.1644 | -0.3524-0.3033 | 4 | 226.84 | Half uptake of resistance-guided treatment with partial restoration of resistant-strain PEP effectiveness. |
| 75% guided treatment; PEP restored | 0.75 | Yes | 1.000 | -0.008818 | -0.6458-0.3988 | 5 | 217.75 | Three-quarter uptake of resistance-guided treatment with partial restoration of resistant-strain PEP effectiveness. |
| 100% guided treatment; PEP restored | 1.000 | Yes | 1.000 | 0.1617 | -0.6767-0.498 | 6 | 204.12 | Full resistance-guided treatment scenario used in the main analysis. |
| 50% guided treatment; no PEP restoration | 0.5 | No | 1.000 | 0.2672 | 0.01423-0.3278 | 8 | 166.62 | Half uptake of resistance-guided treatment; resistant-strain PEP effectiveness remains at baseline. |
| 100% guided treatment; no PEP restoration | 1.000 | No | 1.000 | 0.4764 | -0.3338-0.5007 | 6 | 169.13 | Full treatment restoration but no restoration of resistant-strain PEP effectiveness. |
| 50% guided treatment; low PEP reach | 0.5 | Yes | 0.5 | 0.1502 | -0.2308-0.2723 | 7 | 193.74 | Half uptake and half baseline PEP reach, approximating delayed activation, lower adherence, or household-only reach. |

<div style="page-break-after: always;"></div>

### eTable 17. Infant-contact and maternal passive-protection sensitivity diagnostics.

| Sensitivity dimension | Strategy | Setting | Median infant cases per 100k, 5 y | IQR infant cases per 100k, 5 y | Median infant-case reduction vs current, 5 y | IQR reduction | Countries with positive reduction | Countries | Interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Infant contact multiplier | Current practice | 0.75 | 145.76 | 31.54-453.9 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Current practice | 1.000 | 170.55 | 38.93-525.8 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Current practice | 1.250 | 198.33 | 47.55-589 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Current practice | 1.500 | 228.29 | 57.08-642.8 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Maternal-household composite proxy | 0.75 | 93.37 | 6.945-311.5 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Maternal-household composite proxy | 1.000 | 108.18 | 8.928-354.8 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Maternal-household composite proxy | 1.250 | 121.51 | 11.54-397.1 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Infant contact multiplier | Maternal-household composite proxy | 1.500 | 138.47 | 14.86-442.4 |  |  |  | 10 | Multiplier applied to contact-matrix entries from child/adolescent/adult sources into infant target age groups. |
| Maternal passive-protection duration | Current practice | 90.00 | 141.57 | 37.86-444.7 | 0 | 0-0 | 0 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Direct maternal antibody only | 90.00 | 138.54 | 34.17-434.9 | 0.02741 | 0.007277-0.05927 | 8 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Maternal-household composite proxy | 90.00 | 64.77 | 8.731-339.5 | 0.5508 | 0.2189-0.8074 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Current practice | 180.00 | 140.65 | 37.49-440.3 | 0 | 0-0 | 0 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Direct maternal antibody only | 180.00 | 134.82 | 33.02-424.3 | 0.03965 | 0.02199-0.0903 | 9 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Maternal-household composite proxy | 180.00 | 63.45 | 8.382-331.5 | 0.5615 | 0.2273-0.8138 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Current practice | 270.00 | 140.14 | 37.36-438.4 | 0 | 0-0 | 0 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Direct maternal antibody only | 270.00 | 133.68 | 32.55-419.8 | 0.04332 | 0.02527-0.1017 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |
| Maternal passive-protection duration | Maternal-household composite proxy | 270.00 | 62.39 | 8.24-327.8 | 0.5684 | 0.2299-0.8169 | 10 | 10 | Near-term sensitivity varying passive maternal antibody duration while holding adult boosting and cocooning assumptions fixed within each strategy. |

<div style="page-break-after: always;"></div>

### eTable 18. Higher child-coverage mechanism diagnostics.

| Diagnostic | Country, age group, or scenario | Current infant cases per 100k | Higher child coverage infant cases per 100k | Relative change or share | Largest increase age group | Age-shift IQR | Countries | Interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Country infant-burden change | Australia | 2,574.2 | 2,679.1 | -0.04073 | 1-4 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | Brazil | 21.13 | 24.92 | -0.1792 | 18-39 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | China | 293.87 | 302.70 | -0.03006 | 40-64 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | Japan | 450.16 | 458.70 | -0.01897 | 40-64 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | New Zealand | 1,532.8 | 1,581.9 | -0.03204 | 18-39 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | South Africa | 47.80 | 24.54 | 0.4866 | 0-2 mo |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | Sweden | 421.19 | 439.26 | -0.04289 | 3-11 mo |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | Thailand | 17.11 | 18.45 | -0.07779 | 40-64 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | United Kingdom | 1,272.2 | 1,325.0 | -0.04154 | 18-39 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Country infant-burden change | United States | 31.34 | 32.88 | -0.04941 | 18-39 y |  |  | Country-level infant burden and the age group with the largest absolute infection increase. |
| Age-shift summary | Adolescent 10 17y |  |  | 0.003558 |  | -0.0001746961008806697 to 0.010222033416694398 | 7 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 1-4 y |  |  | 0.006543 |  | 0.00216402192036349 to 0.015322963762981666 | 8 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 5-9 y |  |  | 0.007231 |  | -0.0005767906806657898 to 0.015632290947234104 | 7 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 65+ y |  |  | 0.003104 |  | -0.0011240230048287928 to 0.011640356904092736 | 7 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 0-2 mo |  |  | 0.006604 |  | 0.003211274398845873 to 0.015510574715927835 | 8 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 3-11 mo |  |  | 0.01129 |  | 0.007227388067308576 to 0.018953505701585476 | 9 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 40-64 y |  |  | 0.003289 |  | 0.0004182267264622534 to 0.01126762162125282 | 7 | Median age-specific infection change under higher child coverage. |
| Age-shift summary | 18-39 y |  |  | 0.00392 |  | 0.0006700876497788416 to 0.01084582760566662 | 8 | Median age-specific infection change under higher child coverage. |
| Vaccine-history origin share | Current practice |  |  | 0.4634 |  |  | 10 | Median vaccinated-origin infant infection share; source CSV retains dose-specific shares. |
| Vaccine-history origin share | Higher child coverage |  |  | 0.4324 |  |  | 10 | Median vaccinated-origin infant infection share; source CSV retains dose-specific shares. |

<div style="page-break-after: always;"></div>

### eTable 19. Intervention scenario-ordering sensitivity to analysis-window choice.

| Analysis window | Scenario | Median order position | Countries ordered first | Median infant-case reduction |
| --- | --- | --- | --- | --- |
| 2025-2029 | Combined strategy | 1.000 | 6 | 0.9896 |
| 2025-2029 | Upper-bound vaccine | 2.000 | 3 | 0.98 |
| 2025-2029 | Maternal-household composite proxy | 3.000 | 0 | 0.5755 |
| 2025-2029 | Adolescent booster | 4.000 | 1 | 0.2179 |
| 2025-2029 | Resistance-guided treatment | 5.000 | 0 | 0.1595 |
| 2025-2029 | Current practice | 6.000 | 0 | 0 |
| 2025-2029 | Higher child coverage | 6.000 | 0 | -0.04399 |
| 2025-2034 | Combined strategy | 1.000 | 8 | 0.9886 |
| 2025-2034 | Upper-bound vaccine | 2.000 | 2 | 0.9784 |
| 2025-2034 | Maternal-household composite proxy | 3.500 | 0 | 0.4949 |
| 2025-2034 | Resistance-guided treatment | 4.000 | 0 | 0.4366 |
| 2025-2034 | Adolescent booster | 5.000 | 0 | 0.03761 |
| 2025-2034 | Current practice | 6.000 | 0 | 0 |
| 2025-2034 | Higher child coverage | 7.000 | 0 | -0.04215 |
| 2025-2039 | Combined strategy | 1.000 | 8 | 0.9879 |
| 2025-2039 | Upper-bound vaccine | 2.000 | 2 | 0.977 |
| 2025-2039 | Maternal-household composite proxy | 3.500 | 0 | 0.4143 |
| 2025-2039 | Resistance-guided treatment | 4.000 | 0 | 0.3894 |
| 2025-2039 | Adolescent booster | 5.000 | 0 | 0.008864 |
| 2025-2039 | Current practice | 6.000 | 0 | 0 |
| 2025-2039 | Higher child coverage | 7.000 | 0 | -0.04422 |
| 2025-2050 full horizon | Combined strategy | 1.000 | 8 | 0.9873 |
| 2025-2050 full horizon | Upper-bound vaccine | 2.000 | 2 | 0.975 |
| 2025-2050 full horizon | Maternal-household composite proxy | 3.500 | 0 | 0.4313 |
| 2025-2050 full horizon | Resistance-guided treatment | 4.000 | 0 | 0.4073 |
| 2025-2050 full horizon | Adolescent booster | 5.000 | 0 | 0.0186 |
| 2025-2050 full horizon | Current practice | 6.000 | 0 | 0 |
| 2025-2050 full horizon | Higher child coverage | 7.000 | 0 | -0.04114 |
| 2030-2050 excluding initial transient | Combined strategy | 1.000 | 8 | 0.9866 |
| 2030-2050 excluding initial transient | Upper-bound vaccine | 2.000 | 2 | 0.9734 |
| 2030-2050 excluding initial transient | Resistance-guided treatment | 3.000 | 0 | 0.4322 |
| 2030-2050 excluding initial transient | Maternal-household composite proxy | 4.000 | 0 | 0.3814 |
| 2030-2050 excluding initial transient | Adolescent booster | 5.500 | 0 | 0.001001 |
| 2030-2050 excluding initial transient | Current practice | 5.500 | 0 | 0 |
| 2030-2050 excluding initial transient | Higher child coverage | 7.000 | 0 | -0.0359 |

<div style="page-break-after: always;"></div>

### eTable 20. Cross-diagnostic intervention scenario-ordering stability across countries, analysis windows, and infant age strata.

| Scenario | Full-horizon median order position | Countries ordered first | Countries ordered top 2 | Window cells ordered first | Window cells ordered top 2 | Age-window cells ordered first | Age-window cells ordered top 2 | Age-window cells with reduction | Median age-window reduction | Interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combined strategy | 1.000 | 8 | 10 | 38 | 48 | 78 | 97 | 98 | 0.9886 | Most stable lowest-burden scenario across country, horizon, and infant-age diagnostics. |
| Upper-bound vaccine | 2.000 | 2 | 10 | 11 | 49 | 19 | 95 | 98 | 0.9776 | Often near the lowest modeled burden, but not consistently ordered first. |
| Maternal-household composite proxy | 3.500 | 0 | 0 | 0 | 1 | 1 | 4 | 94 | 0.525 | Usually lower burden than current practice, but ordering is horizon- and age-stratum-dependent. |
| Adolescent booster | 5.000 | 0 | 0 | 1 | 1 | 1 | 2 | 70 | 0.02718 | Usually lower burden than current practice, but ordering is horizon- and age-stratum-dependent. |
| Higher child coverage | 7.000 | 0 | 0 | 0 | 0 | 1 | 1 | 20 | -0.04004 | Low-benefit or unstable scenario in these deterministic diagnostics. |
| Current practice | 6.000 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | Low-benefit or unstable scenario in these deterministic diagnostics. |
| Resistance-guided treatment | 4.000 | 0 | 0 | 0 | 0 | 0 | 0 | 92 | 0.3898 | Usually lower burden than current practice, but ordering is horizon- and age-stratum-dependent. |

<div style="page-break-after: always;"></div>

### eTable 21. Near-term temporal assumption sensitivity for burn-in duration and COVID-19 NPI contact-shock assumptions.

| Temporal dimension | Scenario | Countries | Burn-in years | NPI reduction scale | Median infant cases per 100k, 5 y | IQR infant cases per 100k, 5 y | Median all infections per 100k, 5 y | Median end resistant fraction, 5 y | Implementation note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Burn-in | Burnin 10y | 10 | 10.00 | 1.000 | 52.11 | 33.67-983.2 | 135.77 | 0.3913 | Near-term current-practice run varying pre-analysis burn-in duration. |
| Burn-in | Burnin 15y | 10 | 15.00 | 1.000 | 170.55 | 38.93-525.8 | 354.02 | 0.1046 | Near-term current-practice run varying pre-analysis burn-in duration. |
| Burn-in | Burnin 30y | 10 | 30.00 | 1.000 | 336.36 | 33.89-737.3 | 659.21 | 0.1623 | Near-term current-practice run varying pre-analysis burn-in duration. |
| NPI contact shock | NPI country profile | 1 | 15.00 | 1.000 | 547.24 | 547.2-547.2 | 680.06 | 0.4448 | Near-term current-practice run varying COVID-19 NPI contact-reduction assumptions for countries with explicit NPI periods. |
| NPI contact shock | Half NPI contact shock | 1 | 15.00 | 0.5 | 228.62 | 228.6-228.6 | 297.34 | 0.1921 | Near-term current-practice run varying COVID-19 NPI contact-reduction assumptions for countries with explicit NPI periods. |
| NPI contact shock | No NPI contact shock | 1 | 15.00 |  | 2,996.5 | 2997-2997 | 3,855.4 | 0.9876 | Near-term current-practice run varying COVID-19 NPI contact-reduction assumptions for countries with explicit NPI periods. |

<div style="page-break-after: always;"></div>

### eTable 22. Infant age-stratified intervention outcomes summarized by analysis window.

| Analysis window | Infant age stratum | Scenario | Median infant cases per 100k/y | Median infant-case reduction | Median order position | Countries with positive reduction | Countries |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-2029 | 0-2 mo | Adolescent booster | 216.76 | 0.2182 | 4.000 | 8 | 10 |
| 2025-2029 | 0-2 mo | Combined strategy | 1.221 | 0.9917 | 1.000 | 9 | 10 |
| 2025-2029 | 0-2 mo | Current practice | 251.75 | 0 | 6.000 | 0 | 10 |
| 2025-2029 | 0-2 mo | Higher child coverage | 243.44 | -0.04206 | 6.000 | 4 | 10 |
| 2025-2029 | 0-2 mo | Maternal-household composite proxy | 116.94 | 0.6939 | 3.000 | 9 | 10 |
| 2025-2029 | 0-2 mo | Upper-bound vaccine | 1.860 | 0.9784 | 2.000 | 9 | 10 |
| 2025-2029 | 0-2 mo | Resistance-guided treatment | 300.27 | 0.1612 | 5.000 | 6 | 10 |
| 2025-2029 | 3-11 mo | Adolescent booster | 131.36 | 0.2177 | 4.000 | 8 | 10 |
| 2025-2029 | 3-11 mo | Combined strategy | 1.059 | 0.9889 | 1.000 | 9 | 10 |
| 2025-2029 | 3-11 mo | Current practice | 151.05 | 0 | 6.000 | 0 | 10 |
| 2025-2029 | 3-11 mo | Higher child coverage | 153.54 | -0.0493 | 6.000 | 2 | 10 |
| 2025-2029 | 3-11 mo | Maternal-household composite proxy | 104.51 | 0.5289 | 3.000 | 9 | 10 |
| 2025-2029 | 3-11 mo | Upper-bound vaccine | 0.9514 | 0.9807 | 2.000 | 9 | 10 |
| 2025-2029 | 3-11 mo | Resistance-guided treatment | 181.55 | 0.1588 | 5.000 | 6 | 10 |
| 2025-2034 | 0-2 mo | Adolescent booster | 338.57 | 0.03816 | 5.000 | 8 | 10 |
| 2025-2034 | 0-2 mo | Combined strategy | 1.239 | 0.9909 | 1.000 | 10 | 10 |
| 2025-2034 | 0-2 mo | Current practice | 511.04 | 0 | 6.000 | 0 | 10 |
| 2025-2034 | 0-2 mo | Higher child coverage | 510.72 | -0.007092 | 7.000 | 3 | 10 |
| 2025-2034 | 0-2 mo | Maternal-household composite proxy | 185.76 | 0.6438 | 3.000 | 10 | 10 |
| 2025-2034 | 0-2 mo | Upper-bound vaccine | 1.878 | 0.9766 | 2.000 | 10 | 10 |
| 2025-2034 | 0-2 mo | Resistance-guided treatment | 313.02 | 0.4392 | 4.000 | 10 | 10 |
| 2025-2034 | 3-11 mo | Adolescent booster | 203.80 | 0.03738 | 5.000 | 8 | 10 |
| 2025-2034 | 3-11 mo | Combined strategy | 1.075 | 0.9878 | 1.000 | 10 | 10 |
| 2025-2034 | 3-11 mo | Current practice | 299.73 | 0 | 6.000 | 0 | 10 |
| 2025-2034 | 3-11 mo | Higher child coverage | 312.64 | -0.0576 | 7.000 | 1 | 10 |
| 2025-2034 | 3-11 mo | Maternal-household composite proxy | 165.79 | 0.4349 | 4.000 | 9 | 10 |
| 2025-2034 | 3-11 mo | Upper-bound vaccine | 0.9606 | 0.979 | 2.000 | 10 | 10 |
| 2025-2034 | 3-11 mo | Resistance-guided treatment | 189.16 | 0.4356 | 3.500 | 10 | 10 |
| 2025-2039 | 0-2 mo | Adolescent booster | 477.00 | 0.009437 | 5.000 | 7 | 10 |
| 2025-2039 | 0-2 mo | Combined strategy | 1.260 | 0.9904 | 1.000 | 10 | 10 |
| 2025-2039 | 0-2 mo | Current practice | 575.77 | 0 | 6.000 | 0 | 10 |
| 2025-2039 | 0-2 mo | Higher child coverage | 578.45 | -0.01509 | 7.000 | 2 | 10 |
| 2025-2039 | 0-2 mo | Maternal-household composite proxy | 250.02 | 0.5869 | 3.000 | 10 | 10 |
| 2025-2039 | 0-2 mo | Upper-bound vaccine | 1.932 | 0.9751 | 2.000 | 10 | 10 |
| 2025-2039 | 0-2 mo | Resistance-guided treatment | 316.40 | 0.3909 | 4.000 | 10 | 10 |
| 2025-2039 | 3-11 mo | Adolescent booster | 273.74 | 0.008629 | 5.000 | 7 | 10 |
| 2025-2039 | 3-11 mo | Combined strategy | 1.094 | 0.9871 | 1.000 | 10 | 10 |
| 2025-2039 | 3-11 mo | Current practice | 331.74 | 0 | 6.000 | 0 | 10 |
| 2025-2039 | 3-11 mo | Higher child coverage | 342.03 | -0.05497 | 7.000 | 1 | 10 |
| 2025-2039 | 3-11 mo | Maternal-household composite proxy | 222.26 | 0.3437 | 4.000 | 9 | 10 |
| 2025-2039 | 3-11 mo | Upper-bound vaccine | 0.9881 | 0.9777 | 2.000 | 10 | 10 |
| 2025-2039 | 3-11 mo | Resistance-guided treatment | 191.09 | 0.3888 | 3.500 | 10 | 10 |
| 2025-2050 full horizon | 0-2 mo | Adolescent booster | 476.70 | 0.01916 | 5.000 | 7 | 10 |
| 2025-2050 full horizon | 0-2 mo | Combined strategy | 1.290 | 0.9899 | 1.000 | 10 | 10 |
| 2025-2050 full horizon | 0-2 mo | Current practice | 533.56 | 0 | 6.000 | 0 | 10 |
| 2025-2050 full horizon | 0-2 mo | Higher child coverage | 535.23 | -0.006603 | 7.000 | 2 | 10 |
| 2025-2050 full horizon | 0-2 mo | Maternal-household composite proxy | 239.15 | 0.5987 | 3.000 | 10 | 10 |
| 2025-2050 full horizon | 0-2 mo | Upper-bound vaccine | 2.020 | 0.973 | 2.000 | 10 | 10 |
| 2025-2050 full horizon | 0-2 mo | Resistance-guided treatment | 328.91 | 0.4104 | 4.000 | 10 | 10 |
| 2025-2050 full horizon | 3-11 mo | Adolescent booster | 285.64 | 0.01838 | 5.000 | 7 | 10 |
| 2025-2050 full horizon | 3-11 mo | Combined strategy | 1.120 | 0.9864 | 1.000 | 10 | 10 |
| 2025-2050 full horizon | 3-11 mo | Current practice | 317.27 | 0 | 6.000 | 0 | 10 |
| 2025-2050 full horizon | 3-11 mo | Higher child coverage | 333.42 | -0.05275 | 7.000 | 1 | 10 |
| 2025-2050 full horizon | 3-11 mo | Maternal-household composite proxy | 212.80 | 0.3631 | 4.000 | 9 | 10 |
| 2025-2050 full horizon | 3-11 mo | Upper-bound vaccine | 1.031 | 0.9758 | 2.000 | 10 | 10 |
| 2025-2050 full horizon | 3-11 mo | Resistance-guided treatment | 198.17 | 0.406 | 3.000 | 10 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Adolescent booster | 537.01 | 0.001014 | 5.500 | 5 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Combined strategy | 1.307 | 0.9893 | 1.000 | 10 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Current practice | 596.70 | 0 | 6.000 | 0 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Higher child coverage | 601.07 | -0.002475 | 7.000 | 3 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Maternal-household composite proxy | 267.88 | 0.5634 | 3.000 | 10 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Upper-bound vaccine | 2.059 | 0.9712 | 2.000 | 10 | 10 |
| 2030-2050 excluding initial transient | 0-2 mo | Resistance-guided treatment | 335.77 | 0.4333 | 4.000 | 10 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Adolescent booster | 312.58 | 0.0009956 | 5.000 | 5 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Combined strategy | 1.135 | 0.9857 | 1.000 | 10 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Current practice | 334.60 | 0 | 5.500 | 0 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Higher child coverage | 345.10 | -0.04452 | 7.000 | 1 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Maternal-household composite proxy | 238.28 | 0.3142 | 4.000 | 9 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Upper-bound vaccine | 1.050 | 0.9742 | 2.000 | 10 | 10 |
| 2030-2050 excluding initial transient | 3-11 mo | Resistance-guided treatment | 193.81 | 0.4318 | 3.000 | 10 | 10 |

<div style="page-break-after: always;"></div>

### eTable 23. Deterministic event-scale diagnostics for stochastic-interpretation sensitivity.

| Scenario | Countries | Median annual infant cases | Minimum annual infant cases | Median infant cases per 100k/y | Low-event countries | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| Adolescent booster | 10 | 1,009.0 | 25.55 | 321.21 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Combined strategy | 10 | 17.17 | 1.487 | 1.152 | Sweden; South Africa; Thailand; Brazil; United States; Japan | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Current practice | 10 | 995.63 | 86.07 | 357.53 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Higher child coverage | 10 | 1,037.5 | 92.76 | 370.98 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Maternal-household composite proxy | 10 | 525.21 | 13.79 | 217.70 | Thailand | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Upper-bound vaccine | 10 | 72.95 | 0.7194 | 1.215 | Sweden; South Africa; Thailand; Brazil; United States | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |
| Resistance-guided treatment | 10 | 621.01 | 40.52 | 222.51 | None | Low-event countries are most sensitive to stochastic extinction or clustering assumptions. |

<div style="page-break-after: always;"></div>

### eTable 24. Limitation-to-diagnostic map and residual interpretation.

| Limitation domain | Added or existing diagnostic | Supplement location | Residual interpretation |
| --- | --- | --- | --- |
| Infant outcomes without direct age-specific calibration | Overall calibration fit, fitted reporting gradients, infant contact sensitivity, age-shift diagnostics, and 0-2 month/3-11 month intervention-window summaries. | eTables 7, 12, 17, 18, and 22 | Infant estimates are conditional model outputs, not externally validated infant forecasts. |
| Intervention scenario ordering under joint parameter uncertainty | Analysis-window order positions, cross-diagnostic order-stability summary, infant-age/window summaries, Figure 4B source data retained as repository CSV, and selected-parameter joint PSA order-stability diagnostics. | eTables 19, 20, 22, and 25 | Order-position probabilities are conditional on the epidemiologic PSA ranges and do not include costs, feasibility, or equity weights. |
| Deterministic dynamics without stochastic extinction or superspreading | Event-scale diagnostics identify low-event cells where deterministic persistence assumptions matter most; a small individual stochastic toy model illustrates contact-clustering sensitivity. | eTables 23 and 26 | Near-zero burdens and low-event cells should be read as deterministic thresholds, not stochastic elimination probabilities. |
| No explicit household clustering, contact tracing, or adherence model | Intervention outcome summaries, resistance-guided treatment implementation sensitivity, infant-contact and maternal-duration sensitivity, and individual stochastic contact-clustering illustration. | eTables 15, 16, 17, and 26 | Age-structured proxy diagnostics do not replace household or contact-tracing simulations. |
| Macrolide-resistant strain dynamics depend on fitness and management assumptions | Resistance mechanism decomposition, condensed fitness grid, treatment/PEP implementation sensitivity, vaccine-infectiousness thresholds, and resistance-parameter justification. | eTables 11, 13, 14, 16, and 28 | Resistance trajectories remain stress tests of selection mechanisms rather than unconditional replacement predictions. |
| No costs, quality-adjusted life-years, feasibility, or equity weights | Exploratory QALY-like burden translations are retained as repository outputs rather than submitted appendix tables. | Repository CSV outputs | This is not a formal cost-effectiveness analysis; the submitted model still does not include costs, decision thresholds, discounting, feasibility constraints, or equity weights. |
| In-development vaccine products cannot be treated as available policies | Pipeline-to-mechanism mapping for intranasal BPZE1, OMV-based platforms, genetically detoxified recombinant aP vaccines, and new multicomponent aP candidates. | eTable 27 | Candidate products were represented through mechanism profiles and sensitivity ranges, not product-specific policy scenarios. |

<div style="page-break-after: always;"></div>

### eTable 25. Selected-parameter joint PSA order-stability diagnostics for infant-case intervention ordering.

| Strategy | Pr(ordered first) | Pr(top 2) | Pr(within 10% of best) | Mean order position | Median order position | Median infant cases per 100k/y | Q2.5 infant cases per 100k/y | Q97.5 infant cases per 100k/y | Median reduction vs current | PSA samples |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Adolescent booster | 0 | 0 | 0 | 5.360 | 5.000 | 1,245.2 | 0.4013 | 5,740.1 | 4.33e-05 | 128 |
| Combined strategy | 0.6945 | 1.000 | 0.7867 | 1.305 | 1.000 | 390.48 | 0.1368 | 3,450.4 | 0.6586 | 128 |
| Current practice | 0 | 0 | 0 | 5.589 | 6.000 | 1,246.5 | 0.4695 | 5,773.9 | 0 | 128 |
| Higher child coverage | 0 | 0 | 0 | 6.581 | 7.000 | 1,256.4 | 0.4428 | 5,965.2 | -0.02711 | 128 |
| Maternal-household composite proxy | 0 | 0.003906 | 0.0007813 | 3.180 | 3.000 | 1,012.6 | 0.325 | 5,449.9 | 0.1885 | 128 |
| Upper-bound vaccine | 0.3055 | 0.9961 | 0.4266 | 1.698 | 2.000 | 508.32 | 0.169 | 3,115.4 | 0.586 | 128 |
| Resistance-guided treatment | 0 | 0 | 0 | 4.286 | 4.000 | 1,180.6 | 0.4253 | 5,507.2 | 0.05773 | 128 |

<div style="page-break-after: always;"></div>

### eTable 26. Individual stochastic contact-clustering toy model key diagnostics (100 replicates, synthetic population 1,500, target R=1.08; structural sensitivity only).

| Country | Contact structure | Pr(extinct <=3) | Pr(outbreak >=20 infections) | Total infections, median (95% interval) | Infant infections (mean; Pr any; Q95) | Mean household clusters |
| --- | --- | --- | --- | --- | --- | --- |
| Australia | Homogeneous all contacts | 0.69 | 0.17 | 1 (1-200.925) | mean 0.01; Pr(any) 0.01; Q95 0 | 19.02 |
| Australia | Setting clustered | 0.66 | 0.06 | 2 (1-67.05) | mean 0.04; Pr(any) 0.04; Q95 0 | 4.710 |
| Australia | Setting clustered high household | 0.71 | 0.09 | 1 (1-31.1) | mean 0.08; Pr(any) 0.08; Q95 1 | 3.430 |
| China | Homogeneous all contacts | 0.66 | 0.14 | 1 (1-118.25) | mean 0; Pr(any) 0; Q95 0 | 14.22 |
| China | Setting clustered | 0.68 | 0.05 | 2 (1-33.1) | mean 0.07; Pr(any) 0.07; Q95 1 | 3.370 |
| China | Setting clustered high household | 0.75 | 0.04 | 2 (1-21.525) | mean 0.1; Pr(any) 0.1; Q95 1 | 2.500 |
| Japan | Homogeneous all contacts | 0.72 | 0.12 | 1 (1-131.75) | mean 0; Pr(any) 0; Q95 0 | 14.29 |
| Japan | Setting clustered | 0.64 | 0.14 | 2 (1-68.525) | mean 0.11; Pr(any) 0.11; Q95 1 | 6.660 |
| Japan | Setting clustered high household | 0.68 | 0.05 | 2 (1-20.525) | mean 0.09; Pr(any) 0.09; Q95 1 | 2.970 |
| South Africa | Homogeneous all contacts | 0.54 | 0.29 | 2 (1-195.675) | mean 0.08; Pr(any) 0.06; Q95 1 | 23.51 |
| South Africa | Setting clustered | 0.76 | 0.07 | 1 (1-42.3) | mean 0.01; Pr(any) 0.01; Q95 0 | 3.410 |
| South Africa | Setting clustered high household | 0.75 | 0 | 1 (1-10.525) | mean 0.09; Pr(any) 0.09; Q95 1 | 1.900 |
| United States | Homogeneous all contacts | 0.7 | 0.14 | 2 (1-85.125) | mean 0; Pr(any) 0; Q95 0 | 11.84 |
| United States | Setting clustered | 0.73 | 0.06 | 2 (1-37.575) | mean 0.06; Pr(any) 0.06; Q95 1 | 3.360 |
| United States | Setting clustered high household | 0.74 | 0.03 | 1 (1-19.05) | mean 0.08; Pr(any) 0.07; Q95 1 | 2.390 |

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
| Resistance-guided management scenario | Symptomatic treatment rate 0.065; resistant infectious-duration reduction 0.45; resistant infectiousness reduction 0.35; resistant PEP effectiveness 0.45 | Treatment/PEP implementation scenarios and joint PSA uptake multiplier | CDC resistance-aware treatment guidance translated into a testing-and-alternative-treatment scenario | Represents improved recognition of resistance and use of effective alternatives or restored prophylaxis effectiveness. | Higher uptake or restored PEP effectiveness increases projected benefit; low testing reach and uptake reduce or delay benefit. | Testing availability, turnaround time, clinician suspicion, drug tolerability, and adherence are not modeled explicitly. |
| Resistant importation | Low-level importation enabled; default rate 0.20 per 100,000 persons/year with country/scenario resistant fraction | Resistance mechanism decomposition separates ongoing importation from fitness and treatment/PEP differentials | Persistence/reintroduction assumption anchored to observed international spread | Prevents deterministic extinction of rare resistant strains while allowing decomposition of whether importation alone drives high end fractions. | Higher importation affects persistence and timing; mechanism decomposition suggests it is not the main driver of near-complete replacement in the main runs. | Importation is smooth and low-level rather than a stochastic travel- or outbreak-linked process. |

<div style="page-break-after: always;"></div>
