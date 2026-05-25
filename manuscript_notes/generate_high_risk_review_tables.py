from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


ROOT = Path(__file__).resolve().parents[1]


SELECTED_INTERVENTIONS = (
    "current",
    "higher_child_coverage",
    "adolescent_booster",
    "pregnancy_tdap_scaleup",
    "cocooning_adjunct",
    "maternal_immunization",
    "targeted_pep_high_risk",
    "resistance_guided_treatment",
    "next_generation_vaccine",
    "combined_strategy",
)

INFANT_AGE_GROUPS = ("infant_0_2m", "infant_3_11m")

HORIZON_WINDOWS = (
    ("2025_2029", pd.Timestamp("2025-01-01"), pd.Timestamp("2029-12-31")),
    ("2025_2034", pd.Timestamp("2025-01-01"), pd.Timestamp("2034-12-31")),
    ("2025_2039", pd.Timestamp("2025-01-01"), pd.Timestamp("2039-12-31")),
    ("2030_2050_excluding_initial_transient", pd.Timestamp("2030-01-01"), pd.Timestamp("2050-12-31")),
    ("2025_2050_full_horizon", pd.Timestamp("2025-01-01"), pd.Timestamp("2050-12-31")),
)


def _read_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(ROOT / path)


def _write(df: pd.DataFrame, path: str) -> None:
    full = ROOT / path
    full.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(full, index=False)
    try:
        df.to_parquet(full.with_suffix(".parquet"), index=False)
    except Exception:
        pass


def _read_intervention_timeseries(columns: list[str] | None = None) -> pd.DataFrame:
    return pd.read_parquet(ROOT / "outputs/simulations/intervention_scenarios.parquet", columns=columns)


def higher_child_coverage_mechanism() -> None:
    summary = _read_csv("outputs/summaries/intervention_scenarios_summary.csv")
    summary = summary.loc[summary["scenario"].isin(["current", "higher_child_coverage"])].copy()
    wide = summary.pivot(index="country", columns="scenario", values="annualized_infant_cases_per_100k")

    ts = _read_intervention_timeseries(
        [
            "country",
            "scenario",
            "age_group",
            "strain",
            "total_infections",
            "symptomatic_cases",
            "infant_cases",
            "total_population",
            "population",
            "vaccinated_origin_infection_share",
            "waned_origin_infection_share",
            "maternal_origin_infection_share",
            "dose1_origin_infection_share",
            "dose2_origin_infection_share",
            "dose3plus_origin_infection_share",
        ]
    )
    ts = ts.loc[ts["scenario"].isin(["current", "higher_child_coverage"])].copy()

    age = (
        ts.groupby(["country", "scenario", "age_group"], as_index=False)
        .agg(total_infections=("total_infections", "sum"), symptomatic_cases=("symptomatic_cases", "sum"))
        .pivot(index=["country", "age_group"], columns="scenario")
    )
    age.columns = [f"{metric}_{scenario}" for metric, scenario in age.columns]
    age = age.reset_index()
    age["absolute_change_infections"] = age["total_infections_higher_child_coverage"] - age["total_infections_current"]
    age["relative_change_infections"] = age["absolute_change_infections"] / age["total_infections_current"].replace(0, np.nan)
    age["relative_change_symptomatic_cases"] = (
        age["symptomatic_cases_higher_child_coverage"] - age["symptomatic_cases_current"]
    ) / age["symptomatic_cases_current"].replace(0, np.nan)
    age_summary = (
        age.groupby("age_group", as_index=False)
        .agg(
            median_relative_change_infections=("relative_change_infections", "median"),
            q25_relative_change_infections=("relative_change_infections", lambda x: float(np.nanquantile(x, 0.25))),
            q75_relative_change_infections=("relative_change_infections", lambda x: float(np.nanquantile(x, 0.75))),
            median_relative_change_symptomatic_cases=("relative_change_symptomatic_cases", "median"),
            countries_with_infection_increase=("relative_change_infections", lambda x: int(np.sum(np.asarray(x) > 0))),
        )
        .sort_values("age_group")
    )
    _write(age_summary, "outputs/tables/higher_child_coverage_age_shift.csv")

    drivers = (
        age.sort_values(["country", "absolute_change_infections"], ascending=[True, False])
        .groupby("country", as_index=False)
        .first()[["country", "age_group", "absolute_change_infections", "relative_change_infections"]]
        .rename(
            columns={
                "age_group": "largest_absolute_infection_increase_age_group",
                "absolute_change_infections": "largest_absolute_infection_increase",
                "relative_change_infections": "relative_change_in_that_age_group",
            }
        )
    )
    country = wide.reset_index()
    country["relative_reduction_infant_cases"] = 1.0 - (
        country["higher_child_coverage"] / country["current"].replace(0, np.nan)
    )
    country = country.merge(drivers, on="country", how="left")
    country = country.rename(
        columns={
            "current": "current_infant_cases_per_100k",
            "higher_child_coverage": "higher_child_coverage_infant_cases_per_100k",
        }
    )
    _write(country, "outputs/tables/higher_child_coverage_country_mechanism.csv")

    origin_cols = [
        "vaccinated_origin_infection_share",
        "waned_origin_infection_share",
        "maternal_origin_infection_share",
        "dose1_origin_infection_share",
        "dose2_origin_infection_share",
        "dose3plus_origin_infection_share",
    ]
    infant = ts.loc[ts["age_group"].isin(INFANT_AGE_GROUPS)].copy()
    rows: list[dict[str, object]] = []
    for (country_name, scenario), group in infant.groupby(["country", "scenario"]):
        weights = group["total_infections"].to_numpy(dtype=float)
        denominator = float(weights.sum())
        row: dict[str, object] = {
            "country": country_name,
            "scenario": scenario,
            "infant_infections": denominator,
        }
        for col in origin_cols:
            values = group[col].fillna(0.0).to_numpy(dtype=float)
            row[col] = float(np.average(values, weights=weights)) if denominator > 0 else np.nan
        rows.append(row)
    _write(pd.DataFrame(rows), "outputs/tables/infant_vaccine_history_origin_shares.csv")


