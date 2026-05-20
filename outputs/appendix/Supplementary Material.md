<div style="text-align:center;">
  <h3 style="font-family: inherit; font-weight: normal; margin-bottom: 0;">Supplementary Materials</h3>
  <h1 style="font-family: inherit; font-weight: bold; font-size: 1.5em;">Pertussis Vaccine Mechanisms, Transmission Blocking, and Macrolide Resistance</h1>
  <br>
  <br>
  Kangguo Li et al. (2026)
</div>

<div style="page-break-after: always;"></div>

## Contents

Materials and Methods.

References.

## Materials and Methods

### Study design

We developed a deterministic age-structured compartmental model of *Bordetella pertussis* transmission to evaluate how vaccine mechanism assumptions and macrolide resistance jointly affect infant disease burden, all-age infection burden, notified cases, resistant infections, and projected epidemiologic intervention rankings. The model follows the mechanistic tradition of pertussis resurgence and immunity-waning models, but extends the state space to include explicit maternal and dose-history origins, two strain classes, country-specific demographic and contact profiles, and resistance-dependent treatment and postexposure prophylaxis (PEP) effects [1-6,19-23].

Ten national profiles were analyzed: Australia, Brazil, China, Japan, New Zealand, South Africa, Sweden, Thailand, the United Kingdom, and the United States. The set is purposive rather than globally representative; it was chosen to maximize contrast in programmatic and resistance assumptions, spanning Western Pacific, South-East Asian, European, Americas, and African settings, large and small population denominators, contrasting booster and maternal-immunization program signatures, heterogeneous reported incidence, and both measured and conservative low macrolide-resistance anchors. Country-specific inputs were derived from United Nations World Population Prospects denominators, WHO/UNICEF Joint Reporting Form and immunization schedule records, all available harmonized pertussis surveillance reporting intervals, Prem/contactdata social-contact matrices, and a macrolide-resistance evidence timeline anchored to the latest admissible evidence year for each country [13-18,21-29]. The principal simulations used a 15-year pre-analysis burn-in to reduce dependence on arbitrary initial conditions, followed by a 26-year analysis horizon beginning on 1 January 2025, with model output retained at 7-day intervals.

All incidence measures are reported as annualized counts per 100,000 persons unless stated otherwise. Infant outcomes combine the 0-2 month and 3-11 month age groups, because these strata jointly capture the highest-risk pre-primary-series and partially vaccinated infant population. Projected intervention ranks are epidemiologic point-estimate ranks; they do not incorporate costs, quality-adjusted life-years, feasibility, equity weights, or full probabilistic rank acceptability.

The supplementary appendix is generated directly from the same analysis pipeline used for the simulations, so the text, figures, and tables remain aligned with the model assumptions. eTable 11 summarizes the fixed model settings and output conventions that govern interpretation [35].

### Country profile construction

Population denominators were aggregated from one-year age groups into eight model strata. Age 0 population was partitioned as 25% aged 0-2 months and 75% aged 3-11 months; ages 1-4 years, 5-9 years, 10-17 years, 18-39 years, 40-64 years, and 65 years or older were then aggregated directly. Let \(N_i\) denote the resulting population in age group \(i\).

Routine and maternal immunization inputs were transformed into age-specific vaccine-origin coverage proxies using DTP1 coverage \(v_1\), DTP3 coverage \(v_3\), maternal coverage \(m\), the number of childhood booster doses \(b\), and an indicator \(A\) for an adolescent booster program:

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

These deterministic transformations assign individuals to mechanistic protection histories and do not imply that adult pertussis immunization coverage is directly observed in all settings. They are coverage-to-state mapping rules that translate DTP1, DTP3, booster, and maternal-program records into the compartment origins needed by the model, informed by evidence that acellular pertussis protection wanes, maternal immunization protects young infants, and schedule history affects age-specific susceptibility and disease presentation [1,7-12].

Seasonal forcing parameters were inferred from the timing of positive reported cases. For observation \(l\), let \(c_l\) be reported cases and \(\theta_l=2\pi(d_l-1)/365\), where \(d_l\) is the day of year. The circular concentration was

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

Multi-year recurrence was treated as a diagnostic forcing component rather than direct evidence of a single causal oscillator. Annual reported-case peaks were identified with a minimum spacing of two years and a prominence threshold equal to 10% of the maximum annual count. A 3-5 year median peak interval was considered compatible with multi-year recurrence; otherwise the multi-year amplitude was set to zero [2,3].

Prem/contactdata matrices were first represented on 5-year age bins and then aggregated to the eight model age groups using population weights [15-17]. If \(P_{ab}\) is the fine-age contact matrix, \(w_{ia}\) is the distribution of age group \(i\) over fine source bin \(a\), and \(f_{jb}\) is the fraction of fine target bin \(b\) belonging to model group \(j\), then

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

This correction preserves the average number of cross-group contacts while ensuring \(N_i\tilde{C}_{ij}=N_j\tilde{C}_{ji}\).

### Age groups, strains, and state variables

The model uses eight age groups:

$$
i \in \mathcal{A} = \{0\text{-}2m,\ 3\text{-}11m,\ 1\text{-}4y,\ 5\text{-}9y,\ 10\text{-}17y,\ 18\text{-}39y,\ 40\text{-}64y,\ 65+y\}.
$$

Pertussis infections are divided into macrolide-sensitive and macrolide-resistant strains:

$$
k \in \mathcal{K} = \{S,R\}.
$$

Susceptible individuals retain vaccine or maternal-protection origin histories:

$$
o \in \mathcal{O} = \{U,\ M,\ D1_R,\ D1_W,\ D2_R,\ D2_W,\ D3_R,\ D3_W\}.
$$

Here \(U\) is unvaccinated, \(M\) is maternally protected, \(D1\) and \(D2\) are one- and two-dose histories, and \(D3\) represents three-or-more-dose histories; subscripts \(R\) and \(W\) denote recent and waned protection.

For each age group, the model tracks susceptible-origin states \(S_{i,o}\), exposed states \(E_{i,k,o}\), symptomatic infectious states \(I^{sym}_{i,k,o}\), asymptomatic infectious states \(I^{asym}_{i,k,o}\), treated infectious states \(T_{i,k,o}\), naturally immune states \(R_i\), and waned-natural-immunity states \(W_i\). The per-age state space contains 8 susceptible-origin states, 16 exposed states, 32 infectious states, 16 treated states, and two natural-immunity states, yielding 74 compartments per age group and 592 dynamic state variables.

### Vaccine mechanism parameterization

Four vaccine mechanism parameters define a scenario:

$$
\mathrm{VE}_{sus},\quad \mathrm{VE}_{sym},\quad \mathrm{VE}_{inf},\quad \mathrm{VE}_{dur}.
$$

These represent reductions in susceptibility to infection, symptomatic disease given infection, onward infectiousness after infection, and infectious duration, respectively. Throughout this appendix, \(\mathrm{VE}_{sus}\) is the model parameter corresponding to protection against infection through reduced susceptibility, whereas \(\mathrm{VE}_{inf}\) is not an infection-acquisition endpoint but a reduction in infectiousness among infected vaccine-history origins. Vaccine effects are origin-specific through a relative effect weight \(w_o \in [0,1]\). The default weights distinguish maternal protection, partial-dose histories, recent three-or-more-dose protection, and waned protection:

$$
w_o =
\begin{cases}
0, & o=U,\\
w_M, & o=M,\\
w_1, & o=D1_R,\\
w_1w_W, & o=D1_W,\\
w_2, & o=D2_R,\\
w_2w_W, & o=D2_W,\\
1, & o=D3_R,\\
w_W, & o=D3_W.
\end{cases}
$$

The origin-specific susceptibility multiplier is

$$
q_o = \max(0, 1 - w_o\mathrm{VE}_{sus}).
$$

The probability that an infection in age group \(i\) and origin \(o\) is symptomatic is

$$
\rho_{i,o} = \mathrm{clip}\{\rho_i(1-w_o\mathrm{VE}_{sym}),0,1\},
$$

where \(\rho_i\) is the age-specific baseline symptom probability. The origin-specific infectiousness multiplier is

$$
\eta_o = \mathrm{clip}(1-w_o\mathrm{VE}_{inf},0,1),
$$

and vaccine shortening of infectious duration is represented by a recovery-rate multiplier

$$
m_o = \left[\max(0.05,1-w_o\mathrm{VE}_{dur})\right]^{-1}.
$$

This formulation separates protection against infection, clinical disease, onward infectiousness, and duration of infectiousness. It therefore permits aP-like profiles with strong protection against symptoms but weak infection or transmission blocking, as well as upper-bound high-transmission-blocking profiles with stronger effects on colonization and transmission [1,5-9].

### Seasonal transmission and force of infection

Let \(N_i(t)\) denote the current population in age group \(i\), and \(C_{ij}\) the country-specific reciprocity-balanced contact rate from age group \(i\) to age group \(j\). Seasonal forcing is country specific:

$$
s(t) = \max\left(0,\left[1+a\cos\left(\frac{2\pi(d(t)-\phi)}{365}\right)\right]\left[1+a_m\cos\left(\frac{2\pi(t-\phi_m)}{365P_m}\right)\right]\right),
$$

where \(a\) and \(\phi\) are annual amplitude and phase, \(d(t)\) is calendar day of year, and the optional multi-year term has amplitude \(a_m\), period \(P_m\), and phase \(\phi_m\). The multi-year component is included only when surveillance-derived peak diagnostics support recurrent 3-5 year structure.

The infectious pressure contributed by age group \(j\) and strain \(k\) is

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

where \(r_A\) is the relative infectiousness of asymptomatic infection. The treated-state infectiousness multiplier is strain-specific:

$$
\zeta_k = 1 - e^{inf}_k,
$$

where \(e^{inf}_k\) is the treatment-associated reduction in infectiousness for strain \(k\). The pre-PEP forces of infection are

$$
\lambda^0_{i,S}(t) = \beta_S s(t)\sum_j C_{ij}\Pi_{j,S}(t),
$$

$$
\lambda^0_{i,R}(t) = \beta_S f_R s(t)\sum_j C_{ij}\Pi_{j,R}(t),
$$

where \(\beta_S\) is the sensitive-strain transmission parameter and \(f_R\) is the resistant-strain relative fitness.

Postexposure prophylaxis is represented as a prevalence-triggered reduction in force of infection. Let

$$
D(t)=
\frac{\sum_i p_i^{det}(t)\sum_{k,o} I^{sym}_{i,k,o}}{\sum_i N_i(t)}
$$

be detected symptomatic prevalence, and

$$
A(t)=\frac{D(t)}{D(t)+h}
$$

the activation function, where \(h\) is the activation prevalence. With PEP coverage \(c_{PEP}\) and strain-specific PEP effectiveness \(e^{PEP}_k\),

$$
\lambda_{i,k}(t)=\lambda^0_{i,k}(t)\left[1-c_{PEP}A(t)e^{PEP}_k\right].
$$

PEP is therefore represented as a force-of-infection modifier rather than as a separate prophylaxis state. PEP-averted cases are calculated as a diagnostic contrast between pre-PEP and post-PEP infection flows, not as an additional compartment.

### Infection progression, treatment, and recovery

New infections from susceptible-origin state \(S_{i,o}\) enter the strain-specific exposed states:

$$
\frac{dE_{i,k,o}}{dt}\bigg|_{infection} = \lambda_{i,k}(t)q_oS_{i,o}.
$$

Let \(\sigma\) be the exposed-to-infectious progression rate, \(\gamma_{sym}\) and \(\gamma_{asym}\) baseline recovery rates, and \(\tau_{sym}\) and \(\tau_{asym}\) treatment rates. The infection progression equations are:

$$
\frac{dE_{i,k,o}}{dt} = \lambda_{i,k}q_oS_{i,o} - \sigma E_{i,k,o},
$$

$$
\frac{dI^{sym}_{i,k,o}}{dt} =
\rho_{i,o}\sigma E_{i,k,o}
- \tau_{sym}I^{sym}_{i,k,o}
- m_o\gamma_{sym}I^{sym}_{i,k,o},
$$

$$
\frac{dI^{asym}_{i,k,o}}{dt} =
(1-\rho_{i,o})\sigma E_{i,k,o}
- \tau_{asym}I^{asym}_{i,k,o}
- m_o\gamma_{asym}I^{asym}_{i,k,o}.
$$

Treated infections follow:

$$
\frac{dT_{i,k,o}}{dt} =
\tau_{sym}I^{sym}_{i,k,o}
+ \tau_{asym}I^{asym}_{i,k,o}
- m_o\gamma^T_kT_{i,k,o},
$$

with

$$
\gamma^T_k =
\frac{\gamma_{sym}}{\max(0.05,1-e^{dur}_k)},
$$

where \(e^{dur}_k\) is the treatment-associated reduction in infectious duration for strain \(k\). Macrolide-resistant infections therefore receive smaller treatment effects unless a resistance-guided strategy modifies the resistant treatment block, consistent with clinical guidance that macrolides are standard first-line agents but trimethoprim-sulfamethoxazole or other alternatives may be considered when resistance is suspected or confirmed [19,20].

