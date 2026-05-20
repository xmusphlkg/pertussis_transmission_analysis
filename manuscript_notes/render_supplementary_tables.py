from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path
from statistics import median
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "Supplementary Material.md"
TABLES_HEADING = "## eTables"


@dataclass(frozen=True)
class TableSpec:
    number: str
    title: str
    source: Path | str
    columns: tuple[str, ...]
    labels: tuple[str, ...]
    rows: Callable[[], list[dict[str, str]]] | None = None
    sort_by: tuple[str, ...] = ()


def read_csv_rows(path: Path | str) -> list[dict[str, str]]:
    full_path = ROOT / path
    if not full_path.exists():
        return []
    with full_path.open(newline="", encoding="utf-8-sig") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def outcome_definition_rows() -> list[dict[str, str]]:
    return [
        {
            "quantity": "Total infections",
            "definition": "Symptomatic plus asymptomatic incident infections integrated over the analysis interval; treated infections are counted at infection onset, not as a separate new infection.",
            "denominator": "Mean total population over the interval.",
            "primary_use": "Overall transmission burden.",
        },
        {
            "quantity": "Reported cases",
            "definition": "Symptomatic incident infections multiplied by age-specific reporting probabilities and integrated over the analysis interval.",
            "denominator": "Mean total population over the interval.",
            "primary_use": "Calibration target and surveillance-comparable burden.",
        },
        {
            "quantity": "Infant cases",
            "definition": "Symptomatic incident infections in the 0-2 month and 3-11 month age groups.",
            "denominator": "Mean population in the two infant age groups.",
            "primary_use": "Primary severe-risk outcome.",
        },
        {
            "quantity": "Resistant infections",
            "definition": "Total incident infections attributed to the macrolide-resistant strain.",
            "denominator": "Mean total population over the interval.",
            "primary_use": "Resistance burden and treatment relevance.",
        },
        {
            "quantity": "Resistant fraction",
            "definition": "For interval summaries, resistant incident infections divided by all incident infections; for start/end strain dynamics, resistant active exposed, infectious, and treated compartments divided by all active strain-specific compartments.",
            "denominator": "Total infections or active infected compartments, depending on summary.",
            "primary_use": "Strain-composition diagnostic.",
        },
        {
            "quantity": "PEP-averted cases",
            "definition": "Difference between pre-PEP and post-PEP symptomatic infection flows under the same state trajectory.",
            "denominator": "Not a population-normalized compartment count unless explicitly annualized.",
            "primary_use": "Diagnostic estimate of prophylaxis effect.",
        },
        {
            "quantity": "Relative reduction",
            "definition": "1 - Z/Z0, where Z is the scenario outcome and Z0 is the comparator outcome.",
            "denominator": "Scenario-specific comparator.",
            "primary_use": "Cross-scenario intervention comparison.",
        },
    ]


def fixed_model_setting_rows() -> list[dict[str, str]]:
    return [
        {
            "aspect": "Model class",
            "setting": "Deterministic age-structured compartmental ODE",
            "value": "Two strains, country-specific demographics, vaccination histories, treatment, and PEP are tracked explicitly.",
        },
        {
            "aspect": "Age structure",
            "setting": "Eight model age groups",
            "value": "0-2 months, 3-11 months, 1-4 years, 5-9 years, 10-17 years, 18-39 years, 40-64 years, and 65 years or older.",
        },
        {
            "aspect": "Strain structure",
            "setting": "Two strain classes",
            "value": "Macrolide-sensitive and macrolide-resistant strains are simulated separately.",
        },
        {
            "aspect": "Vaccine-history structure",
            "setting": "Explicit origin states",
            "value": "Unvaccinated, maternally protected, dose-1 recent/waned, dose-2 recent/waned, and dose-3-plus recent/waned states retain distinct effects.",
        },
        {
            "aspect": "Burn-in and horizon",
            "setting": "Long burn-in plus analysis window",
            "value": "Fifteen-year burn-in followed by a 26-year analysis period beginning on 1 January 2025.",
        },
        {
            "aspect": "Time scale",
            "setting": "Daily rates with weekly saved output",
            "value": "All state equations are evaluated in days, and output is stored every 7 days for downstream summaries.",
        },
        {
            "aspect": "Numerical solver",
            "setting": "Adaptive Runge-Kutta integration",
            "value": "RK45 with relative tolerance 1e-5 and absolute tolerance 1e-7.",
        },
        {
            "aspect": "Seasonality",
            "setting": "Annual cosine forcing",
            "value": "A 4-year diagnostic term is available when surveillance peaks support multi-year recurrence.",
        },
        {
            "aspect": "Demography",
            "setting": "WPP trajectory-driven age turnover",
            "value": "Births and aging are driven by UN World Population Prospects 2024 annual trajectories with gentle nudging toward target age profiles; a fixed-profile fallback is retained for tests.",
        },
        {
            "aspect": "Observation model",
            "setting": "Age-specific reporting probabilities",
            "value": "Reporting completeness affects observed cases, while PEP activation uses a separate detection proxy.",
        },
        {
            "aspect": "Calibration target",
            "setting": "Reported surveillance intervals",
            "value": "The fit uses a negative binomial likelihood and requires the retained solution to match the observed annualized mean within tolerance.",
        },
        {
            "aspect": "Resistance anchoring",
            "setting": "Evidence-based initialization",
            "value": "Country-specific anchors use the latest admissible evidence through 2025, with low-level importation preventing deterministic extinction.",
        },
        {
            "aspect": "Sensitivity screening",
            "setting": "Latin-hypercube screening",
            "value": "Forty-eight parameter sets were used for Pearson-correlation robustness screening, separate from posterior inference.",
        },
        {
            "aspect": "Bayesian uncertainty",
            "setting": "Beta-grid posterior predictive analysis with pre-specified checks",
            "value": "A negative binomial reported-case likelihood and literature-informed priors define the beta_S posterior, with weakly identifiable nuisance parameters fixed at evidence-based calibrated values; 95% CrI are used only if beta-grid tail and quadrature-resolution checks pass.",
        },
        {
            "aspect": "Resistance fitness stress test",
            "setting": "Continuous fitness_R grid",
            "value": "Macrolide-resistant strain fitness is varied from 0.70 to 1.25 and crossed with vaccine infectiousness-effect assumptions.",
        },
    ]


