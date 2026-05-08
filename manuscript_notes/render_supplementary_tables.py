from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "Supplementary Material.md"


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


def output_metadata_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted((ROOT / "outputs" / "metadata").glob("*_run_metadata.json")):
        with path.open(encoding="utf-8") as handle:
            payload = json.load(handle)
        row_counts = payload.get("row_counts", {})
        rows.append(
            {
                "stem": str(payload.get("stem", path.stem.replace("_run_metadata", ""))),
                "generated_at_utc": str(payload.get("generated_at_utc", "")),
                "config_hash": str(payload.get("config_hash", ""))[:12],
                "git_commit": str(payload.get("git", {}).get("commit", ""))[:12],
                "git_dirty": str(payload.get("git", {}).get("dirty", "")),
                "timeseries_rows": str(row_counts.get("timeseries", "")),
                "summary_rows": str(row_counts.get("summaries", row_counts.get("summary", ""))),
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
        source="outputs/tables/table_4_intervention_comparison.csv",
        columns=(
            "country",
            "strategy",
            "total_infections",
            "reported_cases",
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
        sort_by=("country", "strategy"),
    ),
    TableSpec(
        number="S10",
        title="Reproducibility metadata for generated simulation outputs.",
        source="outputs/metadata/*_run_metadata.json",
        rows=output_metadata_rows,
        columns=("stem", "generated_at_utc", "config_hash", "git_commit", "git_dirty", "timeseries_rows", "summary_rows"),
        labels=("Output stem", "Generated at UTC", "Config hash", "Git commit", "Dirty", "Timeseries rows", "Summary rows"),
        sort_by=("stem",),
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
    return (
        f"<!-- BEGIN TABLE {spec.number} -->\n"
        f"**Table {spec.number}. {spec.title}**\n\n"
        f"<!-- Generated from `{source}` by `manuscript_notes/render_supplementary_tables.py`; do not edit inside this block. -->\n\n"
        f"{table}\n"
        f"<!-- END TABLE {spec.number} -->"
    )


def replace_block(document: str, spec: TableSpec) -> str:
    pattern = re.compile(
        rf"<!-- BEGIN TABLE {re.escape(spec.number)} -->.*?<!-- END TABLE {re.escape(spec.number)} -->",
        flags=re.DOTALL,
    )
    rendered = render_table(spec)
    if not pattern.search(document):
        raise ValueError(f"Missing table block for {spec.number} in {TARGET}")
    return pattern.sub(rendered, document, count=1)


def main() -> None:
    document = TARGET.read_text(encoding="utf-8")
    for spec in TABLES:
        document = replace_block(document, spec)
    TARGET.write_text(document, encoding="utf-8")
    print(f"Updated {TARGET.relative_to(ROOT)} with {len(TABLES)} generated tables.")


if __name__ == "__main__":
    main()