def intervention_rank_robustness() -> None:
    summary = _read_csv("outputs/summaries/intervention_scenarios_summary.csv")
    summary = summary.loc[summary["scenario"].isin(SELECTED_INTERVENTIONS)].copy()
    summary["rank"] = summary.groupby("country")["annualized_infant_cases_per_100k"].rank(method="min", ascending=True)
    best = summary.groupby("country", as_index=False)["annualized_infant_cases_per_100k"].min().rename(
        columns={"annualized_infant_cases_per_100k": "best_infant_cases_per_100k"}
    )
    summary = summary.merge(best, on="country", how="left")
    summary["within_10_percent_of_best"] = summary["annualized_infant_cases_per_100k"] <= 1.10 * summary[
        "best_infant_cases_per_100k"
    ]
    rank_summary = (
        summary.groupby("scenario", as_index=False)
        .agg(
            median_rank=("rank", "median"),
            min_rank=("rank", "min"),
            max_rank=("rank", "max"),
            countries_ranked_first=("rank", lambda x: int(np.sum(np.asarray(x) == 1))),
            countries_within_10_percent_of_best=("within_10_percent_of_best", "sum"),
            median_infant_cases_per_100k=("annualized_infant_cases_per_100k", "median"),
        )
        .sort_values(["median_rank", "median_infant_cases_per_100k"])
    )
    rank_summary["rank_basis"] = (
        "Empirical scenario-order distribution across 10 purposively selected country profiles; not a decision-ready policy comparison."
    )
    _write(rank_summary, "outputs/tables/intervention_rank_robustness.csv")

    country_rank = summary.loc[
        :,
        [
            "country",
            "scenario",
            "rank",
            "annualized_infant_cases_per_100k",
            "relative_reduction_infant_cases",
            "within_10_percent_of_best",
        ],
    ].sort_values(["country", "rank", "scenario"])
    _write(country_rank, "outputs/tables/intervention_country_rank_heatmap.csv")


