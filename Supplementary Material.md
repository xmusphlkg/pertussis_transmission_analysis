# Supplementary Materials

## Pertussis Vaccine Mechanisms, Transmission Blocking, and Macrolide Resistance

## Contents

Materials and Methods.

Fig. S1. Country profile inputs.

Fig. S2. Diagnostics and sensitivity checks.

Fig. S3. Data provenance and preprocessing audit.

Fig. S4. Calibration acceptance and fit diagnostics.

Fig. S5. Model architecture and state-space accounting.

Fig. S6. Baseline temporal dynamics.

Fig. S7. Vaccine mechanism analysis and source-history decomposition.

Fig. S8. Resistance evidence, initialization, and dynamics.

Fig. S9. Vaccine infectiousness-resistance interaction grid.

Fig. S10. Extended intervention-strategy outcomes.

Fig. S11. Model structure schematic.

Fig. S12. Contact matrix reconstruction.

Table S1. Country-specific population, surveillance, vaccination, and seasonal-forcing inputs.

Table S2. Vaccine-mechanism parameterization used in scenario analyses.

Table S3. Macrolide-resistance initialization, importation, and fitness assumptions.

Table S4. Intervention strategy definitions and modified control levers.

Table S5. Baseline parameter values, admissible ranges, and evidence provenance.

Table S6. Reporting-rate sensitivity scenarios used to probe surveillance uncertainty.

Table S7. Country-specific macrolide-resistance evidence used for resistance anchoring.

Table S8. Calibration acceptance, absolute-fit diagnostics, and fitted transmission parameters.

Table S9. Intervention outcome summaries by country and strategy.

Table S10. Model-derived outcomes and summary definitions.

References.

## Materials and Methods

### Study design

We developed a deterministic age-structured compartmental model of *Bordetella pertussis* transmission to evaluate how vaccine mechanism assumptions and macrolide resistance jointly affect infant disease burden, all-age infection burden, notified cases, resistant infections, and intervention prioritization. The model follows the mechanistic tradition of pertussis resurgence models, but extends the state space to include vaccine-origin histories, two strain classes, country-specific demographic and contact profiles, and resistance-dependent treatment and postexposure prophylaxis (PEP) effects [1-8].

Eight national profiles were analyzed: Australia, China, Japan, New Zealand, Singapore, Sweden, the United Kingdom, and the United States. Country-specific inputs were derived from United Nations World Population Prospects denominators, WHO/UNICEF Joint Reporting Form and immunization schedule records, reported pertussis surveillance series through 2023, Prem/contactdata social-contact matrices, and a macrolide-resistance evidence timeline anchored to the latest admissible evidence year for each country [4-8,12,13]. The principal simulations used a 60-year pre-analysis burn-in to reduce dependence on arbitrary initial conditions, followed by a 30-year analysis horizon beginning on 1 January 2026, with model output retained at 7-day intervals.

All incidence measures are reported as annualized counts per 100,000 persons unless stated otherwise. Infant outcomes combine the 0-2 month and 3-11 month age groups, because these strata jointly capture the highest-risk pre-primary-series and partially vaccinated infant population.

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

These deterministic transformations assign individuals to mechanistic protection histories and do not imply that adult pertussis immunization coverage is directly observed in all settings.

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

Multi-year recurrence was treated as a diagnostic forcing component. Annual reported-case peaks were identified with a minimum spacing of two years and a prominence threshold equal to 10% of the maximum annual count. A 3-5 year median peak interval was considered compatible with multi-year recurrence; otherwise the multi-year amplitude was set to zero.

Prem/contactdata matrices were first represented on 5-year age bins and then aggregated to the five model age groups using population weights. If \(P_{ab}\) is the fine-age contact matrix, \(w_{ia}\) is the distribution of age group \(i\) over fine source bin \(a\), and \(f_{jb}\) is the fraction of fine target bin \(b\) belonging to model group \(j\), then

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

This formulation separates protection against infection, clinical disease, onward infectiousness, and duration of infectiousness. It therefore permits aP-like profiles with strong protection against symptoms but weak infection or transmission blocking, as well as hypothetical next-generation profiles with stronger effects on colonization and transmission [1-3,9,10].

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