def prior_model_comparison_rows() -> list[dict[str, str]]:
    return [
        {
            "prior_model": "Wearing and Rohani 2009",
            "age_structure": "Population-level transmission signatures",
            "waning": "Yes",
            "asymptomatic_transmission": "Implicit or limited",
            "vaccine_infection_blocking": "Composite immunity",
            "vaccine_infectiousness_reduction": "Not separated",
            "resistance": "No",
            "treatment_pep": "No",
            "infant_specific_outcome": "No",
        },
        {
            "prior_model": "Lavine et al 2011",
            "age_structure": "Age-structured pertussis dynamics",
            "waning": "Yes, with immune boosting",
            "asymptomatic_transmission": "Limited",
            "vaccine_infection_blocking": "Composite protection",
            "vaccine_infectiousness_reduction": "Not separated",
            "resistance": "No",
            "treatment_pep": "No",
            "infant_specific_outcome": "Limited",
        },
        {
            "prior_model": "Althouse and Scarpino 2015",
            "age_structure": "Age-structured transmission model",
            "waning": "Yes",
            "asymptomatic_transmission": "Yes",
            "vaccine_infection_blocking": "Composite or scenario-level",
            "vaccine_infectiousness_reduction": "Not decomposed into VE_inf and VE_dur",
            "resistance": "No",
            "treatment_pep": "No",
            "infant_specific_outcome": "Limited",
        },
        {
            "prior_model": "Chit et al 2018",
            "age_structure": "Meta-analysis plus modeling",
            "waning": "Yes",
            "asymptomatic_transmission": "Not primary focus",
            "vaccine_infection_blocking": "Vaccine-effectiveness endpoint",
            "vaccine_infectiousness_reduction": "No",
            "resistance": "No",
            "treatment_pep": "No",
            "infant_specific_outcome": "Limited",
        },
        {
            "prior_model": "Domenech de Celles et al 2018",
            "age_structure": "Age-structured transmission model",
            "waning": "Yes",
            "asymptomatic_transmission": "Implicit in transmission structure",
            "vaccine_infection_blocking": "Composite vaccine-history protection",
            "vaccine_infectiousness_reduction": "Not separated",
            "resistance": "No",
            "treatment_pep": "No",
            "infant_specific_outcome": "Yes, but not resistance-aware",
        },
        {
            "prior_model": "Drivers of resurgence pilot report 2025",
            "age_structure": "Multi-country age-structured model",
            "waning": "Yes",
            "asymptomatic_transmission": "Yes or implicit",
            "vaccine_infection_blocking": "Included",
            "vaccine_infectiousness_reduction": "Incomplete separation",
            "resistance": "No",
            "treatment_pep": "No resistance-aware PEP",
            "infant_specific_outcome": "Yes",
        },
        {
            "prior_model": "Current model",
            "age_structure": "Eight age groups and country-specific contact matrices",
            "waning": "SIRWS waning and boosting",
            "asymptomatic_transmission": "Explicit",
            "vaccine_infection_blocking": "VE_sus",
            "vaccine_infectiousness_reduction": "VE_inf and VE_dur separated",
            "resistance": "Two strain classes with fitness and importation",
            "treatment_pep": "Strain-specific treatment and PEP assumptions",
            "infant_specific_outcome": "Primary outcome",
        },
    ]


def _latest_resistance_anchor_by_country() -> dict[str, str]:
    rows = read_csv_rows("data/raw/country_resistance_timeline.csv")
    anchors: dict[str, dict[str, str]] = {}
    for row in rows:
        country = row.get("country", "")
        try:
            year = int(float(row.get("year", "")))
            fraction = float(row.get("resistant_fraction", ""))
        except ValueError:
            continue
        current = anchors.get(country)
        if current is None or year >= int(float(current.get("year", "0"))):
            anchors[country] = {
                "year": str(year),
                "anchor": f"{fraction * 100:.1f}% ({year})",
            }
    return {country: value["anchor"] for country, value in anchors.items()}