def horizon_rank_sensitivity() -> None:
    ts = _read_intervention_timeseries(
        ["country", "scenario", "calendar_date", "time", "age_group", "strain", "infant_cases", "population"]
    )
    ts = ts.loc[ts["scenario"].isin(SELECTED_INTERVENTIONS)].copy()
    ts["calendar_date"] = pd.to_datetime(ts["calendar_date"], errors="coerce")
    rows: list[pd.DataFrame] = []
    for label, start, end in HORIZON_WINDOWS:
        frame = ts.loc[ts["calendar_date"].between(start, end)].copy()
        infant_cases = frame.groupby(["country", "scenario"], as_index=False)["infant_cases"].sum()
        infant_population = (
            frame.loc[frame["age_group"].isin(INFANT_AGE_GROUPS)]
            .drop_duplicates(["country", "scenario", "time", "age_group"])
            .groupby(["country", "scenario", "time"], as_index=False)["population"]
            .sum()
            .groupby(["country", "scenario"], as_index=False)["population"]
            .mean()
            .rename(columns={"population": "mean_infant_population"})
        )
        out = infant_cases.merge(infant_population, on=["country", "scenario"], how="left")
        years = max((end - start).days / 365.0, 1e-9)
        out["analysis_window"] = label
        out["analysis_years"] = years
        out["annualized_infant_cases_per_100k"] = out["infant_cases"] / (
            years * out["mean_infant_population"].replace(0, np.nan)
        ) * 100_000.0
        out["rank"] = out.groupby("country")["annualized_infant_cases_per_100k"].rank(method="min", ascending=True)
        current = out.loc[out["scenario"].eq("current"), ["country", "annualized_infant_cases_per_100k"]].rename(
            columns={"annualized_infant_cases_per_100k": "current_infant_cases_per_100k"}
        )
        out = out.merge(current, on="country", how="left")
        out["relative_reduction_infant_cases"] = 1.0 - out["annualized_infant_cases_per_100k"] / out[
            "current_infant_cases_per_100k"
        ].replace(0, np.nan)
        rows.append(out)
    combined = pd.concat(rows, ignore_index=True)
    _write(combined, "outputs/tables/intervention_horizon_rank_sensitivity.csv")

    rank_summary = (
        combined.groupby(["analysis_window", "scenario"], as_index=False)
        .agg(
            median_rank=("rank", "median"),
            countries_ranked_first=("rank", lambda x: int(np.sum(np.asarray(x) == 1))),
            median_relative_reduction_infant_cases=("relative_reduction_infant_cases", "median"),
        )
        .sort_values(["analysis_window", "median_rank"])
    )
    _write(rank_summary, "outputs/tables/intervention_horizon_rank_summary.csv")


def _age_stratified_infant_frame() -> pd.DataFrame:
    ts = _read_intervention_timeseries(
        [
            "country",
            "scenario",
            "calendar_date",
            "time",
            "age_group",
            "strain",
            "infant_cases",
            "infant_infections",
            "population",
        ]
    )
    ts = ts.loc[ts["scenario"].isin(SELECTED_INTERVENTIONS) & ts["age_group"].isin(INFANT_AGE_GROUPS)].copy()
    ts["calendar_date"] = pd.to_datetime(ts["calendar_date"], errors="coerce")
    return ts


def _summarise_age_stratified_window(frame: pd.DataFrame, years: float) -> pd.DataFrame:
    burden = (
        frame.groupby(["country", "scenario", "age_group"], as_index=False)
        .agg(
            infant_cases=("infant_cases", "sum"),
            infant_infections=("infant_infections", "sum"),
        )
    )
    population = (
        frame.drop_duplicates(["country", "scenario", "time", "age_group"])
        .groupby(["country", "scenario", "age_group"], as_index=False)["population"]
        .mean()
        .rename(columns={"population": "mean_infant_age_population"})
    )
    out = burden.merge(population, on=["country", "scenario", "age_group"], how="left")
    denominator = years * out["mean_infant_age_population"].replace(0, np.nan)
    out["analysis_years"] = years
    out["annualized_infant_cases_per_100k"] = out["infant_cases"] / denominator * 100_000.0
    out["annualized_infant_infections_per_100k"] = out["infant_infections"] / denominator * 100_000.0
    current = out.loc[
        out["scenario"].eq("current"),
        ["country", "age_group", "annualized_infant_cases_per_100k"],
    ].rename(columns={"annualized_infant_cases_per_100k": "current_infant_cases_per_100k"})
    out = out.merge(current, on=["country", "age_group"], how="left")
    out["relative_reduction_infant_cases"] = 1.0 - out["annualized_infant_cases_per_100k"] / out[
        "current_infant_cases_per_100k"
    ].replace(0, np.nan)
    return out


def infant_age_split_intervention() -> None:
    ts = _age_stratified_infant_frame()
    start = pd.Timestamp("2025-01-01")
    end = pd.Timestamp("2050-12-31")
    frame = ts.loc[ts["calendar_date"].between(start, end)].copy()
    years = max((end - start).days / 365.0, 1e-9)
    out = _summarise_age_stratified_window(frame, years)
    out = out.sort_values(["country", "age_group", "scenario"])
    _write(out, "outputs/tables/infant_age_split_intervention.csv")


