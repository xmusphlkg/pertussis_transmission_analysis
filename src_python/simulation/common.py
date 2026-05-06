from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from copy import deepcopy
from datetime import datetime, timezone
from importlib import metadata as package_metadata
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from src_python.model.compartments import StateIndex
from src_python.model.outputs import compute_timeseries, infer_output_dt, solve_model, summarize_timeseries
from src_python.model.parameters import PreparedParameters
from src_python.utils.io import deep_update, ensure_output_dirs, load_yaml, project_path, read_table, write_dataframe
from src_python.utils.parallel import parallel_map


COUNTRY_RESISTANCE_TIMELINE_COLUMNS = {
    "country",
    "iso3",
    "year",
    "resistant_fraction",
    "lower",
    "upper",
    "evidence_type",
    "source",
    "notes",
}

REQUIRED_RUNTIME_BLOCKS = (
    "baseline_parameters",
    "vaccine_scenarios",
    "resistance_scenarios",
    "intervention_scenarios",
    "sensitivity_parameters",
    "data_sources",
)

METADATA_SCHEMA_VERSION = 1


def load_configs() -> dict[str, dict[str, Any]]:
    settings_path = project_path("config/model_settings.yaml")
    if not settings_path.exists():
        raise FileNotFoundError("config/model_settings.yaml is the runtime configuration source and was not found.")
    settings = load_yaml(settings_path)
    runtime = settings.get("runtime", {})
    missing = [block for block in REQUIRED_RUNTIME_BLOCKS if block not in runtime]
    if missing:
        raise ValueError(f"config/model_settings.yaml is missing runtime blocks: {missing}")
    return {
        "settings": settings,
        "baseline": runtime["baseline_parameters"],
        "vaccines": runtime["vaccine_scenarios"],
        "resistance": runtime["resistance_scenarios"],
        "interventions": runtime["intervention_scenarios"],
        "sensitivity": runtime["sensitivity_parameters"],
        "data_sources": runtime["data_sources"],
        "countries": load_yaml(project_path("config/country_profiles.yaml")),
    }


def config_fingerprint(configs: dict[str, Any] | None = None) -> str:
    configs = configs or load_configs()
    payload = {
        "settings_runtime": configs["settings"].get("runtime", {}),
        "countries": configs["countries"],
    }
    encoded = json.dumps(payload, sort_keys=True, default=str, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _git_metadata() -> dict[str, Any]:
    def run_git(args: list[str]) -> str:
        try:
            return subprocess.check_output(["git", *args], cwd=project_path(), text=True, stderr=subprocess.DEVNULL).strip()
        except Exception:
            return ""

    return {
        "commit": run_git(["rev-parse", "HEAD"]),
        "branch": run_git(["branch", "--show-current"]),
        "dirty": bool(run_git(["status", "--short"])),
    }


def _dependency_versions() -> dict[str, str]:
    names = ("numpy", "pandas", "scipy", "pyyaml", "pydantic", "joblib", "SALib", "pyarrow")
    versions = {"python": sys.version.split()[0]}
    for name in names:
        try:
            versions[name] = package_metadata.version(name)
        except package_metadata.PackageNotFoundError:
            versions[name] = "not-installed"
    return versions


def output_metadata_path(stem: str) -> Path:
    return project_path("outputs", "metadata", f"{stem}_run_metadata.json")


def current_run_metadata(stem: str, *, row_counts: dict[str, int] | None = None) -> dict[str, Any]:
    configs = load_configs()
    return {
        "schema_version": METADATA_SCHEMA_VERSION,
        "stem": stem,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "config_hash": config_fingerprint(configs),
        "git": _git_metadata(),
        "dependency_versions": _dependency_versions(),
        "row_counts": row_counts or {},
    }


def write_run_metadata(stem: str, metadata: dict[str, Any]) -> None:
    path = output_metadata_path(stem)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2, sort_keys=True)