Naturally immune states receive all recoveries and wane into a "waned but boostable" state (W) at rate \(\omega_{RW}\). Individuals in W who are re-exposed to circulating pertussis (total force of infection \(\lambda_i^{total} = \lambda_i^S + \lambda_i^R\)) have their immunity restored to R at rate \(\varepsilon\lambda_i^{total}\), where \(\varepsilon\) is the boosting efficiency. Those in W who are not boosted eventually lose all immunity and return to S at rate \(\omega_{WS}\). This SIRWS structure (Lavine et al. 2011; Wearing & Rohani 2009) naturally produces immunity debt during periods of reduced pathogen circulation:

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

When boosting is disabled (\(\varepsilon = 0\)), the model reduces to the legacy waning-only structure with effective waning rate \(\omega_{RW}\) from R through W to S. The key parameters are: \(\omega_{RW} = 1/1825\) day\(^{-1}\) (5-year R→W transition), \(\omega_{WS} = 1/3650\) day\(^{-1}\) (10-year W→S transition), and \(\varepsilon = 0.70\) (boosting efficiency).

### Waning vaccine and maternal protection

Maternal protection wanes into unvaccinated susceptibility at rate \(\omega_M\):

$$
\frac{dS_{i,\mathrm{maternal}}}{dt}\bigg|_{waning}=-\omega_MS_{i,\mathrm{maternal}},
\quad
\frac{dS_{i,\mathrm{unvaccinated}}}{dt}\bigg|_{maternal\ waning}=+\omega_MS_{i,\mathrm{maternal}}.
$$

Recent vaccine-dose states wane into corresponding waned states at rate \(\omega_V\), and waned vaccine states return to unvaccinated susceptibility at rate \(\omega_W\). For each dose category \(d\),

$$
\frac{dS_{i,d,recent}}{dt}\bigg|_{waning}=-\omega_VS_{i,d,recent},
$$

$$
\frac{dS_{i,d,waned}}{dt}\bigg|_{waning}=+\omega_VS_{i,d,recent}-\omega_WS_{i,d,waned},
$$

$$
\frac{dS_{i,\mathrm{unvaccinated}}}{dt}\bigg|_{waned\ loss}=+\omega_WS_{i,d,waned}.
$$

Routine vaccination is implemented as a relaxation toward country-specific age-group coverage targets. For age group \(i\), desired vaccine-origin mass is proportional to current population \(N_i(t)\), target coverage \(v_i\), and target origin distribution \(g_{i,o}\). For vaccine-dose origins, the deficit is

$$
\delta_{i,o}(t)=
\max\left[
0,\ 
\frac{v_iN_i(t)g_{i,o}}{\sum_{o'\in\mathcal{V}}g_{i,o'}}
-S_{i,o}(t)
\right],
$$

where \(\mathcal{V}\) is the set of vaccine-dose origins. The total vaccination flow from unvaccinated susceptibility is

$$
F_i(t)=\min\left[
\kappa_V\sum_{o\in\mathcal{V}}\delta_{i,o}(t),\ S_{i,U}(t)
\right],
$$

and is distributed in proportion to \(\delta_{i,o}(t)\). This formulation prevents vaccination flows from exceeding the available unvaccinated susceptible pool.

Before burn-in, country-specific vaccine coverage initializes susceptible-origin mass using age-specific origin distributions. The default allocation assigns maternal protection to 0-2 month infants, partial-dose histories to 3-11 month infants, and recent or waned three-or-more-dose histories to older age groups. Initial exposed and infectious seeds are allocated by age and by the susceptible-origin shares within each age group, with strains split according to the initial resistance prevalence.

### Resistance initialization and importation

Each resistance scenario specifies a target resistant fraction at the start of the analysis period. Country-timeline targets combine the raw evidence rows listed in eTable 7 with the analysis-year rule described below; fixed targets provide low-to-very-high contrasts for mechanism exploration. After burn-in, active exposed, infectious, and treated compartments are rebalanced so that for every origin and active compartment pair,

$$
X_{i,R,o}^{active} \leftarrow p_R X_{i,\cdot,o}^{active},
\quad
X_{i,S,o}^{active} \leftarrow (1-p_R)X_{i,\cdot,o}^{active},
$$

where \(p_R\) is the target resistant fraction. This separates the intended resistance scenario from strain fixation that can arise during long deterministic burn-in. Country-timeline scenarios use the latest admissible country-specific resistance estimate at or before the anchor year; fixed scenarios use the low, moderate, high, or very-high values specified in eTable 3.

No ongoing prevalence anchoring was applied during the saved analysis period. After the burn-in rebalance, the resistant fraction evolves through differential strain fitness, treatment and PEP effects, susceptible-origin composition, and importation. This separation was used because recent reports show rapid geographic and temporal heterogeneity in macrolide-resistant *B. pertussis*, including high-prevalence Chinese outbreaks, emerging Japanese clusters related to Chinese MRBP, low but detectable Australian resistance in 2024 specimens, and recent public-health alerts in the Americas [21-29].

Low-level importation adds exposed infections at a country-level rate \(u\) per 100,000 persons per year. With age distribution \(a_i^{imp}\) and resistant importation fraction \(p_R^{imp}\),

$$
M_i(t)=\frac{u}{100000 \times 365}N_{\cdot}a_i^{imp},
$$

and imports are distributed across susceptible origins according to their current share of the susceptible-origin pool. The imported exposed flow is \(M_i(t)p_R^{imp}\) for resistant infection and \(M_i(t)(1-p_R^{imp})\) for sensitive infection. Imported infections are subtracted from susceptible-origin pools according to the current origin composition, preserving vaccine-origin accounting.

### Demography and age movement

Demographic turnover keeps country-specific age profiles approximately stationary while allowing cohort movement through the state space. When a country-specific WPP annual trajectory is available, births are supplied by interpolated WPP age-0 inflow, aging proceeds at rates determined by age-bin durations, and a gentle first-order nudge pulls each age group toward the WPP target population to absorb net migration and differential mortality that are not explicit in the ODE. When no trajectory is available (e.g. in unit tests), a fixed-profile fallback is used in which age-exit rates are chosen so that the absolute ageing flow implied by the reference infant age group is compatible with the country-specific age profile. For a generic compartment \(X_i\),

$$
\frac{dX_i}{dt}\bigg|_{ageing} =
-\mu_iX_i + \mu_{i-1}X_{i-1}
$$

for non-youngest age groups. The oldest age group exits at rate \(\mu_A\). In the WPP-driven mode, births enter the youngest group according to the country-specific birth-entry distribution and are independent of the oldest-group outflow. In the fixed-profile mode, total births equal the outflow from the oldest age group. Maternal protection in the youngest infant group is treated as short-lived maternally derived protection and is converted back to unvaccinated susceptibility when infants age out of the 0-2 month group.

### Numerical solution and burn-in

The model is a continuous-time ordinary differential equation system with rates expressed per day. Main simulations were solved using an adaptive Runge-Kutta method with relative tolerance \(10^{-5}\) and absolute tolerance \(10^{-7}\). State values were projected to non-negative values when evaluating rates so that small numerical undershoots could not produce negative force-of-infection, recovery, or vaccination flows.

The main analysis used 15 years of burn-in followed by resistance rebalancing and a 26-year saved analysis period (1 January 2025 through 31 December 2050). Calibration simulations used a shortened burn-in and coarser output interval to reduce computational cost while preserving annual case totals for likelihood evaluation. All summary statistics were computed from the saved analysis interval only.

### Observation model and incidence summaries

Model output records instantaneous daily rates at scheduled output times and converts rates to interval counts by trapezoidal integration. For an interval \([t_{\ell-1},t_\ell]\) and rate \(r(t)\),

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

where \(p_i^{rep}(t)\) is the age-specific final reporting probability, optionally modified by reporting-rate sensitivity scenarios or calibration. Reporting probabilities are clipped to \([0,1]\) after applying any multiplier or time-varying sensitivity scenario.

The reporting model is intentionally separated from the PEP activation term. Reporting-rate sensitivity scenarios modify only \(p_i^{rep}(t)\), whereas PEP activation uses a distinct detection proxy \(p_i^{det}(t)\) defined in the country profile. This prevents surveillance-completeness sensitivity analyses from mechanically changing true transmission or prophylaxis effects. The age-specific reporting priors used during calibration are broad literature-informed bands rather than direct country-specific estimates, because pertussis notification completeness varies by age, care-seeking, diagnostic access, and case definition, and published estimates remain sparse outside selected settings [30-34].

Annualized incidence per 100,000 persons over an analysis period of length \(Y\) years is

$$
I_{all}=\frac{\sum_{t,i,k}C^{inf}_{i,k}(t)}{Y\bar{N}_{\cdot}}100000,
$$

$$
I_{reported}=\frac{\sum_{t,i,k}C^{rep}_{i,k}(t)}{Y\bar{N}_{\cdot}}100000,
$$

$$
I_{infant}=\frac{\sum_{t,i \in \mathcal{I},k}C^{sym}_{i,k}(t)}{Y\bar{N}_{\mathcal{I}}}100000,
$$

where \(\mathcal{I}\) includes the two infant age groups. Relative reduction for an outcome \(Z\) versus comparator \(Z_0\) is

$$
\Delta_Z = 1-\frac{Z}{Z_0}.
$$

### Calibration and likelihood

Country-level calibration targets reported cases over their observed surveillance intervals. The observed series uses the harmonized pertussis surveillance workbook when available, retaining weekly, monthly, annual, and partial-year records with explicit period start and end dates. The calibration window retains the six most recent observed calendar years represented in those intervals, aligns model time to the first retained observed period, and allocates modeled reported cases by calendar-day overlap before comparing observed and modeled interval totals. Annualized incidence summaries are derived from the actual observed coverage days rather than assuming that partial-year records represent complete calendar years.

The full calibration vector can adjust the sensitive-strain transmission coefficient \(\beta_S\), the reporting multiplier, seasonal amplitude, importation rate, and resistant importation fraction:

$$
\theta =
\{\log\beta_S,\ \log m_{rep},\ \mathrm{logit}(a/0.35),\ \log u,\ \mathrm{logit}(p_R^{imp})\}.
$$

The admissible ranges were \(\beta_S\in[0.002,0.2]\), \(m_{rep}\in[0.01,10]\), \(a\in[0,0.35]\), \(u\in[0.01,2]\) imported infections per 100,000 persons per year, and \(p_R^{imp}\in[0,1]\). The principal calibration used a staged search that brackets and bisects \(\beta_S\) against the annualized mean observed reports, followed by a reporting-multiplier adjustment within prior bounds. A full L-BFGS-B formulation is retained for the same parameter vector as an alternative optimizer. The likelihood for observed reporting-interval cases is negative binomial:

$$
Y_t \sim \mathrm{NegBin}(\mu_t,r),
$$

with probability parameter

$$
p_t=\frac{r}{r+\mu_t}.
$$

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

Reporting-rate priors penalize calibrated reporting probabilities that fall outside country-specific literature-informed bounds. For lower and upper bounds \(L_i\) and \(U_i\), penalty weight \(\xi\), and calibrated probability \(p_i^{rep}\),

$$
P_{rep} =
\xi\sum_i
\begin{cases}
\left(\frac{L_i-p_i^{rep}}{U_i-L_i}\right)^2, & p_i^{rep}<L_i,\\
\left(\frac{p_i^{rep}-U_i}{U_i-L_i}\right)^2, & p_i^{rep}>U_i,\\
0, & L_i\le p_i^{rep}\le U_i.
\end{cases}
$$

The retained fit minimizes the negative log-likelihood plus \(P_{rep}\). Calibration results were considered accepted when the optimizer returned a finite solution and the modeled mean annual reported incidence was within the pre-specified relative tolerance of the observed mean over the calibration window.

### Scenario analyses and uncertainty evaluation

The scenario analysis had eight linked components. Vaccine-mechanism scenarios contrasted no vaccine, symptom-protective aP-like protection, stronger infection blocking, stronger transmission blocking, and upper-bound high-transmission-blocking protection. Macrolide-resistance scenarios used either country-specific evidence anchors or fixed low, moderate, high, and very-high resistant fractions. A two-dimensional grid varied \(\mathrm{VE}_{inf}\) and the initial, target, and importation resistant prevalence together to isolate the interaction between transmission blocking and resistance. A continuous resistance-fitness grid varied \(f_R\) from 0.70 to 1.25 and crossed those values with selected \(\mathrm{VE}_{inf}\) assumptions, so the analysis included equal- and higher-fitness resistant strains rather than assuming a persistent resistant-strain penalty. Intervention strategies then modified routine child coverage, the pregnancy Tdap plus adult/household transmission-reduction package, adolescent boosting, resistance-guided treatment, PEP effectiveness, and vaccine-mechanism assumptions. Reporting-rate sensitivity scenarios perturbed only the observation process, global sensitivity analysis sampled vaccine effects, immunity waning, transmission, treatment, PEP, resistance fitness, and reporting, and the Bayesian posterior predictive workflow used deterministic beta-grid quadrature as a conditional uncertainty analysis.