where \(e^{dur}_k\) is the treatment-associated reduction in infectious duration for strain \(k\). Macrolide-resistant infections therefore receive smaller treatment effects unless a resistance-guided strategy modifies the resistant treatment block.

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

Each resistance scenario specifies a target resistant fraction at the start of the analysis period. After burn-in, active exposed, infectious, and treated compartments are rebalanced so that for every origin and active compartment pair,

$$
X_{i,R,o}^{active} \leftarrow p_R X_{i,\cdot,o}^{active},
\quad
X_{i,S,o}^{active} \leftarrow (1-p_R)X_{i,\cdot,o}^{active},
$$

where \(p_R\) is the target resistant fraction. This separates the intended resistance scenario from strain fixation that can arise during long deterministic burn-in. Country-timeline scenarios use the latest admissible country-specific resistance estimate at or before the anchor year; fixed scenarios use the low, moderate, high, or very-high values specified in Table S3.

No ongoing prevalence anchoring was applied during the saved analysis period. After the burn-in rebalance, the resistant fraction evolves through differential strain fitness, treatment and PEP effects, susceptible-origin composition, and importation.

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

The scenario analysis had six components:

1. Vaccine mechanism scenarios contrasting no vaccine, symptom-protective aP-like protection, stronger infection blocking, stronger transmission blocking, and next-generation protection.
2. Macrolide-resistance scenarios with country-specific evidence anchors and fixed low, moderate, high, and very-high targets.
3. A grid varying \(\mathrm{VE}_{inf}\) and initial, target, and importation resistant prevalence together.
4. Intervention strategies modifying coverage, maternal protection, adolescent boosting, resistance-guided treatment, PEP effectiveness, and vaccine mechanism assumptions.
5. Reporting-rate sensitivity scenarios.
6. Global sensitivity analysis over vaccine effects, immunity waning, transmission, treatment, PEP, resistance fitness, and reporting.

Global sensitivity analysis used a Latin-hypercube design with 24 parameter sets. Parameter-outcome associations were summarized using Pearson correlations between sampled parameter values and total infant cases, providing a screening measure of direction and relative influence rather than a full variance-decomposition estimate.

## Supplementary figures

![Fig. S1](outputs/appendix/extended_data_figure_1_country_inputs.png)

**Fig. S1. Country-specific input data used to instantiate the eight national pertussis transmission profiles.** **(A)** Vaccine programme coverage. DTP1, DTP3, and maternal immunization coverage values used to initialize age-specific vaccine-origin distributions and birth-entry protection. **(B)** Routine schedule timing. Age at first and last routine pertussis-containing dose, with dose count and maternal programme status summarizing major differences in immunization schedules. **(C)** Seasonal forcing inputs. Country-specific annual seasonal phase and amplitude derived from processed surveillance time series, with point encodings indicating observed reported-incidence intensity and recurrence support. **(D)** Aggregated contact intensity. Population-weighted contact rates after reconstruction, aggregation, and reciprocity balancing to the five model age groups.

![Fig. S2](outputs/appendix/extended_data_figure_2_diagnostics_sensitivity.png)

**Fig. S2. Surveillance, calibration, and robustness diagnostics for the modeled country profiles.** **(A)** Observed surveillance time series. Annual reported pertussis incidence used for country input derivation, restricted to the pre-specified surveillance window. **(B)** Calibration diagnostic. Observed annual reported cases are compared with calibrated model means and approximate predictive intervals for countries with accepted country-level calibrations. **(C)** Reporting-rate sensitivity. Median annualized infection, reported-case, and infant-case incidence under alternative reporting assumptions, illustrating the influence of surveillance ascertainment on absolute burden. **(D)** Global sensitivity analysis. Pearson correlations between sampled parameter values and annualized infant case incidence across the Latin-hypercube sensitivity design.

![Fig. S3](outputs/appendix/extended_data_figure_3_data_provenance.png)