def country_selection_rows() -> list[dict[str, str]]:
    inputs = {row.get("config_key", ""): row for row in read_csv_rows("data/processed/country_profile_inputs.csv")}
    profile = {row.get("country", ""): row for row in read_csv_rows("manuscript_notes/country_profile_table.csv")}
    anchors = _latest_resistance_anchor_by_country()
    who_region = {
        "Australia": "Western Pacific",
        "Brazil": "Americas",
        "China": "Western Pacific",
        "Japan": "Western Pacific",
        "New_Zealand": "Western Pacific",
        "South_Africa": "African",
        "Sweden": "European",
        "Thailand": "South-East Asia",
        "United_Kingdom": "European",
        "United_States": "Americas",
    }
    inclusion_reason = {
        "Australia": "High recent reported incidence; measured low but detectable resistance; mature maternal and booster program.",
        "Brazil": "Large Americas profile with wP schedule, maternal program, and detected resistant cases without national fraction.",
        "China": "Large population, marked post-pandemic resurgence, and near-complete measured macrolide resistance anchor.",
        "Japan": "Western Pacific resurgence and high measured resistance in 2024-2025 reports.",
        "New_Zealand": "Small high-income profile with maternal and adolescent programs and emerging resistance concern.",
        "South_Africa": "African-region profile with shorter overlapping calibration window and contrasting demography.",
        "Sweden": "European profile with high-quality surveillance and booster program contrast.",
        "Thailand": "South-East Asian low reported-incidence profile with wP schedule and low maternal coverage.",
        "United_Kingdom": "European maternal-program profile with established pregnancy vaccination and surveillance data.",
        "United_States": "Large Americas profile with adolescent and maternal Tdap program and low reported resistance.",
    }
    data_quality = {
        "Australia": "High",
        "Brazil": "Moderate",
        "China": "High",
        "Japan": "High",
        "New_Zealand": "Moderate",
        "South_Africa": "Moderate",
        "Sweden": "High",
        "Thailand": "Moderate",
        "United_Kingdom": "High",
        "United_States": "High",
    }

    rows: list[dict[str, str]] = []
    for key in who_region:
        source = inputs.get(key, {})
        summary = profile.get(key, {})
        booster_parts = []
        dose_count = source.get("routine_dose_count", "")
        if dose_count:
            booster_parts.append(f"{dose_count} routine doses")
        if str(source.get("adolescent_booster", "")).lower() == "true":
            booster_parts.append("adolescent booster")
        elif source.get("adolescent_booster", "") != "":
            booster_parts.append("no adolescent booster")
        rows.append(
            {
                "country": key.replace("_", " "),
                "who_region": who_region[key],
                "population": summary.get("total_population", ""),
                "dtp3_coverage": source.get("dtp3_coverage", ""),
                "booster_schedule": "; ".join(booster_parts),
                "maternal_vaccination_policy": source.get("maternal_program_note", ""),
                "recent_reported_incidence": summary.get("observed_mean_annual_reported_incidence_per_100k", ""),
                "resistance_anchor": anchors.get(key.replace("_", " "), anchors.get(key, "")),
                "reason_for_inclusion": inclusion_reason[key],
                "data_quality_rating": data_quality[key],
            }
        )
    return rows


