<div style="text-align:center;">
  <h3 style="font-family: inherit; font-weight: normal; margin-bottom: 0;">Supplementary Material</h3>
  <h1 style="font-family: inherit; font-weight: bold; font-size: 1.5em;">Optimization of Infant Pertussis Prevention and Resistance-Management Strategies</h1>
  <br>
  <br>
  Kangguo Li et al. (2026)
</div>

<div style="page-break-after: always;"></div>

## Contents

- eMethods. Model equations, country-profile construction, calibration, scenario definitions, uncertainty evaluation, and interpretation limits.
- eFigure 1. Country-specific input data and macrolide-resistance evidence used to instantiate the ten national pertussis transmission profiles.
- eFigure 2. Surveillance, calibration, and reporting diagnostics for the modeled country profiles.
- eFigure 3. Transmission model structure and vaccine-effect weights.
- eFigure 4. Baseline temporal dynamics over the saved analysis period.
- eFigure 5. Vaccine-mechanism analysis and infection-source decomposition.
- eFigure 6. Dynamic consequences of macrolide-resistance assumptions.
- eFigure 7. Extended intervention-strategy outcomes across countries and endpoints.
- eFigure 8. Resistance hindcast plausibility checks against observed macrolide-resistance trajectories.
- eFigure 9. Scenario-ordering and endpoint-robustness diagnostics.
- eFigure 10. Resistance-management mechanism decomposition, preference-threshold, and transmission-threshold diagnostics.
- eFigure 11. Program portfolio factorial, implementation, and structural robustness diagnostics.
- eTable 1. Country-profile selection rationale and resistance anchors.
- eTable 2. Study parameter-design matrix for scenario, sensitivity, and uncertainty analyses.
- eTable 3. Macrolide-resistance initialization, importation, and fitness assumptions.
- eTable 4. Intervention strategy definitions, modified control levers, and decision domain.
- eTable 5. Baseline parameter values, admissible ranges, and evidence provenance.
- eTable 6. Country-specific macrolide-resistance evidence used for resistance anchoring.
- eTable 7. Calibration acceptance, fitted parameters, and interval-level fit diagnostics.
- eTable 8. Model-derived outcomes and summary definitions.
- eTable 9. Core model settings and implementation choices.
- eTable 10. Bayesian uncertainty priors and fixed nuisance settings for the conditional beta-grid interval analysis.
- eTable 11. Condensed macrolide-resistant fitness and vaccine infectiousness grid definition.
- eTable 12. Fitted age-specific reporting probabilities and prior bounds.
- eTable 13. Limitation-to-diagnostic map and residual interpretation.
- eTable 14. Vaccine-pipeline mechanism mapping to modeled scenario profiles.
- eTable 15. Macrolide-resistance parameter justification and expected direction of bias.
- eTable 16. Strategy domains, decision role, and interpretation of model assumptions.
- eTable 17. Implementation-intensity score definitions.
- eReferences. Supplemental references.

## eMethods

### Study design

We developed a deterministic age-structured compartmental model of *Bordetella pertussis* transmission to identify non-dominated infant-protection strategy profiles under program-only, program plus resistance-management, and future product-target constraints. Outcomes included infant symptomatic cases, all-age infections, notified cases, resistant infections, and conditional optimization diagnostics.

The vaccine-history structure follows the WHO pertussis vaccine framework [1]. The natural-immunity and boosting structure builds on pertussis waning, resurgence, and asymptomatic-transmission models [2-5]. Vaccine transmission-mechanism scenarios were motivated by acellular-vaccine transmission and waning evidence [6-9]. Maternal-origin states represent short-lived passive infant protection informed by pregnancy vaccination effectiveness studies [10-12].

Ten national profiles were analyzed: Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, the United Kingdom, and the United States. The set is purposive rather than globally representative; it was chosen to maximize contrast in programmatic and resistance assumptions, spanning Western Pacific, South-East Asian, European, Americas, and African settings, large and small population denominators, contrasting booster and maternal-immunization program signatures, heterogeneous reported incidence, and both measured and conservative low macrolide-resistance anchors.

Country-specific population denominators came from United Nations World Population Prospects [13]. Vaccine schedule and coverage inputs used WHO/UNICEF Joint Reporting Form and immunization records [14]. Contact matrices used Prem/contactdata social-contact estimates [15-17], and reported-case intervals used the harmonized PertussisIncidence surveillance table [18]. Treatment and PEP assumptions followed CDC clinical guidance [19,20].

Resistance guidance came from CDC and ECDC sources [21,22]. The country evidence timeline combined reports from China [23,24], Australia [25], Japan [26], the Americas [27], and earlier regional MRBP reports [28,29]. The principal simulations used a 15-year pre-analysis burn-in to reduce dependence on arbitrary initial conditions, followed by a 26-year analysis horizon beginning on 1 January 2025, with model output retained at 7-day intervals.

All incidence measures are reported as annualized counts per 100,000 persons unless stated otherwise. Infant outcomes combine the 0-2 month and 3-11 month age groups, because these strata jointly capture the highest-risk pre-primary-series and partially vaccinated infant population. Simulated optimization summaries are epidemiologic diagnostics; selected-parameter regret diagnostics and exploratory burden translations are supplementary sensitivity analyses and do not constitute cost-effectiveness, feasibility, or equity-weighted policy appraisal.

The supplementary appendix is generated directly from the same analysis pipeline used for the simulations, so the text, figures, and tables remain aligned with the model assumptions. <span style="color:#5DADE2;">eTable 2</span> provides the study parameter-design matrix, source/provenance links, and detailed-table locations across scenario, sensitivity, and uncertainty analyses; <span style="color:#5DADE2;">eTable 9</span> summarizes the fixed model settings and output conventions that govern interpretation.

### Country profile construction

Population denominators were aggregated from one-year age groups into eight model strata. Age 0 population was partitioned according to the configured infant age-bin widths, with $2/12$ assigned to the 0-2 month stratum and $10/12$ assigned to the 3-11 month stratum; ages 1-4 years, 5-9 years, 10-17 years, 18-39 years, 40-64 years, and 65 years or older were then aggregated directly. Let $N_i$ denote the resulting population in age group $i$. In the ODE, age movement uses the same configured age-bin durations, so the denominator split and maternal-protection ageing rule are aligned.

