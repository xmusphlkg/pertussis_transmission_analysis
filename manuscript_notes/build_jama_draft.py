from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "manuscript" / "draft.md"


def read_summary(stem: str) -> pd.DataFrame:
    path = ROOT / "outputs" / "summaries" / f"{stem}_summary.csv"
    if not path.exists():
        raise FileNotFoundError(f"Missing required summary: {path}")
    return pd.read_csv(path)


def clean_country(value: str) -> str:
    return str(value).replace("_", " ")


def fmt_number(value: float, digits: int = 1) -> str:
    value = float(value)
    if abs(value) >= 1000:
        return f"{value:,.0f}"
    if abs(value) >= 100:
        return f"{value:,.{max(0, digits)}f}"
    return f"{value:.{digits}f}"


def fmt_pct(value: float) -> str:
    return f"{100.0 * float(value):.1f}%"


def median_iqr(values: pd.Series, *, percent: bool = False, digits: int = 1) -> str:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    if numeric.empty:
        return "not estimable"
    q25, median, q75 = np.percentile(numeric.to_numpy(dtype=float), [25, 50, 75])
    if percent:
        return f"{fmt_pct(median)} (IQR, {fmt_pct(q25)} to {fmt_pct(q75)})"
    return f"{fmt_number(median, digits)} (IQR, {fmt_number(q25, digits)} to {fmt_number(q75, digits)})"


def median_only(values: pd.Series, *, percent: bool = False, digits: int = 1) -> str:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    if numeric.empty:
        return "not estimable"
    median = float(np.median(numeric.to_numpy(dtype=float)))
    return fmt_pct(median) if percent else fmt_number(median, digits)


def minmax_with_countries(df: pd.DataFrame, column: str) -> str:
    values = pd.to_numeric(df[column], errors="coerce")
    low_idx = int(values.idxmin())
    high_idx = int(values.idxmax())
    return (
        f"{fmt_number(values.loc[low_idx], 1)} in {clean_country(df.loc[low_idx, 'country'])} "
        f"to {fmt_number(values.loc[high_idx], 1)} in {clean_country(df.loc[high_idx, 'country'])}"
    )


def scenario_stats(df: pd.DataFrame, scenario: str, column: str, *, percent: bool = True) -> str:
    rows = df.loc[df["scenario"].eq(scenario)]
    if rows.empty:
        return "not estimable"
    return median_iqr(rows[column], percent=percent)


def scenario_median(df: pd.DataFrame, scenario: str, column: str, *, percent: bool = True) -> str:
    rows = df.loc[df["scenario"].eq(scenario)]
    if rows.empty:
        return "not estimable"
    return median_only(rows[column], percent=percent)


def validate_main_window(*frames: pd.DataFrame) -> None:
    for frame in frames:
        if frame.empty:
            continue
        starts = set(frame["calendar_start_date"].astype(str))
        years = pd.to_numeric(frame["analysis_years"], errors="coerce")
        if starts != {"2026-01-01"} or years.isna().any() or not np.allclose(years, 30.0):
            raise ValueError("Main outputs are not the corrected 30-year 2026-start analysis.")


def high_veinf_benefit(grid: pd.DataFrame) -> str:
    required = {"country", "grid_resistance_prevalence", "grid_VE_inf", "annualized_infant_cases_per_100k"}
    if not required.issubset(grid.columns):
        return "not estimable"
    subset = grid.loc[grid["grid_VE_inf"].isin([0.0, 0.9])].copy()
    pivot = subset.pivot_table(
        index=["country", "grid_resistance_prevalence"],
        columns="grid_VE_inf",
        values="annualized_infant_cases_per_100k",
        aggfunc="first",
    )
    if 0.0 not in pivot.columns or 0.9 not in pivot.columns:
        return "not estimable"
    benefit = 1.0 - pivot[0.9] / pivot[0.0]
    return median_iqr(benefit, percent=True)


