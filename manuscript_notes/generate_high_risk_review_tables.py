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
    "maternal_immunization",
    "resistance_guided_treatment",
    "next_generation_vaccine",
    "combined_strategy",
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
    infant = ts.loc[ts["age_group"].isin(["infant_0_2m", "infant_3_11m"])].copy()
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
        "Empirical rank distribution across 10 purposively selected country profiles; not a PSA rank probability."
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
    windows = [
        ("2025_2029", pd.Timestamp("2025-01-01"), pd.Timestamp("2029-12-31")),
        ("2025_2034", pd.Timestamp("2025-01-01"), pd.Timestamp("2034-12-31")),
        ("2025_2039", pd.Timestamp("2025-01-01"), pd.Timestamp("2039-12-31")),
        ("2030_2050_excluding_initial_transient", pd.Timestamp("2030-01-01"), pd.Timestamp("2050-12-31")),
        ("2025_2050_full_horizon", pd.Timestamp("2025-01-01"), pd.Timestamp("2050-12-31")),
    ]
    rows: list[pd.DataFrame] = []
    for label, start, end in windows:
        frame = ts.loc[ts["calendar_date"].between(start, end)].copy()
        infant_cases = frame.groupby(["country", "scenario"], as_index=False)["infant_cases"].sum()
        infant_population = (
            frame.loc[frame["age_group"].isin(["infant_0_2m", "infant_3_11m"])]
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
        "pregnancy_tdap_plus_adult_household_package": "maternal_immunization",
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
                "threshold_basis": "Cross-country median reduction on the VE_inf-only grid at 50% starting resistance prevalence.",
            }
        )
    _write(pd.DataFrame(rows), "outputs/tables/veinf_comparator_thresholds.csv")


def main() -> None:
    higher_child_coverage_mechanism()
    intervention_rank_robustness()
    horizon_rank_sensitivity()
    sensitivity_correlations()
    veinf_thresholds_against_comparators()


if __name__ == "__main__":
    main()