Routine and maternal immunization inputs were transformed into age-specific vaccine-origin coverage proxies using DTP1 coverage $v_1$, DTP3 coverage $v_3$, maternal coverage $m$, the number of childhood booster doses $b$, and an indicator $A$ for an adolescent booster program:

$$
v_{0-2m}=\mathrm{clip}(0.02+0.55m,\ 0.02,\ 0.75),
$$

$$
v_{3-11m}=\mathrm{clip}(0.75v_1+0.12v_3+0.12m,\ 0,\ 0.95),
$$

$$
v_{1-4y}=\mathrm{clip}\{v_3[0.88+0.04\min(b,2)],\ 0,\ 0.98\},
$$

$$
v_{5-9y}=\mathrm{clip}\{v_3[0.80+0.06\min(b,2)],\ 0,\ 0.96\},
$$

$$
v_{10-17y}=\mathrm{clip}\{v_3[0.55+0.12\min(b,2)+0.15A],\ 0,\ 0.95\},
$$

$$
v_{18-39y}=\mathrm{clip}(0.20+0.15A+0.05m,\ 0.10,\ 0.75),
$$

$$
v_{40-64y}=\mathrm{clip}(0.12+0.05A+0.02m,\ 0.08,\ 0.50),
$$

$$
v_{65+y}=\mathrm{clip}(0.08+0.02A,\ 0.05,\ 0.30).
$$

These deterministic transformations assign individuals to mechanistic protection histories and do not imply that age-specific pertussis immunization coverage, especially adult coverage, is directly observed in all settings. They are coverage-to-state mapping proxies that translate DTP1, DTP3, booster, and maternal-program records into the compartment origins needed by the model. The waning structure follows acellular-pertussis vaccine duration evidence [7-9], and the maternal-origin mapping follows pregnancy vaccination effectiveness evidence [10-12]. Adult values represent residual or recently boosted immune-history proxies, not measured adult pertussis vaccine uptake.

Seasonal forcing parameters were inferred from the timing of positive reported cases. For observation $l$, let $c_l$ be reported cases and $\theta_l=2\pi(d_l-1)/365$, where $d_l$ is the day of year. The circular concentration was

$$
R_c=
\frac{
\left[(\sum_l c_l\sin\theta_l)^2+(\sum_l c_l\cos\theta_l)^2\right]^{1/2}
}{
\max(\sum_l c_l,10^{-9})
},
$$

with annual phase

$$
\phi =
\left[
\frac{365}{2\pi}\mathrm{atan2}\left(\sum_l c_l\sin\theta_l,\sum_l c_l\cos\theta_l\right)+1
\right]\bmod 365
$$

and annual amplitude

$$
a=\mathrm{clip}(0.08+0.55R_c,\ 0.08,\ 0.35).
$$

The amplitude mapping is a surveillance-derived heuristic rather than a separately identifiable seasonal-transmission estimate; seasonal amplitude is therefore included in calibration and sensitivity workflows.

Multi-year recurrence was treated as a diagnostic forcing component rather than direct evidence of a single causal oscillator. Annual reported-case peaks were identified with a minimum spacing of two years and a prominence threshold equal to 10% of the maximum annual count. A 3-5 year median peak interval was considered compatible with multi-year recurrence; otherwise the multi-year amplitude was set to zero [2,3].

Prem/contactdata all-setting matrices were first represented on 5-year age bins and then aggregated to the eight model age groups using population weights [15-17]. If $P_{ab}$ is the fine-age contact matrix, $w_{ia}$ is the distribution of age group $i$ over fine source bin $a$, and $f_{jb}$ is the fraction of fine target bin $b$ belonging to model group $j$, then

$$
C_{ij}^{raw}=\sum_a\sum_b w_{ia}P_{ab}f_{jb}.
$$

Population-weighted reciprocity was imposed by replacing each off-diagonal pair with the shared contact total

$$
\tilde{C}_{ij}=
\frac{C_{ij}^{raw}N_i+C_{ji}^{raw}N_j}{2N_i},
\quad
\tilde{C}_{ji}=
\frac{C_{ij}^{raw}N_i+C_{ji}^{raw}N_j}{2N_j}.
$$

This correction preserves the average number of cross-group contacts while ensuring $N_i\tilde{C}_{ij}=N_j\tilde{C}_{ji}$.

For the individual stochastic contact-clustering toy model, the same extraction and aggregation procedure was repeated for the contactdata location-specific matrices (home, school, work, and other). These setting-specific matrices were used only for structural-sensitivity illustration; the calibrated deterministic model used the reciprocity-balanced all-setting matrix. Because Prem/contactdata 5-year bins cannot directly resolve the 0-2 month and 3-11 month infant strata, infant-target contacts are a main structural uncertainty and were evaluated through infant-contact sensitivity diagnostics.

### Age groups, strains, and state variables

The model uses eight age groups:

$$
i \in \mathcal{A} = \{0\text{-}2m,\ 3\text{-}11m,\ 1\text{-}4y,\ 5\text{-}9y,\ 10\text{-}17y,\ 18\text{-}39y,\ 40\text{-}64y,\ 65+y\}.
$$

Pertussis infections are divided into macrolide-sensitive and macrolide-resistant strains:

$$
k \in \mathcal{K} = \{\mathrm{sens},\mathrm{res}\}.
$$

Here strain subscripts $\mathrm{sens}$ and $\mathrm{res}$ denote macrolide-sensitive and macrolide-resistant infection. These strain labels are distinct from susceptible compartments $S_{i,o}$ and naturally immune states $R_i$.

Susceptible individuals retain vaccine or maternal-protection origin histories:

$$
o \in \mathcal{O} = \{U,\ M,\ D1_{rec},\ D1_{wan},\ D2_{rec},\ D2_{wan},\ D3_{rec},\ D3_{wan}\}.
$$

Here $U$ is unvaccinated, $M$ is maternally protected, $D1$ and $D2$ are one- and two-dose histories, and $D3$ represents three-or-more-dose histories; subscripts $rec$ and $wan$ denote recent and waned protection.