def _parse_semicolon_key_values(text: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for item in str(text).split(";"):
        if "=" not in item:
            continue
        key, value = item.split("=", 1)
        parsed[key.strip()] = value.strip()
    return parsed


def reporting_probability_rows() -> list[dict[str, str]]:
    rows = []
    calibration_rows = read_csv_rows("outputs/tables/calibration_all_countries.csv")
    for row in calibration_rows:
        country = row.get("country", "")
        by_age = _parse_semicolon_key_values(row.get("reporting_multiplier_by_age", ""))
        priors = row.get("reporting_rate_prior_by_age", "")
        try:
            child_vals = [
                float(by_age.get("child_1_4y", "nan")),
                float(by_age.get("child_5_9y", "nan")),
            ]
            school_adolescent = [
                float(by_age.get("child_5_9y", "nan")),
                float(by_age.get("adolescent_10_17y", "nan")),
            ]
            adult_vals = [
                float(by_age.get("young_adult_18_39y", "nan")),
                float(by_age.get("middle_adult_40_64y", "nan")),
                float(by_age.get("elderly_65plus", "nan")),
            ]
        except ValueError:
            child_vals = school_adolescent = adult_vals = []

        def mean_text(values: list[float]) -> str:
            finite = [value for value in values if value == value]
            if not finite:
                return ""
            return f"{sum(finite) / len(finite):.4f}"

        rows.append(
            {
                "country": country,
                "infant_0_2m_reporting_probability": by_age.get("infant_0_2m", ""),
                "infant_3_11m_reporting_probability": by_age.get("infant_3_11m", ""),
                "child_1_9y_reporting_probability": mean_text(child_vals),
                "school_adolescent_5_17y_reporting_probability": mean_text(school_adolescent),
                "adult_18plus_reporting_probability": mean_text(adult_vals),
                "prior_bounds": priors,
                "calibrated_value_source": row.get("reporting_rate_prior_evidence_class", ""),
            }
        )
    return rows


def veinf_threshold_rows() -> list[dict[str, str]]:
    source_rows = read_csv_rows("outputs/summaries/fitness_resistance_grid_summary.csv")
    values: dict[tuple[str, float, float], float] = {}
    for row in source_rows:
        country = row.get("country", "")
        try:
            fitness = round(float(row.get("grid_fitness_R", "")), 3)
            ve_inf = round(float(row.get("grid_VE_inf", "")), 3)
            infant = float(row.get("annualized_infant_cases_per_100k", ""))
        except ValueError:
            continue
        values[(country, fitness, ve_inf)] = infant

    selected_fitness = (0.85, 1.00, 1.10, 1.15)
    thresholds = (0.25, 0.50, 0.75)
    ve_grid = sorted({ve for _, _, ve in values})
    rows: list[dict[str, str]] = []
    for fitness in selected_fitness:
        countries = sorted({country for country, fit, ve in values if fit == round(fitness, 3) and ve == 0.25})
        reductions_by_ve: dict[float, list[float]] = {}
        for ve_inf in ve_grid:
            if ve_inf < 0.25:
                continue
            reductions = []
            for country in countries:
                baseline = values.get((country, round(fitness, 3), 0.25))
                outcome = values.get((country, round(fitness, 3), ve_inf))
                if baseline and outcome is not None:
                    reductions.append(1.0 - outcome / baseline)
            if reductions:
                reductions_by_ve[ve_inf] = reductions

        for threshold in thresholds:
            reached = [
                (ve_inf, reductions)
                for ve_inf, reductions in reductions_by_ve.items()
                if median(reductions) >= threshold
            ]
            if reached:
                ve_inf, reductions = reached[0]
                rows.append(
                    {
                        "fitness_R": f"{fitness:.2f}",
                        "target_reduction": f"{threshold * 100:.0f}%",
                        "minimum_VE_inf": f"{ve_inf:.2f}",
                        "median_reduction_at_minimum": f"{median(reductions) * 100:.1f}%",
                        "countries_meeting_threshold": f"{sum(value >= threshold for value in reductions)}/{len(reductions)}",
                        "interpretation": "Threshold reached on the simulated VE_inf grid.",
                    }
                )
            else:
                final_ve = max(reductions_by_ve)
                final_reductions = reductions_by_ve[final_ve]
                rows.append(
                    {
                        "fitness_R": f"{fitness:.2f}",
                        "target_reduction": f"{threshold * 100:.0f}%",
                        "minimum_VE_inf": f"Not reached through {final_ve:.2f}",
                        "median_reduction_at_minimum": f"{median(final_reductions) * 100:.1f}% at {final_ve:.2f}",
                        "countries_meeting_threshold": f"{sum(value >= threshold for value in final_reductions)}/{len(final_reductions)}",
                        "interpretation": "Threshold not reached on the simulated grid.",
                    }
                )
    return rows


TABLES: tuple[TableSpec, ...] = (
    TableSpec(
        number="S1",
        title="Country-specific population, surveillance, vaccination, and seasonal-forcing inputs.",
        source="manuscript_notes/country_profile_table.csv",
        columns=(
            "country",
            "total_population",
            "seasonal_phase",
            "seasonal_amplitude",
            "observed_mean_annual_reported_incidence_per_100k",
            "vaccine_product",
            "adolescent_booster",
            "maternal_program",
        ),
        labels=(
            "Country",
            "Population",
            "Seasonal phase",
            "Seasonal amplitude",
            "Mean reported incidence per 100k",
            "Vaccine product",
            "Adolescent booster",
            "Maternal program",
        ),
    ),
    TableSpec(
        number="S2",
        title="Vaccine-mechanism parameterization used in scenario analyses.",
        source="manuscript_notes/scenario_table.csv",
        columns=("scenario", "VE_sus", "VE_sym", "VE_inf", "VE_dur", "description"),
        labels=("Scenario", "VE_sus", "VE_sym", "VE_inf", "VE_dur", "Description"),
    ),
    TableSpec(
        number="S3",
        title="Macrolide-resistance initialization, importation, and fitness assumptions.",
        source="manuscript_notes/resistance_scenario_table.csv",
        columns=(
            "scenario",
            "target_prevalence_at_analysis_start",
            "importation_fraction",
            "prevalence_anchor_rate_per_year",
            "uses_country_resistance_timeline",
            "fitness_R",
            "description",
        ),
        labels=(
            "Scenario",
            "Target resistant fraction",
            "Importation resistant fraction",
            "Anchor rate per year",
            "Country timeline",
            "Fitness_R",
            "Description",
        ),
    ),
    TableSpec(
        number="S4",
        title="Intervention strategy definitions and modified control levers.",
        source="manuscript_notes/intervention_scenario_table.csv",
        columns=("strategy", "description"),
        labels=("Strategy", "Description"),
    ),
    TableSpec(
        number="S5",
        title="Baseline parameter values, admissible ranges, and evidence provenance.",
        source="manuscript_notes/parameter_table.csv",
        columns=(
            "parameter",
            "description",
            "baseline_value",
            "range",
            "unit",
            "source_or_assumption",
            "used_in_sensitivity_analysis",
        ),
        labels=(
            "Parameter",
            "Description",
            "Baseline value",
            "Range",
            "Unit",
            "Source or assumption",
            "Sensitivity",
        ),
    ),
    TableSpec(
        number="S6",
        title="Reporting-rate sensitivity scenarios used to probe surveillance uncertainty.",
        source="manuscript_notes/reporting_scenario_table.csv",
        columns=("scenario", "multiplier", "uses_age_multipliers", "uses_time_variation", "description"),
        labels=("Scenario", "Multiplier", "Age multipliers", "Time variation", "Description"),
    ),
    TableSpec(
        number="S7",
        title="Country-specific macrolide-resistance evidence used for resistance anchoring.",
        source="data/raw/country_resistance_timeline.csv",
        columns=("country", "iso3", "year", "sample_size", "resistant_fraction", "lower", "upper", "evidence_type", "source"),
        labels=("Country", "ISO3", "Year", "Sample size", "Resistant fraction", "Lower", "Upper", "Evidence type", "Source"),
        sort_by=("country", "year"),
    ),
    TableSpec(
        number="S8",
        title="Calibration acceptance, absolute-fit diagnostics, and fitted transmission parameters.",
        source="outputs/tables/calibration_all_countries.csv",
        columns=(
            "country",
            "calibration_accepted",
            "optimizer_success",
            "absolute_fit_status",
            "observed_mean_annual_reported_incidence_per_100k",
            "annualized_reported_cases_per_100k",
            "model_to_observed_reported_incidence_ratio",
            "data_fit_score",
            "fit_score",
            "calibrated_beta",
        ),
        labels=(
            "Country",
            "Accepted",
            "Optimizer success",
            "Fit status",
            "Observed reported incidence per 100k",
            "Model reported incidence per 100k",
            "Model/observed ratio",
            "Data fit score",
            "Fit score",
            "Calibrated beta",
        ),
        sort_by=("country",),
    ),
    TableSpec(
        number="S9",
        title="Intervention outcome summaries by country and strategy.",
        source="outputs/summaries/intervention_scenarios_summary.csv",
        columns=(
            "country",
            "scenario",
            "total_infections",
            "total_reported_cases",
            "total_infant_cases",
            "resistant_infections",
            "relative_reduction_infant_cases",
            "relative_reduction_total_infections",
        ),
        labels=(
            "Country",
            "Strategy",
            "Total infections",
            "Reported cases",
            "Infant cases",
            "Resistant infections",
            "Infant-case reduction",
            "Infection reduction",
        ),
        sort_by=("country", "scenario"),
    ),
    TableSpec(
        number="S10",
        title="Model-derived outcomes and summary definitions.",
        source="static outcome definitions",
        rows=outcome_definition_rows,
        columns=("quantity", "definition", "denominator", "primary_use"),
        labels=("Quantity", "Definition", "Denominator or reference population", "Primary use"),
    ),
    TableSpec(
        number="S11",
        title="Core model settings and implementation choices.",
        source="configuration summary derived from the analysis pipeline",
        rows=fixed_model_setting_rows,
        columns=("aspect", "setting", "value"),
        labels=("Aspect", "Setting", "Value"),
    ),
    TableSpec(
        number="S12",
        title="Bayesian uncertainty priors and fixed nuisance settings for the beta-grid posterior predictive analysis.",
        source="manuscript_notes/bayesian_prior_table.csv",
        columns=("parameter", "prior", "interpretation"),
        labels=("Parameter", "Prior", "Interpretation"),
    ),
    TableSpec(
        number="S13",
        title="Continuous macrolide-resistant fitness and vaccine infectiousness grid.",
        source="manuscript_notes/fitness_grid_table.csv",
        columns=("fitness_R", "VE_inf", "description"),
        labels=("Fitness_R", "VE_inf", "Description"),
    ),
    TableSpec(
        number="S14",
        title="Selected prior pertussis models and mechanistic features compared with the current model.",
        source="static prior model comparison",
        rows=prior_model_comparison_rows,
        columns=(
            "prior_model",
            "age_structure",
            "waning",
            "asymptomatic_transmission",
            "vaccine_infection_blocking",
            "vaccine_infectiousness_reduction",
            "resistance",
            "treatment_pep",
            "infant_specific_outcome",
        ),
        labels=(
            "Model",
            "Age structure",
            "Waning",
            "Asymptomatic transmission",
            "Vaccine infection blocking",
            "Vaccine infectiousness reduction",
            "Resistance",
            "Treatment/PEP",
            "Infant-specific outcome",
        ),
    ),
    TableSpec(
        number="S15",
        title="Country selection rationale, programmatic dimensions, and data-quality rating.",
        source="data/processed/country_profile_inputs.csv plus manuscript_notes/country_profile_table.csv",
        rows=country_selection_rows,
        columns=(
            "country",
            "who_region",
            "population",
            "dtp3_coverage",
            "booster_schedule",
            "maternal_vaccination_policy",
            "recent_reported_incidence",
            "resistance_anchor",
            "reason_for_inclusion",
            "data_quality_rating",
        ),
        labels=(
            "Country",
            "WHO region",
            "Population",
            "DTP3 coverage",
            "Booster schedule",
            "Maternal vaccination policy",
            "Recent reported incidence per 100k",
            "Resistance anchor",
            "Reason for inclusion",
            "Data quality",
        ),
    ),
    TableSpec(
        number="S16",
        title="Fitted age-specific reporting probabilities and prior bounds.",
        source="outputs/tables/calibration_all_countries.csv",
        rows=reporting_probability_rows,
        columns=(
            "country",
            "infant_0_2m_reporting_probability",
            "infant_3_11m_reporting_probability",
            "child_1_9y_reporting_probability",
            "school_adolescent_5_17y_reporting_probability",
            "adult_18plus_reporting_probability",
            "prior_bounds",
            "calibrated_value_source",
        ),
        labels=(
            "Country",
            "Infant 0-2 mo",
            "Infant 3-11 mo",
            "Child 1-9 y",
            "School/adolescent 5-17 y",
            "Adult 18+ y",
            "Prior bounds by age",
            "Prior evidence class",
        ),
        sort_by=("country",),
    ),
    TableSpec(
        number="S17",
        title="Macrolide-resistance mechanism decomposition across importation, treatment, PEP, and fitness assumptions.",
        source="outputs/tables/resistance_mechanism_decomposition.csv",
        columns=(
            "scenario",
            "importation",
            "treatment_differential",
            "pep_differential",
            "fitness_R",
            "median_end_resistant_fraction",
            "iqr_end_resistant_fraction",
            "median_infant_cases_per_100k",
            "median_resistant_infections_per_100k",
            "interpretation",
        ),
        labels=(
            "Scenario",
            "Importation",
            "Treatment differential",
            "PEP differential",
            "Fitness_R",
            "Median end resistant fraction",
            "IQR end resistant fraction",
            "Median infant cases per 100k",
            "Median resistant infections per 100k",
            "Interpretation",
        ),
    ),
    TableSpec(
        number="S18",
        title="Threshold analysis for vaccine infectiousness reduction under selected resistant-fitness assumptions.",
        source="outputs/summaries/fitness_resistance_grid_summary.csv",
        rows=veinf_threshold_rows,
        columns=(
            "fitness_R",
            "target_reduction",
            "minimum_VE_inf",
            "median_reduction_at_minimum",
            "countries_meeting_threshold",
            "interpretation",
        ),
        labels=(
            "Fitness_R",
            "Target infant-case reduction vs VE_inf=0.25",
            "Minimum VE_inf",
            "Median reduction at threshold",
            "Countries meeting threshold",
            "Interpretation",
        ),
    ),
    TableSpec(
        number="S19",
        title="Calibration diagnostics by country and calibration period.",
        source="outputs/tables/calibration_fit_diagnostics_summary.csv",
        columns=(
            "country",
            "period",
            "n_intervals",
            "observed_total_reported_cases",
            "predicted_total_reported_cases",
            "mean_absolute_percentage_error",
            "peak_observed_year",
            "peak_predicted_year",
            "peak_timing_error_years",
            "peak_magnitude_ratio",
        ),
        labels=(
            "Country",
            "Period",
            "Intervals",
            "Observed reported cases",
            "Modeled reported cases",
            "MAPE",
            "Observed peak year",
            "Modeled peak year",
            "Peak timing error, y",
            "Peak magnitude ratio",
        ),
        sort_by=("country", "period"),
    ),
    TableSpec(
        number="S20",
        title="Near-term implementation sensitivity for resistance-guided treatment and resistant-strain PEP assumptions.",
        source="outputs/tables/treatment_implementation_sensitivity.csv",
        columns=(
            "scenario",
            "implementation_uptake",
            "pep_restored",
            "pep_coverage_multiplier",
            "median_infant_case_reduction_vs_current_5y",
            "iqr_infant_case_reduction_vs_current_5y",
            "countries_with_positive_reduction",
            "median_infant_cases_per_100k",
            "implementation_note",
        ),
        labels=(
            "Scenario",
            "Guided-treatment uptake",
            "PEP restored",
            "PEP reach multiplier",
            "Median infant-case reduction vs current, 5 y",
            "IQR reduction",
            "Countries with positive reduction",
            "Median infant cases per 100k",
            "Implementation note",
        ),
    ),
    TableSpec(
        number="S21",
        title="Near-term infant contact-matrix sensitivity for current practice and the pregnancy Tdap plus adult/household package.",
        source="outputs/tables/infant_contact_sensitivity.csv",
        columns=(
            "strategy",
            "infant_contact_multiplier",
            "median_infant_cases_per_100k",
            "iqr_infant_cases_per_100k",
            "median_all_infections_per_100k",
            "countries",
            "interpretation",
        ),
        labels=(
            "Strategy",
            "Infant-contact multiplier",
            "Median infant cases per 100k",
            "IQR infant cases per 100k",
            "Median all infections per 100k",
            "Countries",
            "Interpretation",
        ),
    ),
    TableSpec(
        number="S22",
        title="Country-specific mechanism diagnostic for the higher child-coverage scenario.",
        source="outputs/tables/higher_child_coverage_country_mechanism.csv",
        columns=(
            "country",
            "current_infant_cases_per_100k",
            "higher_child_coverage_infant_cases_per_100k",
            "relative_reduction_infant_cases",
            "largest_absolute_infection_increase_age_group",
            "largest_absolute_infection_increase",
            "relative_change_in_that_age_group",
        ),
        labels=(
            "Country",
            "Current infant cases per 100k",
            "Higher child coverage infant cases per 100k",
            "Relative infant-case reduction",
            "Largest infection-increase age group",
            "Largest absolute infection increase",
            "Relative change in that age group",
        ),
        sort_by=("country",),
    ),
    TableSpec(
        number="S23",
        title="Age-specific infection shifts under the higher child-coverage scenario.",
        source="outputs/tables/higher_child_coverage_age_shift.csv",
        columns=(
            "age_group",
            "median_relative_change_infections",
            "q25_relative_change_infections",
            "q75_relative_change_infections",
            "median_relative_change_symptomatic_cases",
            "countries_with_infection_increase",
        ),
        labels=(
            "Age group",
            "Median infection change",
            "Q25 infection change",
            "Q75 infection change",
            "Median symptomatic-case change",
            "Countries with infection increase",
        ),
    ),
    TableSpec(
        number="S24",
        title="Empirical intervention-rank robustness across the 10 country profiles.",
        source="outputs/tables/intervention_rank_robustness.csv",
        columns=(
            "scenario",
            "median_rank",
            "min_rank",
            "max_rank",
            "countries_ranked_first",
            "countries_within_10_percent_of_best",
            "median_infant_cases_per_100k",
            "rank_basis",
        ),
        labels=(
            "Scenario",
            "Median rank",
            "Minimum rank",
            "Maximum rank",
            "Countries ranked first",
            "Countries within 10% of best",
            "Median infant cases per 100k",
            "Rank basis",
        ),
    ),
    TableSpec(
        number="S25",
        title="Intervention-rank sensitivity to analysis-window choice.",
        source="outputs/tables/intervention_horizon_rank_summary.csv",
        columns=(
            "analysis_window",
            "scenario",
            "median_rank",
            "countries_ranked_first",
            "median_relative_reduction_infant_cases",
        ),
        labels=(
            "Analysis window",
            "Scenario",
            "Median rank",
            "Countries ranked first",
            "Median infant-case reduction",
        ),
    ),
    TableSpec(
        number="S26",
        title="Pearson, Spearman, and partial-rank screening correlations from the 48-sample Latin-hypercube analysis.",
        source="outputs/tables/sensitivity_correlation_screening.csv",
        columns=(
            "parameter",
            "pearson_r",
            "spearman_r",
            "partial_rank_correlation",
            "screening_note",
        ),
        labels=(
            "Parameter",
            "Pearson r",
            "Spearman r",
            "Partial rank correlation",
            "Screening note",
        ),
    ),
    TableSpec(
        number="S27",
        title="VE_inf threshold diagnostics against intervention comparators and target reductions.",
        source="outputs/tables/veinf_comparator_thresholds.csv",
        columns=(
            "comparator",
            "resistance_prevalence",
            "median_minimum_VE_inf",
            "countries_reaching_comparator",
            "countries_evaluated",
            "threshold_basis",
        ),
        labels=(
            "Comparator",
            "Starting resistance prevalence",
            "Median minimum VE_inf",
            "Countries reaching comparator",
            "Countries evaluated",
            "Threshold basis",
        ),
    ),
    TableSpec(
        number="S28",
        title="Infant infection vaccine-history origin shares under current and higher child-coverage scenarios.",
        source="outputs/tables/infant_vaccine_history_origin_shares.csv",
        columns=(
            "country",
            "scenario",
            "infant_infections",
            "vaccinated_origin_infection_share",
            "waned_origin_infection_share",
            "maternal_origin_infection_share",
            "dose1_origin_infection_share",
            "dose2_origin_infection_share",
            "dose3plus_origin_infection_share",
        ),
        labels=(
            "Country",
            "Scenario",
            "Infant infections",
            "Vaccinated-origin share",
            "Waned-origin share",
            "Maternal-origin share",
            "Dose-1 share",
            "Dose-2 share",
            "Dose-3-plus share",
        ),
        sort_by=("country", "scenario"),
    ),
    TableSpec(
        number="S29",
        title="Near-term temporal assumption sensitivity for burn-in duration and COVID-19 NPI contact-shock assumptions.",
        source="outputs/tables/temporal_assumption_sensitivity.csv",
        columns=(
            "temporal_dimension",
            "scenario",
            "countries",
            "burn_in_years",
            "npi_reduction_scale",
            "median_infant_cases_per_100k_5y",
            "iqr_infant_cases_per_100k_5y",
            "median_all_infections_per_100k_5y",
            "median_end_resistant_fraction_5y",
            "implementation_note",
        ),
        labels=(
            "Temporal dimension",
            "Scenario",
            "Countries",
            "Burn-in years",
            "NPI reduction scale",
            "Median infant cases per 100k, 5 y",
            "IQR infant cases per 100k, 5 y",
            "Median all infections per 100k, 5 y",
            "Median end resistant fraction, 5 y",
            "Implementation note",
        ),
    ),
)


def sort_rows(rows: list[dict[str, str]], keys: tuple[str, ...]) -> list[dict[str, str]]:
    if not keys:
        return rows
    return sorted(rows, key=lambda row: tuple(str(row.get(key, "")) for key in keys))


def format_number(value: float, *, integer_like: bool = False, year_like: bool = False) -> str:
    if year_like:
        return str(int(round(value)))
    if integer_like and float(value).is_integer():
        return f"{value:,.0f}"
    abs_value = abs(value)
    if abs_value >= 100000:
        return f"{value:,.0f}"
    if abs_value >= 1000:
        return f"{value:,.1f}"
    if abs_value >= 10:
        return f"{value:.2f}"
    if abs_value >= 1:
        return f"{value:.3f}"
    if abs_value == 0:
        return "0"
    return f"{value:.4g}"


def format_value(value: object, column: str = "") -> str:
    text = "" if value is None else str(value).strip()
    if text == "" or text.lower() == "nan":
        return ""
    if column == "country":
        text = text.replace("_", " ")
    lowered = text.lower()
    if lowered in {"true", "false"}:
        return "Yes" if lowered == "true" else "No"
    try:
        year_like = "year" in column.lower()
        integer_like = year_like or column.lower() in {
            "sample_size",
            "total_infections",
            "reported_cases",
            "total_infant_cases",
            "resistant_infections",
            "timeseries_rows",
            "summary_rows",
            "countries",
            "countries_ranked_first",
            "countries_within_10_percent_of_best",
            "countries_with_positive_reduction",
            "countries_with_infection_increase",
            "countries_reaching_comparator",
            "countries_evaluated",
        }
        return format_number(float(text), integer_like=integer_like, year_like=year_like)
    except ValueError:
        return text


def markdown_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\n", "<br>")


def markdown_table(rows: list[dict[str, str]], columns: tuple[str, ...], labels: tuple[str, ...]) -> str:
    if not rows:
        return "_No source rows were found when the table was generated._"
    header = "| " + " | ".join(markdown_escape(label) for label in labels) + " |"
    divider = "| " + " | ".join("---" for _ in labels) + " |"
    body = []
    for row in rows:
        values = [markdown_escape(format_value(row.get(column, ""), column)) for column in columns]
        body.append("| " + " | ".join(values) + " |")
    return "\n".join([header, divider, *body])


def render_table(spec: TableSpec) -> str:
    rows = spec.rows() if spec.rows else read_csv_rows(spec.source)
    rows = sort_rows(rows, spec.sort_by)
    table = markdown_table(rows, spec.columns, spec.labels)
    source = spec.source if isinstance(spec.source, str) else str(spec.source)
    display_number = spec.number[1:] if spec.number.startswith("S") else spec.number
    return (
        f"<!-- BEGIN ETABLE {display_number} -->\n"
        f"**eTable {display_number}. {spec.title}**\n\n"
        f"<!-- Generated from `{source}` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->\n\n"
        f"{table}\n"
        f"<!-- END ETABLE {display_number} -->"
    )


def render_all_tables() -> str:
    return "\n\n".join(render_table(spec) for spec in TABLES)


def replace_table_section(document: str) -> str:
    headings = (TABLES_HEADING, "## Supplementary tables")
    heading = next((candidate for candidate in headings if candidate in document), "")
    if not heading:
        raise ValueError(f"Missing table section for generated tables in {TARGET}")
    prefix, _, _ = document.partition(heading)
    return prefix.rstrip() + "\n\n" + TABLES_HEADING + "\n\n" + render_all_tables() + "\n"


def replace_block(document: str, spec: TableSpec) -> str:
    display_number = spec.number[1:] if spec.number.startswith("S") else spec.number
    pattern = re.compile(
        rf"<!-- BEGIN (?:E?TABLE {re.escape(display_number)}|TABLE {re.escape(spec.number)}) -->.*?"
        rf"<!-- END (?:E?TABLE {re.escape(display_number)}|TABLE {re.escape(spec.number)}) -->",
        flags=re.DOTALL,
    )
    rendered = render_table(spec)
    if not pattern.search(document):
        legacy_pattern = re.compile(
            rf"(?ms)^\*\*(?:eTable {re.escape(display_number)}|Table {re.escape(spec.number)})\..*?"
            rf"(?=^\*\*(?:eTable \d+|Table S\d+)\.|\Z)"
        )
        if legacy_pattern.search(document):
            return legacy_pattern.sub(rendered, document, count=1)
        if TABLES_HEADING in document or "## Supplementary tables" in document:
            return document.rstrip() + "\n\n" + rendered + "\n"
        raise ValueError(f"Missing table section for {spec.number} in {TARGET}")
    return pattern.sub(rendered, document, count=1)


def main() -> None:
    document = TARGET.read_text(encoding="utf-8")
    document = replace_table_section(document)
    TARGET.write_text(document, encoding="utf-8")
    print(f"Updated {TARGET.relative_to(ROOT)} with {len(TABLES)} generated tables.")


if __name__ == "__main__":
    main()