def top_sensitivity_terms(sensitivity: pd.DataFrame) -> str:
    corr_cols = [col for col in sensitivity.columns if col.startswith("corr_") and col.endswith("_infant_cases")]
    if not corr_cols or sensitivity.empty:
        return "Sensitivity screening results were available in the Supplement."
    first = sensitivity.iloc[0]
    correlations = []
    for col in corr_cols:
        parameter = col.removeprefix("corr_").removesuffix("_infant_cases")
        correlations.append((parameter, float(first[col])))
    correlations = sorted(correlations, key=lambda item: abs(item[1]), reverse=True)[:3]
    pieces = [f"{name} (r={value:.2f})" for name, value in correlations]
    return "The largest absolute screening correlations with infant cases were " + ", ".join(pieces) + "."


def main() -> None:
    country = read_summary("country_scenarios")
    vaccine = read_summary("vaccine_scenarios")
    resistance = read_summary("resistance_scenarios")
    grid = read_summary("veinf_resistance_grid")
    intervention = read_summary("intervention_scenarios")
    reporting = read_summary("reporting_scenarios")
    sensitivity = read_summary("sensitivity_runs")
    validate_main_window(country, vaccine, resistance, grid, intervention, reporting, sensitivity)

    n_countries = int(country["country"].nunique())
    calibration_loaded = int(country.get("calibration_loaded", pd.Series(False, index=country.index)).astype(bool).sum())
    infant_range = minmax_with_countries(country, "annualized_infant_cases_per_100k")
    infection_range = minmax_with_countries(country, "annualized_infections_per_100k")
    reported_range = minmax_with_countries(country, "annualized_reported_cases_per_100k")
    resistance_start = median_iqr(country["resistant_fraction_start"], percent=True)
    resistance_end = median_iqr(country["resistant_fraction_end"], percent=True)

    ap_infant = scenario_stats(vaccine, "symptom_protective", "relative_reduction_infant_cases")
    ap_infections = scenario_stats(vaccine, "symptom_protective", "relative_reduction_total_infections")
    transmission_infant = scenario_stats(vaccine, "transmission_blocking", "relative_reduction_infant_cases")
    transmission_infections = scenario_stats(vaccine, "transmission_blocking", "relative_reduction_total_infections")
    nextgen_infant = scenario_stats(vaccine, "next_generation", "relative_reduction_infant_cases")
    nextgen_resistant = scenario_stats(vaccine, "next_generation", "relative_reduction_resistant_infections")
    ap_infant_median = scenario_median(vaccine, "symptom_protective", "relative_reduction_infant_cases")
    transmission_infant_median = scenario_median(vaccine, "transmission_blocking", "relative_reduction_infant_cases")
    nextgen_resistant_median = scenario_median(vaccine, "next_generation", "relative_reduction_resistant_infections")

    low_res_infant = scenario_stats(resistance, "low", "annualized_infant_cases_per_100k", percent=False)
    high_resistant_fraction = scenario_stats(resistance, "high", "resistant_fraction", percent=True)
    very_high_resistant_fraction = scenario_stats(resistance, "very_high", "resistant_fraction", percent=True)
    veinf_benefit = high_veinf_benefit(grid)

    higher_child = scenario_stats(intervention, "higher_child_coverage", "relative_reduction_infant_cases")
    adolescent = scenario_stats(intervention, "adolescent_booster", "relative_reduction_infant_cases")
    maternal = scenario_stats(intervention, "maternal_immunization", "relative_reduction_infant_cases")
    guided = scenario_stats(intervention, "resistance_guided_treatment", "relative_reduction_infant_cases")
    nextgen_intervention = scenario_stats(intervention, "next_generation_vaccine", "relative_reduction_infant_cases")
    combined = scenario_stats(intervention, "combined_strategy", "relative_reduction_infant_cases")
    higher_child_median = scenario_median(intervention, "higher_child_coverage", "relative_reduction_infant_cases")
    adolescent_median = scenario_median(intervention, "adolescent_booster", "relative_reduction_infant_cases")
    maternal_median = scenario_median(intervention, "maternal_immunization", "relative_reduction_infant_cases")
    guided_median = scenario_median(intervention, "resistance_guided_treatment", "relative_reduction_infant_cases")
    nextgen_intervention_median = scenario_median(intervention, "next_generation_vaccine", "relative_reduction_infant_cases")
    combined_median = scenario_median(intervention, "combined_strategy", "relative_reduction_infant_cases")
    sensitivity_sentence = top_sensitivity_terms(sensitivity)

    text = f"""# Transmission-Blocking Pertussis Vaccines, Macrolide Resistance, and Intervention Prioritization

**Article type:** Original Investigation; Decision Analytical Model

**Target journal:** JAMA Network Open

**Authors:** Kangguo Li, [coauthors to be added]

**Affiliations:** [Affiliations to be added]

## Key Points

**Question:** How do vaccine transmission-blocking effects and macrolide resistance interact to shape pertussis burden and intervention prioritization across heterogeneous national settings?

**Findings:** In this decision analytical model across {n_countries} country profiles, an acellular pertussis-like vaccine reduced infant cases by {ap_infant} vs no vaccination, while transmission-blocking and next-generation profiles produced larger reductions. Adolescent boosting, maternal immunization, resistance-guided treatment, next-generation vaccines, and combined strategies outperformed higher child coverage alone.

**Meaning:** Pertussis control assessments should distinguish clinical protection from transmission blocking and include resistance-aware management outcomes.

## Abstract

**Importance:** Pertussis persists despite acellular vaccine programs, and macrolide-resistant *Bordetella pertussis* has been reported in multiple settings. Decision models should distinguish symptom protection from transmission blocking.

**Objective:** To evaluate how vaccine mechanisms, macrolide resistance, and intervention strategies influence pertussis burden.

**Design, Setting, and Data Sources:** This decision analytical model used a deterministic age-structured pertussis transmission model with 5 age groups, 2 strain classes, maternal and dose-history states, country-specific contacts, vaccination profiles, seasonality, and reported-case calibration. Eight country profiles were modeled. Main simulations used a 60-year burn-in and a 30-year analysis beginning January 1, 2026.

**Exposures:** Vaccine mechanisms, initial resistant prevalence, child coverage, adolescent boosting, maternal immunization, resistance-guided treatment, next-generation vaccine properties, and combined strategies.

**Main Outcomes and Measures:** Annualized infant cases, all infections, reported cases, resistant infections, resistant fraction, and relative reductions vs comparators.

**Results:** Baseline annualized infant case incidence ranged from {infant_range}; all-infection incidence ranged from {infection_range}. Starting resistant fractions declined from a median of {median_only(country["resistant_fraction_start"], percent=True)} to {median_only(country["resistant_fraction_end"], percent=True)}. Compared with no vaccination, the symptom-protective profile reduced infant cases by {ap_infant_median}; transmission-blocking reduced infant cases by {transmission_infant_median}; and next-generation vaccination reduced resistant infections by {nextgen_resistant_median}. Increasing VE_inf from 0% to 90% across the resistance grid reduced infant cases by {veinf_benefit}. Median infant-case reductions were {higher_child_median} for higher child coverage, {adolescent_median} for adolescent boosting, {maternal_median} for maternal immunization, {guided_median} for resistance-guided treatment, {nextgen_intervention_median} for next-generation vaccination, and {combined_median} for the combined strategy.

**Conclusions and Relevance:** In this model, intervention rankings depended on vaccine transmission blocking and resistance-aware treatment effects. Pertussis decision analyses should include infant burden, total transmission, and resistant infections.

## Introduction

Pertussis remains a public health problem in countries with mature vaccination programs. Acellular pertussis vaccines reduce severe clinical disease, but multiple lines of epidemiologic, immunologic, and experimental evidence suggest that protection wanes and that prevention of colonization or onward transmission may be incomplete.1-9 These features complicate interpretation of reported pertussis trends because surveillance captures only a fraction of infections, especially in adolescents and adults, while infants remain at greatest risk of severe outcomes.10-13

Macrolides are standard first-line agents for pertussis treatment and postexposure prophylaxis, but macrolide-resistant *B pertussis* has become a practical concern. Reports from China, Japan, Australia, the Americas, and other settings indicate that resistance prevalence is geographically heterogeneous and may change rapidly.14-20 Resistance can reduce the expected effect of treatment and prophylaxis, making it important to consider antimicrobial susceptibility alongside vaccine mechanism.

Most policy-facing summaries of pertussis vaccination emphasize disease prevention, but control decisions also depend on transmission, infant protection, reporting, treatment, and resistance. We therefore developed a decision analytical transmission model to compare vaccine mechanism assumptions, macrolide resistance scenarios, and intervention strategies across 8 country profiles. The primary aim was to identify how transmission-blocking vaccine effects and resistance-aware management alter projected infant cases, total infections, reported cases, and resistant infections.

## Methods

### Study Design

This study used a deterministic, age-structured compartmental model of pertussis transmission. The model was designed as a decision analytical model because it synthesized demographic, surveillance, immunization, contact, treatment, and resistance evidence from multiple sources and compared consequences of alternative decision options. The analysis followed relevant non-cost elements of the CHEERS 2022 reporting framework for model-based decision studies. Because the model used aggregated public data and simulated populations, institutional review board review and informed consent were not applicable; this should be confirmed by the submitting institution.

### Country Profiles and Data Sources

Eight national profiles were analyzed: Australia, China, Japan, New Zealand, Singapore, Sweden, the United Kingdom, and the United States. The set was purposive rather than globally representative and was selected to span Western Pacific, European, and Americas settings; different population sizes; contrasting booster and maternal immunization program signatures; heterogeneous reported incidence; and both measured and conservative low resistance anchors. Population denominators came from United Nations World Population Prospects; immunization and schedule inputs came from WHO/UNICEF and national schedule extracts; social contact matrices were based on Prem/contactdata matrices aggregated to the 5 model age groups; and surveillance series through 2023 were used for reported incidence, seasonality, and calibration. Resistance anchors used the latest admissible country-specific evidence through 2025.

### Model Structure

The model tracked 5 age groups: 0 to 2 months, 3 to 11 months, 1 to 6 years, 7 to 17 years, and 18 years or older. Infections were divided into macrolide-sensitive and macrolide-resistant strains. Susceptible individuals retained origin histories corresponding to unvaccinated status, maternal protection, 1-dose recent or waned protection, 2-dose recent or waned protection, and 3-or-more-dose recent or waned protection. Exposed, infectious, and treated states retained these origins so vaccine effects on susceptibility, symptom probability, infectiousness, and infectious duration could act on infection source history rather than on a single aggregate vaccinated state.

Transmission was driven by country-specific contact matrices, annual seasonality, demographic aging and birth turnover, routine vaccination maintenance, importation, and strain-specific treatment and prophylaxis effects. Country-level calibration targeted recent annual reported cases using accepted calibration artifacts; production scenario runs then retained the configured 60-year burn-in and 30-year 2026-start analysis horizon. The main outcomes were annualized infant symptomatic cases per 100,000 infants, all infections per 100,000 persons, reported cases per 100,000 persons, resistant infections, resistant fraction, and relative reduction vs the relevant comparator.

### Scenarios

Vaccine scenarios contrasted no vaccine, an acellular pertussis-like symptom-protective profile, stronger infection blocking, stronger transmission blocking, and next-generation protection. Resistance scenarios used either country-specific resistance timelines or fixed low, moderate, high, and very high resistant prevalence. A 7-by-7 interaction grid varied vaccine reduction in infectiousness and initial resistant prevalence. Intervention strategies represented current practice, higher child coverage, adolescent boosting, maternal immunization, resistance-guided treatment, next-generation vaccination, and a combined strategy. Reporting-rate and global sensitivity analyses evaluated observation uncertainty and parameter influence.

## Results

### Baseline Country Heterogeneity

The calibrated country profiles produced wide variation in projected burden under current acellular pertussis-like vaccination and country-specific resistance anchors. Annualized infant case incidence ranged from {infant_range}, while all-infection incidence ranged from {infection_range}. Reported incidence ranged from {reported_range}, reflecting both transmission differences and age-specific observation assumptions. Resistant fractions started with a median of {resistance_start} and declined to {resistance_end} under the baseline assumption that resistant strains had lower relative fitness than sensitive strains.

### Vaccine Mechanism Scenarios

Compared with no vaccination, the symptom-protective acellular pertussis-like profile reduced infant cases by {ap_infant} and total infections by {ap_infections}. Scenarios with stronger transmission blocking produced larger reductions in population transmission outcomes: the transmission-blocking profile reduced infant cases by {transmission_infant} and total infections by {transmission_infections}. The next-generation profile reduced infant cases by {nextgen_infant} and resistant infections by {nextgen_resistant}, indicating that vaccine effects on infectiousness can influence both clinical and resistance-related outcomes.

### Macrolide Resistance and Transmission Blocking

Fixed resistance scenarios showed that resistant infection burden and resistant fraction were sensitive to initial resistance prevalence and importation. Median annualized infant case incidence under the low-resistance scenario was {low_res_infant}; resistant fractions were {high_resistant_fraction} in the high-resistance scenario and {very_high_resistant_fraction} in the very-high-resistance scenario. Across the VE_inf-resistance grid, increasing vaccine reduction in infectiousness from 0% to 90% reduced infant cases by {veinf_benefit}, supporting the importance of transmission-blocking effects when resistance threatens treatment and prophylaxis performance.

### Intervention Prioritization

Intervention rankings were heterogeneous across countries. Higher child coverage alone had a median infant-case effect of {higher_child}, whereas adolescent boosting reduced infant cases by {adolescent}, maternal immunization by {maternal}, resistance-guided treatment by {guided}, next-generation vaccination by {nextgen_intervention}, and the combined strategy by {combined}. {sensitivity_sentence}

## Discussion

In this decision analytical model, pertussis control conclusions changed when vaccines were allowed to differ in protection against infection, symptoms, infectiousness, and duration. A symptom-protective acellular pertussis-like profile substantially reduced infant cases compared with no vaccination, but profiles with stronger transmission blocking produced larger reductions in total infections and resistant infections. This distinction matters because transmission outcomes affect population-level recurrence, infant exposure risk, and the frequency of infections for which treatment and prophylaxis may be compromised by macrolide resistance.

The findings also suggest that intervention choices should not be evaluated only through routine child coverage. In several modeled settings, adolescent boosting, maternal immunization, resistance-guided treatment, next-generation vaccine assumptions, and combined strategies produced larger median infant-case reductions than higher child coverage alone. This does not imply that routine coverage is unimportant; rather, in high-coverage profiles, marginal increases in child coverage may be less influential than interventions that alter transmission among older age groups, protect the youngest infants directly, or restore treatment effectiveness for resistant infections.

This analysis has limitations. It is a deterministic compartmental model and does not represent stochastic extinction, household clustering, superspreading, or posterior parameter uncertainty. Country profiles combine measured inputs, processed surveillance summaries, and explicit assumptions; therefore, cross-country contrasts should be interpreted as conditional scenario comparisons under a harmonized model rather than definitive national forecasts. Reporting probabilities are literature-informed and calibrated pragmatically, but direct age- and country-specific reporting fractions remain sparse. Resistance anchors are heterogeneous in recency and certainty, and fixed resistance scenarios should be read as stress tests rather than forecasts of clonal spread. Finally, the model does not include costs, quality-adjusted life-years, or formal cost-effectiveness thresholds, so the results inform epidemiologic prioritization rather than economic adoption decisions.

## Conclusions

Across 8 country profiles, vaccine transmission blocking and macrolide resistance materially shaped pertussis burden and intervention rankings. Decision analyses for pertussis should report infant burden, total infections, reported cases, and resistant infections, and should distinguish clinical protection from effects on onward transmission.

## Figure Legends

**Figure 1. Global context, country selection, and baseline heterogeneity.** Reported pertussis incidence, country selection characteristics, model-data reported-incidence anchors, baseline burden metrics, resistance trajectories, and epidemic recurrence diagnostics across the 8 country profiles.

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
"""

    DRAFT.parent.mkdir(parents=True, exist_ok=True)
    DRAFT.write_text(text.rstrip() + "\n", encoding="utf-8")
    word_count = len(text.split())
    print(f"Wrote {DRAFT.relative_to(ROOT)} ({word_count} words, including abstract/references/placeholders).")


if __name__ == "__main__":
    main()