For each age group, the model tracks susceptible-origin states $S_{i,o}$, exposed states $E_{i,k,o}$, symptomatic infectious states $I^{sym}_{i,k,o}$, asymptomatic infectious states $I^{asym}_{i,k,o}$, treated infectious states $T_{i,k,o}$, naturally immune states $R_i$, and waned-natural-immunity states $W_i$. The per-age state space contains 8 susceptible-origin states, 16 exposed states, 32 infectious states, 16 treated states, and two natural-immunity states, yielding 74 compartments per age group and 592 dynamic state variables.

### Vaccine mechanism parameterization

Four vaccine mechanism parameters define a scenario:

$$
\mathrm{VE}_{sus},\quad \mathrm{VE}_{sym},\quad \mathrm{VE}_{inf},\quad \mathrm{VE}_{dur}.
$$

These represent reductions in susceptibility to infection, symptomatic disease given infection, onward infectiousness after infection, and infectious duration, respectively. They are mechanistic scenario-decomposition parameters, not quantities separately identifiable from routine surveillance alone. Throughout this appendix, $\mathrm{VE}_{sus}$ is the model parameter corresponding to protection against infection through reduced susceptibility, whereas $\mathrm{VE}_{inf}$ is not an infection-acquisition endpoint but a reduction in infectiousness among infected vaccine-history origins. Vaccine effects are origin-specific through a relative effect weight $w_o \in [0,1]$. The default weights distinguish maternal protection, partial-dose histories, recent three-or-more-dose protection, and waned protection:

$$
w_o =
\begin{cases}
0, & o=U,\\
w_M, & o=M,\\
w_1, & o=D1_{rec},\\
w_1w_{wan}, & o=D1_{wan},\\
w_2, & o=D2_{rec},\\
w_2w_{wan}, & o=D2_{wan},\\
1, & o=D3_{rec},\\
w_{wan}, & o=D3_{wan}.
\end{cases}
$$

The origin-specific susceptibility multiplier is

$$
q_o = \max(0, 1 - w_o\mathrm{VE}_{sus}).
$$

The probability that an infection in age group $i$ and origin $o$ is symptomatic is

$$
\rho_{i,o} = \mathrm{clip}\{\rho_i(1-w_o\mathrm{VE}_{sym}),0,1\},
$$

where $\rho_i$ is the age-specific baseline symptom probability. The origin-specific infectiousness multiplier is

$$
\eta_o = \mathrm{clip}(1-w_o\mathrm{VE}_{inf},0,1),
$$

and vaccine shortening of infectious duration is represented by a recovery-rate multiplier

$$
m_o = \left[\max(0.05,1-w_o\mathrm{VE}_{dur})\right]^{-1}.
$$

This formulation separates protection against infection, clinical disease, onward infectiousness, and duration of infectiousness. $\mathrm{VE}_{inf}$ and $\mathrm{VE}_{dur}$ jointly reduce onward transmission through infectiousness and duration pathways and should not be interpreted as additive effects. The same origin weight is used across mechanisms for parsimony because mechanism-specific origin weights are not identifiable from the available surveillance data; those assumptions are evaluated through vaccine-mechanism scenarios and sensitivity analyses. Maternal-immunization interventions may override the four vaccine-mechanism parameters only for the maternal-protection origin; otherwise the global scenario values are used for all origins. The parameterization permits aP-like profiles with strong protection against symptoms but weak infection or transmission blocking [6], and waned profiles informed by duration-of-protection evidence [7-9].

### Seasonal transmission and force of infection

Let $N_i(t)$ denote the current population in age group $i$, and $C_{ij}$ the country-specific reciprocity-balanced contact rate from age group $i$ to age group $j$. Seasonal forcing is country specific:

$$
s(t) = \max\left(0,\left[1+a\cos\left(\frac{2\pi(d(t)-\phi)}{365}\right)\right]\left[1+a_m\cos\left(\frac{2\pi(t-\phi_m)}{365P_m}\right)\right]g_{NPI}(t)\right),
$$

where $a$ and $\phi$ are annual amplitude and phase, $d(t)$ is calendar day of year, and the optional multi-year term has amplitude $a_m$, period $P_m$, and phase $\phi_m$. The multiplier $g_{NPI}(t)$ represents configured COVID-19/non-pharmaceutical-intervention contact reductions and equals 1 when no country-specific NPI period is specified. The multi-year component is included only when surveillance-derived peak diagnostics support recurrent 3-5 year structure.

The infectious pressure contributed by age group $j$ and strain $k$ is

$$
\Pi_{j,k}(t) =
\frac{1}{N_j(t)}
\sum_{o \in \mathcal{O}}
\eta_o\left[
I^{sym}_{j,k,o}
+ r_A I^{asym}_{j,k,o}
+ \zeta_k T_{j,k,o}
\right],
$$

where $r_A$ is the relative infectiousness of asymptomatic infection. The treated-state infectiousness multiplier is strain-specific:

$$
\zeta_k = 1 - e^{inf}_k,
$$

where $e^{inf}_k$ is the treatment-associated reduction in infectiousness for strain $k$. The pre-PEP forces of infection are

$$
\lambda^0_{i,\mathrm{sens}}(t) = \beta_{\mathrm{sens}} s(t)\sum_j C_{ij}\Pi_{j,\mathrm{sens}}(t),
$$

$$
\lambda^0_{i,\mathrm{res}}(t) = \beta_{\mathrm{sens}} f_{\mathrm{res}} s(t)\sum_j C_{ij}\Pi_{j,\mathrm{res}}(t),
$$

where $\beta_{\mathrm{sens}}$ is the sensitive-strain transmission parameter and $f_{\mathrm{res}}$ is the resistant-strain relative fitness. The latter is an epidemiologic stress-test scalar, not a direct laboratory measurement of intrinsic bacterial growth or transmissibility.

Postexposure prophylaxis is represented as a prevalence-triggered reduction in force of infection. Let

$$
D(t)=
\frac{\sum_i p_i^{det}(t)\sum_{k,o} I^{sym}_{i,k,o}}{\sum_i N_i(t)}
$$

be detected symptomatic prevalence, and

$$
A(t)=\frac{D(t)}{D(t)+h}
$$

