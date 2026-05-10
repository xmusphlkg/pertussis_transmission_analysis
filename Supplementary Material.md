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

We developed a deterministic age-structured compartmental model of *Bordetella pertussis* transmission to evaluate how vaccine mechanism assumptions and macrolide resistance jointly affect infant disease burden, all-age infection burden, notified cases, resistant infections, and intervention prioritization. The model follows the mechanistic tradition of pertussis resurgence and immunity-waning models, but extends the state space to include explicit maternal and dose-history origins, two strain classes, country-specific demographic and contact profiles, and resistance-dependent treatment and postexposure prophylaxis (PEP) effects [1-6,19-23].

Eight national profiles were analyzed: Australia, China, Japan, New Zealand, Singapore, Sweden, the United Kingdom, and the United States. The set is purposive rather than globally representative; it was chosen to span Western Pacific, European, and Americas settings, large and small population denominators, contrasting booster and maternal-immunization programme signatures, heterogeneous reported incidence, and both measured and conservative low macrolide-resistance anchors. Country-specific inputs were derived from United Nations World Population Prospects denominators, WHO/UNICEF Joint Reporting Form and immunization schedule records, reported pertussis surveillance series through 2023, Prem/contactdata social-contact matrices, and a macrolide-resistance evidence timeline anchored to the latest admissible evidence year for each country [13-18,21-29]. The principal simulations used a 60-year pre-analysis burn-in to reduce dependence on arbitrary initial conditions, followed by a 30-year analysis horizon beginning on 1 January 2026, with model output retained at 7-day intervals.

All incidence measures are reported as annualized counts per 100,000 persons unless stated otherwise. Infant outcomes combine the 0-2 month and 3-11 month age groups, because these strata jointly capture the highest-risk pre-primary-series and partially vaccinated infant population.

The supplementary appendix is generated directly from the same analysis pipeline used for the simulations, so the text, figures, and tables remain aligned with the model assumptions. eTable 11 summarizes the fixed model settings and output conventions that govern interpretation [35].

### Country profile construction

Population denominators were aggregated from one-year age groups into five model strata. Age 0 population was partitioned as 25% aged 0-2 months and 75% aged 3-11 months; ages 1-6 years, 7-17 years, and 18 years or older were then aggregated directly. Let \(N_i\) denote the resulting population in age group \(i\).

Routine and maternal immunization inputs were transformed into age-specific vaccine-origin coverage proxies using DTP1 coverage \(v_1\), DTP3 coverage \(v_3\), maternal coverage \(m\), the number of childhood booster doses \(b\), and an indicator \(A\) for an adolescent booster programme:

$$
v_{0-2m}=\mathrm{clip}(0.02+0.55m,\ 0.02,\ 0.75),
$$

$$
v_{3-11m}=\mathrm{clip}(0.75v_1+0.12v_3+0.12m,\ 0,\ 0.95),
$$

$$
v_{1-6y}=\mathrm{clip}\{v_3[0.88+0.04\min(b,2)],\ 0,\ 0.98\},
$$

$$
v_{7-17y}=\mathrm{clip}\{v_3[0.58+0.10\min(b,2)+0.12A],\ 0,\ 0.95\},
$$

$$
v_{18+y}=\mathrm{clip}(0.12+0.10A+0.03m,\ 0.10,\ 0.75).
$$

These deterministic transformations assign individuals to mechanistic protection histories and do not imply that adult pertussis immunization coverage is directly observed in all settings. They are coverage-to-state mapping rules that translate DTP1, DTP3, booster, and maternal-programme records into the compartment origins needed by the model, informed by evidence that acellular pertussis protection wanes, maternal immunization protects young infants, and schedule history affects age-specific susceptibility and disease presentation [1,7-12].

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

Prem/contactdata matrices were first represented on 5-year age bins and then aggregated to the five model age groups using population weights [15-17]. If \(P_{ab}\) is the fine-age contact matrix, \(w_{ia}\) is the distribution of age group \(i\) over fine source bin \(a\), and \(f_{jb}\) is the fraction of fine target bin \(b\) belonging to model group \(j\), then

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

The model uses five age groups:

$$
i \in \mathcal{A} = \{0\text{-}2m,\ 3\text{-}11m,\ 1\text{-}6y,\ 7\text{-}17y,\ 18+y\}.
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

For each age group, the model tracks susceptible-origin states \(S_{i,o}\), exposed states \(E_{i,k,o}\), symptomatic infectious states \(I^{sym}_{i,k,o}\), asymptomatic infectious states \(I^{asym}_{i,k,o}\), treated infectious states \(T_{i,k,o}\), and naturally immune states \(R_i\). The per-age state space contains 8 susceptible-origin states, 16 exposed states, 32 infectious states, 16 treated states, and one naturally immune state, yielding 73 compartments per age group and 365 dynamic state variables.

### Vaccine mechanism parameterization

Four vaccine mechanism parameters define a scenario:

$$
\mathrm{VE}_{sus},\quad \mathrm{VE}_{sym},\quad \mathrm{VE}_{inf},\quad \mathrm{VE}_{dur}.
$$

These represent reductions in susceptibility to infection, symptomatic disease given infection, onward infectiousness, and infectious duration, respectively. Vaccine effects are origin-specific through a relative effect weight \(w_o \in [0,1]\). The default weights distinguish maternal protection, partial-dose histories, recent three-or-more-dose protection, and waned protection:

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