**Fig. S3. Provenance and preprocessing audit for model inputs and analytical outputs.** **(A)** Source domains. Source entries are grouped by country input data, clinical and mechanistic assumptions, and macrolide-resistance evidence. **(B)** Analysis corpus by processing stage. Raw inputs, harmonized inputs, simulations, summaries, tables, and manuscript-support materials are summarized to document data flow through the analysis. **(C)** Country evidence completeness matrix. Availability of population, surveillance, schedule, contact, seasonality, and resistance inputs is shown for each modeled profile. **(D)** Macrolide-resistance evidence timeline. Country-specific resistance anchors and measured isolate or surveillance fractions are plotted by evidence year, with uncertainty intervals where available.

![Fig. S4](outputs/appendix/extended_data_figure_4_calibration_diagnostics.png)

**Fig. S4. Country-level calibration acceptance and fit diagnostics.** **(A)** Calibration acceptance and fit score. Accepted country calibrations are summarized with their retained fit scores and optimizer status. **(B)** Observed and calibrated annual reports. Observed annual reported cases are compared with calibrated annual model means and approximate predictive intervals. **(C)** Fitted reporting probabilities by age. Age-specific reporting probabilities retained after calibration are shown relative to prior reporting assumptions. **(D)** Calibrated transmission and interval width. Calibrated transmission rate is plotted against the relative width of the predictive interval to identify countries with broader residual uncertainty.

![Fig. S5](outputs/appendix/extended_data_figure_5_model_architecture.png)

**Fig. S5. Model architecture, compartment accounting, and vaccine-effect mapping.** **(A)** State-space components. The full ODE system comprises five age groups, two strains, eight susceptible-origin histories, 73 compartments per age group, and 365 dynamic state variables. **(B)** Compartment block accounting. Per-age compartments are decomposed into susceptible-origin, exposed, infectious, treated, and naturally immune blocks. **(C)** Vaccine-effect routes. VE_sus, VE_sym, VE_inf, and VE_dur are mapped to susceptibility, symptomatic disease, onward infectiousness, and infectious duration. **(D)** Origin-specific effect weights. Maternal, partial-dose, recent, and waned vaccine histories carry distinct relative effect weights used by all vaccine-mechanism scenarios.

![Fig. S6](outputs/appendix/extended_data_figure_6_baseline_dynamics.png)

**Fig. S6. Baseline temporal dynamics over the saved analysis period.** **(A)** All-infection incidence at model output time points. Country-specific infection trajectories show recurrent transmission dynamics under the baseline vaccine and resistance assumptions. **(B)** Infant case incidence at model output time points. Symptomatic infant burden is scaled to infant population denominators to highlight country-level differences in risk to the most vulnerable age groups. **(C)** Resistant fraction dynamics. The resistant infection fraction is tracked after burn-in rebalancing to separate scenario initialization from within-analysis strain dynamics. **(D)** Age and strain contribution. The share of infections attributable to each age group and strain summarizes the demographic and resistance composition of baseline transmission.

![Fig. S7](outputs/appendix/extended_data_figure_7_vaccine_deep_dive.png)

**Fig. S7. Vaccine-mechanism analysis and infection-source decomposition.** **(A)** Vaccine scenario parameter matrix. No-vaccine, aP-like symptom-protective, infection-blocking, transmission-blocking, and next-generation profiles are compared across VE_sus, VE_sym, VE_inf, and VE_dur. **(B)** Country-specific outcome reductions. Relative reductions in infant cases, reported cases, total infections, and resistant infections are shown for each country-scenario combination. **(C)** Infection-source histories. Median infection shares are decomposed by maternal, dose-1, dose-2, dose-3-plus, and waned source histories. **(D)** Representative vaccine trajectories. Infant case trajectories for Australia and China illustrate how vaccine-mechanism assumptions alter both magnitude and temporal pattern.

![Fig. S8](outputs/appendix/extended_data_figure_8_resistance_dynamics.png)