the activation function, where $h$ is the activation prevalence. With PEP coverage $c_{PEP}$ and strain-specific PEP effectiveness $e^{PEP}_k$,

$$
\lambda_{i,k}(t)=\lambda^0_{i,k}(t)\left[1-c_{PEP}A(t)e^{PEP}_k\right].
$$

PEP is therefore represented as a force-of-infection modifier rather than as a separate prophylaxis state. PEP-averted cases are calculated as a diagnostic contrast between pre-PEP and post-PEP infection flows, not as an additional compartment. This reduced-form representation captures partial reach of household or close-contact prophylaxis but does not explicitly model contact tracing, household clustering, adherence, or prophylaxis timing.

### Infection progression, treatment, and recovery

New infections from susceptible-origin state $S_{i,o}$ enter the strain-specific exposed states:

$$
\frac{dE_{i,k,o}}{dt}\bigg|_{infection} = \lambda_{i,k}(t)q_oS_{i,o}.
$$

Let $\sigma$ be the exposed-to-infectious progression rate and $\gamma_{sym}$ and $\gamma_{asym}$ baseline recovery rates. Treatment rates are age-specific because only a fraction of infections are diagnosed and treated. If $\tau_{sym}$ and $\tau_{asym}$ are the configured symptomatic and asymptomatic treatment-rate ceilings and $p_i^{diag}(t)$ is the age-specific diagnosis probability, the implemented rates are

$$
\tau^{sym}_i(t)=\tau_{sym}\frac{p_i^{diag}(t)}{\max_j p_j^{diag}(t)},
\quad
\tau^{asym}_i(t)=\tau_{asym}\frac{p_i^{diag}(t)}{\max_j p_j^{diag}(t)}.
$$

The infection progression equations are:

$$
\frac{dE_{i,k,o}}{dt} = \lambda_{i,k}q_oS_{i,o} - \sigma E_{i,k,o},
$$

$$
\frac{dI^{sym}_{i,k,o}}{dt} =
\rho_{i,o}\sigma E_{i,k,o}
- \tau^{sym}_i(t)I^{sym}_{i,k,o}
- m_o\gamma_{sym}I^{sym}_{i,k,o},
$$

$$
\frac{dI^{asym}_{i,k,o}}{dt} =
(1-\rho_{i,o})\sigma E_{i,k,o}
- \tau^{asym}_i(t)I^{asym}_{i,k,o}
- m_o\gamma_{asym}I^{asym}_{i,k,o}.
$$

Treated infections follow:

$$
\frac{dT_{i,k,o}}{dt} =
\tau^{sym}_i(t)I^{sym}_{i,k,o}
+ \tau^{asym}_i(t)I^{asym}_{i,k,o}
- m_o\gamma^T_kT_{i,k,o},
$$

with

$$
\gamma^T_k =
\frac{\gamma_{sym}}{\max(0.05,1-e^{dur}_k)},
$$

where $e^{dur}_k$ is the treatment-associated reduction in infectious duration for strain $k$. The treated state uses the symptomatic infectious-duration baseline because treatment is assumed to occur mainly among diagnosed symptomatic infections, while asymptomatic treatment is rare. Macrolide-resistant infections therefore receive smaller treatment effects unless a resistance-guided strategy modifies the resistant treatment block. This treatment block follows CDC clinical overview and treatment/PEP guidance, including the use of macrolides as standard first-line agents and alternative antibiotics when resistance is suspected or confirmed [19,20].

Naturally immune states receive all recoveries and wane into a "waned but boostable" state (W) at rate $\omega_{RW}$. Individuals in W who are re-exposed to circulating pertussis (total force of infection $\lambda_i^{total} = \lambda_{i,\mathrm{sens}} + \lambda_{i,\mathrm{res}}$) have their immunity restored to R at rate $\varepsilon\lambda_i^{total}$, where $\varepsilon$ is the boosting efficiency. Those in W who are not boosted eventually lose all immunity and return to S at rate $\omega_{WS}$. This SIRWS structure (Lavine et al. 2011; Wearing & Rohani 2009) naturally produces immunity debt during periods of reduced pathogen circulation:

$$
\frac{dR_i}{dt} =
\sum_{k,o}m_o\left[
\gamma_{sym}I^{sym}_{i,k,o}
+ \gamma_{asym}I^{asym}_{i,k,o}
+ \gamma^T_kT_{i,k,o}
\right]
-\omega_{RW}R_i
+\varepsilon\lambda_i^{total}W_i,
$$

$$
\frac{dW_i}{dt} =
\omega_{RW}R_i
-\varepsilon\lambda_i^{total}W_i
-\omega_{WS}W_i,
$$

$$
\frac{dS_{i,\mathrm{unvaccinated}}}{dt}\bigg|_{W\ loss} = +\omega_{WS}W_i.
$$

When boosting is disabled in the implementation, the legacy comparison uses direct waning from $R_i$ to unvaccinated susceptibility at the configured natural-immunity waning rate. When the SIRWS structure is enabled but $\varepsilon=0$, immunity instead passes through $W_i$ without re-exposure boosting. The key SIRWS parameters are: $\omega_{RW} = 1/1825$ day$^{-1}$ (5-year R→W transition), $\omega_{WS} = 1/3650$ day$^{-1}$ (10-year W→S transition), and $\varepsilon = 0.70$ (boosting efficiency).

### Waning vaccine and maternal protection

Maternal protection wanes into unvaccinated susceptibility at rate $\omega_M$:

$$
\frac{dS_{i,\mathrm{maternal}}}{dt}\bigg|_{waning}=-\omega_MS_{i,\mathrm{maternal}},
\quad
\frac{dS_{i,\mathrm{unvaccinated}}}{dt}\bigg|_{maternal\ waning}=+\omega_MS_{i,\mathrm{maternal}}.
$$

In addition, maternally protected individuals who age out of the youngest infant stratum are converted to unvaccinated susceptibility, because this state represents short-lived maternally derived protection rather than a durable vaccine-dose history.

Recent vaccine-dose states wane into corresponding waned states at rate $\omega_V$, and waned vaccine states return to unvaccinated susceptibility at rate $\omega_W$. For each dose category $d$,