Global sensitivity analysis used a Latin-hypercube design with 48 parameter sets. Parameter-outcome associations were summarized using Pearson correlations between sampled parameter values and total infant cases, providing a screening measure of direction and relative influence rather than a full variance-decomposition estimate. These runs should therefore be read as robustness and scenario-ranking diagnostics, not as posterior uncertainty intervals or formal probabilistic projections [35].

Bayesian uncertainty analysis used the same deterministic ODE model as the scenario analysis, but separated a primary identifiable posterior dimension from weakly identifiable nuisance dimensions. For each country, the posterior density combined a negative binomial reported-case likelihood with a literature-informed prior on \(\beta_S\). The reporting multiplier, \(\mathrm{VE}_{sus}\), \(\mathrm{VE}_{inf}\), \(\mathrm{VE}_{dur}\), relative asymptomatic infectiousness, symptomatic and asymptomatic infectious duration, resistant-strain fitness, and resistance prevalence anchors were fixed at evidence-based calibrated or baseline values in the primary posterior predictive analysis because pilot MCMC and slice-sampling runs showed strong \(\beta_S\)-reporting-VE coupling. Those nuisance assumptions were evaluated through reporting-rate sensitivity analyses, vaccine-mechanism scenarios, global sensitivity screening, resistance scenarios, and the continuous resistance-fitness grid. Posterior draws were obtained by deterministic quadrature over an adaptive log-\(\beta_S\) grid; a country's posterior was accepted only if both grid edges were at least 20 log-posterior units below the mode, the effective number of grid points was at least 10, and no single grid point carried more than 20% posterior mass. Posterior predictive intervals additionally applied the negative-binomial stochastic overlay after scaling the aggregate superspreading dispersion by the number of analysis years, so a 26-year annualized burden estimate was not treated as a single annual observation. Figure 4B used the same horizon-scaled stochastic overlay to annotate deterministic current-vs-intervention reductions with approximate 95% predictive intervals (PI), labelled with JAMA-style interval wording as "95% PI" followed by "lower to upper"; these annotations are not full intervention posterior credible intervals. Main-text 95% credible intervals are reported because all 10 countries passed these pre-specified beta-grid validity checks.

### Model implementation and settings

The model is a deterministic age-structured ODE system with explicit vaccine-history, strain, treatment, and prophylaxis states. Its core settings are summarized in eTable 11, which includes the age partition, strain structure, solver choices, burn-in and analysis horizon, reporting model, and resistance initialization rules. Those settings were chosen so the appendix reflects the epidemiologic structure of the model rather than the mechanics of the file layout used to generate it.

### Interpretation limits

The analysis is a mechanistic scenario study with pragmatic country-level calibration, not a full statistical reconstruction of national pertussis transmission. Deterministic compartments do not represent stochastic fadeout, superspreading, household clustering, or individual vaccination histories. The Bayesian workflow propagates conditional \(\beta_S\) posterior uncertainty through the deterministic model and overlays aggregate stochastic dispersion, but does not convert the model into a stochastic individual-based simulation. Country profiles combine directly measured inputs, processed surveillance summaries, and explicitly labelled assumptions; therefore, cross-country differences should be interpreted as conditional contrasts under harmonized model structure. Macrolide-resistance anchors are intentionally conservative where public numeric estimates were unavailable, and resistance and fitness-grid scenarios are designed to evaluate plausible management consequences rather than forecast future clone frequencies.

## References

1. World Health Organization. Pertussis vaccines: WHO position paper, August 2015. Weekly Epidemiological Record. 2015;90:433-458.
2. Wearing HJ, Rohani P. Estimating the duration of pertussis immunity using epidemiological signatures. PLoS Pathogens. 2009;5:e1000647. doi:10.1371/journal.ppat.1000647.
3. Lavine JS, King AA, Bjornstad ON. Natural immune boosting in pertussis dynamics and the potential for long-term vaccine failure. Proceedings of the National Academy of Sciences. 2011;108:7259-7264. doi:10.1073/pnas.1014394108.
4. Domenech de Celles M, Magpantay FMG, King AA, Rohani P. The impact of past vaccination coverage and immunity on pertussis resurgence. Science Translational Medicine. 2018;10:eaaj1748. doi:10.1126/scitranslmed.aaj1748.
5. Althouse BM, Scarpino SV. Asymptomatic transmission and the resurgence of *Bordetella pertussis*. BMC Medicine. 2015;13:146. doi:10.1186/s12916-015-0382-8.
6. Warfel JM, Zimmerman LI, Merkel TJ. Acellular pertussis vaccines protect against disease but fail to prevent infection and transmission in a nonhuman primate model. Proceedings of the National Academy of Sciences. 2014;111:787-792. doi:10.1073/pnas.1314688110.
7. McGirr A, Fisman DN. Duration of pertussis immunity after DTaP immunization: a meta-analysis. Pediatrics. 2015;135:331-343. doi:10.1542/peds.2014-1729.
8. Chit A, Zivaripiran H, Shin T, Lee JKH, Tomovici A, Macina D, et al. Acellular pertussis vaccines effectiveness over time: a systematic review, meta-analysis and modeling study. PLoS One. 2018;13:e0197970. doi:10.1371/journal.pone.0197970.
9. Klein NP, Bartlett J, Rowhani-Rahbar A, Fireman B, Baxter R. Waning protection after fifth dose of acellular pertussis vaccine in children. New England Journal of Medicine. 2012;367:1012-1019. doi:10.1056/NEJMoa1200850.
10. Amirthalingam G, Andrews N, Campbell H, Ribeiro S, Kara E, Donegan K, et al. Effectiveness of maternal pertussis vaccination in England: an observational study. Lancet. 2014;384:1521-1528. doi:10.1016/S0140-6736(14)60686-3.
11. Amirthalingam G, Campbell H, Ribeiro S, Fry NK, Ramsay M, Miller E, Andrews N. Sustained effectiveness of the maternal pertussis immunization program in England 3 years following introduction. Clinical Infectious Diseases. 2016;63:S236-S243. doi:10.1093/cid/ciw559.
12. Baxter R, Bartlett J, Fireman B, Lewis E, Klein NP. Effectiveness of vaccination during pregnancy to prevent infant pertussis. Pediatrics. 2017;139:e20164091. doi:10.1542/peds.2016-4091.
13. United Nations Department of Economic and Social Affairs, Population Division. World Population Prospects 2024: Summary of Results. New York: United Nations; 2024. https://population.un.org/wpp/.
14. World Health Organization. WHO Immunization Data Portal: WHO/UNICEF Estimates of National Immunization Coverage and Joint Reporting Form data. Geneva: World Health Organization; accessed 2026 May 9. https://immunizationdata.who.int/.
15. Prem K, Cook AR, Jit M. Projecting social contact matrices in 152 countries using contact surveys and demographic data. PLoS Computational Biology. 2017;13:e1005697. doi:10.1371/journal.pcbi.1005697.
16. Prem K, van Zandvoort K, Klepac P, Eggo RM, Davies NG, CMMID COVID-19 Working Group, et al. Projecting contact matrices in 177 geographical regions: an update and comparison with empirical data for the COVID-19 era. PLoS Computational Biology. 2021;17:e1009098. doi:10.1371/journal.pcbi.1009098.
17. Gruson H, Prem K, Cook AR, Jit M. contactdata: Social Contact Matrices for 177 Countries. R package documentation. 2026.
18. Li K. PertussisIncidence surveillance table. GitHub repository. https://github.com/xmusphlkg/PertussisIncidence.
19. Centers for Disease Control and Prevention. Clinical overview of pertussis. Atlanta: CDC; updated 2025; accessed 2026 May 9. https://www.cdc.gov/pertussis/hcp/clinical-overview/index.html.
20. Centers for Disease Control and Prevention. Treatment of pertussis and postexposure antimicrobial prophylaxis. Atlanta: CDC; updated 2025; accessed 2026 May 9. https://www.cdc.gov/pertussis/hcp/clinical-care/index.html.
21. Centers for Disease Control and Prevention. Antibiotic-resistant *Bordetella pertussis*. Atlanta: CDC; updated 2025; accessed 2026 May 9. https://www.cdc.gov/pertussis/hcp/antibiotic-resistance/index.html.
22. European Centre for Disease Prevention and Control. External quality assurance scheme for *Bordetella pertussis* antimicrobial susceptibility testing, 2022. Stockholm: ECDC; 2023.
23. Fu P, Zhou J, Yang C, Nijati Y, Zhou L, Jiang W, et al. Molecular evolution and increasing macrolide resistance of *Bordetella pertussis*, Shanghai, China, 2016-2022. Emerging Infectious Diseases. 2024;30:117-127. doi:10.3201/eid3001.221588.
24. Cai J, Liu Q, Chen B, Jiang Y, Zeng X, Huang J, et al. Waning immunity, prevailing non-vaccine type ptxP3 and macrolide-resistant strains in the 2024 pertussis outbreak in China: a multicentre cross-sectional descriptive study. Lancet Regional Health Western Pacific. 2025;60:101628. doi:10.1016/j.lanwpc.2025.101628.
25. Fong W, Rockett RJ, Tam KKG, Nguyen T, Sim EM, Tay E, et al. Characterisation of *Bordetella pertussis* virulence and macrolide resistance in Australia by targeted culture-independent sequencing: a genomic epidemiology study. Lancet Microbe. 2026;7:101286. doi:10.1016/j.lanmic.2025.101286.
26. Komatsu S, Nakanishi N, Matsubara K, Inenaga Y, Hori M, Shiotani K, et al. Molecular analysis of emerging MT27 macrolide-resistant *Bordetella pertussis*, Kobe, Japan, 2025. Emerging Infectious Diseases. 2026;32:150-153. doi:10.3201/eid3201.250890.
27. Pan American Health Organization. PAHO calls for strengthened vaccination and surveillance amid the spread of antibiotic-resistant pertussis in the Americas. Washington, DC: PAHO; 2025; accessed 2026 May 9. https://www.paho.org/en/news/26-8-2025-paho-calls-strengthened-vaccination-and-surveillance-amid-spread-antibiotic.
28. Li L, Deng J, Ma X, Zhou K, Meng Q, Yuan L, et al. High prevalence of macrolide-resistant *Bordetella pertussis* and ptxP1 genotype, mainland China, 2014-2016. Emerging Infectious Diseases. 2019;25:2205-2214. doi:10.3201/eid2512.181836.
29. Kamachi K, Duong HT, Dang AD, Hai T, Do D, Koide K, et al. Macrolide-resistant *Bordetella pertussis*, Vietnam, 2016-2017. Emerging Infectious Diseases. 2020;26:2511-2513. doi:10.3201/eid2610.201035.
30. Clarkson JA, Fine PEM. The efficiency of measles and pertussis notification in England and Wales. International Journal of Epidemiology. 1985;14:153-168. doi:10.1093/ije/14.1.153.
31. Mark A, Granstrom M. Cumulative incidence of pertussis in an unvaccinated preschool cohort based on notifications, interview and serology. European Journal of Epidemiology. 1991;7:121-126. doi:10.1007/BF00237354.
32. Crowcroft NS, Johnson C, Chen C, Li Y, Marchand-Austin A, Bolotin S, et al. Under-reporting of pertussis in Ontario: a Canadian Immunization Research Network study using capture-recapture. PLoS One. 2018;13:e0195984. doi:10.1371/journal.pone.0195984.
33. Miller E, Fleming DM, Ashworth LA, Mabbett DA, Vurdien JE, Elliott TS. Serological evidence of pertussis in patients presenting with cough in general practice in Birmingham. Communicable Disease and Public Health. 2000;3:132-134.
34. Dai H, He H, Xu J, Zhu Y, Fu T, Chen B, et al. Underestimated incidence rate of pertussis in the community: results from active population-based surveillance in Yiwu, China. Microorganisms. 2024;12:2186. doi:10.3390/microorganisms12112186.
35. World Health Organization. Guidance for using modelling for immunization decision-making. Geneva: World Health Organization; 2026; accessed 2026 May 9. https://iris.who.int/handle/10665/385083.

## eFigures

![eFigure 1](extended_data_figure_1_country_inputs.png)

**eFigure 1. Country-specific input data used to instantiate the ten national pertussis transmission profiles.** **(A)** Vaccine program coverage. DTP1, DTP3, and maternal immunization coverage values used to initialize age-specific vaccine-origin distributions and birth-entry protection. **(B)** Routine schedule timing. Age at first and last routine pertussis-containing dose, with dose count and maternal program status summarizing major differences in immunization schedules. **(C)** Seasonal forcing inputs. Country-specific annual seasonal phase and amplitude derived from processed surveillance time series, with point encodings indicating observed reported-incidence intensity and recurrence support. **(D)** Aggregated contact intensity. Population-weighted contact rates after reconstruction, aggregation, and reciprocity balancing to the eight model age groups.

