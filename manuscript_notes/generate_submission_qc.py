from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src_python.simulation.common import validate_run_metadata

OUT_DIR = ROOT / "outputs" / "metadata"
JSON_OUT = OUT_DIR / "jama_submission_readiness_qc.json"
MD_OUT = OUT_DIR / "jama_submission_readiness_qc.md"
CURRENT_MANUSCRIPT_TITLE = "Country-Differentiated Prioritization of Infant Pertussis Prevention Strategies After Resurgence"
JAMA_ORIGINAL_INVESTIGATION_WORD_LIMIT = 3000
MANUSCRIPT_PDFS = [
    "manuscript/draft.pdf",
    "manuscript/Supplementary Material.pdf",
]

EXPECTED_STRATEGIES = {
    "current",
    "higher_child_coverage",
    "timeliness_only",
    "adolescent_booster",
    "pregnancy_tdap_scaleup",
    "cocooning_adjunct",
    "maternal_immunization",
    "targeted_pep_high_risk",
    "resistance_guided_treatment",
    "transmission_blocking_vaccine",
    "next_generation_vaccine",
    "combined_strategy",
}
EXPECTED_RANK_ROWS = 128 * 10 * len(EXPECTED_STRATEGIES)

SOURCE_DATA_FILES = [
    "outputs/tables/optimization_frontier_points.csv",
    "outputs/tables/constrained_optimization_summary.csv",
    "outputs/tables/optimization_regret_summary.csv",
    "outputs/tables/country_profile_preferred_portfolios.csv",
    "outputs/tables/resistance_management_policy_decomposition.csv",
    "outputs/tables/resistance_preference_weight_summary.csv",
    "outputs/tables/resistance_preference_country_thresholds.csv",
    "outputs/tables/resistance_epsilon_constraint_summary.csv",
    "outputs/tables/implementation_intensity_removed_dominance_sensitivity.csv",
    "outputs/tables/program_portfolio_factorial_summary.csv",
    "outputs/tables/program_portfolio_factorial_country.csv",
    "outputs/metadata/program_portfolio_factorial_run_metadata.json",
    "outputs/tables/figure4a_country_strategy_reductions.csv",
    "outputs/tables/figure4b_decision_frontier.csv",
    "outputs/tables/figure4c_preference_weight_curve.csv",
    "outputs/tables/figure4d_multioutcome_reductions.csv",
    "outputs/tables/figure4e_regret_robustness.csv",
    "outputs/figures/figure_4_country_strategy_prioritization.png",
    "outputs/figures/figure_4_country_strategy_prioritization.pdf",
    "outputs/appendix/extended_data_figure_10_resistance_management_policy.png",
    "outputs/appendix/extended_data_figure_10_resistance_management_policy.pdf",
    "outputs/appendix/extended_data_figure_11_implementation_structural_robustness.png",
    "outputs/appendix/extended_data_figure_11_implementation_structural_robustness.pdf",
    "outputs/appendix/Supplementary Material.md",
    "manuscript/figure_source_data_manifest.md",
    "manuscript/CHEERS_2022_non_cost_checklist.md",
]

RUN_METADATA_STEMS = [
    "baseline_timeseries",
    "country_scenarios",
    "vaccine_scenarios",
    "resistance_scenarios",
    "reporting_scenarios",
    "veinf_resistance_grid",
    "fitness_resistance_grid",
    "intervention_scenarios",
    "routine_timeliness_sensitivity",
    "sensitivity_runs",
    "immunity_sensitivity",
    "resistance_fitness_sensitivity",
    "resistance_mechanism_decomposition",
    "program_portfolio_factorial",
    "infant_contact_sensitivity",
    "maternal_duration_sensitivity",
    "temporal_assumption_sensitivity",
    "treatment_implementation_sensitivity",
    "bayesian_uncertainty",
    "joint_psa_rank_acceptability",
    "individual_stochastic_toy",
]