**Fig. S8. Macrolide-resistance evidence, initialization, and dynamic consequences.** **(A)** Scenario target versus realized initialization. Fixed resistance scenarios and country-timeline runs are compared with realized starting resistant fractions after burn-in rebalancing. **(B)** Resistant infection burden. Annualized resistant infection incidence is summarized by country and resistance scenario. **(C)** Treatment and PEP event burden. Treated-case and PEP-averted event rates are compared across resistance assumptions to quantify management-related outcome changes. **(D)** Sensitive and resistant strain trajectories. Representative country-timeline trajectories for Australia and China show how initial resistance prevalence, fitness, and importation interact during the saved analysis period.

![Fig. S9](outputs/appendix/extended_data_figure_9_full_grid.png)

**Fig. S9. Full interaction surface between vaccine transmission blocking and initial resistance prevalence.** **(A)** Country-specific infant burden grid. Annualized infant case incidence is shown for each country across the seven-by-seven grid of VE_inf and initial resistant prevalence. **(B)** Benefit of high transmission blocking. The relative infant-case benefit of increasing VE_inf from 0% to 90% is displayed by country and resistance prevalence. **(C)** Median burden across countries. Median infant-case and all-infection incidence are summarized across countries over the same parameter grid. **(D)** Threshold for 50% infant-case reduction. The minimum VE_inf required to reduce infant cases by at least 50% relative to VE_inf = 0 is shown where the threshold is reached.

![Fig. S10](outputs/appendix/extended_data_figure_10_intervention_extended.png)

**Fig. S10. Extended intervention-strategy outcomes across countries and endpoints.** **(A)** Intervention lever matrix. Each strategy is mapped to the child-coverage, adolescent-booster, maternal-immunization, resistance-guided-treatment, and vaccine-improvement levers it modifies. **(B)** Country-specific outcome reductions. Relative reductions in infant cases, reported cases, total infections, and resistant infections are shown for each strategy and country. **(C)** Current versus combined trajectories. Infant case trajectories compare the current strategy with the combined strategy in Australia and China. **(D)** Intervention rank by country. Strategies are ranked within each country by relative reduction in infant cases, highlighting heterogeneity in priority ordering.

![Fig. S11](outputs/appendix/extended_data_figure_11_model_structure.png)

**Fig. S11. Compartmental transmission schematic used to define the dynamic state space.** **(A)** Age-omitted transmission schematic. The schematic condenses the full model into one representative age group, showing origin-specific susceptible histories, strain-specific exposed and infectious branches, treated infection states, and retained infection-source histories. The full ODE repeats this template across five age groups and couples age groups through the contact matrix, demographic ageing, importation, vaccination, and postexposure prophylaxis.

![Fig. S12](outputs/appendix/extended_data_figure_12_contact_matrix_reconstruction.png)

**Fig. S12. Reconstruction and aggregation of country-specific contact matrices.** **(A)** Australia: raw 5-year matrix and reconstructed five-group model matrix. **(B)** China: raw and reconstructed contact matrices. **(C)** Japan: raw and reconstructed contact matrices. **(D)** New Zealand: raw and reconstructed contact matrices. **(E)** Singapore: raw and reconstructed contact matrices. **(F)** Sweden: raw and reconstructed contact matrices. **(G)** United Kingdom: raw and reconstructed contact matrices. **(H)** United States: raw and reconstructed contact matrices. Reconstructed matrices are population weighted and reciprocity balanced before use in force-of-infection calculations.

## Supplementary tables

**Table S1. Country-specific population, surveillance, vaccination, and seasonal-forcing inputs.**

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
**Table S2. Vaccine-mechanism parameterization used in scenario analyses.**

| Scenario | VE_sus | VE_sym | VE_inf | VE_dur | Description |
| --- | --- | --- | --- | --- | --- |
| no_vaccine | 0 | 0 | 0 | 0 | No vaccine protection. |
| symptom_protective | 0.15 | 0.85 | 0.08 | 0 | aP-like disease protection with limited infection/transmission blocking. |
| infection_blocking | 0.7 | 0.85 | 0.2 | 0.1 | Stronger reduction in susceptibility to infection. |
| transmission_blocking | 0.3 | 0.85 | 0.7 | 0.3 | Strong reduction in onward infectiousness and duration. |
| next_generation | 0.8 | 0.9 | 0.75 | 0.4 | Strong infection, symptom, and transmission protection. |
**Table S3. Macrolide-resistance initialization, importation, and fitness assumptions.**