$$
\frac{dS_{i,d,recent}}{dt}\bigg|_{waning}=-\omega_VS_{i,d,recent},
$$

$$
\frac{dS_{i,d,waned}}{dt}\bigg|_{waning}=+\omega_VS_{i,d,recent}-\omega_WS_{i,d,waned},
$$

$$
\frac{dS_{i,\mathrm{unvaccinated}}}{dt}\bigg|_{waned\ loss}=+\omega_WS_{i,d,waned}.
$$

The return to unvaccinated susceptibility is a model-level loss of mechanistic protection, not a claim that individual vaccination history is forgotten or unobservable.

Routine vaccination is implemented as a relaxation toward country-specific age-group coverage targets. For age group $i$, desired vaccine-origin mass is proportional to current population $N_i(t)$, target coverage $v_i$, and target origin distribution $g_{i,o}$. For vaccine-dose origins, the deficit is

$$
\delta_{i,o}(t)=
\max\left[
0,\ 
\frac{v_iN_i(t)g_{i,o}}{\sum_{o'\in\mathcal{V}}g_{i,o'}}
-S_{i,o}(t)
\right],
$$

where $\mathcal{V}$ is the set of vaccine-dose origins. The total vaccination flow from unvaccinated susceptibility is capped by both the available unvaccinated susceptible pool and the configured maximum daily flow fraction $\phi_V=0.01$ day$^{-1}$:

$$
F_i(t)=\min\left[
\kappa_V\sum_{o\in\mathcal{V}}\delta_{i,o}(t),\ \phi_VS_{i,U}(t)
\right],
$$

and is distributed in proportion to $\delta_{i,o}(t)$. This formulation prevents vaccination flows from exceeding 1% of the available unvaccinated susceptible pool per day. Routine and booster interventions are therefore represented as susceptible-origin redistribution toward age-specific targets rather than as explicit individual vaccination events among all disease states.

For the routine-timeliness sensitivity, the target-relaxation rate was increased from 2.0 to 6.0 per year and the maximum daily flow fraction from 0.01 to 0.03. The vaccine-origin targets were shifted toward earlier age-appropriate histories: 3-11 month infants used 10% dose-1 recent, 30% dose-2 recent, and 60% dose-3-plus recent; children aged 1-4 years used 80% recent and 20% waned; and children aged 5-9 years used 65% recent and 35% waned. This sensitivity tests schedule timeliness within the model's broad age bins and should not be interpreted as a directly observed country-specific timeliness estimate.

Before burn-in, country-specific vaccine coverage initializes susceptible-origin mass using age-specific origin distributions. The default allocation assigns maternal protection to 0-2 month infants, partial-dose histories to 3-11 month infants, and recent or waned three-or-more-dose histories to older age groups. Initial exposed and infectious seeds are allocated by age and by the susceptible-origin shares within each age group, with strains split according to the initial resistance prevalence.

### Resistance initialization and importation

Each resistance scenario specifies a target resistant fraction at the start of the analysis period. Country-timeline targets combine the raw evidence rows listed in <span style="color:#5DADE2;">eTable 6</span> with the analysis-year rule described below; fixed targets provide low-to-very-high contrasts for mechanism exploration. After burn-in, active exposed, infectious, and treated compartments are rebalanced so that for every origin and active compartment pair,

$$
X_{i,\mathrm{res},o}^{active} \leftarrow p_{\mathrm{res}} X_{i,\cdot,o}^{active},
\quad
X_{i,\mathrm{sens},o}^{active} \leftarrow (1-p_{\mathrm{res}})X_{i,\cdot,o}^{active},
$$

where $p_{\mathrm{res}}$ is the target resistant fraction. The same target fraction is applied across active age, origin, and infectious-stage pairs at the analysis start. This separates the intended resistance scenario from strain fixation that can arise during long deterministic burn-in. Country-timeline scenarios use the latest admissible country-specific resistance estimate at or before the anchor year; fixed scenarios use the low, moderate, high, or very-high values specified in <span style="color:#5DADE2;">eTable 3</span>.

No ongoing prevalence anchoring was applied during the saved analysis period. After the burn-in rebalance, the resistant fraction evolves through differential strain fitness, treatment and PEP effects, susceptible-origin composition, and importation. This separation was used because macrolide-resistance interpretation differs across evidence types. CDC and ECDC guidance define the clinical and laboratory context [21,22]. Country anchors then use molecular and outbreak reports from China [23,24], Australia [25], Japan [26], the Americas [27], and regional historical MRBP reports [28,29].

Low-level importation adds exposed infections at a country-level rate $u$ per 100,000 persons per year. With age distribution $a_i^{imp}$ and resistant importation fraction $p_{\mathrm{res}}^{imp}$,

$$
M_i(t)=\frac{u}{100000 \times 365}N_{\cdot}a_i^{imp},
$$

and imports are distributed across susceptible origins according to their current share of the susceptible-origin pool. The imported exposed flow is $M_i(t)p_{\mathrm{res}}^{imp}$ for resistant infection and $M_i(t)(1-p_{\mathrm{res}}^{imp})$ for sensitive infection. Imported infections are subtracted from susceptible-origin pools according to the current origin composition, preserving vaccine-origin accounting. Importation is a smooth low-level reintroduction process and is not intended to represent stochastic travel clusters or outbreak-linked introductions.

### Demography and age movement

Demographic turnover keeps country-specific age profiles approximately stationary while allowing cohort movement through the state space. When a country-specific WPP annual trajectory is available, births are supplied by interpolated WPP age-0 inflow, aging proceeds at rates determined by age-bin durations, and a gentle first-order nudge pulls each age group toward the WPP target population to absorb net migration and differential mortality that are not explicit in the ODE. When no trajectory is available (e.g. in unit tests), a fixed-profile fallback is used in which age-exit rates are chosen so that the absolute ageing flow implied by the reference infant age group is compatible with the country-specific age profile. For a generic compartment $X_i$, the age-transition component is

$$
\frac{dX_i}{dt}\bigg|_{ageing} =
-\mu_iX_i + \mu_{i-1}X_{i-1}
$$

for non-youngest age groups. The youngest age group additionally receives births according to the country-specific birth-entry distribution $\pi_X$,