This formulation separates protection against infection, clinical disease, onward infectiousness, and duration of infectiousness. It therefore permits aP-like profiles with strong protection against symptoms but weak infection or transmission blocking, as well as hypothetical next-generation profiles with stronger effects on colonization and transmission [1,5-9].

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

Naturally immune states receive all recoveries and wane at rate \(\omega_N\):

$$
\frac{dR_i}{dt} =
\sum_{k,o}m_o\left[
\gamma_{sym}I^{sym}_{i,k,o}
+ \gamma_{asym}I^{asym}_{i,k,o}
+ \gamma^T_kT_{i,k,o}
\right]
-\omega_NR_i.
$$

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

Demographic turnover keeps country-specific age profiles approximately stationary while allowing cohort movement through the state space. Age-exit rates \(\mu_i\) are chosen so that the absolute ageing flow implied by the reference infant age group is compatible with the country-specific age profile. For a generic compartment \(X_i\),

$$
\frac{dX_i}{dt}\bigg|_{ageing} =
-\mu_iX_i + \mu_{i-1}X_{i-1}
$$

for non-youngest age groups. The oldest age group exits at rate \(\mu_A\). Total births equal the outflow from the oldest age group and enter the youngest group according to the country-specific birth-entry distribution. Maternal protection in the youngest infant group is treated as short-lived maternally derived protection and is converted back to unvaccinated susceptibility when infants age out of the 0-2 month group.

### Numerical solution and burn-in

The model is a continuous-time ordinary differential equation system with rates expressed per day. Main simulations were solved using an adaptive Runge-Kutta method with relative tolerance \(10^{-5}\) and absolute tolerance \(10^{-7}\). State values were projected to non-negative values when evaluating rates so that small numerical undershoots could not produce negative force-of-infection, recovery, or vaccination flows.

The main analysis used 60 years of burn-in followed by resistance rebalancing and a 30-year saved analysis period. Calibration simulations used a shortened burn-in and coarser output interval to reduce computational cost while preserving annual case totals for likelihood evaluation. All summary statistics were computed from the saved analysis interval only.

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

Country-level calibration targets annual reported cases. The observed series uses WHO reported-case extracts when available and otherwise uses the harmonized pertussis surveillance series; observations after the 2023 surveillance cutoff were excluded from incidence calibration. The calibration window retains the six most recent observed annual records, aligns model time to the first retained observed year, and allocates modelled reporting intervals across calendar-year boundaries before comparing annual totals.

The full calibration vector can adjust the sensitive-strain transmission coefficient \(\beta_S\), the reporting multiplier, seasonal amplitude, importation rate, and resistant importation fraction:

$$
\theta =
\{\log\beta_S,\ \log m_{rep},\ \mathrm{logit}(a/0.35),\ \log u,\ \mathrm{logit}(p_R^{imp})\}.
$$

The admissible ranges were \(\beta_S\in[0.002,0.2]\), \(m_{rep}\in[0.1,10]\), \(a\in[0,0.35]\), \(u\in[0.01,2]\) imported infections per 100,000 persons per year, and \(p_R^{imp}\in[0,1]\). The principal calibration used a staged search that brackets and bisects \(\beta_S\) against the mean observed annual reports, followed by a reporting-multiplier adjustment within prior bounds. A full L-BFGS-B formulation is retained for the same parameter vector as an alternative optimizer. The likelihood for annual reported cases is negative binomial:

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

The scenario analysis had six linked components. Vaccine-mechanism scenarios contrasted no vaccine, symptom-protective aP-like protection, stronger infection blocking, stronger transmission blocking, and next-generation protection. Macrolide-resistance scenarios used either country-specific evidence anchors or fixed low, moderate, high, and very-high resistant fractions. A two-dimensional grid varied \(\mathrm{VE}_{inf}\) and the initial, target, and importation resistant prevalence together to isolate the interaction between transmission blocking and resistance. Intervention strategies then modified routine child coverage, maternal protection, adolescent boosting, resistance-guided treatment, PEP effectiveness, and vaccine-mechanism assumptions. Reporting-rate sensitivity scenarios perturbed only the observation process, and global sensitivity analysis sampled vaccine effects, immunity waning, transmission, treatment, PEP, resistance fitness, and reporting.

Global sensitivity analysis used a Latin-hypercube design with 24 parameter sets. Parameter-outcome associations were summarized using Pearson correlations between sampled parameter values and total infant cases, providing a screening measure of direction and relative influence rather than a full variance-decomposition estimate. These runs should therefore be read as robustness and prioritization diagnostics, not as posterior uncertainty intervals or formal probabilistic projections [35].

### Model implementation and settings

The model is a deterministic age-structured ODE system with explicit vaccine-history, strain, treatment, and prophylaxis states. Its core settings are summarized in eTable 11, which includes the age partition, strain structure, solver choices, burn-in and analysis horizon, reporting model, and resistance initialization rules. Those settings were chosen so the appendix reflects the epidemiologic structure of the model rather than the mechanics of the file layout used to generate it.

### Interpretation limits