def read_run_metadata(stem: str) -> dict[str, Any]:
    path = output_metadata_path(stem)
    if not path.exists():
        raise FileNotFoundError(f"Missing run metadata for {stem}: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_run_metadata(stem: str) -> dict[str, Any]:
    metadata = read_run_metadata(stem)
    if int(metadata.get("schema_version", -1)) != METADATA_SCHEMA_VERSION:
        raise ValueError(f"Run metadata schema mismatch for {stem}.")
    expected_hash = config_fingerprint()
    if metadata.get("config_hash") != expected_hash:
        raise ValueError(
            f"Output {stem} was generated from a stale configuration "
            f"({metadata.get('config_hash')}); current config hash is {expected_hash}."
        )
    return metadata


def _clear_stem_outputs(stem: str) -> None:
    candidates = [
        project_path("outputs", "simulations", f"{stem}.csv"),
        project_path("outputs", "simulations", f"{stem}.parquet"),
        project_path("outputs", "summaries", f"{stem}_summary.csv"),
        project_path("outputs", "summaries", f"{stem}_summary.parquet"),
        output_metadata_path(stem),
    ]
    for path in candidates:
        if path.exists():
            path.unlink()


def _apply_vaccine(config: dict[str, Any], vaccine: dict[str, Any]) -> dict[str, Any]:
    out = deepcopy(config)
    out["vaccine"] = {k: v for k, v in vaccine.items() if k.startswith("VE_")}
    return out


def _apply_resistance(config: dict[str, Any], resistance: dict[str, Any]) -> dict[str, Any]:
    out = deepcopy(config)
    target = float(
        resistance.get(
            "target_prevalence_at_analysis_start",
            resistance.get("initial_resistance_prevalence", 0.0),
        )
    )
    out["initial_conditions"]["initial_resistance_prevalence"] = float(
        resistance.get("initial_resistance_prevalence", target)
    )
    out.setdefault("resistance", {})
    out["resistance"]["target_prevalence_at_analysis_start"] = target
    out["resistance"]["importation_fraction"] = float(resistance.get("importation_fraction", target))
    out["resistance"]["rebalance_after_burn_in"] = bool(resistance.get("rebalance_after_burn_in", True))
    out["resistance"]["prevalence_anchor_rate_per_year"] = float(
        resistance.get(
            "prevalence_anchor_rate_per_year",
            out.get("resistance", {}).get("prevalence_anchor_rate_per_year", 0.0),
        )
    )
    out["resistance"]["anchor_during_dynamics"] = bool(resistance.get("anchor_during_dynamics", False))
    out["resistance"]["use_country_resistance_timeline"] = bool(
        resistance.get("use_country_resistance_timeline", False)
    )
    out.setdefault("importation", {})["resistant_fraction"] = out["resistance"]["importation_fraction"]
    out["transmission"]["fitness_R"] = float(resistance.get("fitness_R", out["transmission"].get("fitness_R", 1.0)))
    return out


def _load_country_resistance_timeline(data_sources: dict[str, Any]) -> pd.DataFrame:
    relative_path = data_sources.get("country_resistance_timeline_csv", "data/raw/country_resistance_timeline.csv")
    path = project_path(relative_path)
    if not path.exists():
        raise FileNotFoundError(f"Country resistance timeline not found: {path}")
    timeline = pd.read_csv(path)
    missing = COUNTRY_RESISTANCE_TIMELINE_COLUMNS.difference(timeline.columns)
    if missing:
        raise ValueError(f"Country resistance timeline is missing columns: {sorted(missing)}")

    timeline = timeline.copy()
    timeline["country"] = timeline["country"].astype(str)
    timeline["iso3"] = timeline["iso3"].astype(str).str.upper()
    timeline["evidence_type"] = timeline["evidence_type"].astype(str).str.strip()
    timeline["source"] = timeline["source"].astype(str).str.strip()
    timeline["year"] = pd.to_numeric(timeline["year"], errors="coerce")
    for column in ["resistant_fraction", "lower", "upper"]:
        timeline[column] = pd.to_numeric(timeline[column], errors="coerce")
    timeline = timeline.dropna(subset=["country", "iso3", "year", "resistant_fraction"])
    timeline["year"] = timeline["year"].astype(int)

    for column in ["resistant_fraction", "lower", "upper"]:
        values = timeline[column].dropna()
        if not values.between(0.0, 1.0).all():
            raise ValueError(f"Country resistance timeline column {column} must be within [0, 1].")
    for column in ["evidence_type", "source"]:
        if timeline[column].eq("").any() or timeline[column].str.lower().eq("nan").any():
            raise ValueError(f"Country resistance timeline column {column} must be populated.")
    return timeline


def _timeline_rows_for_country(timeline: pd.DataFrame, country: str, iso3: str | None) -> pd.DataFrame:
    country_key = str(country)
    iso3_key = str(iso3 or "").upper()
    rows = timeline.loc[timeline["country"].eq(country_key)]
    if rows.empty and iso3_key:
        rows = timeline.loc[timeline["iso3"].eq(iso3_key)]
    if rows.empty:
        raise KeyError(f"No country resistance timeline rows found for {country_key} ({iso3_key}).")
    return rows.sort_values("year")


def _interpolate_optional(years: np.ndarray, values: np.ndarray, analysis_year: int) -> float:
    finite = np.isfinite(values)
    if not finite.any():
        return float("nan")
    finite_years = years[finite]
    finite_values = values[finite]
    if analysis_year <= finite_years.min():
        return float(finite_values[np.argmin(finite_years)])
    if analysis_year >= finite_years.max():
        return float(finite_values[np.argmax(finite_years)])
    return float(np.interp(analysis_year, finite_years, finite_values))


def _country_resistance_estimate(rows: pd.DataFrame, anchor_year: int, *, allow_future: bool = False) -> dict[str, Any]:
    evidence_pool = rows.copy()
    if not allow_future:
        evidence_pool = evidence_pool.loc[evidence_pool["year"].astype(int) <= anchor_year]
        if evidence_pool.empty:
            raise ValueError(
                f"No resistance evidence is available at or before {anchor_year}; "
                "set allow_future_resistance_evidence=true only for explicitly labelled current-evidence scenarios."
            )

    years = evidence_pool["year"].to_numpy(dtype=float)
    values = evidence_pool["resistant_fraction"].to_numpy(dtype=float)
    target = _interpolate_optional(years, values, anchor_year)
    lower = _interpolate_optional(years, evidence_pool["lower"].to_numpy(dtype=float), anchor_year)
    upper = _interpolate_optional(years, evidence_pool["upper"].to_numpy(dtype=float), anchor_year)

    if anchor_year in set(evidence_pool["year"].astype(int)):
        method = "exact_year"
        evidence_rows = evidence_pool.loc[evidence_pool["year"].eq(anchor_year)]
    elif anchor_year < int(evidence_pool["year"].min()) or anchor_year > int(evidence_pool["year"].max()):
        method = "nearest_year" if allow_future else "nearest_past_year"
        nearest_idx = (evidence_pool["year"].astype(int) - anchor_year).abs().idxmin()
        evidence_rows = evidence_pool.loc[[nearest_idx]]
    else:
        method = "linear_interpolation"
        before = evidence_pool.loc[evidence_pool["year"] < anchor_year].tail(1)
        after = evidence_pool.loc[evidence_pool["year"] > anchor_year].head(1)
        evidence_rows = pd.concat([before, after], ignore_index=True)

    def join_unique(column: str) -> str:
        values = [str(value) for value in evidence_rows[column].dropna().unique() if str(value)]
        return "; ".join(values)

    return {
        "resistance_anchor_year": int(anchor_year),
        "resistant_fraction": float(np.clip(target, 0.0, 1.0)),
        "lower": float(np.clip(lower, 0.0, 1.0)) if np.isfinite(lower) else np.nan,
        "upper": float(np.clip(upper, 0.0, 1.0)) if np.isfinite(upper) else np.nan,
        "method": method,
        "evidence_years": ";".join(str(int(year)) for year in evidence_rows["year"].tolist()),
        "evidence_type": join_unique("evidence_type"),
        "source": join_unique("source"),
        "notes": join_unique("notes"),
    }


def _apply_country_resistance_timeline(
    config: dict[str, Any],
    *,
    country: str,
    country_profile: dict[str, Any],
    data_sources: dict[str, Any],
) -> dict[str, Any]:
    out = deepcopy(config)
    anchor_year = int(data_sources.get("resistance_anchor_year", data_sources.get("analysis_year", 2023)))
    allow_future = bool(data_sources.get("allow_future_resistance_evidence", False))
    iso3 = country_profile.get("iso3")
    timeline = _load_country_resistance_timeline(data_sources)
    rows = _timeline_rows_for_country(timeline, country, iso3)
    estimate = _country_resistance_estimate(rows, anchor_year, allow_future=allow_future)
    target = estimate["resistant_fraction"]

    out["initial_conditions"]["initial_resistance_prevalence"] = target
    out.setdefault("resistance", {})
    out["resistance"]["target_prevalence_at_analysis_start"] = target
    out["resistance"]["importation_fraction"] = target
    out["resistance"]["prevalence_anchor_rate_per_year"] = float(
        out["resistance"].get("prevalence_anchor_rate_per_year", 2.0)
    )
    out["resistance"]["country_timeline"] = {
        "country": country,
        "iso3": iso3,
        **estimate,
    }
    out.setdefault("importation", {})["resistant_fraction"] = target
    metadata = out.setdefault("metadata", {})
    metadata["resistance_timeline_country"] = country
    metadata["resistance_timeline_iso3"] = iso3 or ""
    metadata["resistance_timeline_anchor_year"] = anchor_year
    metadata["resistance_timeline_allows_future_evidence"] = allow_future
    metadata["resistance_timeline_method"] = estimate["method"]
    metadata["resistance_timeline_evidence_years"] = estimate["evidence_years"]
    metadata["resistance_timeline_evidence_type"] = estimate["evidence_type"]
    metadata["resistance_timeline_source"] = estimate["source"]
    metadata["resistance_timeline_notes"] = estimate["notes"]
    return out


def _apply_coverage_updates(config: dict[str, Any], updates: dict[str, float] | None) -> dict[str, Any]:
    out = deepcopy(config)
    if not updates:
        return out
    for record in out["age_groups"]:
        if record["label"] in updates:
            record["vaccine_coverage"] = float(updates[record["label"]])
    return out


def make_config(
    *,
    vaccine_scenario: str | None = None,
    resistance_scenario: str | None = None,
    country_profile: str | None = None,
    vaccine_overrides: dict[str, Any] | None = None,
    resistance_overrides: dict[str, Any] | None = None,
    config_overrides: dict[str, Any] | None = None,
) -> dict[str, Any]:
    configs = load_configs()
    base = deepcopy(configs["baseline"])
    vaccine_name = vaccine_scenario or base["baseline_vaccine_scenario"]
    resistance_name = resistance_scenario or base["baseline_resistance_scenario"]

    vaccine = deepcopy(configs["vaccines"][vaccine_name])
    if vaccine_overrides:
        vaccine = deep_update(vaccine, vaccine_overrides)
    resistance = deepcopy(configs["resistance"][resistance_name])
    resistance_prevalence_overridden = bool(
        resistance_overrides
        and {
            "target_prevalence_at_analysis_start",
            "initial_resistance_prevalence",
            "importation_fraction",
            "prevalence_anchor_rate_per_year",
        }.intersection(resistance_overrides)
    )
    if resistance_overrides:
        resistance = deep_update(resistance, resistance_overrides)

    out = _apply_vaccine(base, vaccine)
    out = _apply_resistance(out, resistance)
    if config_overrides:
        out = deep_update(out, config_overrides)
    country_name = country_profile or base.get("baseline_country_profile")
    if country_name and country_name in configs["countries"]:
        out = _apply_country_profile_from_profile(out, country_name, configs["countries"][country_name])
        uses_country_timeline = out.get("resistance", {}).get("use_country_resistance_timeline", False)
        if uses_country_timeline and not resistance_prevalence_overridden:
            out = _apply_country_resistance_timeline(
                out,
                country=country_name,
                country_profile=configs["countries"][country_name],
                data_sources=configs["data_sources"],
            )
    if sum(float(value) for key, value in out.get("vaccine", {}).items() if key.startswith("VE_")) == 0.0:
        for record in out["age_groups"]:
            record["vaccine_coverage"] = 0.0
        out.setdefault("demography", {})["birth_entry"] = {"S": 1.0, "V": 0.0}
    return out


def make_intervention_config(name: str, *, country_profile: str | None = None) -> tuple[dict[str, Any], str]:
    configs = load_configs()
    intervention = configs["interventions"][name]
    vaccine_name = intervention.get("vaccine_scenario", configs["baseline"].get("baseline_vaccine_scenario"))
    config = make_config(
        vaccine_scenario=vaccine_name,
        resistance_scenario=configs["baseline"].get("baseline_resistance_scenario"),
        country_profile=country_profile,
    )
    config = _apply_coverage_updates(config, intervention.get("coverage_updates"))
    if "vaccine_overrides" in intervention:
        config["vaccine"] = deep_update(config["vaccine"], intervention["vaccine_overrides"])
    if "treatment_updates" in intervention:
        config["treatment"] = deep_update(config["treatment"], intervention["treatment_updates"])
    if "pep_updates" in intervention:
        config["PEP"] = deep_update(config["PEP"], intervention["pep_updates"])
    return config, vaccine_name


def _apply_country_profile_from_profile(config: dict[str, Any], country: str, profile: dict[str, Any]) -> dict[str, Any]:
    out = deepcopy(config)
    for record in out["age_groups"]:
        label = record["label"]
        if label in profile.get("population", {}):
            record["population"] = float(profile["population"][label])
        if label in profile.get("reporting_rate", {}):
            record["reporting_rate"] = float(profile["reporting_rate"][label])
        if label in profile.get("vaccine_coverage", {}):
            record["vaccine_coverage"] = float(profile["vaccine_coverage"][label])
    if "contact_matrix" in profile:
        out["contact_matrix"]["rows"] = profile["contact_matrix"]
    if "contact_reciprocity" in profile:
        out.setdefault("metadata", {})["contact_reciprocity"] = profile["contact_reciprocity"]
    if "birth_entry" in profile:
        out.setdefault("demography", {})["birth_entry"] = profile["birth_entry"]
    if "transmission_overrides" in profile:
        out["transmission"] = deep_update(out["transmission"], profile["transmission_overrides"])
    out["country"] = country
    return out


def apply_country_profile(config: dict[str, Any], country: str) -> dict[str, Any]:
    configs = load_configs()
    if country not in configs["countries"]:
        raise KeyError(f"Unknown country profile: {country}")
    return _apply_country_profile_from_profile(config, country, configs["countries"][country])


def run_prepared_config(
    config: dict[str, Any],
    *,
    analysis: str,
    scenario: str,
    vaccine_scenario: str = "",
    resistance_scenario: str = "",
    intervention: str = "",
    metadata: dict[str, Any] | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    params = PreparedParameters.from_config(
        config,
        analysis=analysis,
        scenario=scenario,
        vaccine_scenario=vaccine_scenario,
        resistance_scenario=resistance_scenario,
        intervention=intervention,
        metadata=metadata,
    )
    index = StateIndex(params.age_groups)
    solution = solve_model(params, index)
    timeseries = compute_timeseries(solution, params, index)
    summary = summarize_timeseries(
        timeseries,
        dt=infer_output_dt(timeseries),
    )
    for key, value in params.metadata.items():
        if isinstance(value, (str, int, float, bool, np.number)):
            timeseries[key] = value
            summary[key] = value
    for key, value in (metadata or {}).items():
        timeseries[key] = value
        summary[key] = value
    _add_absolute_fit_context(summary, params.raw, metadata or {})
    return timeseries, summary


def _add_absolute_fit_context(summary: pd.DataFrame, config: dict[str, Any], metadata: dict[str, Any]) -> None:
    country = metadata.get("country") or config.get("country")
    if not country:
        summary["absolute_fit_status"] = "not_country_specific"
        return
    configs = load_configs()
    countries = configs["countries"]
    observed = countries.get(str(country), {}).get("observed_incidence", {})
    observed_mean = observed.get("observed_mean_annual_reported_incidence_per_100k", np.nan)
    summary["observed_mean_annual_reported_incidence_per_100k"] = observed_mean
    modeled = summary["annualized_reported_cases_per_100k"].astype(float)
    if np.isfinite(float(observed_mean)) and float(observed_mean) > 0:
        summary["model_to_observed_reported_incidence_ratio"] = modeled / float(observed_mean)
    else:
        summary["model_to_observed_reported_incidence_ratio"] = np.nan
    tolerance = float(configs["baseline"].get("calibration", {}).get("relative_incidence_tolerance", 0.25))
    ratio = summary["model_to_observed_reported_incidence_ratio"].astype(float)
    summary["absolute_fit_relative_error"] = (ratio - 1.0).abs()
    summary["absolute_fit_relative_tolerance"] = tolerance
    is_calibration = summary["analysis"].eq("calibration")
    is_within_tolerance = summary["absolute_fit_relative_error"].le(tolerance) & np.isfinite(
        summary["absolute_fit_relative_error"].astype(float)
    )
    summary["absolute_fit_status"] = np.select(
        [is_calibration & is_within_tolerance, is_calibration & ~is_within_tolerance],
        ["calibrated_to_reported_cases", "calibration_failed_absolute_fit"],
        default="uncalibrated_scenario_analysis",
    )


def _run_scenario_item(item: dict[str, Any]) -> tuple[pd.DataFrame, pd.DataFrame]:
    return run_prepared_config(**item)


def add_relative_reductions(
    summary: pd.DataFrame,
    *,
    reference_scenario: str,
) -> pd.DataFrame:
    out = summary.copy()
    mapping = {
        "relative_reduction_infant_cases": "total_infant_cases",
        "relative_reduction_total_infections": "total_infections",
        "relative_reduction_reported_cases": "total_reported_cases",
        "relative_reduction_resistant_infections": "resistant_infections",
    }
    for new_col in mapping:
        out[new_col] = np.nan

    group_cols = ["country"] if "country" in out.columns else []
    if not group_cols:
        grouped = [(None, out.index)]
    else:
        grouped = [(key, group.index) for key, group in out.groupby(group_cols, dropna=False)]

    for _, idx in grouped:
        group = out.loc[idx]
        reference = group.loc[group["scenario"].eq(reference_scenario)]
        if reference.empty:
            continue
        base = reference.iloc[0]
        for new_col, source_col in mapping.items():
            denom = float(base[source_col])
            out.loc[idx, new_col] = 1.0 - out.loc[idx, source_col] / denom if denom > 0 else np.nan
    out["relative_reduction_vs_baseline"] = out["relative_reduction_total_infections"]
    return out


def write_outputs(timeseries: pd.DataFrame, summary: pd.DataFrame, stem: str) -> None:
    ensure_output_dirs()
    project_path("outputs", "metadata").mkdir(parents=True, exist_ok=True)
    _clear_stem_outputs(stem)
    write_dataframe(timeseries, project_path(f"outputs/simulations/{stem}.parquet"))
    write_dataframe(summary, project_path(f"outputs/summaries/{stem}_summary.csv"))
    write_run_metadata(
        stem,
        current_run_metadata(
            stem,
            row_counts={
                "timeseries": int(len(timeseries)),
                "summary": int(len(summary)),
            },
        ),
    )


def execute_scenario_list(
    scenarios: list[dict[str, Any]],
    *,
    stem: str,
    n_jobs: int | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if not scenarios:
        raise ValueError(f"No scenarios were provided for {stem}.")
    if n_jobs is None:
        n_jobs = scenarios[0]["config"].get("simulation", {}).get("n_jobs")
    results = parallel_map(_run_scenario_item, scenarios, desc=stem, n_jobs=n_jobs)
    frames = [ts for ts, _ in results]
    summaries = [sm for _, sm in results]
    return pd.concat(frames, ignore_index=True), pd.concat(summaries, ignore_index=True)


def run_scenario_list(
    scenarios: list[dict[str, Any]],
    *,
    stem: str,
    reference_scenario: str,
    n_jobs: int | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    timeseries, summary = execute_scenario_list(scenarios, stem=stem, n_jobs=n_jobs)
    summary = add_relative_reductions(summary, reference_scenario=reference_scenario)
    write_outputs(timeseries, summary, stem)
    return timeseries, summary


def write_manuscript_tables() -> None:
    configs = load_configs()
    baseline = configs["baseline"]
    vaccines = configs["vaccines"]
    resistance = configs["resistance"]
    interventions = configs["interventions"]
    countries = configs["countries"]
    settings = configs.get("settings", {})
    parameter_sources = settings.get("parameter_sources", {})

    sensitivity_paths = {
        spec.get("path")
        for spec in configs["sensitivity"].get("parameters", {}).values()
        if isinstance(spec, dict)
    }
    parameter_specs = [
        ("simulation.end_time", "Simulation analysis horizon", baseline["simulation"]["end_time"], "days"),
        ("simulation.burn_in_years", "Pre-analysis burn-in horizon", baseline["simulation"]["burn_in_years"], "years"),
        ("transmission.beta_S", "Transmission rate for macrolide-sensitive pertussis", baseline["transmission"]["beta_S"], "per contact day"),
        ("transmission.relative_infectiousness_asymptomatic", "Relative infectiousness of asymptomatic infection", baseline["transmission"]["relative_infectiousness_asymptomatic"], "ratio"),
        ("transmission.multi_year_period_years", "Target/diagnostic inter-epidemic period", baseline["transmission"]["multi_year_period_years"], "years"),
        ("transmission.multi_year_amplitude", "Weak multi-year phase-locking amplitude", baseline["transmission"]["multi_year_amplitude"], "ratio"),
        ("natural_history.latent_duration", "Latent period duration", baseline["natural_history"]["latent_duration"], "days"),
        ("natural_history.infectious_duration_symptomatic", "Symptomatic infectious duration", baseline["natural_history"]["infectious_duration_symptomatic"], "days"),
        ("natural_history.infectious_duration_asymptomatic", "Asymptomatic infectious duration", baseline["natural_history"]["infectious_duration_asymptomatic"], "days"),
        ("natural_history.recovered_immunity_duration", "Duration of post-infection protection", baseline["natural_history"]["recovered_immunity_duration"], "days"),
        ("natural_history.vaccine_protection_duration", "Duration of vaccine-derived protection proxy", baseline["natural_history"]["vaccine_protection_duration"], "days"),
        ("treatment.treatment_rate_symptomatic", "Daily transition from symptomatic infection to treatment", baseline["treatment"]["treatment_rate_symptomatic"], "per day"),
        ("PEP.coverage_household_contacts", "Dynamic PEP coverage ceiling among close contacts", baseline["PEP"]["coverage_household_contacts"], "proportion"),
    ]
    parameter_rows = []
    for path, description, value, unit in parameter_specs:
        source_note = parameter_sources.get(path, parameter_sources.get(path.split(".")[0], {}))
        parameter_rows.append(
            {
                "parameter": path,
                "description": description,
                "baseline_value": value,
                "range": "see config/model_settings.yaml sensitivity_parameters",
                "unit": unit,
                "source_or_assumption": source_note.get("source", ""),
                "source_note": source_note.get("note", ""),
                "used_in_sensitivity_analysis": path in sensitivity_paths,
            }
        )
    write_dataframe(pd.DataFrame(parameter_rows), project_path("manuscript_notes/parameter_table.csv"))

    vaccine_rows = []
    for name, values in vaccines.items():
        row = {"scenario": name}
        row.update({k: values[k] for k in ["VE_sus", "VE_sym", "VE_inf", "VE_dur"]})
        row["description"] = values.get("description", "")
        vaccine_rows.append(row)
    write_dataframe(pd.DataFrame(vaccine_rows), project_path("manuscript_notes/scenario_table.csv"))

    resistance_rows = []
    for name, values in resistance.items():
        resistance_rows.append(
            {
                "scenario": name,
                "target_prevalence_at_analysis_start": values.get(
                    "target_prevalence_at_analysis_start",
                    values.get("initial_resistance_prevalence"),
                ),
                "initial_resistance_prevalence_deprecated": values.get("initial_resistance_prevalence", np.nan),
                "importation_fraction": values.get("importation_fraction", np.nan),
                "prevalence_anchor_rate_per_year": values.get("prevalence_anchor_rate_per_year", np.nan),
                "anchor_during_dynamics": bool(values.get("anchor_during_dynamics", False)),
                "uses_country_resistance_timeline": bool(values.get("use_country_resistance_timeline", False)),
                "fitness_R": values.get("fitness_R", 1.0),
                "treatment_effect_resistant": baseline["treatment"]["resistant"]["infectious_duration_reduction"],
                "PEP_effectiveness_resistant": baseline["PEP"]["effectiveness_resistant"],
                "description": values.get("description", ""),
            }
        )
    write_dataframe(pd.DataFrame(resistance_rows), project_path("manuscript_notes/resistance_scenario_table.csv"))

    intervention_rows = [
        {"strategy": name, "description": values.get("description", "")}
        for name, values in interventions.items()
    ]
    write_dataframe(pd.DataFrame(intervention_rows), project_path("manuscript_notes/intervention_scenario_table.csv"))

    reporting_rows = []
    for name, values in baseline["reporting_rate_sensitivity"].items():
        reporting_rows.append(
            {
                "scenario": name,
                "multiplier": values.get("multiplier", np.nan),
                "uses_age_multipliers": bool(values.get("age_multipliers")),
                "uses_time_variation": bool(values.get("time_variation")),
                "description": "Reporting-rate sensitivity assumption.",
            }
        )
    write_dataframe(pd.DataFrame(reporting_rows), project_path("manuscript_notes/reporting_scenario_table.csv"))

    country_rows = [
        {
            "country": name,
            "description": values.get("description", ""),
            "total_population": sum(float(v) for v in values.get("population", {}).values()),
            "seasonal_phase": values.get("transmission_overrides", {}).get("seasonal_phase", np.nan),
            "seasonal_amplitude": values.get("transmission_overrides", {}).get("seasonal_amplitude", np.nan),
            "multi_year_period_years": values.get("transmission_overrides", {}).get("multi_year_period_years", np.nan),
            "multi_year_amplitude": values.get("transmission_overrides", {}).get("multi_year_amplitude", np.nan),
            "observed_mean_annual_reported_incidence_per_100k": values.get("observed_incidence", {}).get("observed_mean_annual_reported_incidence_per_100k", np.nan),
            "observed_peak_annual_reported_incidence_per_100k": values.get("observed_incidence", {}).get("observed_peak_annual_reported_incidence_per_100k", np.nan),
            "vaccine_product": values.get("vaccine_schedule", {}).get("vaccine_product", ""),
            "adolescent_booster": values.get("vaccine_schedule", {}).get("adolescent_booster", np.nan),
            "maternal_program": values.get("vaccine_schedule", {}).get("maternal_program", np.nan),
            "contact_source": values.get("contact_source", ""),
            "source_type_note": "; ".join(
                f"{key}={value}" for key, value in values.get("source_types", {}).items()
            ),
            "source_or_assumption": "WPP population, PertussisIncidence seasonality/cycles, WUENIC/JRF schedule metadata, Prem/contactdata contacts",
        }
        for name, values in countries.items()
    ]
    write_dataframe(pd.DataFrame(country_rows), project_path("manuscript_notes/country_profile_table.csv"))

    intervention_summary_path = project_path("outputs/summaries/intervention_scenarios_summary.csv")
    if intervention_summary_path.exists():
        try:
            validate_run_metadata("intervention_scenarios")
        except Exception:
            return
        else:
            intervention_summary = read_table(intervention_summary_path)
            cols = [
                "country",
                "scenario",
                "total_infections",
                "total_reported_cases",
                "total_infant_cases",
                "resistant_infections",
                "relative_reduction_infant_cases",
                "relative_reduction_total_infections",
            ]
            table = intervention_summary.loc[:, cols].rename(
                columns={
                    "scenario": "strategy",
                    "total_reported_cases": "reported_cases",
                }
            )
            write_dataframe(table, project_path("outputs/tables/table_4_intervention_comparison.csv"))