$$
\frac{dX_0}{dt}\bigg|_{births}=B(t)\pi_X,
$$

and the oldest age group exits at rate $\mu_A$. In the WPP-driven mode, $B(t)$ is the interpolated WPP daily birth inflow and a first-order within-age nudge $\nu_i(t)X_i$ absorbs net migration and differential mortality not represented explicitly in the ODE. In the fixed-profile mode, total births equal the outflow from the oldest age group. Maternal protection in the youngest infant group is treated as short-lived maternally derived protection and is converted back to unvaccinated susceptibility when infants age out of the 0-2 month group.

### Numerical solution and burn-in

The model is a continuous-time ordinary differential equation system with rates expressed per day. Main simulations were solved using an adaptive Runge-Kutta method with relative tolerance $10^{-5}$ and absolute tolerance $10^{-7}$. State values were projected to non-negative values when evaluating rates so that small numerical undershoots could not produce negative force-of-infection, recovery, or vaccination flows.

The main analysis used 15 years of burn-in followed by resistance rebalancing and a 26-year saved analysis period (1 January 2025 through 31 December 2050). Calibration simulations used the same 15-year burn-in with coarser saved output and calibration-specific tolerances to reduce computational cost while preserving annual case totals for likelihood evaluation. All summary statistics were computed from the saved analysis interval only.

### Observation model and incidence summaries

Model output records instantaneous daily rates at scheduled output times and converts rates to interval counts by trapezoidal integration. For an interval $[t_{\ell-1},t_\ell]$ and rate $r(t)$,

$$
\widehat{C}_\ell =
\frac{r(t_{\ell-1})+r(t_\ell)}{2}
(t_\ell-t_{\ell-1}).
$$

Age-specific symptomatic case incidence is

$$
C^{sym}_{i,k}(t)=\sum_o \lambda_{i,k}(t)q_oS_{i,o}(t)\rho_{i,o}.
$$

Reported cases are

$$
C^{rep}_{i,k}(t)=p_i^{rep}(t)C^{sym}_{i,k}(t),
$$

where $p_i^{rep}(t)$ is the age-specific final reporting probability, optionally modified by reporting-rate sensitivity scenarios or calibration. Reporting probabilities are clipped to $[0,1]$ after applying any multiplier or time-varying sensitivity scenario.

The reporting model is intentionally separated from the PEP activation term. Reporting-rate sensitivity scenarios modify only $p_i^{rep}(t)$, whereas PEP activation uses a distinct detection proxy $p_i^{det}(t)$ defined in the country profile. This prevents surveillance-completeness sensitivity analyses from mechanically changing true transmission or prophylaxis effects. The age-specific reporting priors used during calibration are broad literature-informed bands rather than direct country-specific estimates. Notification-efficiency and serology studies informed under-ascertainment scale and age-pattern uncertainty [30,31]. Capture-recapture and cough-serology evidence informed under-reporting in selected settings [32,33], and active surveillance informed China-specific under-ascertainment [34].

Annualized incidence per 100,000 persons over an analysis period of length $Y$ years is

$$
I_{all}=\frac{\sum_{\ell,i,k}\widehat{C}^{inf}_{\ell,i,k}}{Y\bar{N}_{\cdot}}100000,
$$

$$
I_{reported}=\frac{\sum_{\ell,i,k}\widehat{C}^{rep}_{\ell,i,k}}{Y\bar{N}_{\cdot}}100000,
$$

$$
I_{infant}=\frac{\sum_{\ell,i \in \mathcal{I},k}\widehat{C}^{sym}_{\ell,i,k}}{Y\bar{N}_{\mathcal{I}}}100000,
$$

where $\mathcal{I}$ includes the two infant age groups. Infant symptomatic cases are model-generated age-specific outcomes; calibration is to country-level reported-case intervals rather than to an external infant-only incidence series. Relative reduction for an outcome $Z$ versus comparator $Z_0$ is

$$
\Delta_Z = 1-\frac{Z}{Z_0}.
$$

### Calibration and likelihood

Country-level calibration targets reported cases over their observed surveillance intervals. The observed series uses the harmonized pertussis surveillance workbook when available, retaining weekly, monthly, annual, and partial-year records with explicit period start and end dates. The calibration window retains the six most recent observed calendar years represented in those intervals, aligns model time to the first retained observed period, and allocates modeled reported cases by calendar-day overlap before comparing observed and modeled interval totals. Annualized incidence summaries are derived from the actual observed coverage days rather than assuming that partial-year records represent complete calendar years.

The full calibration-vector formulation can adjust the sensitive-strain transmission coefficient $\beta_{\mathrm{sens}}$ (stored as `transmission.beta_S` in configuration files and <span style="color:#5DADE2;">eTables</span>), the reporting multiplier, seasonal amplitude, importation rate, and resistant importation fraction:

$$
\theta =
\{\log\beta_{\mathrm{sens}},\ \log m_{rep},\ \mathrm{clogit}(a/0.35),\ \log u,\ \mathrm{clogit}(p_{\mathrm{res}}^{imp})\}.
$$

Here $\mathrm{clogit}$ denotes a logit transform after clipping the argument away from 0 and 1. The admissible ranges were $\beta_{\mathrm{sens}}\in[0.002,0.2]$, $m_{rep}\in[0.01,10]$, $a\in[0,0.35]$, $u\in[0.01,2]$ imported infections per 100,000 persons per year, and $p_{\mathrm{res}}^{imp}\in[0,1]$. The retained principal calibration used a staged search that brackets and bisects $\beta_{\mathrm{sens}}$ against the annualized mean observed reports, followed by a reporting-multiplier adjustment within prior bounds. A full L-BFGS-B formulation is retained for the same parameter vector as an alternative optimizer contract. The likelihood for observed reporting-interval cases is negative binomial:

$$
Y_t \sim \mathrm{NegBin}(\mu_t,r),
$$

with probability parameter

$$
p_t=\frac{r}{r+\mu_t}.
$$

Under this parameterization, $E(Y_t)=\mu_t$ and $\mathrm{Var}(Y_t)=\mu_t+\mu_t^2/r$.

The negative log-likelihood is