CALIBRATION_STATUS_FILES = [
    "outputs/summaries/baseline_timeseries_summary.csv",
    "outputs/summaries/country_scenarios_summary.csv",
    "outputs/summaries/intervention_scenarios_summary.csv",
    "outputs/summaries/vaccine_scenarios_summary.csv",
    "outputs/summaries/resistance_scenarios_summary.csv",
    "outputs/summaries/reporting_scenarios_summary.csv",
    "outputs/summaries/veinf_resistance_grid_summary.csv",
    "outputs/summaries/fitness_resistance_grid_summary.csv",
    "outputs/summaries/routine_timeliness_sensitivity_summary.csv",
    "outputs/summaries/sensitivity_runs_summary.csv",
    "outputs/summaries/immunity_sensitivity_summary.csv",
    "outputs/summaries/resistance_fitness_sensitivity_summary.csv",
    "outputs/summaries/resistance_mechanism_decomposition_summary.csv",
    "outputs/summaries/bayesian_uncertainty_summary.csv",
    "outputs/summaries/infant_contact_sensitivity_summary.csv",
    "outputs/summaries/maternal_duration_sensitivity_summary.csv",
    "outputs/summaries/temporal_assumption_sensitivity_summary.csv",
    "outputs/summaries/treatment_implementation_sensitivity_summary.csv",
    "outputs/tables/program_portfolio_factorial_country.csv",
]


def _run_git(args: list[str]) -> str:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""
    return completed.stdout.strip()


def _main_text_word_count(text: str) -> int:
    main = "## Introduction" + text.split("## Introduction", 1)[1].split("## Supplement", 1)[0]
    main = re.sub(r"<[^>]+>", " ", main)
    main = re.sub(r"\^.*?\^", " ", main)
    main = re.sub(r"[`*_#|]", " ", main)
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?", main))


def _draft_checks() -> dict[str, object]:
    draft = (ROOT / "manuscript" / "draft.md").read_text(encoding="utf-8")
    stale_text_scope = {
        "draft": draft,
        "supplement": (ROOT / "outputs" / "appendix" / "Supplementary Material.md").read_text(encoding="utf-8"),
        "supplement_figures": (ROOT / "outputs" / "appendix" / "figure.md").read_text(encoding="utf-8"),
        "figure_manifest": (ROOT / "manuscript" / "figure_source_data_manifest.md").read_text(encoding="utf-8"),
    }
    word_count = _main_text_word_count(draft)
    stated_match = re.search(r"\*\*Main text word count:\*\*\s*(\d+)", draft)
    stated_word_count = int(stated_match.group(1)) if stated_match else None
    forbidden_patterns = [
        "among included strategies",
        "routine-timeliness-only",
        "transmission-blocking-only product targets",
        "did not include the separate routine",
        "eTable 25",
        "eTable 26",
        "eTables 1-26",
        "Infant Pertussis Prevention and Macrolide-Resistance Management Across 10 Country Profiles",
        "Optimization of Infant Pertussis Prevention and Resistance-Management Strategies",
        "Country-Differentiated Optimization of Global Infant Pertussis Prevention After Resurgence",
        "global strategy optimization",
        "global strategy-optimization",
        "conditional global strategy",
        "global conditional prioritization",
    ]
    forbidden_hits = [
        f"{location}: {pattern}"
        for location, text in stale_text_scope.items()
        for pattern in forbidden_patterns
        if pattern in text
    ]
    return {
        "stated_word_count": stated_word_count,
        "computed_word_count": word_count,
        "word_count_matches": stated_word_count == word_count,
        "word_limit": JAMA_ORIGINAL_INVESTIGATION_WORD_LIMIT,
        "word_count_within_limit": word_count <= JAMA_ORIGINAL_INVESTIGATION_WORD_LIMIT,
        "forbidden_text_hits": forbidden_hits,
    }