The analysis is a mechanistic scenario study with pragmatic country-level calibration, not a full statistical reconstruction of national pertussis transmission. Deterministic compartments do not represent stochastic fadeout, superspreading, household clustering, individual vaccination histories, or posterior parameter uncertainty. Country profiles combine directly measured inputs, processed surveillance summaries, and explicitly labelled assumptions; therefore, cross-country differences should be interpreted as conditional contrasts under harmonized model structure. Macrolide-resistance anchors are intentionally conservative where public numeric estimates were unavailable, and resistance scenarios are designed to evaluate plausible management consequences rather than forecast future clone frequencies.

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

![eFigure 1](outputs/appendix/extended_data_figure_1_country_inputs.png)

**eFigure 1. Country-specific input data used to instantiate the eight national pertussis transmission profiles.** **(A)** Vaccine programme coverage. DTP1, DTP3, and maternal immunization coverage values used to initialize age-specific vaccine-origin distributions and birth-entry protection. **(B)** Routine schedule timing. Age at first and last routine pertussis-containing dose, with dose count and maternal programme status summarizing major differences in immunization schedules. **(C)** Seasonal forcing inputs. Country-specific annual seasonal phase and amplitude derived from processed surveillance time series, with point encodings indicating observed reported-incidence intensity and recurrence support. **(D)** Aggregated contact intensity. Population-weighted contact rates after reconstruction, aggregation, and reciprocity balancing to the five model age groups.

![eFigure 2](outputs/appendix/extended_data_figure_2_diagnostics_sensitivity.png)

**eFigure 2. Surveillance, calibration, and robustness diagnostics for the modeled country profiles.** **(A)** Observed surveillance time series. Annual reported pertussis incidence used for country input derivation, restricted to the pre-specified surveillance window. **(B)** Calibration diagnostic. Observed annual reported cases are compared with calibrated model means and approximate predictive intervals for countries with accepted country-level calibrations. **(C)** Reporting-rate sensitivity. Median annualized infection, reported-case, and infant-case incidence under alternative reporting assumptions, illustrating the influence of surveillance ascertainment on absolute burden. **(D)** Global sensitivity analysis. Pearson correlations between sampled parameter values and annualized infant case incidence across the Latin-hypercube sensitivity design.

![eFigure 3](outputs/appendix/extended_data_figure_3_data_provenance.png)

**eFigure 3. Provenance and preprocessing audit for model inputs and analytical outputs.** **(A)** Source domains. Source entries are grouped by country input data, clinical and mechanistic assumptions, and macrolide-resistance evidence. **(B)** Analysis corpus by processing stage. Raw inputs, harmonized inputs, simulations, summaries, tables, and manuscript-support materials are summarized to document data flow through the analysis. **(C)** Country evidence completeness matrix. Availability of population, surveillance, schedule, contact, seasonality, and resistance inputs is shown for each modeled profile. **(D)** Macrolide-resistance evidence timeline. Country-specific resistance anchors and measured isolate or surveillance fractions are plotted by evidence year, with uncertainty intervals where available.

![eFigure 4](outputs/appendix/extended_data_figure_4_calibration_diagnostics.png)

**eFigure 4. Country-level calibration acceptance and fit diagnostics.** **(A)** Calibration acceptance and fit score. Accepted country calibrations are summarized with their retained fit scores and optimizer status. **(B)** Observed and calibrated annual reports. Observed annual reported cases are compared with calibrated annual model means and approximate predictive intervals. **(C)** Fitted reporting probabilities by age. Age-specific reporting probabilities retained after calibration are shown relative to prior reporting assumptions. **(D)** Calibrated transmission and interval width. Calibrated transmission rate is plotted against the relative width of the predictive interval to identify countries with broader residual uncertainty.

![eFigure 5](outputs/appendix/extended_data_figure_5_model_architecture.png)

**eFigure 5. Model architecture, compartment accounting, and vaccine-effect mapping.** **(A)** State-space components. The full ODE system comprises five age groups, two strains, eight susceptible-origin histories, 73 compartments per age group, and 365 dynamic state variables. **(B)** Compartment block accounting. Per-age compartments are decomposed into susceptible-origin, exposed, infectious, treated, and naturally immune blocks. **(C)** Vaccine-effect routes. VE_sus, VE_sym, VE_inf, and VE_dur are mapped to susceptibility, symptomatic disease, onward infectiousness, and infectious duration. **(D)** Origin-specific effect weights. Maternal, partial-dose, recent, and waned vaccine histories carry distinct relative effect weights used by all vaccine-mechanism scenarios.

![eFigure 6](outputs/appendix/extended_data_figure_6_baseline_dynamics.png)

**eFigure 6. Baseline temporal dynamics over the saved analysis period.** **(A)** All-infection incidence at model output time points. Country-specific infection trajectories show recurrent transmission dynamics under the baseline vaccine and resistance assumptions. **(B)** Infant case incidence at model output time points. Symptomatic infant burden is scaled to infant population denominators to highlight country-level differences in risk to the most vulnerable age groups. **(C)** Resistant fraction dynamics. The resistant infection fraction is tracked after burn-in rebalancing to separate scenario initialization from within-analysis strain dynamics. **(D)** Age and strain contribution. The share of infections attributable to each age group and strain summarizes the demographic and resistance composition of baseline transmission.

![eFigure 7](outputs/appendix/extended_data_figure_7_vaccine_deep_dive.png)