![eFigure 2](extended_data_figure_2_diagnostics_sensitivity.png)

**eFigure 2. Surveillance, calibration, and robustness diagnostics for the modeled country profiles.** **(A)** Observed surveillance time series. Harmonized reported pertussis incidence used for country input derivation, with weekly, monthly, annual, and partial-year observations annualized by their actual coverage days. **(B)** Calibration diagnostic. Observed reported-case intervals are compared with calibrated model means and approximate predictive intervals for countries with accepted country-level calibrations. **(C)** Reporting-rate sensitivity. Median annualized infection, reported-case, and infant-case incidence under alternative reporting assumptions, illustrating the influence of surveillance ascertainment on absolute burden. **(D)** Global sensitivity analysis. Pearson correlations between sampled parameter values and annualized infant case incidence across the Latin-hypercube sensitivity design.

![eFigure 3](extended_data_figure_3_data_provenance.png)

**eFigure 3. Provenance and preprocessing audit for model inputs and analytical outputs.** **(A)** Source domains. Source entries are grouped by country input data, clinical and mechanistic assumptions, and macrolide-resistance evidence. **(B)** Analysis corpus by processing stage. Raw inputs, harmonized inputs, simulations, summaries, tables, and manuscript-support materials are summarized to document data flow through the analysis. **(C)** Country evidence completeness matrix. Availability of population, surveillance, schedule, contact, seasonality, and resistance inputs is shown for each modeled profile. **(D)** Macrolide-resistance evidence timeline. Country-specific resistance anchors and measured isolate or surveillance fractions are plotted by evidence year, with uncertainty intervals where available.

![eFigure 4](extended_data_figure_4_calibration_diagnostics.png)

**eFigure 4. Country-level calibration acceptance and fit diagnostics.** **(A)** Calibration acceptance and fit score. Accepted country calibrations are summarized with their retained fit scores and optimizer status. **(B)** Observed and calibrated annual reports. Observed annual reported cases are compared with calibrated annual model means and approximate predictive intervals. **(C)** Fitted reporting probabilities by age. Age-specific reporting probabilities retained after calibration are shown relative to prior reporting assumptions. **(D)** Calibrated transmission and interval width. Calibrated transmission rate is plotted against the relative width of the predictive interval to identify countries with broader residual uncertainty.

![eFigure 5](extended_data_figure_5_model_architecture.png)

**eFigure 5. Model architecture, compartment accounting, and vaccine-effect mapping.** **(A)** State-space components. The full ODE system comprises eight age groups, two strains, eight susceptible-origin histories, 74 compartments per age group, and 592 dynamic state variables. **(B)** Compartment block accounting. Per-age compartments are decomposed into susceptible-origin, exposed, infectious, treated, and natural/waned-immunity blocks. **(C)** Vaccine-effect routes. VE_sus, VE_sym, VE_inf, and VE_dur are mapped to susceptibility, symptomatic disease, onward infectiousness, and infectious duration. **(D)** Origin-specific effect weights. Maternal, partial-dose, recent, and waned vaccine histories carry distinct relative effect weights used by all vaccine-mechanism scenarios.

![eFigure 6](extended_data_figure_6_baseline_dynamics.png)

**eFigure 6. Baseline temporal dynamics over the saved analysis period.** **(A)** All-infection incidence at model output time points. Country-specific infection trajectories show recurrent transmission dynamics under the baseline vaccine and resistance assumptions. **(B)** Infant case incidence at model output time points. Symptomatic infant burden is scaled to infant population denominators to highlight country-level differences in risk to the most vulnerable age groups. **(C)** Resistant fraction dynamics. The resistant infection fraction is tracked after burn-in rebalancing to separate scenario initialization from within-analysis strain dynamics. **(D)** Age and strain contribution. The share of infections attributable to each age group and strain summarizes the demographic and resistance composition of baseline transmission.

![eFigure 7](extended_data_figure_7_vaccine_deep_dive.png)

**eFigure 7. Vaccine-mechanism analysis and infection-source decomposition.** **(A)** Vaccine scenario parameter matrix. No-vaccine, aP-like symptom-protective, infection-blocking, transmission-blocking, and upper-bound high-transmission-blocking profiles are compared across VE_sus, VE_sym, VE_inf, and VE_dur. **(B)** Country-specific outcome reductions. Relative reductions in infant cases, reported cases, total infections, and resistant infections are shown for each country-scenario combination. **(C)** Infection-source histories. Median infection shares are decomposed by maternal, dose-1, dose-2, dose-3-plus, and waned source histories. **(D)** Representative vaccine trajectories. Infant case trajectories for Australia and China illustrate how vaccine-mechanism assumptions alter both magnitude and temporal pattern.

![eFigure 8](extended_data_figure_8_resistance_dynamics.png)

**eFigure 8. Macrolide-resistance evidence, initialization, and dynamic consequences.** **(A)** Scenario target versus realized initialization. Fixed resistance scenarios and country-timeline runs are compared with realized starting resistant fractions after burn-in rebalancing. **(B)** Resistant infection burden. Annualized resistant infection incidence is summarized by country and resistance scenario. **(C)** Treatment and PEP event burden. Treated-case and PEP-averted event rates are compared across resistance assumptions to quantify management-related outcome changes. **(D)** Sensitive and resistant strain trajectories. Representative country-timeline trajectories for Australia and China show how initial resistance prevalence, fitness, and importation interact during the saved analysis period.

![eFigure 9](extended_data_figure_9_full_grid.png)

**eFigure 9. Full interaction surface between vaccine transmission blocking and initial resistance prevalence.** **(A)** Country-specific infant burden grid. Annualized infant case incidence is shown for each country across the seven-by-seven grid of VE_inf and initial resistant prevalence. **(B)** Benefit of high transmission blocking. The relative infant-case benefit of increasing VE_inf from the lowest to the highest grid value is displayed by country and resistance prevalence. **(C)** Median burden across countries. Median infant-case and all-infection incidence are summarized across countries over the same parameter grid. **(D)** Threshold for 50% infant-case reduction. The minimum VE_inf required to reduce infant cases by at least 50% relative to the lowest grid value is shown where the threshold is reached.

![eFigure 10](extended_data_figure_10_intervention_extended.png)

**eFigure 10. Extended intervention-strategy outcomes across countries and endpoints.** **(A)** Intervention lever matrix. Each strategy is mapped to the child-coverage, adolescent-booster, maternal-immunization, resistance-guided-treatment, and vaccine-improvement levers it modifies. **(B)** Country-specific outcome reductions. Relative reductions in infant cases, reported cases, total infections, and resistant infections are shown for each strategy and country. **(C)** Current versus combined trajectories. Infant case trajectories compare the current strategy with the combined strategy in Australia and China. **(D)** Intervention rank by country. Strategies are ranked within each country by relative reduction in infant cases, highlighting heterogeneity in priority ordering.

![eFigure 11](extended_data_figure_11_model_structure.png)

**eFigure 11. Compartmental transmission schematic used to define the dynamic state space.** **(A)** Age-omitted transmission schematic. The schematic condenses the full model into one representative age group, showing origin-specific susceptible histories, strain-specific exposed and infectious branches, treated infection states, and retained infection-source histories. The full ODE repeats this template across eight age groups and couples age groups through the contact matrix, demographic ageing, importation, vaccination, and postexposure prophylaxis.

![eFigure 12](extended_data_figure_12_contact_matrix_reconstruction.png)

**eFigure 12. Reconstruction and aggregation of country-specific contact matrices.** The dynamic layout pairs the raw 5-year Prem/contactdata matrix with the reconstructed eight-group model matrix for each country in the standard project order: Australia, China, Japan, New Zealand, Sweden, United Kingdom, United States, Brazil, and Thailand. Reconstructed matrices are population weighted and reciprocity balanced before use in force-of-infection calculations.

![eFigure 13](extended_data_figure_13_resistance_hindcast.png)

**eFigure 13. Resistance hindcast plausibility checks against observed macrolide-resistance trajectories.** **(A)** China hindcast. Modeled resistant fractions are compared with observed resistance prevalence anchors from 2016 through 2024 across resistant-fitness assumptions. **(B)** Japan hindcast. Modeled trajectories are compared with the observed high-prevalence 2024 to 2025 resistance estimate. **(C)** Australia hindcast. Modeled trajectories are compared with low but detectable 2024 resistance, testing whether the model maintains low resistance under neutral fitness and limited importation. **(D)** Hindcast scoring summary. Mean absolute error is summarized by country and fitness value, with the best-fitting fitness value highlighted for each country.

## eTables

<!-- BEGIN ETABLE 1 -->
**eTable 1. Country-specific population, surveillance, vaccination, and seasonal-forcing inputs.**

<!-- Generated from `manuscript_notes/country_profile_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Population | Seasonal phase | Seasonal amplitude | Mean reported incidence per 100k | Vaccine product | Adolescent booster | Maternal program |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | 26,713,206 | 300.45 | 0.1646 | 54.98 | aP | Yes | Yes |
| Brazil | 211,998,565 | 325.83 | 0.18 | 0.8601 | wP | No | Yes |
| China | 1,419,321,285 | 155.34 | 0.2994 | 4.431 | aP | No | No |
| Japan | 123,753,042 | 191.35 | 0.2794 | 7.837 | aP | No | No |
| New Zealand | 5,213,946 | 358.27 | 0.1963 | 25.11 | aP | Yes | Yes |
| South Africa | 64,007,189 | 184.59 | 0.2007 | 2.276 | aP | Yes | Yes |
| Sweden | 10,606,995 | 281.95 | 0.2059 | 5.955 | aP | Yes | Yes |
| Thailand | 71,668,012 | 28.67 | 0.2359 | 0.1977 | wP | No | Yes |
| United Kingdom | 69,138,185 | 133.56 | 0.1959 | 7.268 | aP | No | Yes |
| United States | 345,426,570 | 335.77 | 0.1043 | 1.439 | aP | Yes | Yes |
<!-- END ETABLE 1 -->

<!-- BEGIN ETABLE 2 -->
**eTable 2. Vaccine-mechanism parameterization used in scenario analyses.**

<!-- Generated from `manuscript_notes/scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Scenario | VE_sus | VE_sym | VE_inf | VE_dur | Description |
| --- | --- | --- | --- | --- | --- |
| no_vaccine | 0 | 0 | 0 | 0 | No vaccine protection. |
| symptom_protective | 0.15 | 0.85 | 0.25 | 0 | aP-like disease protection with moderate infection/transmission blocking. VE_inf = 0.25 represents the time-averaged effect of aP vaccination on onward infectiousness, accounting for rapid waning from initial ~50-60% to <10% within 3-5 years post-vaccination (Warfel et al. 2014 baboon model; Althouse & Scarpino 2015; McGirr & Fisman 2015 meta-analysis). This is a population-average across recently and distantly vaccinated individuals. |
| infection_blocking | 0.7 | 0.85 | 0.4 | 0.1 | Stronger reduction in susceptibility to infection. VE_inf = 0.40 represents the upper range of current aP effectiveness against transmission in recently vaccinated individuals. |
| transmission_blocking | 0.3 | 0.85 | 0.55 | 0.3 | Strong reduction in onward infectiousness and duration. Represents an improved aP formulation or wP-like transmission blocking. |
| next_generation | 0.8 | 0.9 | 0.65 | 0.4 | Strong infection, symptom, and transmission protection. Represents an upper-bound high-transmission-blocking pertussis vaccine profile with mucosal immunity induction (e.g. live-attenuated nasal or outer membrane vesicle platforms). |
<!-- END ETABLE 2 -->

<!-- BEGIN ETABLE 3 -->
**eTable 3. Macrolide-resistance initialization, importation, and fitness assumptions.**