def infant_age_split_horizon_sensitivity() -> None:
    ts = _age_stratified_infant_frame()
    rows: list[pd.DataFrame] = []
    for label, start, end in HORIZON_WINDOWS:
        frame = ts.loc[ts["calendar_date"].between(start, end)].copy()
        years = max((end - start).days / 365.0, 1e-9)
        out = _summarise_age_stratified_window(frame, years)
        out["analysis_window"] = label
        out["rank"] = out.groupby(["country", "age_group"])["annualized_infant_cases_per_100k"].rank(
            method="min", ascending=True
        )
        rows.append(out)
    combined = pd.concat(rows, ignore_index=True)
    combined = combined.sort_values(["analysis_window", "country", "age_group", "rank", "scenario"])
    _write(combined, "outputs/tables/infant_age_split_horizon_sensitivity.csv")


def intervention_rank_stability_diagnostics() -> None:
    full = _read_csv("outputs/tables/intervention_country_rank_heatmap.csv")
    horizon = _read_csv("outputs/tables/intervention_horizon_rank_sensitivity.csv")
    infant_age = _read_csv("outputs/tables/infant_age_split_horizon_sensitivity.csv")
    rows: list[dict[str, object]] = []
    for scenario in SELECTED_INTERVENTIONS:
        full_s = full.loc[full["scenario"].eq(scenario)]
        horizon_s = horizon.loc[horizon["scenario"].eq(scenario)]
        age_s = infant_age.loc[infant_age["scenario"].eq(scenario)]
        top2_age = int(np.sum(age_s["rank"].to_numpy(dtype=float) <= 2))
        age_cells = int(len(age_s))
        first_age = int(np.sum(age_s["rank"].to_numpy(dtype=float) == 1))
        positive_age = int(np.sum(age_s["relative_reduction_infant_cases"].to_numpy(dtype=float) > 0))
        if age_cells and first_age / age_cells >= 0.50:
            interpretation = "Most stable lowest-burden scenario across country, horizon, and infant-age diagnostics."
        elif age_cells and top2_age / age_cells >= 0.50:
            interpretation = "Often near the lowest modeled burden, but not consistently ordered first."
        elif age_cells and positive_age / age_cells >= 0.50:
            interpretation = "Usually lower burden than current practice, but ordering is horizon- and age-stratum-dependent."
        else:
            interpretation = "Low-benefit or unstable scenario in these deterministic diagnostics."
        rows.append(
            {
                "scenario": scenario,
                "full_horizon_median_rank": float(full_s["rank"].median()),
                "full_horizon_countries_ranked_first": int(np.sum(full_s["rank"].to_numpy(dtype=float) == 1)),
                "full_horizon_countries_ranked_top_two": int(np.sum(full_s["rank"].to_numpy(dtype=float) <= 2)),
                "analysis_window_cells": int(len(horizon_s)),
                "analysis_window_cells_ranked_first": int(np.sum(horizon_s["rank"].to_numpy(dtype=float) == 1)),
                "analysis_window_cells_ranked_top_two": int(np.sum(horizon_s["rank"].to_numpy(dtype=float) <= 2)),
                "analysis_window_cells_positive_reduction": int(
                    np.sum(horizon_s["relative_reduction_infant_cases"].to_numpy(dtype=float) > 0)
                ),
                "infant_age_window_cells": age_cells,
                "infant_age_window_cells_ranked_first": first_age,
                "infant_age_window_cells_ranked_top_two": top2_age,
                "infant_age_window_cells_positive_reduction": positive_age,
                "median_infant_age_window_reduction": float(age_s["relative_reduction_infant_cases"].median()),
                "minimum_infant_age_window_reduction": float(age_s["relative_reduction_infant_cases"].min()),
                "maximum_infant_age_window_reduction": float(age_s["relative_reduction_infant_cases"].max()),
                "rank_stability_interpretation": interpretation,
            }
        )
    out = pd.DataFrame(rows).sort_values(
        ["infant_age_window_cells_ranked_first", "infant_age_window_cells_ranked_top_two"], ascending=False
    )
    _write(out, "outputs/tables/intervention_rank_stability_diagnostics.csv")