**eFigure 7. Vaccine-mechanism analysis and infection-source decomposition.** **(A)** Vaccine scenario parameter matrix. No-vaccine, aP-like symptom-protective, infection-blocking, transmission-blocking, and next-generation profiles are compared across VE_sus, VE_sym, VE_inf, and VE_dur. **(B)** Country-specific outcome reductions. Relative reductions in infant cases, reported cases, total infections, and resistant infections are shown for each country-scenario combination. **(C)** Infection-source histories. Median infection shares are decomposed by maternal, dose-1, dose-2, dose-3-plus, and waned source histories. **(D)** Representative vaccine trajectories. Infant case trajectories for Australia and China illustrate how vaccine-mechanism assumptions alter both magnitude and temporal pattern.

![eFigure 8](outputs/appendix/extended_data_figure_8_resistance_dynamics.png)

**eFigure 8. Macrolide-resistance evidence, initialization, and dynamic consequences.** **(A)** Scenario target versus realized initialization. Fixed resistance scenarios and country-timeline runs are compared with realized starting resistant fractions after burn-in rebalancing. **(B)** Resistant infection burden. Annualized resistant infection incidence is summarized by country and resistance scenario. **(C)** Treatment and PEP event burden. Treated-case and PEP-averted event rates are compared across resistance assumptions to quantify management-related outcome changes. **(D)** Sensitive and resistant strain trajectories. Representative country-timeline trajectories for Australia and China show how initial resistance prevalence, fitness, and importation interact during the saved analysis period.

![eFigure 9](outputs/appendix/extended_data_figure_9_full_grid.png)

**eFigure 9. Full interaction surface between vaccine transmission blocking and initial resistance prevalence.** **(A)** Country-specific infant burden grid. Annualized infant case incidence is shown for each country across the seven-by-seven grid of VE_inf and initial resistant prevalence. **(B)** Benefit of high transmission blocking. The relative infant-case benefit of increasing VE_inf from 0% to 90% is displayed by country and resistance prevalence. **(C)** Median burden across countries. Median infant-case and all-infection incidence are summarized across countries over the same parameter grid. **(D)** Threshold for 50% infant-case reduction. The minimum VE_inf required to reduce infant cases by at least 50% relative to VE_inf = 0 is shown where the threshold is reached.

![eFigure 10](outputs/appendix/extended_data_figure_10_intervention_extended.png)

**eFigure 10. Extended intervention-strategy outcomes across countries and endpoints.** **(A)** Intervention lever matrix. Each strategy is mapped to the child-coverage, adolescent-booster, maternal-immunization, resistance-guided-treatment, and vaccine-improvement levers it modifies. **(B)** Country-specific outcome reductions. Relative reductions in infant cases, reported cases, total infections, and resistant infections are shown for each strategy and country. **(C)** Current versus combined trajectories. Infant case trajectories compare the current strategy with the combined strategy in Australia and China. **(D)** Intervention rank by country. Strategies are ranked within each country by relative reduction in infant cases, highlighting heterogeneity in priority ordering.

![eFigure 11](outputs/appendix/extended_data_figure_11_model_structure.png)

**eFigure 11. Compartmental transmission schematic used to define the dynamic state space.** **(A)** Age-omitted transmission schematic. The schematic condenses the full model into one representative age group, showing origin-specific susceptible histories, strain-specific exposed and infectious branches, treated infection states, and retained infection-source histories. The full ODE repeats this template across five age groups and couples age groups through the contact matrix, demographic ageing, importation, vaccination, and postexposure prophylaxis.

![eFigure 12](outputs/appendix/extended_data_figure_12_contact_matrix_reconstruction.png)

**eFigure 12. Reconstruction and aggregation of country-specific contact matrices.** **(A)** Australia: raw 5-year matrix and reconstructed five-group model matrix. **(B)** China: raw and reconstructed contact matrices. **(C)** Japan: raw and reconstructed contact matrices. **(D)** New Zealand: raw and reconstructed contact matrices. **(E)** Singapore: raw and reconstructed contact matrices. **(F)** Sweden: raw and reconstructed contact matrices. **(G)** United Kingdom: raw and reconstructed contact matrices. **(H)** United States: raw and reconstructed contact matrices. Reconstructed matrices are population weighted and reciprocity balanced before use in force-of-infection calculations.

## eTables

<!-- BEGIN ETABLE 1 -->
**eTable 1. Country-specific population, surveillance, vaccination, and seasonal-forcing inputs.**