def _manuscript_claim_checks() -> dict[str, object]:
    draft = (ROOT / "manuscript" / "draft.md").read_text(encoding="utf-8")
    required_claims = [
        "6.5% (IQR, 4.3%-8.4%)",
        "peak-timing error of 1.5 years",
        "peak magnitude ratio was 0.31",
        "from a median of 566 to 2.3 per 100,000",
        "from -4% to 11%",
        "9.0 infant cases per 100,000/y",
        "11.2 per 100,000/y",
        "360.2 per 100,000/y",
        "20.0 vs 126.8 per 100,000/y",
        "1.0% vs 8.0%",
        "77% vs 23%",
    ]
    stale_claims = [
        "5.5% (IQR, 3.9%-7.8%)",
        "median absolute peak-timing error of 1 year",
        "from a median of 574 to 2 per 100,000",
        "97% (IQR, 62%-100%)",
        "-16% to 16%",
        "10.1 infant cases per 100,000/y",
        "11.5 per 100,000/y",
        "434.0 per 100,000/y",
        "43.5 vs 103.8 per 100,000/y",
        "1.8% vs 6.9%",
        "and ranked first in 69%.",
    ]
    missing_required = [claim for claim in required_claims if claim not in draft]
    stale_hits = [claim for claim in stale_claims if claim in draft]

    calibration = pd.read_csv(ROOT / "outputs" / "tables" / "calibration_fit_diagnostics_summary.csv")
    overall = calibration.loc[calibration["period"].eq("overall")]
    regret = pd.read_csv(ROOT / "outputs" / "tables" / "optimization_regret_summary.csv")
    treatment = pd.read_csv(ROOT / "outputs" / "tables" / "treatment_implementation_sensitivity.csv")
    improved_pep = treatment.loc[treatment["scenario"].str.contains("pep_restored", regex=False)]
    source_values = {
        "overall_mape_median": round(float(overall["mean_absolute_percentage_error"].median()), 2),
        "overall_mape_q1": round(float(overall["mean_absolute_percentage_error"].quantile(0.25)), 2),
        "overall_mape_q3": round(float(overall["mean_absolute_percentage_error"].quantile(0.75)), 2),
        "overall_peak_timing_abs_median": round(float(overall["peak_timing_error_years"].abs().median()), 1),
        "overall_peak_magnitude_ratio_median": round(float(overall["peak_magnitude_ratio"].median()), 2),
        "improved_pep_median_reduction_min_pct": round(
            100 * float(improved_pep["median_infant_case_reduction_vs_current_5y"].min()), 1
        ),
        "improved_pep_median_reduction_max_pct": round(
            100 * float(improved_pep["median_infant_case_reduction_vs_current_5y"].max()), 1
        ),
    }
    for constraint in ["program_only", "program_plus_resistance", "future_product_target"]:
        subset = regret.loc[regret["optimization_constraint"].eq(constraint)]
        best = subset.sort_values("mean_absolute_regret_infant_cases_per_100k").iloc[0]
        source_values[f"{constraint}_best_strategy"] = best["strategy"]
        source_values[f"{constraint}_best_mean_regret"] = round(
            float(best["mean_absolute_regret_infant_cases_per_100k"]), 3
        )
        source_values[f"{constraint}_best_standardized_regret"] = round(
            float(best["mean_standardized_regret_vs_current"]), 4
        )
        source_values[f"{constraint}_best_probability"] = round(float(best["probability_best_in_draw"]), 4)

    rgm = regret.loc[
        regret["optimization_constraint"].eq("program_plus_resistance")
        & regret["strategy"].eq("resistance_guided_treatment")
    ].iloc[0]
    source_values["rgm_program_plus_resistance_mean_regret"] = round(
        float(rgm["mean_absolute_regret_infant_cases_per_100k"]), 3
    )
    source_values["rgm_program_plus_resistance_standardized_regret"] = round(
        float(rgm["mean_standardized_regret_vs_current"]), 4
    )

    return {
        "missing_required_claims": missing_required,
        "stale_claim_hits": stale_hits,
        "source_values": source_values,
        "all_current": not missing_required and not stale_hits,
    }


def _rank_checks() -> dict[str, object]:
    path = ROOT / "outputs" / "tables" / "joint_psa_infant_rank_samples.csv"
    rank = pd.read_csv(path, usecols=["psa_sample_id", "country", "strategy"])
    counts = rank.groupby("strategy").size().to_dict()
    strategies = set(counts)
    duplicates = int(rank.duplicated(["psa_sample_id", "country", "strategy"]).sum())
    return {
        "rows": int(len(rank)),
        "expected_rows": EXPECTED_RANK_ROWS,
        "samples": int(rank["psa_sample_id"].nunique()),
        "countries": int(rank["country"].nunique()),
        "strategies": int(rank["strategy"].nunique()),
        "missing_strategies": sorted(EXPECTED_STRATEGIES - strategies),
        "unexpected_strategies": sorted(strategies - EXPECTED_STRATEGIES),
        "per_strategy_min": int(min(counts.values())),
        "per_strategy_max": int(max(counts.values())),
        "duplicate_cells": duplicates,
        "complete": (
            len(rank) == EXPECTED_RANK_ROWS
            and rank["psa_sample_id"].nunique() == 128
            and rank["country"].nunique() == 10
            and strategies == EXPECTED_STRATEGIES
            and min(counts.values()) == max(counts.values()) == 1280
            and duplicates == 0
        ),
    }