$$
-\ell =
-\sum_t
\left[
\log \Gamma(Y_t+r)
-\log \Gamma(r)
-\log \Gamma(Y_t+1)
+r\log p_t
+Y_t\log(1-p_t)
\right].
$$

Reporting-rate priors penalize calibrated reporting probabilities that fall outside country-specific literature-informed bounds. For lower and upper bounds $L_i$ and $U_i$, penalty weight $\xi$ (default 1.0 unless a country profile specifies otherwise), and calibrated probability $p_i^{rep}$,

$$
P_{rep} =
\xi\sum_i
\begin{cases}
\left(\frac{L_i-p_i^{rep}}{U_i-L_i}\right)^2, & p_i^{rep}<L_i,\\
\left(\frac{p_i^{rep}-U_i}{U_i-L_i}\right)^2, & p_i^{rep}>U_i,\\
0, & L_i\le p_i^{rep}\le U_i.
\end{cases}
$$

The retained fit minimizes the negative log-likelihood plus $P_{rep}$. This is a penalized likelihood constraint on reporting probabilities rather than a full Bayesian prior. Calibration results were considered accepted when the optimizer returned a finite solution and the modeled mean annual reported incidence was within the pre-specified relative tolerance of the observed mean over the calibration window.

A separate saved-horizon diagnostic compared annualized model-reported incidence over the 2025-2050 scenario horizon with each profile's recent observed mean reported incidence. This comparison was not included in the calibration likelihood; it is a scenario-horizon diagnostic, not a forecast. It differed from recent observed mean reported incidence by a median across illustrative profiles of 65.00% (IQR, 14.10%-143.40%; range, 6.20%-350.30%), reflecting that the diagnostic summarizes a long scenario horizon with post-2025 dynamics rather than interval-level calibration-window fit.

External age-pattern triangulation used public surveillance summaries that were not calibration targets. In the United States, 2025 provisional surveillance reported infants younger than 1 year as 12.40% of cases (7.50% aged <6 months and 4.90% aged 6-11 months), close to the modeled reported infant share of 14.70%; CDC hospitalization proportions by age (41.20% for <6 months and 9.50% for 6-11 months) also bracketed the model's median infant hospitalization-to-symptomatic-case ratio of 26.30%, although denominators differ [41]. In England, infants younger than 1 year accounted for 6.00% of 2024 laboratory-confirmed cases, below the modeled United Kingdom reported infant share of 19.80% [42]. For EU/EEA surveillance, the 2024 infant notification rate was 318.50 per 100,000, broadly comparable to the Sweden model endpoint of 408.90 per 100,000 infants, but the modeled Sweden infant reported share (15.60%) exceeded the EU/EEA infant case share (10,166 of 209,674 [4.80%]) [43]. Australia reported a school-age-dominated 2024 distribution, with children aged 5 to 14 years comprising 57.00% of cases, whereas the modeled infant reported share was 23.50% [44]. Age-pattern agreement weights were calculated from absolute external-vs-modeled differences scaled by prespecified tolerances; the pass-filter retained profiles with country age-pattern weight of at least 0.50. These checks support severe-infant-risk plausibility but do not externally validate absolute infant rates.

### Scenario analyses and uncertainty evaluation

The scenario analysis had eight linked components, summarized as a study parameter-design matrix in <span style="color:#5DADE2;">eTable 2</span> and interpreted as constrained outcome optimization across program-only, program plus resistance-management, and future product-target decision domains. Vaccine-mechanism profiles contrasted no vaccine, symptom-protective aP-like protection, stronger infection blocking, stronger transmission blocking, and upper-bound high-transmission-blocking protection. Macrolide-resistance analyses were organized into empirically anchored starting-composition baselines, mechanistic stress tests, and implementation-dependent resistance-management modifiers. Country-specific evidence anchors defined starting strain composition for the empirical baseline; fixed low, moderate, high, and very-high resistant fractions were scenario contrasts. A two-dimensional grid varied $\mathrm{VE}_{inf}$ and the initial, target, and importation resistant prevalence together to isolate the interaction between transmission blocking and resistance. A continuous resistance-fitness grid varied $f_{\mathrm{res}}$ from 0.70 to 1.25 and crossed those values with selected $\mathrm{VE}_{inf}$ assumptions; the neutral-fitness value $f_{\mathrm{res}}=1.00$ was retained as a mechanistic stress-test comparator, not an empirically validated base-case forecast. Intervention profiles then modified a nominal coverage floor without timeliness improvement, adolescent boosting, pregnancy Tdap scale-up, close-contact adult adjuncts, targeted high-risk PEP, resistance-guided treatment, and vaccine-mechanism assumptions. A routine-timeliness sensitivity contrasted current practice, nominal coverage-floor changes, timeliness improvements alone, and coverage-floor plus timeliness improvements. A supplementary program-portfolio factorial layered routine timeliness, infant-exposure reduction, targeted high-risk PEP, and resistance-guided management to evaluate feasible combination packages separately from the primary predefined-profile optimization.

The primary optimization objective was to minimize annualized modeled infant symptomatic cases within each country profile and constraint. Secondary objectives were to reduce resistant infections, preserve implementability, and assess robustness under sensitivity analyses. A strategy was considered dominated within a country and constraint if another allowed strategy had at least as large an infant-case reduction, at least as large a resistant-infection reduction, and no greater implementation-intensity score, with improvement in at least one dimension. Implementation intensity was a prespecified ordinal feasibility proxy based on the number and operational complexity of added components; it was used in dominance and visualization, not as a cost, utility, or budget constraint (<span style="color:#5DADE2;">eTable 17</span>). Lambda-weighted preference scores were benefit scores, calculated as `(1 - lambda) x infant-case reduction + lambda x resistant-infection reduction`, with higher scores preferred. Preferred profile outputs report the infant-case-minimizing strategy under each constraint; these outputs are retained as Figure 4 source data, while selected-parameter minimum-regret results are retained as repository CSV files. Reporting-rate sensitivity scenarios perturbed only the observation process, global sensitivity analysis sampled vaccine effects, immunity waning, transmission, treatment, PEP, resistance fitness, and reporting, and the beta-grid interval workflow used deterministic quadrature as a conditional uncertainty analysis.