<!-- Generated from `manuscript_notes/country_profile_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Population | Seasonal phase | Seasonal amplitude | Mean reported incidence per 100k | Vaccine product | Adolescent booster | Maternal program |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | 26,451,124 | 310.63 | 0.149 | 36.32 | aP | Yes | Yes |
| China | 1,422,584,932 | 223.07 | 0.1738 | 1.315 | aP | No | No |
| United Kingdom | 68,682,962 | 335.29 | 0.1236 | 3.460 | aP | No | Yes |
| Japan | 124,370,946 | 250.79 | 0.1377 | 2.752 | aP | No | No |
| New Zealand | 5,172,836 | 343.47 | 0.1689 | 20.01 | aP | Yes | Yes |
| Sweden | 10,551,494 | 292.99 | 0.1788 | 4.253 | aP | Yes | Yes |
| Singapore | 5,789,090 | 71.72 | 0.1119 | 0.8004 | aP | Yes | Yes |
| United States | 343,477,335 | 147.97 | 0.08455 | 1.108 | aP | Yes | Yes |
<!-- END ETABLE 1 -->

<!-- BEGIN ETABLE 2 -->
**eTable 2. Vaccine-mechanism parameterization used in scenario analyses.**

<!-- Generated from `manuscript_notes/scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Scenario | VE_sus | VE_sym | VE_inf | VE_dur | Description |
| --- | --- | --- | --- | --- | --- |
| no_vaccine | 0 | 0 | 0 | 0 | No vaccine protection. |
| symptom_protective | 0.15 | 0.85 | 0.08 | 0 | aP-like disease protection with limited infection/transmission blocking. |
| infection_blocking | 0.7 | 0.85 | 0.2 | 0.1 | Stronger reduction in susceptibility to infection. |
| transmission_blocking | 0.3 | 0.85 | 0.7 | 0.3 | Strong reduction in onward infectiousness and duration. |
| next_generation | 0.8 | 0.9 | 0.75 | 0.4 | Strong infection, symptom, and transmission protection. |
<!-- END ETABLE 2 -->

<!-- BEGIN ETABLE 3 -->
**eTable 3. Macrolide-resistance initialization, importation, and fitness assumptions.**

<!-- Generated from `manuscript_notes/resistance_scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Scenario | Target resistant fraction | Importation resistant fraction | Anchor rate per year | Country timeline | Fitness_R | Description |
| --- | --- | --- | --- | --- | --- | --- |
| country_timeline | 0.3 | 0.3 | 2 | Yes | 0.7 | Country-specific macrolide resistance prevalence from data/raw/country_resistance_timeline.csv, mixing measured surveillance/isolate rows with conservative low anchors where public numeric estimates were not found. |
| low | 0.05 | 0.05 | 2 | No | 0.7 | Low macrolide resistance prevalence. |
| moderate | 0.3 | 0.3 | 2 | No | 0.7 | Moderate macrolide resistance prevalence. |
| high | 0.7 | 0.7 | 2 | No | 0.7 | High macrolide resistance prevalence. |
| very_high | 0.95 | 0.95 | 2 | No | 0.7 | Very high macrolide resistance prevalence. |
<!-- END ETABLE 3 -->

<!-- BEGIN ETABLE 4 -->
**eTable 4. Intervention strategy definitions and modified control levers.**

<!-- Generated from `manuscript_notes/intervention_scenario_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Strategy | Description |
| --- | --- |
| current | Current vaccination and standard macrolide treatment. |
| higher_child_coverage | Increased routine childhood vaccine coverage. |
| adolescent_booster | Additional booster for school-age children and adolescents. |
| maternal_immunization | Direct infant protection through maternal immunization. |
| resistance_guided_treatment | Resistance testing plus alternative treatment for resistant infections. |
| next_generation_vaccine | Improved transmission-blocking vaccine. |
| combined_strategy | Maternal immunization, adolescent booster, and resistance-guided treatment. |
<!-- END ETABLE 4 -->

<!-- BEGIN ETABLE 5 -->
**eTable 5. Baseline parameter values, admissible ranges, and evidence provenance.**