| Scenario | Target resistant fraction | Importation resistant fraction | Nominal anchor rate per year | Country timeline | Fitness_R | Description |
| --- | --- | --- | --- | --- | --- | --- |
| country_timeline | 0.3 | 0.3 | 2 | Yes | 0.7 | Country-specific macrolide-resistance prevalence based on measured surveillance or isolate evidence, supplemented with conservative low-prevalence anchors where numeric estimates were unavailable. |
| low | 0.05 | 0.05 | 2 | No | 0.7 | Low macrolide resistance prevalence. |
| moderate | 0.3 | 0.3 | 2 | No | 0.7 | Moderate macrolide resistance prevalence. |
| high | 0.7 | 0.7 | 2 | No | 0.7 | High macrolide resistance prevalence. |
| very_high | 0.95 | 0.95 | 2 | No | 0.7 | Very high macrolide resistance prevalence. |
**Table S4. Intervention strategy definitions and modified control levers.**

| Strategy | Description |
| --- | --- |
| current | Current vaccination and standard macrolide treatment. |
| higher_child_coverage | Increased routine childhood vaccine coverage. |
| adolescent_booster | Additional booster for school-age children and adolescents. |
| maternal_immunization | Direct infant protection through maternal immunization. |
| resistance_guided_treatment | Resistance testing plus alternative treatment for resistant infections. |
| next_generation_vaccine | Improved transmission-blocking vaccine. |
| combined_strategy | Maternal immunization, adolescent booster, and resistance-guided treatment. |
**Table S5. Baseline parameter values, admissible ranges, and evidence provenance.**

| Parameter | Description | Baseline value | Range | Unit | Source or assumption | Sensitivity |
| --- | --- | --- | --- | --- | --- | --- |
| simulation.end_time | Simulation analysis horizon | 10,950.0 | Fixed main-analysis value | days | Pertussis recurrence literature | No |
| simulation.burn_in_years | Pre-analysis burn-in horizon | 60.00 | Fixed main-analysis value | years | Pertussis recurrence literature | No |
| transmission.beta_S | Transmission rate for macrolide-sensitive pertussis | 0.03 | Country-calibrated where accepted | per contact day | Surveillance calibration | No |
| transmission.relative_infectiousness_asymptomatic | Relative infectiousness of asymptomatic infection | 0.35 | 0.25-0.85 | ratio | WHO position paper and mechanistic assumption | Yes |
| transmission.multi_year_period_years | Target/diagnostic inter-epidemic period | 4.000 | Fixed unless supported by country recurrence diagnostics | years | Pertussis recurrence literature | No |
| transmission.multi_year_amplitude | Weak multi-year phase-locking amplitude | 0 | 0-0.18 | ratio | Recurrence diagnostic assumption | Yes |
| natural_history.latent_duration | Latent period duration | 8.000 | Fixed main-analysis value | days | Clinical pertussis guidance | No |
| natural_history.infectious_duration_symptomatic | Symptomatic infectious duration | 21.00 | Fixed main-analysis value | days | Clinical pertussis guidance | No |
| natural_history.infectious_duration_asymptomatic | Asymptomatic infectious duration | 14.00 | Fixed main-analysis value | days | Clinical pertussis guidance | No |
| natural_history.recovered_immunity_duration | Duration of post-infection protection | 3,285.0 | 2,000-10,000 | days | Natural-immunity literature and sensitivity range | Yes |
| natural_history.vaccine_protection_duration | Duration of vaccine-derived protection proxy | 1,825.0 | 909-5,000 | days | Acellular-vaccine waning evidence | Yes |
| treatment.treatment_rate_symptomatic | Daily transition from symptomatic infection to treatment | 0.05 | 0.020-0.090 | per day | Treatment and PEP guidance | Yes |
| PEP.coverage_household_contacts | Dynamic PEP coverage ceiling among close contacts | 0.3 | 0.05-0.60 | proportion | Close-contact PEP guidance and modeling assumption | Yes |
**Table S6. Reporting-rate sensitivity scenarios used to probe surveillance uncertainty.**