def _regret_checks() -> dict[str, object]:
    regret = pd.read_csv(ROOT / "outputs" / "tables" / "optimization_regret_summary.csv")
    best = (
        regret.sort_values(["optimization_constraint", "mean_absolute_regret_infant_cases_per_100k"])
        .groupby("optimization_constraint", as_index=False)
        .first()
    )
    return {
        row["optimization_constraint"]: {
            "strategy": row["strategy"],
            "mean_regret_per_100k_y": round(float(row["mean_absolute_regret_infant_cases_per_100k"]), 3),
            "mean_standardized_regret": round(float(row["mean_standardized_regret_vs_current"]), 4),
            "probability_best": round(float(row["probability_best_in_draw"]), 4),
            "decision_cells": int(row["n_decision_cells"]),
        }
        for _, row in best.iterrows()
    }


def _supplement_checks() -> dict[str, object]:
    supplement = (ROOT / "outputs" / "appendix" / "Supplementary Material.md").read_text(encoding="utf-8")
    table_numbers = [int(value) for value in re.findall(r"^### eTable (\d+)\.", supplement, flags=re.MULTILINE)]
    return {
        "etable_count": len(table_numbers),
        "etable_min": min(table_numbers) if table_numbers else None,
        "etable_max": max(table_numbers) if table_numbers else None,
        "sequential": table_numbers == list(range(1, len(table_numbers) + 1)),
    }


def _supplement_content_checks() -> dict[str, object]:
    supplement = (ROOT / "outputs" / "appendix" / "Supplementary Material.md").read_text(encoding="utf-8")
    stale_age_sentence = "whereas the modeled infant reported share was 23.50%" in supplement
    corrected_age_sentence = "whereas the modeled 5-17 year reported-share proxy was 31.40%" in supplement

    table_path = ROOT / "manuscript_notes" / "intervention_scenario_table.csv"
    required_columns = [
        "strategy",
        "description",
        "scenario_category",
        "interpretive_status",
        "modified_control_levers",
        "interpretation_note",
    ]
    intervention_table = pd.read_csv(table_path, dtype=str).fillna("")
    missing_columns = [column for column in required_columns if column not in intervention_table.columns]
    incomplete_columns = {
        column: int(intervention_table[column].astype(str).str.strip().eq("").sum())
        for column in required_columns
        if column in intervention_table.columns
    }
    present_strategies = set(intervention_table["strategy"]) if "strategy" in intervention_table.columns else set()
    missing_expected_strategies = sorted(EXPECTED_STRATEGIES - present_strategies)

    etable4_match = re.search(
        r"^### eTable 4\..*?(?=^<div style=\"page-break-after: always;\"></div>\n\n### eTable 5\.)",
        supplement,
        flags=re.MULTILINE | re.DOTALL,
    )
    empty_etable4_rows: list[str] = []
    if etable4_match:
        for line in etable4_match.group(0).splitlines():
            if not line.startswith("|") or "---" in line:
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if cells and any(cell == "" for cell in cells):
                empty_etable4_rows.append(line)
    else:
        empty_etable4_rows.append("eTable 4 block not found")

    complete_intervention_table = (
        not missing_columns
        and not missing_expected_strategies
        and all(count == 0 for count in incomplete_columns.values())
        and not empty_etable4_rows
    )
    return {
        "stale_age_sentence": stale_age_sentence,
        "corrected_age_sentence": corrected_age_sentence,
        "intervention_table_missing_columns": missing_columns,
        "intervention_table_incomplete_columns": incomplete_columns,
        "intervention_table_missing_expected_strategies": missing_expected_strategies,
        "etable4_empty_rows": empty_etable4_rows,
        "intervention_table_complete": complete_intervention_table,
        "all_current": not stale_age_sentence and corrected_age_sentence and complete_intervention_table,
    }