<!-- Generated from `manuscript_notes/parameter_table.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Parameter | Description | Baseline value | Range | Unit | Source or assumption | Sensitivity |
| --- | --- | --- | --- | --- | --- | --- |
| simulation.end_time | Simulation analysis horizon | 10,950.0 | see config/model_settings.yaml sensitivity_parameters | days | pertussis_cycle_model | No |
| simulation.burn_in_years | Pre-analysis burn-in horizon | 60.00 | see config/model_settings.yaml sensitivity_parameters | years | pertussis_cycle_model | No |
| transmission.beta_S | Transmission rate for macrolide-sensitive pertussis | 0.03 | see config/model_settings.yaml sensitivity_parameters | per contact day | pertussis_incidence | No |
| transmission.relative_infectiousness_asymptomatic | Relative infectiousness of asymptomatic infection | 0.35 | see config/model_settings.yaml sensitivity_parameters | ratio | who_pertussis_position | Yes |
| transmission.multi_year_period_years | Target/diagnostic inter-epidemic period | 4.000 | see config/model_settings.yaml sensitivity_parameters | years | pertussis_cycle_model | No |
| transmission.multi_year_amplitude | Weak multi-year phase-locking amplitude | 0 | see config/model_settings.yaml sensitivity_parameters | ratio | pertussis_cycle_model | Yes |
| natural_history.latent_duration | Latent period duration | 8.000 | see config/model_settings.yaml sensitivity_parameters | days | cdc_clinical | No |
| natural_history.infectious_duration_symptomatic | Symptomatic infectious duration | 21.00 | see config/model_settings.yaml sensitivity_parameters | days | cdc_clinical | No |
| natural_history.infectious_duration_asymptomatic | Asymptomatic infectious duration | 14.00 | see config/model_settings.yaml sensitivity_parameters | days | cdc_clinical | No |
| natural_history.recovered_immunity_duration | Duration of post-infection protection | 3,285.0 | see config/model_settings.yaml sensitivity_parameters (reciprocal of rates.waning_natural) | days | cdc_clinical | Yes |
| natural_history.vaccine_protection_duration | Duration of vaccine-derived protection proxy | 1,825.0 | see config/model_settings.yaml sensitivity_parameters (reciprocal of rates.waning_vaccine) | days | ap_waning_meta_analysis | Yes |
| treatment.treatment_rate_symptomatic | Daily transition from symptomatic infection to treatment | 0.05 | see config/model_settings.yaml sensitivity_parameters | per day | cdc_treatment_pep | Yes |
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
<!-- END ETABLE 6 -->

<!-- BEGIN ETABLE 7 -->
**eTable 7. Country-specific macrolide-resistance evidence used for resistance anchoring.**

<!-- Generated from `data/raw/country_resistance_timeline.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | ISO3 | Year | Sample size | Resistant fraction | Lower | Upper | Evidence type | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | AUS | 2024 | 188 | 0.043 | 0.019 | 0.082 | measured_national_genomic_surveillance_fraction | https://doi.org/10.1016/j.lanmic.2025.101286 |
| China | CHN | 2016 |  | 0.364 | 0.28 | 0.45 | measured_regional_isolate_fraction | https://wwwnc.cdc.gov/eid/article/30/1/22-1588_article |
| China | CHN | 2022 |  | 0.972 | 0.94 | 0.99 | measured_regional_isolate_fraction | https://wwwnc.cdc.gov/eid/article/30/1/22-1588_article |
| China | CHN | 2024 | 394 | 0.997 | 0.986 | 1.000 | measured_multicenter_isolate_fraction | https://www.sciencedirect.com/science/article/pii/S2666606525001658 |
| Japan | JPN | 2024 | 8 | 0.875 | 0.473 | 0.997 | measured_regional_case_series_fraction | https://www.sciencedirect.com/science/article/pii/S1341321X26000140 |
| Japan | JPN | 2025 | 52 | 0.827 | 0.697 | 0.918 | measured_multicenter_isolate_fraction | https://www.mdpi.com/2227-9059/14/1/167 |
| New Zealand | NZL | 1995 | 88 | 0 | 0 | 0.041 | measured_historical_national_isolate_fraction | https://pubmed.ncbi.nlm.nih.gov/9579709/ |
| New Zealand | NZL | 2025 |  | 0.01 | 0 | 0.05 | low_detected_model_anchor | https://www.tewhatuora.govt.nz/for-health-professionals/clinical-guidance/communicable-disease-control-manual/pertussis |
| Singapore | SGP | 2025 |  | 0.01 | 0 | 0.05 | low_imported_model_anchor | https://www.cda.gov.sg/professionals/diseases/pertussis |
| Sweden | SWE | 2025 |  | 0.01 | 0 | 0.05 | low_imported_model_anchor | https://www.folkhalsomyndigheten.se/contentassets/975cc036216b48a39b7bf34319d4ecee/pertussis-surveillance-sweden-23rd-annual-report.pdf |
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
| Australia | Yes | Yes | calibrated_to_reported_cases | 19.85 | 19.79 | 0.9972 | 216.30 | 216.31 | 0.015 |
| China | Yes | Yes | calibrated_to_reported_cases | 1.706 | 1.706 | 1 | 111.04 | 111.04 | 0.01192 |
| Japan | Yes | Yes | calibrated_to_reported_cases | 5.001 | 5.001 | 1.000 | 221.81 | 221.81 | 0.01434 |
| New Zealand | Yes | Yes | calibrated_to_reported_cases | 21.05 | 21.05 | 1 | 319.38 | 319.38 | 0.01346 |
| Singapore | Yes | Yes | calibrated_to_reported_cases | 0.7802 | 0.766 | 0.9818 | 79.04 | 79.04 | 0.01165 |
| Sweden | Yes | Yes | calibrated_to_reported_cases | 3.083 | 3.083 | 1.000 | 241.94 | 241.94 | 0.01222 |
| United Kingdom | Yes | Yes | calibrated_to_reported_cases | 2.508 | 2.540 | 1.013 | 304.94 | 305.09 | 0.01303 |
| United States | Yes | Yes | calibrated_to_reported_cases | 3.129 | 3.152 | 1.007 | 136.04 | 136.05 | 0.01188 |
<!-- END ETABLE 8 -->

<!-- BEGIN ETABLE 9 -->
**eTable 9. Intervention outcome summaries by country and strategy.**