def deterministic_event_scale_diagnostics() -> None:
    summary = _read_csv("outputs/summaries/intervention_scenarios_summary.csv")
    summary = summary.loc[summary["scenario"].isin(SELECTED_INTERVENTIONS)].copy()
    summary["annual_total_infections_count"] = summary["total_infections"] / summary["analysis_years"].replace(0, np.nan)
    summary["annual_reported_cases_count"] = summary["total_reported_cases"] / summary["analysis_years"].replace(0, np.nan)
    summary["annual_infant_cases_count"] = summary["total_infant_cases"] / summary["analysis_years"].replace(0, np.nan)

    def flag(row: pd.Series) -> str:
        if row["annual_total_infections_count"] < 1000:
            return "Low aggregate event count; deterministic persistence is a strong assumption."
        if row["annual_infant_cases_count"] < 25:
            return "Low infant-event count; modeled infant cases are especially sensitive to stochastic variation."
        if row["annual_reported_cases_count"] < 50:
            return "Low reported-event count; surveillance stochasticity is likely material."
        return "Aggregate event counts are not near extinction, but stochastic clustering remains unmodeled."

    out = summary.loc[
        :,
        [
            "country",
            "scenario",
            "analysis_years",
            "total_infections",
            "total_reported_cases",
            "total_infant_cases",
            "annualized_infant_cases_per_100k",
            "n_epidemic_peaks",
            "resistant_fraction_end",
            "annual_total_infections_count",
            "annual_reported_cases_count",
            "annual_infant_cases_count",
        ],
    ].copy()
    out["event_scale_flag"] = out.apply(flag, axis=1)
    out = out.sort_values(["scenario", "annual_total_infections_count", "country"])
    _write(out, "outputs/tables/deterministic_event_scale_diagnostics.csv")


