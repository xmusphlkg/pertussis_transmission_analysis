from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "metadata"
JSON_OUT = OUT_DIR / "jama_submission_readiness_qc.json"
MD_OUT = OUT_DIR / "jama_submission_readiness_qc.md"

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
    "outputs/tables/program_portfolio_factorial_summary.csv",
    "outputs/tables/program_portfolio_factorial_country.csv",
    "outputs/metadata/program_portfolio_factorial_run_metadata.json",
    "outputs/tables/figure4a_country_strategy_reductions.csv",
    "outputs/tables/figure4b_decision_frontier.csv",
    "outputs/tables/figure4c_preference_weight_curve.csv",
    "outputs/tables/figure4d_multioutcome_reductions.csv",
    "outputs/tables/figure4e_regret_robustness.csv",
    "outputs/figures/figure_4_intervention_prioritisation.png",
    "outputs/figures/figure_4_intervention_prioritisation.pdf",
    "outputs/appendix/extended_data_figure_10_resistance_management_policy.png",
    "outputs/appendix/extended_data_figure_10_resistance_management_policy.pdf",
    "outputs/appendix/extended_data_figure_11_implementation_structural_robustness.png",
    "outputs/appendix/extended_data_figure_11_implementation_structural_robustness.pdf",
    "outputs/appendix/Supplementary Material.md",
    "manuscript/figure_source_data_manifest.md",
    "manuscript/CHEERS_2022_non_cost_checklist.md",
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
    ]
    forbidden_hits = [pattern for pattern in forbidden_patterns if pattern in draft]
    return {
        "stated_word_count": stated_word_count,
        "computed_word_count": word_count,
        "word_count_matches": stated_word_count == word_count,
        "forbidden_text_hits": forbidden_hits,
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


def _source_data_checks() -> dict[str, object]:
    missing = [path for path in SOURCE_DATA_FILES if not (ROOT / path).exists()]
    return {"missing_files": missing, "all_present": not missing}


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
        "joint_psa_rank_samples": _rank_checks(),
        "minimum_regret_winners": _regret_checks(),
        "supplement": _supplement_checks(),
        "figure_source_data": _source_data_checks(),
    }
    report["ready_core_checks"] = all(
        [
            report["draft"]["word_count_matches"],
            not report["draft"]["forbidden_text_hits"],
            report["joint_psa_rank_samples"]["complete"],
            report["supplement"]["sequential"],
            report["figure_source_data"]["all_present"],
        ]
    )
    return report


def _markdown(report: dict[str, object]) -> str:
    rank = report["joint_psa_rank_samples"]
    draft = report["draft"]
    supplement = report["supplement"]
    source = report["figure_source_data"]
    regret = report["minimum_regret_winners"]
    lines = [
        "# JAMA Submission Readiness QC",
        "",
        f"Generated UTC: {report['generated_at_utc']}",
        f"Git: `{report['git']['branch']}` `{report['git']['commit'][:12]}`; dirty worktree: {report['git']['dirty']}",
        f"Core checks ready: {report['ready_core_checks']}",
        "",
        "## Draft",
        "",
        f"- Stated word count: {draft['stated_word_count']}",
        f"- Computed word count: {draft['computed_word_count']}",
        f"- Word count matches: {draft['word_count_matches']}",
        f"- Forbidden stale text hits: {', '.join(draft['forbidden_text_hits']) if draft['forbidden_text_hits'] else 'none'}",
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
            "- {constraint}: {strategy}, mean regret {regret} per 100,000/y, standardized mean regret {std}, Pr(best) {prob}".format(
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
            f"- Figure/source files present: {source['all_present']}",
            f"- Missing files: {', '.join(source['missing_files']) if source['missing_files'] else 'none'}",
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