<!-- Generated from `manuscript_notes/resistance_scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Scenario | Target resistant fraction | Importation resistant fraction | Anchor rate per year | Country timeline | Fitness_R | Description |
| --- | --- | --- | --- | --- | --- | --- |
| country_timeline | 0.3 | 0.3 | 2 | Yes | 1.000 | Country-specific macrolide resistance prevalence from data/raw/country_resistance_timeline.csv. Fitness set to 1.0 (neutral) based on epidemiological evidence: China MRBP rose from 36% (2016) to near-fixation (>99%, 2024) within 8 years, and the MT28-ptxP3 clone spread to Japan (83-88%, 2024-2025), France, and the US without apparent transmission disadvantage. Rapid fixation is inconsistent with a substantial fitness cost (Fu et al. EID 2024; Cai et al. medRxiv 2025; Fong et al. Lancet Microbe 2026). The fitness_grid and fitness_sensitivity scenarios explore the full range [0.70-1.25]. |
| low | 0.05 | 0.05 | 2 | No | 1.000 | Low macrolide resistance prevalence with fitness-neutral strain. |
| moderate | 0.3 | 0.3 | 2 | No | 1.000 | Moderate macrolide resistance prevalence with fitness-neutral strain. |
| high | 0.7 | 0.7 | 2 | No | 1.000 | High macrolide resistance prevalence with fitness-neutral strain. |
| very_high | 0.95 | 0.95 | 2 | No | 1.000 | Very high macrolide resistance prevalence with fitness-neutral strain. |
| country_timeline_fitness_cost | 0.3 | 0.3 | 2 | Yes | 0.85 | Country-timeline resistance with moderate fitness cost (15%). Retained as a sensitivity scenario representing the traditional assumption that ribosomal mutations impose a growth penalty. Contradicted by the observed rapid fixation in China and Japan but included to bound the optimistic end of resistance projections. |
| country_timeline_fitness_advantage | 0.3 | 0.3 | 2 | Yes | 1.100 | Country-timeline resistance with fitness advantage (10%). The MT28-ptxP3 MRBP clone carries additional virulence-associated alleles (ptxA1, prn- negative, fim3-2) that may confer a selective advantage in partially vaccinated populations (Hu et al. 2025; genomic surveillance studies report co-selection of resistance and vaccine-escape alleles). This scenario tests whether a modest fitness advantage materially changes long-term resistance burden projections. |
| high_fitness_advantage | 0.7 | 0.7 | 2 | No | 1.150 | High resistance prevalence with fitness advantage (15%). Worst-case scenario combining high initial resistance with a fitness-advantaged strain, representing the upper bound of resistant infection burden. Motivated by the observation that MRBP clones in China carry compensatory mutations and virulence factor combinations that may enhance transmissibility in the aP-vaccinated population context. |
<!-- END ETABLE 3 -->

<!-- BEGIN ETABLE 4 -->
**eTable 4. Intervention strategy definitions and modified control levers.**

<!-- Generated from `manuscript_notes/intervention_scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Strategy | Description |
| --- | --- |
| current | Current vaccination and standard macrolide treatment. |
| higher_child_coverage | Increased routine childhood vaccine coverage. |
| adolescent_booster | Additional booster for school-age children and adolescents. |
| maternal_immunization | Pregnancy Tdap-based infant protection package. The package combines short-lived passive antibody protection for newborns, a reproductive-age adult recent-boosting proxy, and cocooning protection. The coverage_updates for young_adult_18_39y represent the fraction of the age group with recently boosted immunity from pregnancy Tdap (~72% uptake among pregnant women, with ~4% of women pregnant per year and boosting lasting ~3-5 years, giving ~10-15% of the age group with recent boosting at any time, added to the baseline ~40% coverage). The contact_matrix_reduction captures the cocooning pathway: vaccinated mothers transmit less to their own infants, reducing the effective contact rate in the mother-infant dyad. Observational studies attribute ~20-30% of total infant protection to this indirect pathway (Amirthalingam et al. 2014; Skoff et al. 2017). |
| resistance_guided_treatment | Resistance testing plus alternative treatment for resistant infections. |
| next_generation_vaccine | Improved transmission-blocking vaccine. |
| combined_strategy | Pregnancy Tdap-based infant protection package, adolescent booster, and resistance-guided treatment. |
<!-- END ETABLE 4 -->

<!-- BEGIN ETABLE 5 -->
**eTable 5. Baseline parameter values, admissible ranges, and evidence provenance.**

<!-- Generated from `manuscript_notes/parameter_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Parameter | Description | Baseline value | Range | Unit | Source or assumption | Sensitivity |
| --- | --- | --- | --- | --- | --- | --- |
| simulation.end_time | Simulation analysis horizon | 9,495.0 | see config/model_settings.yaml sensitivity_parameters | days | pertussis_cycle_model | No |
| simulation.burn_in_years | Pre-analysis burn-in horizon | 60.00 | see config/model_settings.yaml sensitivity_parameters | years | pertussis_cycle_model | No |
| transmission.beta_S | Transmission rate for macrolide-sensitive pertussis | 0.01 | see config/model_settings.yaml sensitivity_parameters | per contact day | pertussis_incidence | No |
| transmission.relative_infectiousness_asymptomatic | Relative infectiousness of asymptomatic infection | 0.35 | see config/model_settings.yaml sensitivity_parameters | ratio | who_pertussis_position | Yes |
| transmission.multi_year_period_years | Target/diagnostic inter-epidemic period | 4.000 | see config/model_settings.yaml sensitivity_parameters | years | pertussis_cycle_model | No |
| transmission.multi_year_amplitude | Weak multi-year phase-locking amplitude | 0 | see config/model_settings.yaml sensitivity_parameters | ratio | pertussis_cycle_model | Yes |
| natural_history.latent_duration | Latent period duration | 8.000 | see config/model_settings.yaml sensitivity_parameters | days | cdc_clinical | No |
| natural_history.infectious_duration_symptomatic | Symptomatic infectious duration | 21.00 | see config/model_settings.yaml sensitivity_parameters | days | cdc_clinical | Yes |
| natural_history.infectious_duration_asymptomatic | Asymptomatic infectious duration | 14.00 | see config/model_settings.yaml sensitivity_parameters | days | cdc_clinical | Yes |
| natural_history.recovered_immunity_duration | Duration of post-infection protection | 3,285.0 | see config/model_settings.yaml sensitivity_parameters (reciprocal of rates.waning_natural) | days | cdc_clinical | Yes |
| natural_history.vaccine_protection_duration | Duration of vaccine-derived protection proxy | 1,825.0 | see config/model_settings.yaml sensitivity_parameters (reciprocal of rates.waning_vaccine) | days | ap_waning_meta_analysis | Yes |
| treatment.treatment_rate_symptomatic | Daily transition from symptomatic infection to treatment | 0.025 | see config/model_settings.yaml sensitivity_parameters | per day | cdc_treatment_pep | Yes |
| PEP.coverage_household_contacts | Dynamic PEP coverage ceiling among close contacts | 0.3 | see config/model_settings.yaml sensitivity_parameters | proportion | cdc_treatment_pep | Yes |
<!-- END ETABLE 5 -->

<!-- BEGIN ETABLE 6 -->
**eTable 6. Reporting-rate sensitivity scenarios used to probe surveillance uncertainty.**

<!-- Generated from `manuscript_notes/reporting_scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Scenario | Multiplier | Age multipliers | Time variation | Description |
| --- | --- | --- | --- | --- |
| medium | 1.000 | No | No | Reporting-rate sensitivity assumption. |
| high | 1.500 | No | No | Reporting-rate sensitivity assumption. |
| low | 0.5 | No | No | Reporting-rate sensitivity assumption. |
| age_biased |  | Yes | No | Reporting-rate sensitivity assumption. |
| time_varying | 1.000 | No | Yes | Reporting-rate sensitivity assumption. |
| infant_high_adult_very_low |  | Yes | No | Reporting-rate sensitivity assumption. |
| infant_moderate_adult_minimal |  | Yes | No | Reporting-rate sensitivity assumption. |
| enhanced_surveillance |  | Yes | No | Reporting-rate sensitivity assumption. |
| adult_focused_improvement |  | Yes | No | Reporting-rate sensitivity assumption. |
| china_passive_system |  | Yes | No | Reporting-rate sensitivity assumption. |
<!-- END ETABLE 6 -->

<!-- BEGIN ETABLE 7 -->
**eTable 7. Country-specific macrolide-resistance evidence used for resistance anchoring.**

<!-- Generated from `data/raw/country_resistance_timeline.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | ISO3 | Year | Sample size | Resistant fraction | Lower | Upper | Evidence type | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | AUS | 2024 | 188 | 0.043 | 0.019 | 0.082 | measured_national_genomic_surveillance_fraction | https://doi.org/10.1016/j.lanmic.2025.101286 |
| Brazil | BRA | 2025 |  | 0.01 | 0 | 0.05 | low_detected_model_anchor | https://www.paho.org/en/news/26-8-2025-paho-calls-strengthened-vaccination-and-surveillance-amid-spread-antibiotic |
| China | CHN | 2016 |  | 0.364 | 0.28 | 0.45 | measured_regional_isolate_fraction | https://wwwnc.cdc.gov/eid/article/30/1/22-1588_article |
| China | CHN | 2022 |  | 0.972 | 0.94 | 0.99 | measured_regional_isolate_fraction | https://wwwnc.cdc.gov/eid/article/30/1/22-1588_article |
| China | CHN | 2024 | 394 | 0.997 | 0.986 | 1.000 | measured_multicenter_isolate_fraction | https://www.sciencedirect.com/science/article/pii/S2666606525001658 |
| Japan | JPN | 2024 | 8 | 0.875 | 0.473 | 0.997 | measured_regional_case_series_fraction | https://www.sciencedirect.com/science/article/pii/S1341321X26000140 |
| Japan | JPN | 2025 | 52 | 0.827 | 0.697 | 0.918 | measured_multicenter_isolate_fraction | https://www.mdpi.com/2227-9059/14/1/167 |
| New Zealand | NZL | 1995 | 88 | 0 | 0 | 0.041 | measured_historical_national_isolate_fraction | https://pubmed.ncbi.nlm.nih.gov/9579709/ |
| New Zealand | NZL | 2025 |  | 0.01 | 0 | 0.05 | low_detected_model_anchor | https://www.tewhatuora.govt.nz/for-health-professionals/clinical-guidance/communicable-disease-control-manual/pertussis |
| South Africa | ZAF | 2025 |  | 0.02 | 0.005 | 0.05 | global_surveillance_extrapolation | https://www.cdc.gov/pertussis/hcp/antibiotic-resistance/; https://www.mdpi.com/2079-6382/11/11/1570 |
| Sweden | SWE | 2025 |  | 0.01 | 0 | 0.05 | low_imported_model_anchor | https://www.folkhalsomyndigheten.se/contentassets/975cc036216b48a39b7bf34319d4ecee/pertussis-surveillance-sweden-23rd-annual-report.pdf |
| Thailand | THA | 2025 |  | 0.01 | 0 | 0.05 | low_imported_model_anchor | https://www.cdc.gov/pertussis/hcp/antibiotic-resistance/index.html |
| United Kingdom | GBR | 2009 | 583 | 0 | 0 | 0.006 | measured_historical_national_isolate_fraction | https://researchportal.ukhsa.gov.uk/en/publications/antimicrobial-susceptibility-testing-of-historical-and-recent-cli/ |
| United Kingdom | GBR | 2024 | 661 | 0.003 | 0 | 0.011 | measured_national_surveillance_fraction | https://www.postersessiononline.eu/173580348_eu/congresos/UKHSA2025/aula/-P_58_UKHSA2025.pdf |
| United States | USA | 1997 | 47 | 0.021 | 0.001 | 0.113 | measured_regional_isolate_fraction | https://pubmed.ncbi.nlm.nih.gov/9350776/ |
| United States | USA | 2015 | 1,208 | 0 | 0 | 0.003 | measured_multistate_surveillance_fraction | https://www.walshmedicalmedia.com/conference-abstracts-files/2155-9597.C1.016-015.pdf |
<!-- END ETABLE 7 -->

<!-- BEGIN ETABLE 8 -->
**eTable 8. Calibration acceptance, absolute-fit diagnostics, and fitted transmission parameters.**

<!-- Generated from `outputs/tables/calibration_all_countries.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Accepted | Optimizer success | Fit status | Observed reported incidence per 100k | Model reported incidence per 100k | Model/observed ratio | Data fit score | Fit score | Calibrated beta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | Yes | Yes | calibrated_to_reported_cases | 61.49 | 61.76 | 1.005 | 8,790.0 | 8,790.0 | 0.0231 |
| Brazil | Yes | Yes | calibrated_to_reported_cases | 0.9975 | 0.9728 | 0.9752 | 3,231.6 | 3,231.6 | 0.009043 |
| China | Yes | Yes | calibrated_to_reported_cases | 7.037 | 7.267 | 1.033 | 5,733.0 | 5,733.1 | 0.009717 |
| Japan | Yes | Yes | calibrated_to_reported_cases | 12.57 | 14.29 | 1.137 | 7,398.0 | 7,398.0 | 0.0119 |
| New Zealand | Yes | Yes | calibrated_to_reported_cases | 19.15 | 19.23 | 1.004 | 852.71 | 852.71 | 0.015 |
| South Africa | Yes | Yes | calibrated_to_reported_cases | 2.276 | 2.143 | 0.9415 | 429.24 | 429.24 | 0.009416 |
| Sweden | Yes | Yes | calibrated_to_reported_cases | 6.299 | 6.522 | 1.035 | 1,911.2 | 1,911.2 | 0.01105 |
| Thailand | Yes | Yes | calibrated_to_reported_cases | 0.4605 | 0.4797 | 1.042 | 1,150.2 | 1,150.2 | 0.009217 |
| United Kingdom | Yes | Yes | calibrated_to_reported_cases | 9.553 | 9.916 | 1.038 | 7,711.5 | 7,711.5 | 0.015 |
| United States | Yes | Yes | calibrated_to_reported_cases | 1.394 | 1.415 | 1.014 | 6,377.9 | 6,377.9 | 0.009501 |
<!-- END ETABLE 8 -->