def resistance_parameter_justification() -> None:
    rows = [
        {
            "parameter_group": "Country-specific starting resistant fraction",
            "baseline_value": "Latest admissible country timeline anchor; fixed scenarios also used 5%, 30%, 70%, and 95%",
            "explored_range_or_scenarios": "Country timeline; fixed low, moderate, high, and very-high resistance scenarios",
            "source_or_anchor": "Country resistance timeline assembled from China, Japan, Australia, Americas, Europe, and low-anchor surveillance reports through the evidence lock",
            "rationale": "Separates observed or conservative starting strain composition from subsequent modeled selection dynamics.",
            "expected_direction_of_bias": "Higher starting resistant fraction increases resistant burden and the apparent value of resistance-guided management; lower anchors delay resistant dominance.",
            "residual_caveat": "Resistance sampling is heterogeneous across countries and years; anchors are not a globally representative surveillance system.",
        },
        {
            "parameter_group": "Resistant-strain relative fitness (fitness_R)",
            "baseline_value": "1.00 (fitness neutral)",
            "explored_range_or_scenarios": "0.70-1.25 grid and selected-parameter sensitivity range; selected narrative contrasts at 0.85, 1.00, and 1.15",
            "source_or_anchor": "Rapid MRBP expansion and international spread without a demonstrated transmission penalty; local evidence note in manuscript_notes/resistance_fitness_evidence.md",
            "rationale": "Avoids assuming a persistent fitness cost when epidemiologic trajectories in China, Japan, and Australia do not rule out neutral or above-neutral fitness.",
            "expected_direction_of_bias": "Lower fitness reduces projected resistant fraction and resistant-guided treatment benefit; higher fitness accelerates replacement and increases resistant burden.",
            "residual_caveat": "Fitness is represented as one transmission scalar and may vary with vaccine history, treatment pressure, strain background, and host immunity.",
        },
        {
            "parameter_group": "Sensitive-strain treatment effect",
            "baseline_value": "Infectious-duration reduction 0.20; infectiousness reduction 0.15",
            "explored_range_or_scenarios": "Treatment implementation and resistance-mechanism decomposition scenarios",
            "source_or_anchor": "CDC pertussis treatment/PEP guidance and model scenario assumptions",
            "rationale": "Represents early macrolide benefit for susceptible infections without assuming treatment fully blocks transmission.",
            "expected_direction_of_bias": "Stronger sensitive-strain treatment benefit increases selection pressure favoring resistant strains; weaker benefit reduces modeled treatment-mediated selection.",
            "residual_caveat": "Real-world treatment effect depends on timing, diagnosis, adherence, and clinical practice, none of which are explicitly modeled as individual pathways.",
        },
        {
            "parameter_group": "Resistant-strain treatment effect under standard macrolide practice",
            "baseline_value": "Infectious-duration reduction 0.10; infectiousness reduction 0.05",
            "explored_range_or_scenarios": "Equalized treatment counterfactual; resistance-guided treatment alternative",
            "source_or_anchor": "Resistance-aware scenario assumption informed by macrolide resistance biology and treatment guidance",
            "rationale": "Allows resistant infections to receive less benefit from standard macrolide management while testing whether that differential drives replacement.",
            "expected_direction_of_bias": "Lower resistant treatment benefit increases resistant burden and infant cases; equalizing treatment effects lowers selection for resistance.",
            "residual_caveat": "The model does not identify strain-specific treatment effect from patient-level outcome data.",
        },
        {
            "parameter_group": "Postexposure prophylaxis (PEP) coverage",
            "baseline_value": "Household-contact coverage 0.30",
            "explored_range_or_scenarios": "0.05-0.60 in sensitivity analysis and selected-parameter sensitivity multiplier; implementation scenarios vary PEP reach",
            "source_or_anchor": "CDC/PAHO-style public health PEP guidance translated into scenario coverage assumptions",
            "rationale": "Represents partial household/contact implementation rather than universal prophylaxis.",
            "expected_direction_of_bias": "Higher PEP reach amplifies any strain-specific PEP effectiveness differential; lower PEP reach weakens PEP-mediated selection and management benefit.",
            "residual_caveat": "PEP targeting, timing, adherence, and contact tracing are not explicit household processes in the deterministic model.",
        },
        {
            "parameter_group": "PEP effectiveness by strain",
            "baseline_value": "Sensitive 0.70; resistant 0.10 under standard macrolide PEP",
            "explored_range_or_scenarios": "Resistant PEP effectiveness 0.00-0.50; equalized PEP and treatment+PEP decomposition scenarios",
            "source_or_anchor": "Macrolide-resistance mechanism, clinical guidance, and resistance-management scenario assumptions",
            "rationale": "Tests whether strain-specific prophylaxis failure can plausibly create selection pressure under standard macrolide PEP.",
            "expected_direction_of_bias": "A larger sensitive-resistant PEP gap favors resistant strains; equalized PEP effectiveness markedly lowers projected end resistant fraction.",
            "residual_caveat": "PEP effectiveness is not estimated from strain-specific household trial data; results are stress tests conditional on PEP reach and timing.",
        },
        {
            "parameter_group": "Resistance-guided management scenario",
            "baseline_value": "Symptomatic treatment rate 0.065; resistant infectious-duration reduction 0.45; resistant infectiousness reduction 0.35; resistant PEP effectiveness 0.45",
            "explored_range_or_scenarios": "Treatment/PEP implementation scenarios and selected-parameter sensitivity uptake multiplier",
            "source_or_anchor": "CDC resistance-aware treatment guidance translated into a testing-and-alternative-treatment scenario",
            "rationale": "Represents improved recognition of resistance and use of effective alternatives or restored prophylaxis effectiveness.",
            "expected_direction_of_bias": "Higher uptake or restored PEP effectiveness increases projected benefit; low testing reach and uptake reduce or delay benefit.",
            "residual_caveat": "Testing availability, turnaround time, clinician suspicion, drug tolerability, and adherence are not modeled explicitly.",
        },
        {
            "parameter_group": "Resistant importation",
            "baseline_value": "Low-level importation enabled; default rate 0.20 per 100,000 persons/year with country/scenario resistant fraction",
            "explored_range_or_scenarios": "Resistance mechanism decomposition separates ongoing importation from fitness and treatment/PEP differentials",
            "source_or_anchor": "Persistence/reintroduction assumption anchored to observed international spread",
            "rationale": "Prevents deterministic extinction of rare resistant strains while allowing decomposition of whether importation alone drives high end fractions.",
            "expected_direction_of_bias": "Higher importation affects persistence and timing; mechanism decomposition suggests it is not the main driver of near-complete replacement in the main runs.",
            "residual_caveat": "Importation is smooth and low-level rather than a stochastic travel- or outbreak-linked process.",
        },
    ]
    _write(pd.DataFrame(rows), "outputs/tables/resistance_parameter_justification.csv")