| Scenario | Multiplier | Age multipliers | Time variation | Description |
| --- | --- | --- | --- | --- |
| medium | 1.000 | No | No | Baseline age-specific reporting probabilities. |
| high | 1.500 | No | No | Uniform 50% increase in reporting probabilities, clipped at 1. |
| low | 0.5 | No | No | Uniform 50% reduction in reporting probabilities. |
| age_biased |  | Yes | No | Higher infant ascertainment and lower school-age/adult ascertainment. |
| time_varying | 1.000 | No | Yes | Linear transition from lower to higher ascertainment across the analysis interval. |
**Table S7. Country-specific macrolide-resistance evidence used for resistance anchoring.**

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
**Table S8. Calibration acceptance, absolute-fit diagnostics, and fitted transmission parameters.**

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
**Table S9. Intervention outcome summaries by country and strategy.**

| Country | Strategy | Total infections | Reported cases | Infant cases | Resistant infections | Infant-case reduction | Infection reduction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Australia | adolescent_booster | 1,728,525 | 26,567.2 | 7,925.3 | 29,746.8 | 0.1833 | 0.1394 |
| Australia | combined_strategy | 3,018.6 | 45.57 | 13.61 | 30.69 | 0.9986 | 0.9985 |
| Australia | current | 2,008,520 | 31,414.4 | 9,703.8 | 32,947.0 | 0 | 0 |
| Australia | higher_child_coverage | 2,010,544 | 31,582.5 | 9,973.7 | 33,407.5 | -0.02781 | -0.001008 |
| Australia | maternal_immunization | 1,568,373 | 23,628.3 | 7,469.7 | 26,335.4 | 0.2302 | 0.2191 |
| Australia | next_generation_vaccine | 1,987.3 | 29.84 | 9.215 | 52.25 | 0.9991 | 0.999 |
| Australia | resistance_guided_treatment | 1,751,929 | 27,253.0 | 8,242.4 | 5,009.6 | 0.1506 | 0.1278 |
| China | adolescent_booster | 381,046 | 6,094.0 | 1,342.1 | 371,930 | 0.955 | 0.9565 |
| China | combined_strategy | 30,360.8 | 508.17 | 128.97 | 30,063.4 | 0.9957 | 0.9965 |
| China | current | 8,754,511 | 145,589 | 29,821.1 | 6,551,764 | 0 | 0 |
| China | higher_child_coverage | 8,741,218 | 145,505 | 30,201.4 | 6,531,065 | -0.01275 | 0.001518 |
| China | maternal_immunization | 654,385 | 10,636.8 | 2,309.2 | 624,355 | 0.9226 | 0.9253 |
| China | next_generation_vaccine | 74,143.6 | 1,202.5 | 276.51 | 73,787.8 | 0.9907 | 0.9915 |
| China | resistance_guided_treatment | 114,288 | 1,976.8 | 426.19 | 87,421.9 | 0.9857 | 0.9869 |
| Japan | adolescent_booster | 100,548 | 1,422.2 | 278.33 | 38,388.4 | 0.9603 | 0.9605 |
| Japan | combined_strategy | 3,836.4 | 57.84 | 14.32 | 2,169.3 | 0.998 | 0.9985 |
| Japan | current | 2,548,707 | 37,319.0 | 7,017.0 | 568,905 | 0 | 0 |
| Japan | higher_child_coverage | 2,556,734 | 37,534.4 | 7,115.9 | 564,532 | -0.01409 | -0.00315 |
| Japan | maternal_immunization | 241,573 | 3,454.2 | 661.60 | 71,938.0 | 0.9057 | 0.9052 |
| Japan | next_generation_vaccine | 7,870.2 | 115.02 | 24.68 | 5,778.7 | 0.9965 | 0.9969 |
| Japan | resistance_guided_treatment | 93,900.2 | 1,383.5 | 261.69 | 9,620.3 | 0.9627 | 0.9632 |
| New Zealand | adolescent_booster | 302,144 | 5,231.3 | 1,605.0 | 1,132.7 | 0.2225 | 0.1809 |
| New Zealand | combined_strategy | 510.02 | 8.822 | 2.691 | 1.365 | 0.9987 | 0.9986 |
| New Zealand | current | 368,877 | 6,533 | 2,064.4 | 1,341.6 | 0 | 0 |
| New Zealand | higher_child_coverage | 375,592 | 6,706.8 | 2,139.4 | 1,418.5 | -0.03633 | -0.0182 |
| New Zealand | maternal_immunization | 283,526 | 4,923.5 | 1,565.7 | 1,089.6 | 0.2416 | 0.2314 |
| New Zealand | next_generation_vaccine | 375.60 | 6.510 | 2.045 | 2.383 | 0.999 | 0.999 |
| New Zealand | resistance_guided_treatment | 321,276 | 5,680.3 | 1,754.3 | 211.40 | 0.1502 | 0.129 |
| Singapore | adolescent_booster | 3,576.4 | 50.19 | 12.68 | 12.26 | 0.8726 | 0.874 |
| Singapore | combined_strategy | 408.77 | 5.855 | 1.614 | 1.502 | 0.9838 | 0.9856 |
| Singapore | current | 28,385.5 | 399.11 | 99.58 | 40.19 | 0 | 0 |
| Singapore | higher_child_coverage | 28,914.9 | 407.60 | 103.58 | 40.44 | -0.0401 | -0.01865 |
| Singapore | maternal_immunization | 2,951.4 | 40.89 | 10.93 | 11.11 | 0.8902 | 0.896 |
| Singapore | next_generation_vaccine | 320.84 | 4.541 | 1.310 | 2.314 | 0.9868 | 0.9887 |
| Singapore | resistance_guided_treatment | 3,821.2 | 54.17 | 13.62 | 4.162 | 0.8633 | 0.8654 |
| Sweden | adolescent_booster | 5,256.3 | 84.93 | 22.63 | 18.92 | 0.9559 | 0.956 |
| Sweden | combined_strategy | 442.82 | 7.308 | 2.199 | 1.807 | 0.9957 | 0.9963 |
| Sweden | current | 119,559 | 1,952 | 512.94 | 186.71 | 0 | 0 |
| Sweden | higher_child_coverage | 122,101 | 2,002.1 | 540.42 | 187.93 | -0.05359 | -0.02126 |
| Sweden | maternal_immunization | 4,255.8 | 67.86 | 19.37 | 16.68 | 0.9622 | 0.9644 |
| Sweden | next_generation_vaccine | 328.81 | 5.372 | 1.696 | 2.477 | 0.9967 | 0.9972 |
| Sweden | resistance_guided_treatment | 11,583.9 | 189.97 | 49.75 | 9.375 | 0.903 | 0.9031 |
| United Kingdom | adolescent_booster | 21,756.2 | 366.35 | 110.63 | 29.63 | 0.9621 | 0.9632 |
| United Kingdom | combined_strategy | 2,775.1 | 47.56 | 15.79 | 3.537 | 0.9946 | 0.9953 |
| United Kingdom | current | 590,886 | 10,466.9 | 2,915.4 | 376.06 | 0 | 0 |
| United Kingdom | higher_child_coverage | 535,540 | 9,476.5 | 2,682.7 | 322.77 | 0.07982 | 0.09367 |
| United Kingdom | maternal_immunization | 47,896.7 | 836.70 | 242.23 | 53.64 | 0.9169 | 0.9189 |
| United Kingdom | next_generation_vaccine | 3,311.6 | 57.41 | 17.54 | 7.315 | 0.994 | 0.9944 |
| United Kingdom | resistance_guided_treatment | 70,620.6 | 1,256.8 | 349.48 | 20.06 | 0.8801 | 0.8805 |
| United States | adolescent_booster | 183,707 | 2,912.4 | 860.29 | 0 | 0.961 | 0.9611 |
| United States | combined_strategy | 15,658.1 | 253.11 | 82.72 | 0 | 0.9963 | 0.9967 |
| United States | current | 4,725,321 | 75,773.6 | 22,059.2 | 0 | 0 | 0 |
| United States | higher_child_coverage | 4,842,313 | 78,027.6 | 23,210.8 | 0 | -0.05221 | -0.02476 |
| United States | maternal_immunization | 154,602 | 2,428.1 | 762.77 | 0 | 0.9654 | 0.9673 |
| United States | next_generation_vaccine | 11,891.4 | 191.36 | 65.74 | 0 | 0.997 | 0.9975 |
| United States | resistance_guided_treatment | 435,756 | 7,009.9 | 2,027.4 | 0 | 0.9081 | 0.9078 |
**Table S10. Model-derived outcomes and summary definitions.**