<!-- BEGIN ETABLE 9 -->
**eTable 9. Intervention outcome summaries by country and strategy.**

<!-- Generated from `outputs/summaries/intervention_scenarios_summary.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Strategy | Total infections | Reported cases | Infant cases | Resistant infections | Infant-case reduction | Infection reduction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | adolescent_booster | 23,703,692 | 364,020 | 201,802 | 22,256,086 | 0.0002906 | 0.0002224 |
| Australia | combined_strategy | 19,000,707 | 241,148 | 100,416 | 4,690,889 | 0.5025 | 0.1986 |
| Australia | current | 23,708,963 | 364,096 | 201,861 | 22,263,371 | 0 | 0 |
| Australia | higher_child_coverage | 23,708,672 | 367,223 | 210,084 | 22,266,792 | -0.04073 | 1.23e-05 |
| Australia | maternal_adult_boosting_only | 24,058,210 | 367,657 | 205,396 | 22,653,449 | -0.01751 | -0.01473 |
| Australia | maternal_cocooning_only | 23,691,297 | 360,296 | 193,393 | 22,236,370 | 0.04195 | 0.0007451 |
| Australia | maternal_direct_antibody_only | 23,716,125 | 360,436 | 200,663 | 22,261,351 | 0.005937 | -0.0003021 |
| Australia | maternal_immunization | 24,039,453 | 359,866 | 195,445 | 22,598,330 | 0.03179 | -0.01394 |
| Australia | next_generation_vaccine | 19,834,824 | 254,777 | 117,943 | 17,131,100 | 0.4157 | 0.1634 |
| Australia | resistance_guided_treatment | 22,231,209 | 326,439 | 168,319 | 6,610,781 | 0.1662 | 0.06233 |
| Brazil | adolescent_booster | 615,207 | 9,514.9 | 2,487.2 | 8,788.7 | 0.7892 | 0.7919 |
| Brazil | combined_strategy | 43,120.6 | 650.53 | 171.07 | 382.84 | 0.9855 | 0.9854 |
| Brazil | current | 2,956,879 | 46,757.5 | 11,801.2 | 137,405 | 0 | 0 |
| Brazil | higher_child_coverage | 3,412,049 | 54,457.0 | 13,916.1 | 192,020 | -0.1792 | -0.1539 |
| Brazil | maternal_adult_boosting_only | 463,960 | 7,221.8 | 1,862.5 | 6,099.7 | 0.8422 | 0.8431 |
| Brazil | maternal_cocooning_only | 2,757,585 | 43,238.2 | 10,348.8 | 116,867 | 0.1231 | 0.0674 |
| Brazil | maternal_direct_antibody_only | 2,923,305 | 45,865.3 | 11,437.9 | 132,654 | 0.03078 | 0.01135 |
| Brazil | maternal_immunization | 441,745 | 6,770.0 | 1,644.0 | 5,718.5 | 0.8607 | 0.8506 |
| Brazil | next_generation_vaccine | 48,195.8 | 725.06 | 199.39 | 499.64 | 0.9831 | 0.9837 |
| Brazil | resistance_guided_treatment | 1,244,675 | 19,613.2 | 4,920.2 | 4,324.7 | 0.5831 | 0.5791 |
| China | adolescent_booster | 130,662,073 | 5,328,231 | 463,694 | 130,618,789 | 0.2471 | 0.2669 |
| China | combined_strategy | 552,634 | 21,365.1 | 1,623.3 | 550,673 | 0.9974 | 0.9969 |
| China | current | 178,244,151 | 7,455,036 | 615,909 | 178,195,300 | 0 | 0 |
| China | higher_child_coverage | 179,500,677 | 7,535,480 | 634,423 | 179,452,275 | -0.03006 | -0.007049 |
| China | maternal_adult_boosting_only | 101,857,400 | 4,137,140 | 349,802 | 101,813,627 | 0.4321 | 0.4286 |
| China | maternal_cocooning_only | 175,853,701 | 7,322,276 | 574,306 | 175,804,762 | 0.06755 | 0.01341 |
| China | maternal_direct_antibody_only | 176,146,628 | 7,301,609 | 569,517 | 176,097,366 | 0.07532 | 0.01177 |
| China | maternal_immunization | 99,055,593 | 3,972,800 | 301,889 | 99,011,235 | 0.5098 | 0.4443 |
| China | next_generation_vaccine | 1,126,669 | 43,865.0 | 3,542.2 | 1,123,520 | 0.9942 | 0.9937 |
| China | resistance_guided_treatment | 91,979,850 | 3,821,289 | 305,719 | 70,888,041 | 0.5036 | 0.484 |
| Japan | adolescent_booster | 27,126,238 | 421,076 | 83,012.1 | 26,778,021 | 0.03691 | 0.0402 |
| Japan | combined_strategy | 262,084 | 3,627.3 | 568.52 | 184,024 | 0.9934 | 0.9907 |
| Japan | current | 28,262,454 | 444,912 | 86,193.9 | 27,892,984 | 0 | 0 |
| Japan | higher_child_coverage | 28,342,658 | 448,252 | 87,828.9 | 27,973,715 | -0.01897 | -0.002838 |
| Japan | maternal_adult_boosting_only | 21,609,868 | 327,595 | 64,035.2 | 21,277,273 | 0.2571 | 0.2354 |
| Japan | maternal_cocooning_only | 28,189,436 | 440,333 | 80,958.4 | 27,818,620 | 0.06074 | 0.002584 |
| Japan | maternal_direct_antibody_only | 28,225,971 | 437,903 | 79,874.0 | 27,852,933 | 0.07332 | 0.001291 |
| Japan | maternal_immunization | 21,480,491 | 318,643 | 55,788.6 | 21,143,441 | 0.3528 | 0.24 |
| Japan | next_generation_vaccine | 6,952,510 | 100,566 | 17,745.0 | 6,721,798 | 0.7941 | 0.754 |
| Japan | resistance_guided_treatment | 20,682,848 | 320,933 | 59,397.1 | 11,569,481 | 0.3109 | 0.2682 |
| New Zealand | adolescent_booster | 3,299,380 | 50,856.8 | 21,881.6 | 2,949,680 | -0.002729 | -0.002268 |
| New Zealand | combined_strategy | 1,734,772 | 22,653.4 | 7,591.4 | 11,646.8 | 0.6521 | 0.473 |
| New Zealand | current | 3,291,916 | 50,717.4 | 21,822.1 | 2,942,347 | 0 | 0 |
| New Zealand | higher_child_coverage | 3,307,603 | 51,401.9 | 22,521.4 | 2,958,680 | -0.03204 | -0.004765 |
| New Zealand | maternal_adult_boosting_only | 3,169,538 | 47,917.3 | 20,628.7 | 2,824,768 | 0.05469 | 0.03718 |
| New Zealand | maternal_cocooning_only | 3,284,792 | 50,158.7 | 20,816.8 | 2,933,481 | 0.04607 | 0.002164 |
| New Zealand | maternal_direct_antibody_only | 3,278,429 | 49,785.3 | 21,126.0 | 2,926,194 | 0.0319 | 0.004097 |
| New Zealand | maternal_immunization | 3,149,067 | 46,524.1 | 19,079.0 | 2,799,778 | 0.1257 | 0.04339 |
| New Zealand | next_generation_vaccine | 1,680,745 | 21,509.3 | 8,136.2 | 1,339,246 | 0.6272 | 0.4894 |
| New Zealand | resistance_guided_treatment | 2,898,683 | 43,267.9 | 17,546.6 | 69,473.9 | 0.1959 | 0.1195 |
| South Africa | adolescent_booster | 308,577 | 4,678.5 | 1,783.7 | 12,275.3 | 0.8675 | 0.8696 |
| South Africa | combined_strategy | 12,322.2 | 175.40 | 59.55 | 217.79 | 0.9956 | 0.9948 |
| South Africa | current | 2,367,000 | 36,536.3 | 13,465.4 | 853,554 | 0 | 0 |
| South Africa | higher_child_coverage | 1,311,484 | 19,292.3 | 6,913.8 | 214,845 | 0.4866 | 0.4459 |
| South Africa | maternal_adult_boosting_only | 723,777 | 11,136.6 | 4,126.6 | 64,067.2 | 0.6935 | 0.6942 |
| South Africa | maternal_cocooning_only | 2,218,749 | 33,952.6 | 11,930.7 | 738,885 | 0.114 | 0.06263 |
| South Africa | maternal_direct_antibody_only | 1,683,310 | 24,994.2 | 8,190.2 | 389,169 | 0.3918 | 0.2888 |
| South Africa | maternal_immunization | 422,390 | 6,196.8 | 1,952.4 | 21,153.6 | 0.855 | 0.8216 |
| South Africa | next_generation_vaccine | 12,859.1 | 199.47 | 83.03 | 267.20 | 0.9938 | 0.9946 |
| South Africa | resistance_guided_treatment | 1,044,265 | 16,150.2 | 5,915.9 | 4,073.3 | 0.5607 | 0.5588 |
| Sweden | adolescent_booster | 2,499,441 | 36,235.1 | 10,653.2 | 1,939,412 | 3.212e-05 | 8.172e-06 |
| Sweden | combined_strategy | 11,624.3 | 151.32 | 38.68 | 81.59 | 0.9964 | 0.9953 |
| Sweden | current | 2,499,462 | 36,232.5 | 10,653.5 | 1,939,413 | 0 | 0 |
| Sweden | higher_child_coverage | 2,492,302 | 36,305.8 | 11,110.4 | 1,933,897 | -0.04289 | 0.002864 |
| Sweden | maternal_adult_boosting_only | 2,107,513 | 30,040.5 | 8,874.4 | 1,567,275 | 0.167 | 0.1568 |
| Sweden | maternal_cocooning_only | 2,477,141 | 35,611.6 | 10,006.4 | 1,915,233 | 0.06074 | 0.00893 |
| Sweden | maternal_direct_antibody_only | 2,442,416 | 34,958.4 | 10,326.5 | 1,878,236 | 0.0307 | 0.02282 |
| Sweden | maternal_immunization | 2,042,451 | 28,509.6 | 8,099.9 | 1,496,213 | 0.2397 | 0.1828 |
| Sweden | next_generation_vaccine | 4,964.4 | 64.32 | 18.71 | 52.56 | 0.9982 | 0.998 |
| Sweden | resistance_guided_treatment | 1,874,157 | 26,746.3 | 7,566.7 | 4,146.2 | 0.2897 | 0.2502 |
| Thailand | adolescent_booster | 198,336 | 2,826.1 | 664.62 | 2,619.8 | 0.7031 | 0.7081 |
| Thailand | combined_strategy | 16,993.8 | 232.68 | 51.12 | 151.08 | 0.9772 | 0.975 |
| Thailand | current | 679,557 | 9,868.8 | 2,238.9 | 17,517.7 | 0 | 0 |
| Thailand | higher_child_coverage | 738,534 | 10,788.9 | 2,413.1 | 20,758.5 | -0.07779 | -0.08679 |
| Thailand | maternal_adult_boosting_only | 130,853 | 1,868.7 | 438.39 | 1,575.7 | 0.8042 | 0.8074 |
| Thailand | maternal_cocooning_only | 642,667 | 9,263.0 | 1,995.2 | 15,745.9 | 0.1088 | 0.05428 |
| Thailand | maternal_direct_antibody_only | 643,950 | 9,214.1 | 1,930.8 | 15,760.0 | 0.1376 | 0.0524 |
| Thailand | maternal_immunization | 124,111 | 1,734.7 | 358.62 | 1,478.6 | 0.8398 | 0.8174 |
| Thailand | next_generation_vaccine | 21,620.7 | 299.69 | 74.03 | 224.85 | 0.9669 | 0.9682 |
| Thailand | resistance_guided_treatment | 321,326 | 4,659.1 | 1,054.0 | 1,393.3 | 0.5292 | 0.5272 |
| United Kingdom | adolescent_booster | 35,235,664 | 564,131 | 229,297 | 30,152,692 | -0.01071 | -0.01073 |
| United Kingdom | combined_strategy | 11,313,692 | 150,347 | 47,285.4 | 7,687.3 | 0.7916 | 0.6755 |
| United Kingdom | current | 34,861,762 | 558,047 | 226,868 | 29,678,350 | 0 | 0 |
| United Kingdom | higher_child_coverage | 35,323,850 | 570,968 | 236,292 | 30,160,000 | -0.04154 | -0.01325 |
| United Kingdom | maternal_adult_boosting_only | 31,190,722 | 483,109 | 195,992 | 26,104,017 | 0.1361 | 0.1053 |
| United Kingdom | maternal_cocooning_only | 34,699,611 | 549,685 | 213,823 | 29,485,410 | 0.0575 | 0.004651 |
| United Kingdom | maternal_direct_antibody_only | 34,622,029 | 546,214 | 218,553 | 29,377,936 | 0.03665 | 0.006877 |
| United Kingdom | maternal_immunization | 30,958,302 | 468,177 | 179,261 | 25,787,082 | 0.2098 | 0.112 |
| United Kingdom | next_generation_vaccine | 16,923,385 | 231,056 | 80,711.9 | 12,007,283 | 0.6442 | 0.5146 |
| United Kingdom | resistance_guided_treatment | 29,924,750 | 466,834 | 178,558 | 69,932.2 | 0.2129 | 0.1416 |
| United States | adolescent_booster | 7,650,433 | 121,682 | 30,612.3 | 0 | -0.02116 | -0.0211 |
| United States | combined_strategy | 82,614.0 | 1,279.7 | 324.75 | 0 | 0.9892 | 0.989 |
| United States | current | 7,492,343 | 119,170 | 29,977.9 | 0 | 0 | 0 |
| United States | higher_child_coverage | 7,509,394 | 120,142 | 31,459.1 | 0 | -0.04941 | -0.002276 |
| United States | maternal_adult_boosting_only | 2,461,613 | 38,711.9 | 9,820.8 | 0 | 0.6724 | 0.6714 |
| United States | maternal_cocooning_only | 7,161,747 | 112,957 | 27,016.0 | 0 | 0.0988 | 0.04412 |
| United States | maternal_direct_antibody_only | 6,888,976 | 108,310 | 27,401.1 | 0 | 0.08596 | 0.08053 |
| United States | maternal_immunization | 2,199,605 | 33,945.4 | 8,246.3 | 0 | 0.7249 | 0.7064 |
| United States | next_generation_vaccine | 56,898.5 | 879.91 | 253.16 | 0 | 0.9916 | 0.9924 |
| United States | resistance_guided_treatment | 3,728,369 | 59,054.9 | 14,763.2 | 0 | 0.5075 | 0.5024 |
<!-- END ETABLE 9 -->

<!-- BEGIN ETABLE 10 -->
**eTable 10. Model-derived outcomes and summary definitions.**

<!-- Generated from `static outcome definitions` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Quantity | Definition | Denominator or reference population | Primary use |
| --- | --- | --- | --- |
| Total infections | Symptomatic plus asymptomatic incident infections integrated over the analysis interval; treated infections are counted at infection onset, not as a separate new infection. | Mean total population over the interval. | Overall transmission burden. |
| Reported cases | Symptomatic incident infections multiplied by age-specific reporting probabilities and integrated over the analysis interval. | Mean total population over the interval. | Calibration target and surveillance-comparable burden. |
| Infant cases | Symptomatic incident infections in the 0-2 month and 3-11 month age groups. | Mean population in the two infant age groups. | Primary severe-risk outcome. |
| Resistant infections | Total incident infections attributed to the macrolide-resistant strain. | Mean total population over the interval. | Resistance burden and treatment relevance. |
| Resistant fraction | For interval summaries, resistant incident infections divided by all incident infections; for start/end strain dynamics, resistant active exposed, infectious, and treated compartments divided by all active strain-specific compartments. | Total infections or active infected compartments, depending on summary. | Strain-composition diagnostic. |
| PEP-averted cases | Difference between pre-PEP and post-PEP symptomatic infection flows under the same state trajectory. | Not a population-normalized compartment count unless explicitly annualized. | Diagnostic estimate of prophylaxis effect. |
| Relative reduction | 1 - Z/Z0, where Z is the scenario outcome and Z0 is the comparator outcome. | Scenario-specific comparator. | Cross-scenario intervention comparison. |
<!-- END ETABLE 10 -->

<!-- BEGIN ETABLE 11 -->
**eTable 11. Core model settings and implementation choices.**

<!-- Generated from `configuration summary derived from the analysis pipeline` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Aspect | Setting | Value |
| --- | --- | --- |
| Model class | Deterministic age-structured compartmental ODE | Two strains, country-specific demographics, vaccination histories, treatment, and PEP are tracked explicitly. |
| Age structure | Eight model age groups | 0-2 months, 3-11 months, 1-4 years, 5-9 years, 10-17 years, 18-39 years, 40-64 years, and 65 years or older. |
| Strain structure | Two strain classes | Macrolide-sensitive and macrolide-resistant strains are simulated separately. |
| Vaccine-history structure | Explicit origin states | Unvaccinated, maternally protected, dose-1 recent/waned, dose-2 recent/waned, and dose-3-plus recent/waned states retain distinct effects. |
| Burn-in and horizon | Long burn-in plus analysis window | Fifteen-year burn-in followed by a 26-year analysis period beginning on 1 January 2025. |
| Time scale | Daily rates with weekly saved output | All state equations are evaluated in days, and output is stored every 7 days for downstream summaries. |
| Numerical solver | Adaptive Runge-Kutta integration | RK45 with relative tolerance 1e-5 and absolute tolerance 1e-7. |
| Seasonality | Annual cosine forcing | A 4-year diagnostic term is available when surveillance peaks support multi-year recurrence. |
| Demography | WPP trajectory-driven age turnover | Births and aging are driven by UN World Population Prospects 2024 annual trajectories with gentle nudging toward target age profiles; a fixed-profile fallback is retained for tests. |
| Observation model | Age-specific reporting probabilities | Reporting completeness affects observed cases, while PEP activation uses a separate detection proxy. |
| Calibration target | Reported surveillance intervals | The fit uses a negative binomial likelihood and requires the retained solution to match the observed annualized mean within tolerance. |
| Resistance anchoring | Evidence-based initialization | Country-specific anchors use the latest admissible evidence through 2025, with low-level importation preventing deterministic extinction. |
| Sensitivity screening | Latin-hypercube screening | Forty-eight parameter sets were used for Pearson-correlation robustness screening, separate from posterior inference. |
| Bayesian uncertainty | Beta-grid posterior predictive analysis with pre-specified checks | A negative binomial reported-case likelihood and literature-informed priors define the beta_S posterior, with weakly identifiable nuisance parameters fixed at evidence-based calibrated values; 95% CrI are used only if beta-grid tail and quadrature-resolution checks pass. |
| Resistance fitness stress test | Continuous fitness_R grid | Macrolide-resistant strain fitness is varied from 0.70 to 1.25 and crossed with vaccine infectiousness-effect assumptions. |
<!-- END ETABLE 11 -->

<!-- BEGIN ETABLE 12 -->
**eTable 12. Bayesian uncertainty priors and fixed nuisance settings for the beta-grid posterior predictive analysis.**

<!-- Generated from `manuscript_notes/bayesian_prior_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Parameter | Prior | Interpretation |
| --- | --- | --- |
| log_beta_S | Normal(log calibrated beta_S, 0.5) | Primary uncertain transmission parameter integrated by deterministic log-beta grid quadrature. |
| log_reporting_multiplier | Fixed at calibrated/evidence value in primary beta-grid analysis | Weakly identifiable with beta_S and therefore fixed in the conditional beta-grid posterior workflow; explored through reporting-rate sensitivity analyses. |
| VE_sus | Fixed at evidence-based aP profile value in primary beta-grid analysis | Weakly identifiable with beta_S and reporting; scenario and sensitivity analyses vary vaccine susceptibility protection. |
| VE_inf | Fixed at evidence-based aP profile value in primary beta-grid analysis | Weakly identifiable with beta_S and reporting; vaccine-mechanism, VE_inf-resistance, and fitness-grid analyses vary onward-infectiousness protection. |
| VE_dur | Fixed at evidence-based aP profile value in primary beta-grid analysis | Vaccine duration effects are fixed in the posterior predictive analysis and varied through vaccine-mechanism scenarios. |
| relative_infectiousness_asymptomatic | Fixed at literature-informed baseline in primary beta-grid analysis | High-impact but weakly identifiable nuisance parameter; varied in Latin-hypercube sensitivity screening. |
| infectious_duration_symptomatic | Fixed at baseline duration in primary beta-grid analysis | Duration uncertainty is not sampled in the conditional beta-grid posterior workflow; duration assumptions are evaluated through sensitivity analyses. |
| infectious_duration_asymptomatic | Fixed at baseline duration in primary beta-grid analysis | Duration uncertainty is not sampled in the conditional beta-grid posterior workflow; asymptomatic duration is evaluated through sensitivity analyses. |
| fitness_R | Fixed at neutral-fitness baseline in primary beta-grid analysis | Resistance fitness is weakly identifiable from reported cases and is instead evaluated in continuous fitness and hindcast sensitivity analyses. |
| resistance_prevalence | Country-specific evidence anchor | Resistance prevalence is anchored by the latest admissible country-specific evidence and stress-tested through fixed resistance and fitness-grid scenarios. |
| reporting_trend | Fixed to no secular trend in primary beta-grid analysis | Secular reporting change is not sampled in the conditional beta-grid posterior workflow; reporting uncertainty is evaluated in reporting-rate sensitivity analyses. |
<!-- END ETABLE 12 -->

