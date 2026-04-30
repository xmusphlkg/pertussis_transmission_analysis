from __future__ import annotations

from copy import deepcopy
from typing import Any

import numpy as np
import pandas as pd
from src_python.model.compartments import StateIndex
from src_python.model.outputs import compute_timeseries, infer_output_dt, solve_model, summarize_timeseries
from src_python.model.parameters import PreparedParameters
from src_python.utils.io import deep_update, ensure_output_dirs, load_yaml, project_path, read_table, write_dataframe
from src_python.utils.parallel import parallel_map


def load_configs() -> dict[str, dict[str, Any]]:
    settings_path = project_path("config/model_settings.yaml")
    settings = load_yaml(settings_path) if settings_path.exists() else {}
    runtime = settings.get("runtime", {})
    return {
        "settings": settings,
        "baseline": runtime.get("baseline_parameters") or load_yaml(project_path("config/baseline_parameters.yaml")),
        "vaccines": runtime.get("vaccine_scenarios") or load_yaml(project_path("config/vaccine_scenarios.yaml")),
        "resistance": runtime.get("resistance_scenarios") or load_yaml(project_path("config/resistance_scenarios.yaml")),
        "interventions": runtime.get("intervention_scenarios") or load_yaml(project_path("config/intervention_scenarios.yaml")),
        "sensitivity": runtime.get("sensitivity_parameters") or load_yaml(project_path("config/sensitivity_parameters.yaml")),
        "data_sources": runtime.get("data_sources") or load_yaml(project_path("config/data_sources.yaml")),
        "countries": load_yaml(project_path("config/country_profiles.yaml")),
    }


def _apply_vaccine(config: dict[str, Any], vaccine: dict[str, Any]) -> dict[str, Any]:
    out = deepcopy(config)
    out["vaccine"] = {k: v for k, v in vaccine.items() if k.startswith("VE_")}
    return out


def _apply_resistance(config: dict[str, Any], resistance: dict[str, Any]) -> dict[str, Any]:
    out = deepcopy(config)
    out["initial_conditions"]["initial_resistance_prevalence"] = float(
        resistance["initial_resistance_prevalence"]
    )
    out["transmission"]["fitness_R"] = float(resistance.get("fitness_R", out["transmission"].get("fitness_R", 1.0)))
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
    vaccine_name = vaccine_scenario or base.get("baseline_vaccine_scenario", "symptom_protective")
    resistance_name = resistance_scenario or base.get("baseline_resistance_scenario", "moderate")

    vaccine = deepcopy(configs["vaccines"][vaccine_name])
    if vaccine_overrides:
        vaccine = deep_update(vaccine, vaccine_overrides)
    resistance = deepcopy(configs["resistance"][resistance_name])
    if resistance_overrides:
        resistance = deep_update(resistance, resistance_overrides)

    out = _apply_vaccine(base, vaccine)
    out = _apply_resistance(out, resistance)
    if config_overrides:
        out = deep_update(out, config_overrides)
    country_name = country_profile or base.get("baseline_country_profile")
    if country_name and country_name in configs["countries"]:
        out = _apply_country_profile_from_profile(out, country_name, configs["countries"][country_name])
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
    for key, value in (metadata or {}).items():
        timeseries[key] = value
        summary[key] = value
    return timeseries, summary


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
    write_dataframe(timeseries, project_path(f"outputs/simulations/{stem}.parquet"))
    write_dataframe(summary, project_path(f"outputs/summaries/{stem}_summary.csv"))


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
                "initial_resistance_prevalence": values["initial_resistance_prevalence"],
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
            "source_or_assumption": "WPP population, PertussisIncidence seasonality/cycles, WUENIC/JRF schedule metadata, Prem/contactdata contacts",
        }
        for name, values in countries.items()
    ]
    write_dataframe(pd.DataFrame(country_rows), project_path("manuscript_notes/country_profile_table.csv"))

    intervention_summary_path = project_path("outputs/summaries/intervention_scenarios_summary.csv")
    if intervention_summary_path.exists():
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