<!-- Generated from `outputs/tables/table_4_intervention_comparison.csv` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Country | Strategy | Total infections | Reported cases | Infant cases | Resistant infections | Infant-case reduction | Infection reduction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | adolescent_booster | 7,214,076 | 112,213 | 33,254.2 | 16,901.2 | 0.3119 | 0.278 |
| Australia | combined_strategy | 14,361.5 | 217.47 | 65.25 | 138.50 | 0.9986 | 0.9986 |
| Australia | current | 9,992,298 | 158,122 | 48,327.3 | 28,390.5 | 0 | 0 |
| Australia | higher_child_coverage | 9,980,713 | 158,456 | 49,549.5 | 28,402.9 | -0.02529 | 0.001159 |
| Australia | maternal_immunization | 6,461,657 | 97,880.8 | 30,874.1 | 13,989.2 | 0.3611 | 0.3533 |
| Australia | next_generation_vaccine | 8,967.5 | 134.85 | 42.45 | 235.48 | 0.9991 | 0.9991 |
| Australia | resistance_guided_treatment | 8,128,345 | 127,832 | 38,300.7 | 3,016.2 | 0.2075 | 0.1865 |
| China | adolescent_booster | 6,076,269 | 96,087.0 | 20,869.8 | 2,736,137 | 0.9656 | 0.9648 |
| China | combined_strategy | 150,248 | 2,517.4 | 641.73 | 148,753 | 0.9989 | 0.9991 |
| China | current | 172,477,209 | 2,859,349 | 607,202 | 12,064,533 | 0 | 0 |
| China | higher_child_coverage | 173,156,035 | 2,873,129 | 618,299 | 12,132,633 | -0.01828 | -0.003936 |
| China | maternal_immunization | 52,359,510 | 841,397 | 182,577 | 4,936,966 | 0.6993 | 0.6964 |
| China | next_generation_vaccine | 357,988 | 5,804.0 | 1,347.1 | 356,257 | 0.9978 | 0.9979 |
| China | resistance_guided_treatment | 67,222,191 | 1,114,058 | 231,075 | 924,985 | 0.6194 | 0.6103 |
| Japan | adolescent_booster | 1,538,147 | 21,630.3 | 4,184.1 | 152,548 | 0.8777 | 0.8735 |
| Japan | combined_strategy | 18,961.9 | 286.16 | 71.40 | 10,597.7 | 0.9979 | 0.9984 |
| Japan | current | 12,156,370 | 178,278 | 34,210.8 | 532,117 | 0 | 0 |
| Japan | higher_child_coverage | 12,251,373 | 180,142 | 34,857.5 | 537,886 | -0.0189 | -0.007815 |
| Japan | maternal_immunization | 4,045,443 | 57,666.4 | 11,083.8 | 240,497 | 0.676 | 0.6672 |
| Japan | next_generation_vaccine | 37,575.6 | 549.44 | 119.75 | 27,478.2 | 0.9965 | 0.9969 |
| Japan | resistance_guided_treatment | 2,366,206 | 34,641.9 | 6,497.7 | 40,857.4 | 0.8101 | 0.8054 |
| New Zealand | adolescent_booster | 1,273,430 | 22,304.2 | 6,797.1 | 682.38 | 0.3529 | 0.3213 |
| New Zealand | combined_strategy | 2,382.1 | 41.04 | 12.64 | 6.182 | 0.9988 | 0.9987 |
| New Zealand | current | 1,876,286 | 33,524.9 | 10,504.3 | 1,260.9 | 0 | 0 |
| New Zealand | higher_child_coverage | 1,887,649 | 34,007.7 | 10,759.9 | 1,294.3 | -0.02434 | -0.006056 |
| New Zealand | maternal_immunization | 1,201,990 | 20,940.1 | 6,648.7 | 631.00 | 0.367 | 0.3594 |
| New Zealand | next_generation_vaccine | 1,675.3 | 28.83 | 9.255 | 10.65 | 0.9991 | 0.9991 |
| New Zealand | resistance_guided_treatment | 1,535,064 | 27,359.1 | 8,387.2 | 138.60 | 0.2015 | 0.1819 |
| Singapore | adolescent_booster | 11,058.5 | 155.60 | 39.31 | 35.41 | 0.8244 | 0.8262 |
| Singapore | combined_strategy | 1,352.5 | 19.40 | 5.355 | 4.933 | 0.9761 | 0.9787 |
| Singapore | current | 63,642.1 | 894.28 | 223.83 | 63.56 | 0 | 0 |
| Singapore | higher_child_coverage | 67,037.2 | 944.57 | 240.68 | 64.84 | -0.0753 | -0.05335 |
| Singapore | maternal_immunization | 9,127.2 | 126.41 | 33.93 | 33.03 | 0.8484 | 0.8566 |
| Singapore | next_generation_vaccine | 1,036.3 | 14.66 | 4.268 | 7.485 | 0.9809 | 0.9837 |
| Singapore | resistance_guided_treatment | 11,479.9 | 162.68 | 41.05 | 11.72 | 0.8166 | 0.8196 |
| Sweden | adolescent_booster | 23,576.8 | 382.45 | 102.08 | 72.99 | 0.9421 | 0.9421 |
| Sweden | combined_strategy | 2,153.6 | 35.61 | 10.80 | 8.675 | 0.9939 | 0.9947 |
| Sweden | current | 407,521 | 6,658.9 | 1,762.2 | 233.22 | 0 | 0 |
| Sweden | higher_child_coverage | 430,318 | 7,063.1 | 1,919.7 | 241.92 | -0.0894 | -0.05594 |
| Sweden | maternal_immunization | 19,104.2 | 304.67 | 87.53 | 67.46 | 0.9503 | 0.9531 |
| Sweden | next_generation_vaccine | 1,574.4 | 25.77 | 8.261 | 11.85 | 0.9953 | 0.9961 |
| Sweden | resistance_guided_treatment | 44,461.2 | 729.76 | 192.17 | 26.61 | 0.891 | 0.8909 |
| United Kingdom | adolescent_booster | 97,206.1 | 1,626.7 | 496.71 | 119.59 | 0.9457 | 0.9473 |
| United Kingdom | combined_strategy | 13,039.6 | 222.43 | 75.06 | 16.38 | 0.9918 | 0.9929 |
| United Kingdom | current | 1,845,700 | 32,447.7 | 9,149.1 | 472.03 | 0 | 0 |
| United Kingdom | higher_child_coverage | 1,971,078 | 34,869.9 | 9,946.4 | 492.37 | -0.08714 | -0.06793 |
| United Kingdom | maternal_immunization | 188,729 | 3,273.4 | 960.84 | 178.43 | 0.895 | 0.8977 |
| United Kingdom | next_generation_vaccine | 15,044.6 | 258.96 | 81.09 | 33.08 | 0.9911 | 0.9918 |
| United Kingdom | resistance_guided_treatment | 270,015 | 4,766.7 | 1,342.4 | 54.58 | 0.8533 | 0.8537 |
| United States | adolescent_booster | 690,418 | 10,987.3 | 3,244.0 | 0 | 0.9463 | 0.9464 |
| United States | combined_strategy | 65,805.1 | 1,065.6 | 349.62 | 0 | 0.9942 | 0.9949 |
| United States | current | 12,881,377 | 206,449 | 60,374.0 | 0 | 0 | 0 |
| United States | higher_child_coverage | 13,650,248 | 219,889 | 65,706.5 | 0 | -0.08832 | -0.05969 |
| United States | maternal_immunization | 568,993 | 8,932.8 | 2,823.4 | 0 | 0.9532 | 0.9558 |
| United States | next_generation_vaccine | 48,657.0 | 783.10 | 272.76 | 0 | 0.9955 | 0.9962 |
| United States | resistance_guided_treatment | 1,259,829 | 20,261.7 | 5,890.9 | 0 | 0.9024 | 0.9022 |
<!-- END ETABLE 9 -->

