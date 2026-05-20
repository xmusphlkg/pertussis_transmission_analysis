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