| Quantity | Definition | Denominator or reference population | Primary use |
| --- | --- | --- | --- |
| Total infections | Symptomatic plus asymptomatic incident infections integrated over the analysis interval. | Total population averaged over the interval. | Overall transmission burden. |
| Reported cases | Symptomatic incident infections multiplied by age-specific reporting probabilities and integrated over the analysis interval. | Total population averaged over the interval. | Calibration target and surveillance-comparable burden. |
| Infant cases | Symptomatic incident infections in the 0-2 month and 3-11 month age groups. | Mean population in the two infant age groups. | Primary severe-risk outcome. |
| Resistant infections | Total incident infections attributed to the macrolide-resistant strain. | Total population averaged over the interval. | Resistance burden and treatment relevance. |
| Resistant fraction | Resistant infections divided by total infections at a time point or over a summary interval. | Total infections. | Strain-composition diagnostic. |
| PEP-averted cases | Difference between pre-PEP and post-PEP symptomatic infection flows under the same state trajectory. | Not a population-normalized compartment count unless explicitly annualized. | Diagnostic estimate of prophylaxis effect. |
| Relative reduction | \(1-Z/Z_0\), where \(Z\) is the scenario outcome and \(Z_0\) is the comparator outcome. | Scenario-specific comparator. | Cross-scenario intervention comparison. |
## References