<!-- BEGIN ETABLE 13 -->
**eTable 13. Continuous macrolide-resistant fitness and vaccine infectiousness grid.**

<!-- Generated from `manuscript_notes/fitness_grid_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Fitness_R | VE_inf | Description |
| --- | --- | --- |
| 0.7 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.7 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.7 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.7 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.7 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.7 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.7 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.7 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.7 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.7 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.7 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.8 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.8 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.8 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.8 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.8 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.8 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.8 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.8 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.8 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.8 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.8 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.85 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.85 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.85 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.85 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.85 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.85 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.85 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.85 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.85 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.85 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.85 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.9 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.9 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.9 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.9 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.9 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.9 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.9 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.9 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.9 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.9 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.9 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.95 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.95 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.95 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.95 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.95 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.95 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.95 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.95 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.95 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.95 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.95 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.98 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.98 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.98 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.98 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.98 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.98 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.98 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.98 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.98 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.98 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 0.98 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.000 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.000 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.000 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.000 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.000 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.000 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.000 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.000 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.000 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.000 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.000 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.020 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.020 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.020 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.020 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.020 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.020 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.020 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.020 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.020 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.020 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.020 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.050 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.050 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.050 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.050 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.050 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.050 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.050 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.050 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.050 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.050 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.050 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.100 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.100 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.100 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.100 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.100 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.100 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.100 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.100 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.100 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.100 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.100 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.150 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.150 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.150 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.150 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.150 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.150 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.150 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.150 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.150 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.150 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.150 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.200 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.200 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.200 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.200 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.200 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.200 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.200 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.200 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.200 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.200 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.200 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.250 | 0.05 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.250 | 0.1 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.250 | 0.15 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.250 | 0.2 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.250 | 0.25 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.250 | 0.3 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.250 | 0.35 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.250 | 0.4 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.250 | 0.45 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.250 | 0.5 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
| 1.250 | 0.55 | Continuous macrolide-resistant strain fitness stress test crossed with plausible-to-upper-bound vaccine infectiousness effects. VE_inf is the reduction in onward infectiousness among infected vaccine-history origins, not protection against infection. The fitness grid now includes finer resolution around fitness_R = 1.0 (neutral) because epidemiological evidence from China (36% to >99% MRBP in 8 years), Japan (83-88% in 2024-2025), and international MT28 spread suggests the true fitness is near or above 1.0. Values below 0.85 are retained for completeness but are increasingly inconsistent with observed resistance dynamics. VE_inf axis expanded from 5 to 11 uniform steps (0.05 increments) to improve heatmap resolution in Figure 3E/F panels. |
<!-- END ETABLE 13 -->

<!-- BEGIN ETABLE 14 -->
**eTable 14. Selected prior pertussis models and mechanistic features compared with the current model.**

<!-- Generated from `static prior model comparison` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Model | Age structure | Waning | Asymptomatic transmission | Vaccine infection blocking | Vaccine infectiousness reduction | Resistance | Treatment/PEP | Infant-specific outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wearing and Rohani 2009 | Population-level transmission signatures | Yes | Implicit or limited | Composite immunity | Not separated | No | No | No |
| Lavine et al 2011 | Age-structured pertussis dynamics | Yes, with immune boosting | Limited | Composite protection | Not separated | No | No | Limited |
| Althouse and Scarpino 2015 | Age-structured transmission model | Yes | Yes | Composite or scenario-level | Not decomposed into VE_inf and VE_dur | No | No | Limited |
| Chit et al 2018 | Meta-analysis plus modeling | Yes | Not primary focus | Vaccine-effectiveness endpoint | No | No | No | Limited |
| Domenech de Celles et al 2018 | Age-structured transmission model | Yes | Implicit in transmission structure | Composite vaccine-history protection | Not separated | No | No | Yes, but not resistance-aware |
| Drivers of resurgence pilot report 2025 | Multi-country age-structured model | Yes | Yes or implicit | Included | Incomplete separation | No | No resistance-aware PEP | Yes |
| Current model | Eight age groups and country-specific contact matrices | SIRWS waning and boosting | Explicit | VE_sus | VE_inf and VE_dur separated | Two strain classes with fitness and importation | Strain-specific treatment and PEP assumptions | Primary outcome |
<!-- END ETABLE 14 -->

<!-- BEGIN ETABLE 15 -->
**eTable 15. Country selection rationale, programmatic dimensions, and data-quality rating.**

<!-- Generated from `data/processed/country_profile_inputs.csv plus manuscript_notes/country_profile_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | WHO region | Population | DTP3 coverage | Booster schedule | Maternal vaccination policy | Recent reported incidence per 100k | Resistance anchor | Reason for inclusion | Data quality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | Western Pacific | 26,713,206 | 0.9266 | 6 routine doses; adolescent booster | 20-32w | 54.98 | 4.3% (2024) | High recent reported incidence; measured low but detectable resistance; mature maternal and booster program. | High |
| Brazil | Americas | 211,998,565 | 0.8891 | 5 routine doses; no adolescent booster | 20-32w | 0.8601 | 1.0% (2025) | Large Americas profile with wP schedule, maternal program, and detected resistant cases without national fraction. | Moderate |
| China | Western Pacific | 1,419,321,285 | 0.988 | 4 routine doses; no adolescent booster | No routine maternal programme recorded | 4.431 | 99.7% (2024) | Large population, marked post-pandemic resurgence, and near-complete measured macrolide resistance anchor. | High |
| Japan | Western Pacific | 123,753,042 | 0.9862 | 4 routine doses; no adolescent booster | No routine maternal programme recorded | 7.837 | 82.7% (2025) | Western Pacific resurgence and high measured resistance in 2024-2025 reports. | High |
| New Zealand | Western Pacific | 5,213,946 | 0.8791 | 5 routine doses; adolescent booster | 16-26w | 25.11 | 1.0% (2025) | Small high-income profile with maternal and adolescent programs and emerging resistance concern. | Moderate |
| South Africa | African | 64,007,189 | 0.739 | 6 routine doses; adolescent booster | 26-34w | 2.276 | 2.0% (2025) | African-region profile with shorter overlapping calibration window and contrasting demography. | Moderate |
| Sweden | European | 10,606,995 | 0.95 | 5 routine doses; adolescent booster | 16-36w | 5.955 | 1.0% (2025) | European profile with high-quality surveillance and booster program contrast. | High |
| Thailand | South-East Asia | 71,668,012 | 0.8922 | 5 routine doses; no adolescent booster | NA | 0.1977 | 1.0% (2025) | South-East Asian low reported-incidence profile with wP schedule and low maternal coverage. | Moderate |
| United Kingdom | European | 69,138,185 | 0.917 | 4 routine doses; no adolescent booster | 16-32w | 7.268 | 0.3% (2024) | European maternal-program profile with established pregnancy vaccination and surveillance data. | High |
| United States | Americas | 345,426,570 | 0.94 | 6 routine doses; adolescent booster | 27-36w | 1.439 | 0.0% (2015) | Large Americas profile with adolescent and maternal Tdap program and low reported resistance. | High |
<!-- END ETABLE 15 -->