<!-- BEGIN ETABLE 10 -->
**eTable 10. Model-derived outcomes and summary definitions.**

<!-- Generated from `static outcome definitions` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Quantity | Definition | Denominator or reference population | Primary use |
| --- | --- | --- | --- |
| Total infections | Symptomatic plus asymptomatic incident infections integrated over the analysis interval. | Mean total population over the interval. | Overall transmission burden. |
| Reported cases | Symptomatic incident infections multiplied by age-specific reporting probabilities and integrated over the analysis interval. | Mean total population over the interval. | Calibration target and surveillance-comparable burden. |
| Infant cases | Symptomatic incident infections in the 0-2 month and 3-11 month age groups. | Mean population in the two infant age groups. | Primary severe-risk outcome. |
| Resistant infections | Total incident infections attributed to the macrolide-resistant strain. | Mean total population over the interval. | Resistance burden and treatment relevance. |
| Resistant fraction | Resistant infections divided by total infections at a time point or over a summary interval. | Total infections. | Strain-composition diagnostic. |
| PEP-averted cases | Difference between pre-PEP and post-PEP symptomatic infection flows under the same state trajectory. | Not a population-normalized compartment count unless explicitly annualized. | Diagnostic estimate of prophylaxis effect. |
| Relative reduction | 1 - Z/Z0, where Z is the scenario outcome and Z0 is the comparator outcome. | Scenario-specific comparator. | Cross-scenario intervention comparison. |
<!-- END ETABLE 10 -->

<!-- BEGIN ETABLE 11 -->
**eTable 11. Core model settings and implementation choices.**

<!-- Generated from `configuration summary derived from the analysis pipeline` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->

| Aspect | Setting | Value |
| --- | --- | --- |
| Model class | Deterministic age-structured compartmental ODE | Two strains, country-specific demographics, vaccination histories, treatment, and PEP are tracked explicitly. |
| Age structure | Five model age groups | 0-2 months, 3-11 months, 1-6 years, 7-17 years, and 18 years or older. |
| Strain structure | Two strain classes | Macrolide-sensitive and macrolide-resistant strains are simulated separately. |
| Vaccine-history structure | Explicit origin states | Unvaccinated, maternally protected, dose-1 recent/waned, dose-2 recent/waned, and dose-3-plus recent/waned states retain distinct effects. |
| Burn-in and horizon | Long burn-in plus analysis window | Sixty-year burn-in followed by a 30-year analysis period beginning on 1 January 2026. |
| Time scale | Daily rates with weekly saved output | All state equations are evaluated in days, and output is stored every 7 days for downstream summaries. |
| Numerical solver | Adaptive Runge-Kutta integration | RK45 with relative tolerance 1e-5 and absolute tolerance 1e-7. |
| Seasonality | Annual cosine forcing | A 4-year diagnostic term is available when surveillance peaks support multi-year recurrence. |
| Demography | Fixed age turnover | Births and aging maintain the country age profile used to initialize each profile. |
| Observation model | Age-specific reporting probabilities | Reporting completeness affects observed cases, while PEP activation uses a separate detection proxy. |
| Calibration target | Annual reported cases | The fit uses a negative binomial likelihood and requires the retained solution to match the observed mean within tolerance. |
| Resistance anchoring | Evidence-based initialization | Country-specific anchors use the latest admissible evidence through 2025, with low-level importation preventing deterministic extinction. |
| Sensitivity screening | Latin-hypercube screening | Twenty-four parameter sets were used for Pearson-correlation robustness screening, not posterior inference. |
<!-- END ETABLE 11 -->