def limitation_diagnostic_map() -> None:
    rows = [
        {
            "limitation_domain": "Infant outcomes without direct age-specific calibration",
            "added_or_existing_diagnostic": "Overall calibration fit, fitted reporting gradients, infant contact sensitivity, event-scale diagnostics, and routine-timeliness, infant-age/window, and external age-pattern weighted ordering diagnostics.",
            "supplement_location": "Supplementary Methods, eTables 7, 12, 17, and 19, and eFigure 9",
            "residual_interpretation": "Infant estimates are conditional model outputs; age-pattern weighting is a partial external consistency diagnostic, not full recalibration.",
        },
        {
            "limitation_domain": "Strategy-profile ordering under selected-parameter sensitivity",
            "added_or_existing_diagnostic": "Country-level order positions, analysis-window order positions, infant-age/window order positions, strategy-ordering summary, Figure 4B conditional-interval audit data, and selected-parameter deterministic strategy-ordering diagnostics.",
            "supplement_location": "eTable 15 and eFigure 9",
            "residual_interpretation": "Order-position probabilities are conditional on the selected epidemiologic sensitivity ranges and do not include costs, feasibility, or equity weights.",
        },
        {
            "limitation_domain": "Deterministic dynamics without stochastic extinction or superspreading",
            "added_or_existing_diagnostic": "Event-scale diagnostics identify low-event cells where deterministic persistence assumptions matter most; a small individual stochastic toy model illustrates contact-clustering sensitivity.",
            "supplement_location": "eTables 19 and 21",
            "residual_interpretation": "Near-zero burdens and low-event cells should be read as deterministic thresholds, not stochastic elimination probabilities.",
        },
        {
            "limitation_domain": "No explicit household clustering, contact tracing, or adherence model",
            "added_or_existing_diagnostic": "Resistance-guided treatment implementation sensitivity, infant contact-matrix sensitivity, maternal package component decomposition, and individual stochastic contact-clustering illustration.",
            "supplement_location": "eTables 16, 17, 21, and 24, and eFigure 9",
            "residual_interpretation": "Age-structured proxy diagnostics do not replace household or contact-tracing simulations.",
        },
        {
            "limitation_domain": "Macrolide-resistant strain dynamics depend on fitness and management assumptions",
            "added_or_existing_diagnostic": "Resistance mechanism decomposition, fitness grids, hindcast plausibility checks, treatment/PEP implementation sensitivity, vaccine-infectiousness thresholds, and resistance-parameter justification.",
            "supplement_location": "eTables 13, 14, 16, and 23, and eFigure 9",
            "residual_interpretation": "Resistance trajectories remain stress tests of selection mechanisms rather than unconditional replacement predictions.",
        },
        {
            "limitation_domain": "No costs, utility weights, feasibility, or equity weights",
            "added_or_existing_diagnostic": "Exploratory burden translation from model deaths and symptomatic cases, with hospitalization imputed from transparent scenario assumptions.",
            "supplement_location": "Repository health-utility output tables",
            "residual_interpretation": "This is not a formal cost-effectiveness analysis; the model still does not include costs, decision thresholds, discounting, feasibility constraints, or equity weights.",
        },
        {
            "limitation_domain": "In-development vaccine products cannot be treated as available policies",
            "added_or_existing_diagnostic": "Pipeline-to-mechanism mapping for intranasal BPZE1, OMV-based platforms, genetically detoxified recombinant aP vaccines, and new multicomponent aP candidates.",
            "supplement_location": "eTable 22",
            "residual_interpretation": "Candidate products were represented through mechanism profiles and sensitivity ranges, not product-specific policy scenarios.",
        },
    ]
    _write(pd.DataFrame(rows), "outputs/tables/limitation_diagnostic_map.csv")


def sensitivity_correlations() -> None:
    df = _read_csv("outputs/summaries/sensitivity_runs_summary.csv")
    params = [
        "VE_sus",
        "VE_sym",
        "VE_inf",
        "VE_dur",
        "infectious_duration_symptomatic",
        "infectious_duration_asymptomatic",
        "waning_rate_vaccine",
        "waning_rate_natural",
        "relative_infectiousness_asymptomatic",
        "seasonal_amplitude",
        "multi_year_amplitude",
        "treatment_rate_symptomatic",
        "PEP_coverage",
        "PEP_effectiveness_resistant",
        "fitness_R",
        "reporting_rate_multiplier",
    ]
    outcome = "annualized_infant_cases_per_100k"
    frame = df.loc[:, params + [outcome]].dropna().copy()
    ranks = frame.apply(stats.rankdata)
    rows = []
    y = ranks[outcome].to_numpy(dtype=float)
    xmat = ranks[params].to_numpy(dtype=float)
    for idx, param in enumerate(params):
        x = xmat[:, idx]
        other = np.delete(xmat, idx, axis=1)
        design = np.column_stack([np.ones(len(other)), other])
        x_resid = x - design @ np.linalg.lstsq(design, x, rcond=None)[0]
        y_resid = y - design @ np.linalg.lstsq(design, y, rcond=None)[0]
        pearson = float(stats.pearsonr(frame[param], frame[outcome]).statistic)
        spearman = float(stats.spearmanr(frame[param], frame[outcome]).statistic)
        prcc = float(stats.pearsonr(x_resid, y_resid).statistic)
        rows.append(
            {
                "parameter": param,
                "pearson_r": pearson,
                "spearman_r": spearman,
                "partial_rank_correlation": prcc,
                "absolute_prcc": abs(prcc),
                "screening_note": "Exploratory 48-sample LHS screening; not variance decomposition.",
            }
        )
    out = pd.DataFrame(rows).sort_values("absolute_prcc", ascending=False)
    _write(out, "outputs/tables/sensitivity_correlation_screening.csv")