Uncertainty was organized into four layers. Parameter uncertainty included transmission rate, reporting, vaccine effects, maternal protection duration, contact assumptions, and resistance fitness. Structural uncertainty included age grouping, waning and immune boosting, strain competition, treatment/PEP mechanisms, and deterministic vs stochastic transmission. Data uncertainty included surveillance quality, age-specific reporting, resistance ascertainment, and external age-pattern agreement. Scenario uncertainty included implementation reach, adherence, diagnostic turnaround time, and feasibility. The analyses below map diagnostics to these layers, but they do not constitute a full probabilistic ensemble.

Global sensitivity analysis used a Latin-hypercube design with 48 parameter sets. Parameter-outcome associations were summarized using Pearson, Spearman, and PRCC screening correlations between sampled parameter values and total infant cases, providing measures of direction and relative influence rather than a full variance-decomposition estimate. These runs should therefore be read as optimization-robustness diagnostics, not as posterior uncertainty intervals or formal probabilistic projections [35].

Bayesian uncertainty analysis used the same deterministic ODE model as the scenario analysis, but separated a primary identifiable posterior dimension from weakly identifiable nuisance dimensions. For each country, the posterior density combined a negative binomial reported-case likelihood with a literature-informed prior on $\beta_{\mathrm{sens}}$. The reporting multiplier, $\mathrm{VE}_{sus}$, $\mathrm{VE}_{inf}$, $\mathrm{VE}_{dur}$, relative asymptomatic infectiousness, symptomatic and asymptomatic infectious duration, resistant-strain fitness, and resistance prevalence anchors were fixed at calibrated, literature-informed, or pre-specified baseline values in the primary beta-grid interval analysis because pilot MCMC and slice-sampling runs showed strong $\beta_{\mathrm{sens}}$-reporting-VE coupling. Those nuisance assumptions were evaluated through reporting-rate sensitivity analyses, vaccine-mechanism scenarios, global sensitivity screening, resistance scenarios, and the continuous resistance-fitness grid. Posterior draws were obtained by deterministic quadrature over an adaptive log-$\beta_{\mathrm{sens}}$ grid; a country's posterior was accepted only if both grid edges were at least 20 log-posterior units below the mode, the effective number of grid points was at least 10, and no single grid point carried more than 20% posterior mass. Conditional beta-grid intervals additionally applied the negative-binomial stochastic overlay after scaling the aggregate superspreading dispersion by the number of analysis years, so a 26-year annualized burden estimate was not treated as a single annual observation. The 128-sample selected-parameter Latin-hypercube analysis varied reporting, infant contacts, $\mathrm{VE}_{inf}$, resistant-strain fitness, asymptomatic infectiousness, resistance-management uptake, and PEP reach across 12 strategy profiles; regret was calculated as excess modeled infant cases relative to the best allowed strategy in the same country-sample draw, and standardized regret divided this excess by current-practice modeled infant cases. That selected-parameter regret analysis did not jointly vary infant-exposure strategy implementation, contact-matrix structure, timeliness implementation intensity beyond the fixed timeliness profile, product-specific vaccine efficacy beyond the defined transmission-blocking profiles, or alternative model structures; it is therefore a deterministic optimization-robustness envelope rather than a full probabilistic uncertainty ensemble.

### Model implementation and settings

The model is a deterministic age-structured ODE system with explicit vaccine-history, strain, and treatment states; PEP is applied as a force-of-infection modifier rather than as an explicit prophylaxis compartment. Its core settings are summarized in <span style="color:#5DADE2;">eTable 9</span>, which includes the age partition, strain structure, solver choices, burn-in and analysis horizon, reporting model, and resistance initialization rules. Primary outputs were generated with Python 3.12.3, NumPy 2.4.4, pandas 3.0.3, SciPy 1.17.1, PyYAML 6.0.3, Pydantic 2.13.4, joblib 1.5.3, pyarrow 24.0.0, and SALib 1.5.2; figures were generated with R 4.6.0, ggplot2 4.0.3, dplyr 1.2.1, tidyr 1.3.2, patchwork 1.3.2, and readr 2.2.0. Runtime metadata stored with generated outputs record the repository commit, dirty-worktree flag, configuration hash, dependency versions, row counts, and analysis-specific settings; the joint selected-parameter rank analysis metadata records commit `da453779dd4613832737e5f751a11a80175c2ac6`, dirty-worktree status, configuration hash `044204d3b33e071e238354f04a5bea0297123159a53e258a8027b0914cb29550`, 128 parameter samples, and 15,360 country-strategy-sample rank rows. Principal calibration used the staged bracket-and-bisection search for `transmission.beta_S` with reporting-multiplier adjustment described above, with `maxiter=12`, negative-binomial dispersion `r=50`, and acceptance requiring a finite objective and modeled annualized reported incidence within the pre-specified 25% relative tolerance of the calibration-window mean. The retained full-vector alternative used SciPy L-BFGS-B with `ftol=1e-6` for the same likelihood and penalty structure. Conditional beta-grid intervals required both posterior grid edges to be at least 20 log-posterior units below the mode, an effective grid size of at least 10, and no single grid point carrying more than 20% posterior mass. For stochastic overlays, negative-binomial overdispersion used the NB2 parameterization, with aggregate superspreading dispersion and household-clustering design effects combined before horizon scaling.

### Interpretation limits

The analysis is a mechanistic scenario study with pragmatic country-level calibration, not a full statistical reconstruction of national pertussis transmission. Deterministic compartments do not represent stochastic fadeout, superspreading, household clustering, or individual vaccination histories. The Bayesian workflow propagates conditional $\beta_{\mathrm{sens}}$ posterior uncertainty through the deterministic model and overlays aggregate stochastic dispersion, but does not convert the model into a stochastic individual-based simulation. Country profiles combine directly measured inputs, processed surveillance summaries, and explicitly labelled assumptions; therefore, cross-country differences should be interpreted as conditional contrasts under harmonized model structure. Macrolide-resistance anchors are intentionally conservative where public numeric estimates were unavailable, and resistance and fitness-grid scenarios are designed to evaluate plausible management consequences rather than forecast future clone frequencies.

<div style="page-break-after: always;"></div>