<!-- BEGIN ETABLE 16 -->
**eTable 16. Fitted age-specific reporting probabilities and prior bounds.**

<!-- Generated from `outputs/tables/calibration_all_countries.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Infant 0-2 mo | Infant 3-11 mo | Child 1-9 y | School/adolescent 5-17 y | Adult 18+ y | Prior bounds by age | Prior evidence class |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | 0.5146 | 0.4288 | 0.1844 | 0.1115 | 0.0343 | infant_0_2m=0.6000[0.3000,0.7500];infant_3_11m=0.5000[0.2500,0.7000];child_1_4y=0.2500[0.1000,0.5000];child_5_9y=0.1800[0.0800,0.4000];adolescent_10_17y=0.0800[0.0400,0.2000];young_adult_18_39y=0.0500[0.0100,0.1200];middle_adult_40_64y=0.0300[0.0050,0.1000];elderly_65plus=0.0400[0.0100,0.1200] | serology_proxy |
| Brazil | 0.5779 | 0.4816 | 0.2071 | 0.1253 | 0.0385 | infant_0_2m=0.6000[0.2000,0.7000];infant_3_11m=0.5000[0.1800,0.6500];child_1_4y=0.2500[0.0500,0.4000];child_5_9y=0.1800[0.0400,0.3000];adolescent_10_17y=0.0800[0.0300,0.1500];young_adult_18_39y=0.0500[0.0030,0.0800];middle_adult_40_64y=0.0300[0.0030,0.0600];elderly_65plus=0.0400[0.0030,0.0800] | passive_surveillance_proxy |
| China | 0.6 | 0.5 | 0.215 | 0.13 | 0.04 | infant_0_2m=0.6000[0.2000,0.7000];infant_3_11m=0.5000[0.2000,0.6500];child_1_4y=0.2500[0.0500,0.4000];child_5_9y=0.1800[0.0400,0.3000];adolescent_10_17y=0.0800[0.0300,0.1500];young_adult_18_39y=0.0500[0.0030,0.0800];middle_adult_40_64y=0.0300[0.0030,0.0600];elderly_65plus=0.0400[0.0030,0.0800] | active_surveillance_proxy |
| Japan | 0.5961 | 0.4968 | 0.2136 | 0.1291 | 0.0397 | infant_0_2m=0.6000[0.2500,0.7000];infant_3_11m=0.5000[0.2000,0.6500];child_1_4y=0.2500[0.0800,0.4500];child_5_9y=0.1800[0.0600,0.3500];adolescent_10_17y=0.0800[0.0300,0.1500];young_adult_18_39y=0.0500[0.0050,0.0800];middle_adult_40_64y=0.0300[0.0050,0.0600];elderly_65plus=0.0400[0.0050,0.0800] | laboratory_surveillance_proxy |
| New Zealand | 0.587 | 0.4892 | 0.2104 | 0.1272 | 0.0391 | infant_0_2m=0.6000[0.3000,0.7500];infant_3_11m=0.5000[0.2500,0.7000];child_1_4y=0.2500[0.1000,0.5000];child_5_9y=0.1800[0.0800,0.4000];adolescent_10_17y=0.0800[0.0400,0.1800];young_adult_18_39y=0.0500[0.0100,0.1000];middle_adult_40_64y=0.0300[0.0080,0.0800];elderly_65plus=0.0400[0.0100,0.1000] | high_income_underreporting_proxy |
| South Africa | 0.604 | 0.5033 | 0.2164 | 0.1308 | 0.0403 | infant_0_2m=0.6000[0.2000,0.7000];infant_3_11m=0.5000[0.1800,0.6500];child_1_4y=0.2500[0.0500,0.4000];child_5_9y=0.1800[0.0400,0.3000];adolescent_10_17y=0.0800[0.0300,0.1500];young_adult_18_39y=0.0500[0.0030,0.0800];middle_adult_40_64y=0.0300[0.0030,0.0600];elderly_65plus=0.0400[0.0030,0.0800] | passive_notification_proxy |
| Sweden | 0.6151 | 0.5126 | 0.2204 | 0.1333 | 0.041 | infant_0_2m=0.6000[0.4000,0.8000];infant_3_11m=0.5000[0.3500,0.7500];child_1_4y=0.2500[0.2500,0.6000];child_5_9y=0.1800[0.1440,0.5000];adolescent_10_17y=0.0800[0.0800,0.2500];young_adult_18_39y=0.0500[0.0200,0.1200];middle_adult_40_64y=0.0300[0.0150,0.1000];elderly_65plus=0.0400[0.0200,0.1200] | direct_preschool_anchor |
| Thailand | 0.6127 | 0.5106 | 0.2196 | 0.1327 | 0.0408 | infant_0_2m=0.6000[0.2000,0.7000];infant_3_11m=0.5000[0.1800,0.6500];child_1_4y=0.2500[0.0500,0.4000];child_5_9y=0.1800[0.0400,0.3000];adolescent_10_17y=0.0800[0.0300,0.1500];young_adult_18_39y=0.0500[0.0030,0.0800];middle_adult_40_64y=0.0300[0.0030,0.0600];elderly_65plus=0.0400[0.0030,0.0800] | passive_surveillance_proxy |
| United Kingdom | 0.5679 | 0.4733 | 0.2035 | 0.123 | 0.0379 | infant_0_2m=0.6000[0.3000,0.7500];infant_3_11m=0.5000[0.2500,0.7000];child_1_4y=0.2500[0.1000,0.4500];child_5_9y=0.1800[0.0800,0.3500];adolescent_10_17y=0.0800[0.0400,0.2000];young_adult_18_39y=0.0500[0.0050,0.1000];middle_adult_40_64y=0.0300[0.0050,0.0800];elderly_65plus=0.0400[0.0050,0.1000] | notification_efficiency_low |
| United States | 0.6177 | 0.5147 | 0.2213 | 0.1338 | 0.0412 | infant_0_2m=0.6000[0.3000,0.7500];infant_3_11m=0.5000[0.2500,0.7000];child_1_4y=0.2500[0.1000,0.5000];child_5_9y=0.1800[0.0800,0.4000];adolescent_10_17y=0.0800[0.0400,0.1800];young_adult_18_39y=0.0500[0.0050,0.1000];middle_adult_40_64y=0.0300[0.0050,0.0800];elderly_65plus=0.0400[0.0050,0.1000] | capture_recapture_proxy |
<!-- END ETABLE 16 -->

<!-- BEGIN ETABLE 17 -->
**eTable 17. Macrolide-resistance mechanism decomposition across importation, treatment, PEP, and fitness assumptions.**

<!-- Generated from `outputs/tables/resistance_mechanism_decomposition.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Scenario | Importation | Treatment differential | PEP differential | Fitness_R | Median end resistant fraction | IQR end resistant fraction | Median infant cases per 100k | Median resistant infections per 100k | Interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_full_mechanism | yes | yes | yes | 1.000 | 0.9965 | 0.2815-0.9986 | 357.53 | 596.21 | Full baseline mechanism: country anchor, resistant importation, strain-specific treatment and PEP, neutral fitness. |
| no_resistant_importation | no | yes | yes | 1.000 | 0.9795 | 0.2463-0.9976 | 352.84 | 579.92 | Tests dependence on ongoing resistant-strain importation after the analysis-start anchor. |
| equal_treatment_effect | yes | no | yes | 1.000 | 0.995 | 0.0586-0.9985 | 327.98 | 525.11 | Tests treatment-mediated selection by making resistant treatment effects equal to sensitive-strain effects. |
| equal_pep_effect | yes | yes | no | 1.000 | 0.1224 | 0.04585-0.3797 | 276.63 | 28.44 | Tests PEP-mediated selection by making resistant PEP effectiveness equal to sensitive-strain PEP effectiveness. |
| no_treatment_or_pep_differential | yes | no | no | 1.000 | 0.01 | 0.01-0.03725 | 266.87 | 5.879 | Tests neutral strain competition under importation when treatment and PEP do not favor resistant strains. |
| fitness_cost | yes | yes | yes | 0.85 | 0.0001373 | 1.909e-05-0.0005749 | 246.81 | 0.1656 | Fitness-cost stress test retaining baseline importation and management assumptions. |
<!-- END ETABLE 17 -->

<!-- BEGIN ETABLE 18 -->
**eTable 18. Threshold analysis for vaccine infectiousness reduction under selected resistant-fitness assumptions.**

<!-- Generated from `outputs/summaries/fitness_resistance_grid_summary.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Fitness_R | Target infant-case reduction vs VE_inf=0.25 | Minimum VE_inf | Median reduction at threshold | Countries meeting threshold | Interpretation |
| --- | --- | --- | --- | --- | --- |
| 0.85 | 25% | 0.4 | 31.5% | 6/10 | Threshold reached on the simulated VE_inf grid. |
| 0.85 | 50% | 0.5 | 50.6% | 5/10 | Threshold reached on the simulated VE_inf grid. |
| 0.85 | 75% | Not reached through 0.55 | 59.5% at 0.55 | 4/10 | Threshold not reached on the simulated grid. |
| 1.000 | 25% | 0.4 | 32.1% | 6/10 | Threshold reached on the simulated VE_inf grid. |
| 1.000 | 50% | 0.5 | 52.4% | 6/10 | Threshold reached on the simulated VE_inf grid. |
| 1.000 | 75% | Not reached through 0.55 | 61.1% at 0.55 | 4/10 | Threshold not reached on the simulated grid. |
| 1.100 | 25% | 0.5 | 29.1% | 6/10 | Threshold reached on the simulated VE_inf grid. |
| 1.100 | 50% | Not reached through 0.55 | 35.1% at 0.55 | 4/10 | Threshold not reached on the simulated grid. |
| 1.100 | 75% | Not reached through 0.55 | 35.1% at 0.55 | 0/10 | Threshold not reached on the simulated grid. |
| 1.150 | 25% | 0.45 | 25.4% | 5/10 | Threshold reached on the simulated VE_inf grid. |
| 1.150 | 50% | Not reached through 0.55 | 32.5% at 0.55 | 4/10 | Threshold not reached on the simulated grid. |
| 1.150 | 75% | Not reached through 0.55 | 32.5% at 0.55 | 0/10 | Threshold not reached on the simulated grid. |
<!-- END ETABLE 18 -->