def _pdf_checks() -> dict[str, object]:
    checks: list[dict[str, object]] = []
    for relative in MANUSCRIPT_PDFS:
        path = ROOT / relative
        entry: dict[str, object] = {
            "file": relative,
            "exists": path.exists(),
            "contains_current_title": False,
            "pdftotext_available": None,
            "error": None,
        }
        if path.exists():
            entry["modified_utc"] = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat()
            try:
                completed = subprocess.run(
                    ["pdftotext", str(path), "-"],
                    cwd=ROOT,
                    check=True,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                entry["pdftotext_available"] = True
                text = completed.stdout
                entry["contains_current_title"] = CURRENT_MANUSCRIPT_TITLE in text
                title_line = next((line.strip() for line in text.splitlines() if line.strip()), "")
                entry["first_text_line"] = title_line[:200]
            except FileNotFoundError:
                entry["pdftotext_available"] = False
                entry["error"] = "pdftotext not available"
            except subprocess.CalledProcessError as exc:
                entry["pdftotext_available"] = True
                entry["error"] = exc.stderr.strip() or "pdftotext failed"
        checks.append(entry)
    return {
        "files": checks,
        "all_current": all(entry["exists"] and entry["contains_current_title"] for entry in checks),
    }


def _source_data_checks() -> dict[str, object]:
    missing = [path for path in SOURCE_DATA_FILES if not (ROOT / path).exists()]
    return {"missing_files": missing, "all_present": not missing}


def _run_metadata_checks() -> dict[str, object]:
    failures: list[str] = []
    checked: list[str] = []
    for stem in RUN_METADATA_STEMS:
        metadata_path = ROOT / "outputs" / "metadata" / f"{stem}_run_metadata.json"
        output_exists = any(
            [
                (ROOT / "outputs" / "summaries" / f"{stem}_summary.csv").exists(),
                (ROOT / "outputs" / "summaries" / f"{stem}_summary.parquet").exists(),
                (ROOT / "outputs" / "simulations" / f"{stem}.parquet").exists(),
                (ROOT / "outputs" / "simulations" / f"{stem}.csv").exists(),
            ]
        )
        if not metadata_path.exists():
            if output_exists:
                failures.append(f"{stem}: missing run metadata")
            continue
        checked.append(stem)
        try:
            validate_run_metadata(stem)
        except Exception as exc:
            failures.append(f"{stem}: {exc}")
    return {
        "checked_stems": checked,
        "failures": failures,
        "all_current": not failures,
    }


def _calibration_status_checks() -> dict[str, object]:
    files: list[dict[str, object]] = []
    stale_rows = 0
    stale_countries: set[str] = set()
    unreadable: list[str] = []
    for relative in CALIBRATION_STATUS_FILES:
        path = ROOT / relative
        if not path.exists():
            continue
        try:
            header = pd.read_csv(path, nrows=0)
            if "calibration_hash_status" not in header.columns:
                continue
            usecols = ["calibration_hash_status"]
            if "country" in header.columns:
                usecols.append("country")
            df = pd.read_csv(path, usecols=usecols)
        except Exception as exc:
            unreadable.append(f"{relative}: {exc}")
            continue
        status_counts = df["calibration_hash_status"].astype(str).value_counts(dropna=False).to_dict()
        stale = df.loc[df["calibration_hash_status"].eq("stale_parameter_overlay")]
        stale_count = int(len(stale))
        stale_rows += stale_count
        if stale_count and "country" in stale.columns:
            stale_countries.update(stale["country"].dropna().astype(str).unique())
        files.append(
            {
                "file": relative,
                "rows": int(len(df)),
                "status_counts": status_counts,
                "stale_rows": stale_count,
            }
        )
    return {
        "files_checked": files,
        "stale_rows": stale_rows,
        "stale_countries": sorted(stale_countries),
        "unreadable_files": unreadable,
        "all_current": stale_rows == 0 and not unreadable,
    }


def _archive_checks(draft: dict[str, object]) -> dict[str, object]:
    text = (ROOT / "manuscript" / "draft.md").read_text(encoding="utf-8")
    exact_tag = _run_git(["describe", "--exact-match", "--tags", "HEAD"])
    dirty_paths = _run_git(["status", "--porcelain"]).splitlines()
    claimed_tags = re.findall(r"`([^`]*submission[^`]*)`", text)
    unresolved_placeholders = [
        phrase
        for phrase in [
            "final immutable commit hash",
            "Zenodo DOI should be inserted",
            "repository archival",
            "final repository tag",
            "immutable commit hash",
            "Zenodo DOI will be inserted",
            "will be inserted after final QC",
        ]
        if phrase in text
    ]
    claimed_tag_at_head = bool(claimed_tags and exact_tag in claimed_tags)
    return {
        "exact_head_tag": exact_tag,
        "claimed_tags": claimed_tags,
        "claimed_tag_at_head": claimed_tag_at_head,
        "dirty_path_count": len(dirty_paths),
        "unresolved_placeholders": unresolved_placeholders,
        "ready_for_archive_statement": bool(exact_tag and not dirty_paths and not unresolved_placeholders),
    }


def build_report() -> dict[str, object]:
    status = _run_git(["status", "--porcelain"])
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "git": {
            "commit": _run_git(["rev-parse", "HEAD"]),
            "branch": _run_git(["branch", "--show-current"]),
            "dirty": bool(status),
        },
        "draft": _draft_checks(),
        "manuscript_claims": _manuscript_claim_checks(),
        "joint_psa_rank_samples": _rank_checks(),
        "minimum_regret_winners": _regret_checks(),
        "supplement": _supplement_checks(),
        "supplement_content": _supplement_content_checks(),
        "pdf_freshness": _pdf_checks(),
        "figure_source_data": _source_data_checks(),
        "run_metadata": _run_metadata_checks(),
        "calibration_status": _calibration_status_checks(),
    }
    report["archive"] = _archive_checks(report["draft"])
    report["ready_core_checks"] = all(
        [
            report["draft"]["word_count_matches"],
            report["draft"]["word_count_within_limit"],
            not report["draft"]["forbidden_text_hits"],
            report["manuscript_claims"]["all_current"],
            report["joint_psa_rank_samples"]["complete"],
            report["supplement"]["sequential"],
            report["supplement_content"]["all_current"],
            report["pdf_freshness"]["all_current"],
            report["figure_source_data"]["all_present"],
            report["run_metadata"]["all_current"],
            report["calibration_status"]["all_current"],
        ]
    )
    report["ready_archive_checks"] = report["archive"]["ready_for_archive_statement"]
    return report


