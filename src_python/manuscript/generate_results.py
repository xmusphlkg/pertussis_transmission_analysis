"""Generate manuscript results text from final simulation outputs.

This script reads the validated summary CSVs and produces:
1. A structured CSV of all numbers used in the manuscript
2. A markdown fragment with pre-formatted result sentences
3. Key Points text with validated numbers

All manuscript numbers should come from this script, never from manual copy-paste.

Usage:
    python -m src_python.manuscript.generate_results
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from src_python.simulation.common import (
    config_fingerprint,
    load_configs,
    validate_run_metadata,
)
from src_python.utils.io import project_path, read_table, write_dataframe


def _fmt_pct(value: float, decimals: int = 1) -> str:
    """Format a proportion as percentage string."""
    return f"{value * 100:.{decimals}f}%"


def _fmt_rate(value: float, decimals: int = 0) -> str:
    """Format a rate per 100k."""
    return f"{value:,.{decimals}f}"


def _median_iqr(series: pd.Series, decimals: int = 1) -> str:
    """Format median (IQR) from a series."""
    med = series.median()
    q25 = series.quantile(0.25)
    q75 = series.quantile(0.75)
    return f"{med:.{decimals}f} (IQR, {q25:.{decimals}f} to {q75:.{decimals}f})"


def _median_iqr_pct(series: pd.Series, decimals: int = 1) -> str:
    """Format median (IQR) as percentages."""
    med = series.median() * 100
    q25 = series.quantile(0.25) * 100
    q75 = series.quantile(0.75) * 100
    return f"{med:.{decimals}f}% (IQR, {q25:.{decimals}f}% to {q75:.{decimals}f}%)"


def _safe_read(stem: str) -> pd.DataFrame | None:
    """Read a summary CSV if it exists and passes metadata validation."""
    path = project_path("outputs", "summaries", f"{stem}_summary.csv")
    if not path.exists():
        parquet_path = path.with_suffix(".parquet")
        if parquet_path.exists():
            path = parquet_path
        else:
            return None
    try:
        validate_run_metadata(stem)
    except (FileNotFoundError, ValueError) as exc:
        print(f"  WARNING: {stem} metadata validation failed: {exc}")
        return None
    return read_table(path)


def generate_baseline_numbers(results: dict) -> None:
    """Extract baseline country heterogeneity numbers."""
    df = _safe_read("country_scenarios")
    if df is None:
        df = _safe_read("baseline_timeseries")
    if df is None:
        results["baseline"] = {"status": "MISSING - outputs not available"}
        return

    # Infant case incidence range
    if "annualized_infant_case_rate_per_100k" in df.columns:
        infant_col = "annualized_infant_case_rate_per_100k"
    elif "total_infant_cases" in df.columns and "analysis_years" in df.columns:
        df = df.copy()
        # Approximate rate
        infant_col = "total_infant_cases"
    else:
        results["baseline"] = {"status": "MISSING - required columns not found"}
        return

    results["baseline"] = {
        "status": "generated",
        "n_countries": int(df["country"].nunique()) if "country" in df.columns else "N/A",
    }


def generate_vaccine_numbers(results: dict) -> None:
    """Extract vaccine mechanism scenario numbers."""
    df = _safe_read("vaccine_scenarios")
    if df is None:
        results["vaccine_scenarios"] = {"status": "MISSING"}
        return

    numbers = {"status": "generated"}

    # Relative reductions vs no_vaccine
    for scenario in ["symptom_protective", "infection_blocking", "next_generation"]:
        subset = df[df["scenario"] == scenario] if "scenario" in df.columns else pd.DataFrame()
        if subset.empty:
            continue
        if "relative_reduction_infant_cases" in subset.columns:
            col = subset["relative_reduction_infant_cases"].dropna()
            if not col.empty:
                numbers[f"{scenario}_infant_reduction"] = _median_iqr_pct(col)
        if "relative_reduction_total_infections" in subset.columns:
            col = subset["relative_reduction_total_infections"].dropna()
            if not col.empty:
                numbers[f"{scenario}_infection_reduction"] = _median_iqr_pct(col)
        if "relative_reduction_resistant_infections" in subset.columns:
            col = subset["relative_reduction_resistant_infections"].dropna()
            if not col.empty:
                numbers[f"{scenario}_resistant_reduction"] = _median_iqr_pct(col)

    results["vaccine_scenarios"] = numbers


def generate_intervention_numbers(results: dict) -> None:
    """Extract intervention prioritization numbers."""
    df = _safe_read("intervention_scenarios")
    if df is None:
        results["interventions"] = {"status": "MISSING"}
        return

    numbers = {"status": "generated"}

    for intervention in [
        "higher_child_coverage",
        "adolescent_booster",
        "maternal_immunization",
        "maternal_direct_antibody_only",
        "maternal_adult_boosting_only",
        "maternal_cocooning_only",
        "resistance_guided_treatment",
        "next_generation_vaccine",
        "combined_strategy",
    ]:
        subset = df[df["scenario"] == intervention] if "scenario" in df.columns else pd.DataFrame()
        if subset.empty:
            continue
        if "relative_reduction_infant_cases" in subset.columns:
            col = subset["relative_reduction_infant_cases"].dropna()
            if not col.empty:
                numbers[f"{intervention}_infant_reduction"] = _median_iqr_pct(col)

    results["interventions"] = numbers


def generate_resistance_numbers(results: dict) -> None:
    """Extract resistance scenario numbers."""
    df = _safe_read("resistance_scenarios")
    if df is None:
        results["resistance"] = {"status": "MISSING"}
        return

    numbers = {"status": "generated"}

    if "scenario" in df.columns and "resistant_fraction_end" in df.columns:
        for scenario in df["scenario"].unique():
            subset = df[df["scenario"] == scenario]
            col = subset["resistant_fraction_end"].dropna()
            if not col.empty:
                numbers[f"{scenario}_end_resistant_fraction"] = _median_iqr_pct(col)

    results["resistance"] = numbers


def generate_sensitivity_numbers(results: dict) -> None:
    """Extract sensitivity analysis correlation numbers."""
    df = _safe_read("sensitivity_runs")
    if df is None:
        results["sensitivity"] = {"status": "MISSING"}
        return

    results["sensitivity"] = {"status": "generated"}


def generate_bayesian_numbers(results: dict) -> None:
    """Extract Bayesian uncertainty numbers (if converged)."""
    # Check convergence first
    convergence_path = project_path("outputs/summaries/bayesian_convergence_summary.txt")
    if convergence_path.exists():
        text = convergence_path.read_text()
        if "All parameters converged: False" in text:
            results["bayesian"] = {
                "status": "NOT_CONVERGED",
                "note": "Bayesian results should be reported as exploratory only. "
                        "Do not use 95% CrI in main text until convergence is achieved.",
            }
            return

    df = _safe_read("bayesian_uncertainty")
    if df is None:
        results["bayesian"] = {"status": "MISSING"}
        return

    results["bayesian"] = {"status": "generated_check_convergence"}


def generate_calibration_status(results: dict) -> None:
    """Check calibration status across all production outputs."""
    stems = [
        "country_scenarios",
        "vaccine_scenarios",
        "intervention_scenarios",
        "resistance_scenarios",
    ]
    status = {}
    for stem in stems:
        df = _safe_read(stem)
        if df is None:
            status[stem] = "MISSING"
            continue
        if "calibration_loaded" in df.columns:
            n_uncalibrated = int(df["calibration_loaded"].eq(False).sum())
            n_total = len(df)
            if n_uncalibrated > 0:
                status[stem] = f"WARNING: {n_uncalibrated}/{n_total} rows uncalibrated"
            else:
                status[stem] = f"OK: all {n_total} rows calibrated"
        else:
            status[stem] = "calibration_loaded column not present"

    results["calibration_status"] = status


def _build_key_points(results: dict) -> str:
    """Build Key Points text from validated numbers."""
    lines = [
        "## Key Points (auto-generated)",
        "",
        "**Question:** How do vaccine transmission-blocking effects and macrolide "
        "resistance interact to shape pertussis burden and intervention prioritization "
        "across heterogeneous national settings?",
        "",
    ]

    # Findings
    findings_parts = []
    vaccine = results.get("vaccine_scenarios", {})
    interventions = results.get("interventions", {})

    if vaccine.get("status") == "generated":
        sp = vaccine.get("symptom_protective_infant_reduction", "N/A")
        ng = vaccine.get("next_generation_infant_reduction", "N/A")
        findings_parts.append(
            f"the symptom-protective profile reduced infant cases by {sp} vs no vaccination, "
            f"while the next-generation profile achieved {ng}"
        )

    if interventions.get("status") == "generated":
        rgt = interventions.get("resistance_guided_treatment_infant_reduction", "N/A")
        combined = interventions.get("combined_strategy_infant_reduction", "N/A")
        hcc = interventions.get("higher_child_coverage_infant_reduction", "N/A")
        findings_parts.append(
            f"resistance-guided treatment reduced infant cases by {rgt}, "
            f"the combined strategy by {combined}, "
            f"while higher child coverage alone achieved {hcc}"
        )

    if findings_parts:
        lines.append(f"**Findings:** In this decision analytical model, {'; '.join(findings_parts)}.")
    else:
        lines.append("**Findings:** [Numbers not yet available - run pipeline first]")

    lines.extend([
        "",
        "**Meaning:** Pertussis control assessments should distinguish clinical "
        "protection from transmission blocking and include resistance-aware "
        "management outcomes.",
        "",
    ])

    # Bayesian status warning
    bayesian = results.get("bayesian", {})
    if bayesian.get("status") == "NOT_CONVERGED":
        lines.extend([
            "",
            "⚠️ BAYESIAN WARNING: Posterior predictive results have NOT converged. "
            "Do NOT include 95% CrI in Key Points or Abstract until MCMC diagnostics pass.",
            "",
        ])

    return "\n".join(lines)


def _build_results_fragment(results: dict) -> str:
    """Build a markdown fragment with all manuscript numbers."""
    lines = [
        "# Manuscript Results (auto-generated)",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"Config hash: {config_fingerprint()}",
        "",
    ]

    # Calibration status
    lines.append("## Calibration Status")
    cal_status = results.get("calibration_status", {})
    for stem, status in cal_status.items():
        icon = "✅" if "OK" in str(status) else "⚠️"
        lines.append(f"- {icon} {stem}: {status}")
    lines.append("")

    # Bayesian status
    bayesian = results.get("bayesian", {})
    if bayesian.get("status") == "NOT_CONVERGED":
        lines.extend([
            "## ⚠️ Bayesian Analysis Status: NOT CONVERGED",
            "",
            "All Bayesian posterior predictive results and 95% CrI should be:",
            "- Removed from Abstract and Key Points",
            "- Reported as 'exploratory' in supplementary material only",
            "- Replaced with probabilistic sensitivity intervals if needed",
            "",
        ])

    # Vaccine scenarios
    lines.append("## Vaccine Mechanism Scenarios")
    vaccine = results.get("vaccine_scenarios", {})
    if vaccine.get("status") == "generated":
        for key, value in vaccine.items():
            if key != "status":
                lines.append(f"- {key}: {value}")
    else:
        lines.append(f"- Status: {vaccine.get('status', 'unknown')}")
    lines.append("")

    # Interventions
    lines.append("## Intervention Prioritization")
    interventions = results.get("interventions", {})
    if interventions.get("status") == "generated":
        for key, value in interventions.items():
            if key != "status":
                lines.append(f"- {key}: {value}")
    else:
        lines.append(f"- Status: {interventions.get('status', 'unknown')}")
    lines.append("")

    # Resistance
    lines.append("## Resistance Scenarios")
    resistance = results.get("resistance", {})
    if resistance.get("status") == "generated":
        for key, value in resistance.items():
            if key != "status":
                lines.append(f"- {key}: {value}")
    else:
        lines.append(f"- Status: {resistance.get('status', 'unknown')}")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    """Generate all manuscript numbers from validated outputs."""
    print("Generating manuscript results from simulation outputs...")
    print(f"  Config hash: {config_fingerprint()}")
    print()

    results = {}

    generate_calibration_status(results)
    generate_baseline_numbers(results)
    generate_vaccine_numbers(results)
    generate_intervention_numbers(results)
    generate_resistance_numbers(results)
    generate_sensitivity_numbers(results)
    generate_bayesian_numbers(results)

    # Write structured results
    output_dir = project_path("manuscript_notes")
    output_dir.mkdir(parents=True, exist_ok=True)

    # JSON with all numbers
    json_path = output_dir / "generated_manuscript_numbers.json"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"  Written: {json_path}")

    # Markdown fragment
    fragment = _build_results_fragment(results)
    md_path = output_dir / "generated_results_for_text.md"
    md_path.write_text(fragment, encoding="utf-8")
    print(f"  Written: {md_path}")

    # Key Points
    key_points = _build_key_points(results)
    kp_path = output_dir / "generated_key_points.md"
    kp_path.write_text(key_points, encoding="utf-8")
    print(f"  Written: {kp_path}")

    # Print summary
    print()
    print("=" * 60)
    print("MANUSCRIPT NUMBER GENERATION COMPLETE")
    print("=" * 60)
    print()

    # Warnings
    bayesian = results.get("bayesian", {})
    if bayesian.get("status") == "NOT_CONVERGED":
        print("⚠️  BAYESIAN: Not converged. Do NOT use CrI in main text.")

    cal_status = results.get("calibration_status", {})
    for stem, status in cal_status.items():
        if "WARNING" in str(status):
            print(f"⚠️  CALIBRATION: {stem} has uncalibrated rows.")

    missing = [k for k, v in results.items() if isinstance(v, dict) and v.get("status") == "MISSING"]
    if missing:
        print(f"⚠️  MISSING OUTPUTS: {', '.join(missing)}")
        print("   Run `make simulate` to generate these outputs.")

    print()
    print("Next steps:")
    print("  1. Review generated_results_for_text.md")
    print("  2. Update manuscript/draft.md with generated numbers")
    print("  3. Never manually copy numbers - always regenerate from this script")


if __name__ == "__main__":
    main()