1. World Health Organization. Pertussis vaccines: WHO position paper, August 2015.
2. Wearing HJ, Rohani P. Estimating the duration of pertussis immunity using epidemiological signatures. PLoS Pathogens. 2009;5:e1000647.
3. Domenech de Celles M, Magpantay FMG, King AA, Rohani P. The impact of past vaccination coverage and immunity on pertussis resurgence. Science Translational Medicine. 2018;10:eaaj1748.
4. Prem K, Cook AR, Jit M. Projecting social contact matrices in 152 countries using contact surveys and demographic data. PLoS Computational Biology. 2017;13:e1005697.
5. United Nations Department of Economic and Social Affairs, Population Division. World Population Prospects 2024.
6. World Health Organization. WHO Immunization Data Portal, WUENIC and Joint Reporting Form extracts.
7. Centers for Disease Control and Prevention. Pertussis clinical features, treatment, postexposure prophylaxis, and antibiotic-resistance guidance.
8. European Centre for Disease Prevention and Control. External quality assurance scheme for Bordetella pertussis antimicrobial susceptibility testing, 2022.
9. Warfel JM, Zimmerman LI, Merkel TJ. Acellular pertussis vaccines protect against disease but fail to prevent infection and transmission in a nonhuman primate model. Proceedings of the National Academy of Sciences. 2014;111:787-792.
10. McGirr A, Fisman DN. Duration of pertussis immunity after DTaP immunization: A meta-analysis. Pediatrics. 2015;135:331-343.
11. Lavine JS, King AA, Bjornstad ON. Natural immune boosting in pertussis dynamics and the potential for long-term vaccine failure. Proceedings of the National Academy of Sciences. 2011;108:7259-7264.
12. Centers for Disease Control and Prevention. Antibiotic-resistant *Bordetella pertussis* clinical and surveillance guidance.
13. Pan American Health Organization. Regional alert on antibiotic-resistant pertussis and strengthened vaccination and surveillance, 2025.