def _markdown(report: dict[str, object]) -> str:
    rank = report["joint_psa_rank_samples"]
    draft = report["draft"]
    claims = report["manuscript_claims"]
    supplement = report["supplement"]
    supplement_content = report["supplement_content"]
    pdfs = report["pdf_freshness"]
    source = report["figure_source_data"]
    regret = report["minimum_regret_winners"]
    metadata = report["run_metadata"]
    calibration = report["calibration_status"]
    archive = report["archive"]
    lines = [
        "# JAMA Submission Readiness QC",
        "",
        f"Generated UTC: {report['generated_at_utc']}",
        f"Git: `{report['git']['branch']}` `{report['git']['commit'][:12]}`; dirty worktree: {report['git']['dirty']}",
        f"Core checks ready: {report['ready_core_checks']}",
        f"Archive statement ready: {report['ready_archive_checks']}",
        "",
        "## Draft",
        "",
        f"- Stated word count: {draft['stated_word_count']}",
        f"- Computed word count: {draft['computed_word_count']}",
        f"- Word count matches: {draft['word_count_matches']}",
        f"- JAMA Original Investigation limit: {draft['word_limit']}; within limit: {draft['word_count_within_limit']}",
        f"- Forbidden stale text hits: {', '.join(draft['forbidden_text_hits']) if draft['forbidden_text_hits'] else 'none'}",
        "",
        "## Manuscript Claim Sentinels",
        "",
        f"- Current numeric/text sentinels present: {claims['all_current']}",
        f"- Missing required current claims: {'; '.join(claims['missing_required_claims']) if claims['missing_required_claims'] else 'none'}",
        f"- Stale claim hits: {'; '.join(claims['stale_claim_hits']) if claims['stale_claim_hits'] else 'none'}",
        f"- Source values: `{json.dumps(claims['source_values'], sort_keys=True)}`",
        "",
        "## Joint PSA Matrix",
        "",
        f"- Rows: {rank['rows']} of expected {rank['expected_rows']}",
        f"- Samples/countries/strategies: {rank['samples']}/{rank['countries']}/{rank['strategies']}",
        f"- Per-strategy rows: {rank['per_strategy_min']} to {rank['per_strategy_max']}",
        f"- Duplicate sample-country-strategy cells: {rank['duplicate_cells']}",
        f"- Complete: {rank['complete']}",
        "",
        "## Minimum-Regret Winners",
        "",
    ]
    for constraint, values in regret.items():
        lines.append(
            "- {constraint}: {strategy}, mean regret {regret} per 100,000/y, standardized mean regret {std}, proportion best across sampled sets {prob}".format(
                constraint=constraint,
                strategy=values["strategy"],
                regret=values["mean_regret_per_100k_y"],
                std=values["mean_standardized_regret"],
                prob=values["probability_best"],
            )
        )
    lines.extend(
        [
            "",
            "## Supplement And Source Data",
            "",
            f"- eTables: {supplement['etable_count']} (range {supplement['etable_min']}-{supplement['etable_max']}), sequential: {supplement['sequential']}",
            f"- Supplement content current: {supplement_content['all_current']}",
            f"- Australia age-pattern sentence corrected: {supplement_content['corrected_age_sentence']}; stale sentence present: {supplement_content['stale_age_sentence']}",
            f"- Intervention table missing expected strategies: {', '.join(supplement_content['intervention_table_missing_expected_strategies']) if supplement_content['intervention_table_missing_expected_strategies'] else 'none'}",
            f"- Intervention table incomplete columns: `{json.dumps(supplement_content['intervention_table_incomplete_columns'], sort_keys=True)}`",
            f"- eTable 4 empty rows: {'; '.join(supplement_content['etable4_empty_rows']) if supplement_content['etable4_empty_rows'] else 'none'}",
            f"- Figure/source files present: {source['all_present']}",
            f"- Missing files: {', '.join(source['missing_files']) if source['missing_files'] else 'none'}",
            "",
            "## PDF Freshness",
            "",
            f"- PDF files current: {pdfs['all_current']}",
            *[
                "- {file}: exists {exists}, contains current title {contains}, modified UTC {modified}, first text line `{line}`{error}".format(
                    file=entry["file"],
                    exists=entry["exists"],
                    contains=entry["contains_current_title"],
                    modified=entry.get("modified_utc", "n/a"),
                    line=entry.get("first_text_line", ""),
                    error=f", error: {entry['error']}" if entry.get("error") else "",
                )
                for entry in pdfs["files"]
            ],
            "",
            "## Runtime Metadata",
            "",
            f"- Checked stems: {', '.join(metadata['checked_stems']) if metadata['checked_stems'] else 'none'}",
            f"- Current config metadata: {metadata['all_current']}",
            f"- Failures: {'; '.join(metadata['failures']) if metadata['failures'] else 'none'}",
            "",
            "## Calibration Status",
            "",
            f"- Files checked: {len(calibration['files_checked'])}",
            f"- Stale calibration rows: {calibration['stale_rows']}",
            f"- Stale countries: {', '.join(calibration['stale_countries']) if calibration['stale_countries'] else 'none'}",
            f"- Unreadable files: {'; '.join(calibration['unreadable_files']) if calibration['unreadable_files'] else 'none'}",
            "",
            "## Archive Statement",
            "",
            f"- Exact HEAD tag: {archive['exact_head_tag'] or 'none'}",
            f"- Claimed tags in draft: {', '.join(archive['claimed_tags']) if archive['claimed_tags'] else 'none'}",
            f"- Dirty paths: {archive['dirty_path_count']}",
            f"- Placeholder text: {', '.join(archive['unresolved_placeholders']) if archive['unresolved_placeholders'] else 'none'}",
            "",
            "Note: a dirty worktree is acceptable during drafting but should be resolved before replacing the repository URL with a final archived commit or DOI.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report = build_report()
    JSON_OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    MD_OUT.write_text(_markdown(report), encoding="utf-8")
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(f"Wrote {MD_OUT.relative_to(ROOT)}")
    print(f"Core checks ready: {report['ready_core_checks']}")


if __name__ == "__main__":
    main()