def veinf_thresholds_against_comparators() -> None:
    grid = _read_csv("outputs/summaries/veinf_resistance_grid_summary.csv")
    intervention = _read_csv("outputs/summaries/intervention_scenarios_summary.csv")
    comparator_map = {
        "infant_exposure_reduction_strategy": "maternal_immunization",
        "resistance_guided_treatment": "resistance_guided_treatment",
    }
    selected_prevalence = [0.0, 0.5, 1.0]
    rows: list[dict[str, object]] = []
    for prevalence in selected_prevalence:
        grid_p = grid.loc[np.isclose(grid["grid_resistance_prevalence"], prevalence)].copy()
        for comparator_label, scenario in comparator_map.items():
            comp = intervention.loc[intervention["scenario"].eq(scenario), ["country", "annualized_infant_cases_per_100k"]]
            comp = comp.rename(columns={"annualized_infant_cases_per_100k": "comparator_infant_cases_per_100k"})
            merged = grid_p.merge(comp, on="country", how="inner")
            thresholds = []
            for country, group in merged.groupby("country"):
                eligible = group.loc[
                    group["annualized_infant_cases_per_100k"].le(group["comparator_infant_cases_per_100k"])
                ]
                thresholds.append(float(eligible["grid_VE_inf"].min()) if not eligible.empty else np.nan)
            finite = [value for value in thresholds if np.isfinite(value)]
            rows.append(
                {
                    "comparator": comparator_label,
                    "resistance_prevalence": prevalence,
                    "median_minimum_VE_inf": float(np.nanmedian(thresholds)) if finite else np.nan,
                    "countries_reaching_comparator": int(len(finite)),
                    "countries_evaluated": int(len(thresholds)),
                    "threshold_basis": "VE_inf-only grid; VE_sus and VE_dur held at the grid baseline.",
                }
            )

    base_prevalence = 0.5
    grid_p = grid.loc[np.isclose(grid["grid_resistance_prevalence"], base_prevalence)].copy()
    reductions_by_ve: dict[float, list[float]] = {}
    for country, group in grid_p.groupby("country"):
        group = group.sort_values("grid_VE_inf")
        baseline = group.loc[np.isclose(group["grid_VE_inf"], 0.2), "annualized_infant_cases_per_100k"]
        if baseline.empty:
            continue
        baseline_value = float(baseline.iloc[0])
        for _, row in group.iterrows():
            ve_inf = float(row["grid_VE_inf"])
            reduction = 1.0 - float(row["annualized_infant_cases_per_100k"]) / max(baseline_value, 1e-9)
            reductions_by_ve.setdefault(ve_inf, []).append(reduction)
    for target in (0.25, 0.50, 0.75):
        eligible = [
            (ve_inf, reductions)
            for ve_inf, reductions in sorted(reductions_by_ve.items())
            if float(np.nanmedian(reductions)) >= target
        ]
        if eligible:
            selected_ve, selected_reductions = eligible[0]
            countries_reaching = int(np.sum(np.asarray(selected_reductions) >= target))
            countries_evaluated = int(len(selected_reductions))
            median_minimum = float(selected_ve)
        else:
            countries_reaching = 0
            countries_evaluated = int(max((len(v) for v in reductions_by_ve.values()), default=0))
            median_minimum = np.nan
        rows.append(
            {
                "comparator": f"{int(target * 100)}% reduction vs VE_inf_0.20",
                "resistance_prevalence": base_prevalence,
                "median_minimum_VE_inf": median_minimum,
                "countries_reaching_comparator": countries_reaching,
                "countries_evaluated": countries_evaluated,
                "threshold_basis": "Median across evaluated profiles on the VE_inf-only grid at 50% starting resistance prevalence.",
            }
        )
    _write(pd.DataFrame(rows), "outputs/tables/veinf_comparator_thresholds.csv")


def main() -> None:
    higher_child_coverage_mechanism()
    intervention_rank_robustness()
    horizon_rank_sensitivity()
    infant_age_split_intervention()
    infant_age_split_horizon_sensitivity()
    intervention_rank_stability_diagnostics()
    deterministic_event_scale_diagnostics()
    resistance_parameter_justification()
    limitation_diagnostic_map()
    sensitivity_correlations()
    veinf_thresholds_against_comparators()


if __name__ == "__main__":
    main()
