from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml
from scipy.signal import find_peaks

from src_python.model.contact_matrix import balance_reciprocity, reciprocity_error
from src_python.utils.io import load_yaml, project_path


AGE_GROUPS = (
    "infant_0_2m",
    "infant_3_11m",
    "child_1_6y",
    "school_7_17y",
    "adult_18plus",
)


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def _resolve_path(path: str | Path) -> Path:
    path = Path(path)
    if path.exists():
        return path
    repo_path = project_path(path)
    if repo_path.exists():
        return repo_path
    return path


def load_data_sources() -> dict[str, Any]:
    settings_path = project_path("config/model_settings.yaml")
    if not settings_path.exists():
        raise FileNotFoundError("config/model_settings.yaml is required for data-source configuration.")
    settings = load_yaml(settings_path)
    if "runtime" not in settings or "data_sources" not in settings["runtime"]:
        raise ValueError("config/model_settings.yaml is missing runtime.data_sources.")
    sources = settings["runtime"]["data_sources"]
    if not sources:
        raise ValueError("config/model_settings.yaml is missing runtime.data_sources.")
    return sources


def _require_key(mapping: dict[str, Any], key: str, *, context: str) -> Any:
    if key not in mapping or mapping[key] in (None, ""):
        raise ValueError(f"{context} must define {key!r}.")
    return mapping[key]


def validate_data_sources(sources: dict[str, Any]) -> None:
    required = (
        "wpp_population_csv",
        "pertussis_incidence_csv",
        "vaccine_data_csv",
        "epydemix_data_root",
        "population_year",
        "countries",
    )
    for key in required:
        _require_key(sources, key, context="runtime.data_sources")
    if "contact_matrix_csv" in sources:
        raise ValueError("contact_matrix_csv is not allowed in final analysis; use epydemix_data_root only.")
    for country_code, meta in sources["countries"].items():
        context = f"runtime.data_sources.countries.{country_code}"
        for key in (
            "config_key",
            "iso3",
            "epydemix_population_name",
            "epydemix_contacts_source",
            "vaccine_product",
            "primary_doses",
            "child_booster_doses",
            "adolescent_booster",
            "maternal_program",
            "maternal_coverage",
            "schedule_note",
        ):
            _require_key(meta, key, context=context)
        forbidden = sorted(key for key in meta if key.startswith("fallback_"))
        if forbidden:
            raise ValueError(f"{context} contains development fallback fields: {forbidden}")


def baseline_reporting_rates() -> dict[str, float]:
    settings_path = project_path("config/model_settings.yaml")
    settings = load_yaml(settings_path)
    try:
        age_records = settings["runtime"]["baseline_parameters"]["age_groups"]
    except KeyError as exc:
        raise ValueError("config/model_settings.yaml must define runtime.baseline_parameters.age_groups.") from exc
    reporting = {}
    for record in age_records:
        label = str(_require_key(record, "label", context="runtime.baseline_parameters.age_groups[]"))
        reporting_rate = float(_require_key(record, "reporting_rate", context=f"age group {label}"))
        if not 0.0 <= reporting_rate <= 1.0:
            raise ValueError(f"Age group {label} reporting_rate must be in [0, 1].")
        reporting[label] = reporting_rate
    missing = [label for label in AGE_GROUPS if label not in reporting]
    if missing:
        raise ValueError(f"Baseline reporting rates are missing age groups: {missing}")
    return {label: reporting[label] for label in AGE_GROUPS}


def aggregate_wpp_population(wpp_csv: Path, *, iso3: str, year: int) -> dict[str, float]:
    usecols = ["Iso3", "Time", "Sex", "AgeStart", "Value"]
    df = pd.read_csv(wpp_csv, usecols=usecols)
    df = df.loc[
        df["Iso3"].eq(iso3)
        & df["Time"].eq(year)
        & df["Sex"].eq("Both sexes")
    ].copy()
    if df.empty:
        raise ValueError(f"No WPP population rows found for {iso3} in {year}.")

    age = df["AgeStart"].astype(float)
    value = df["Value"].astype(float)
    age0 = float(value.loc[age.eq(0)].sum())
    return {
        "infant_0_2m": age0 * 0.25,
        "infant_3_11m": age0 * 0.75,
        "child_1_6y": float(value.loc[age.between(1, 6)].sum()),
        "school_7_17y": float(value.loc[age.between(7, 17)].sum()),
        "adult_18plus": float(value.loc[age.ge(18)].sum()),
    }


def load_wpp_one_year(wpp_csv: Path, *, iso3: str, year: int) -> pd.DataFrame:
    usecols = ["Iso3", "Time", "Sex", "AgeStart", "Value"]
    df = pd.read_csv(wpp_csv, usecols=usecols)
    df = df.loc[
        df["Iso3"].eq(iso3)
        & df["Time"].eq(year)
        & df["Sex"].eq("Both sexes")
    ].copy()
    if df.empty:
        raise ValueError(f"No WPP population rows found for {iso3} in {year}.")
    df["AgeStart"] = df["AgeStart"].astype(int)
    df["Value"] = pd.to_numeric(df["Value"], errors="coerce").fillna(0.0)
    return df


def load_incidence(incidence_csv: Path, country_code: str) -> pd.DataFrame:
    df = pd.read_csv(incidence_csv)
    df = df.loc[df["Country"].eq(country_code)].copy()
    if df.empty:
        raise ValueError(f"No reported pertussis rows found for {country_code}.")
    df["Date"] = pd.to_datetime(df["Date"])
    df["Cases"] = pd.to_numeric(df["Cases"], errors="coerce").fillna(0.0)
    return df


def _normalize_epydemix_contact_source(source: str) -> str:
    value = str(source).strip().lower()
    supported = {"prem_2017", "prem_2021", "mistry_2021", "litvinova_2025"}
    if value not in supported:
        raise ValueError(f"Unsupported epydemix contact source: {source!r}")
    return value


def _epydemix_resource_root(root: str | Path, *parts: str) -> str:
    base = str(root).rstrip("/")
    suffix = "/".join(part.strip("/") for part in parts if part)
    return f"{base}/{suffix}" if suffix else base


def _epydemix_contact_age_ranges(contacts_source: str, n_bins: int) -> list[tuple[float, float | None]]:
    source = _normalize_epydemix_contact_source(contacts_source)
    if source in {"prem_2017", "prem_2021", "litvinova_2025"}:
        if n_bins != 16:
            raise ValueError(f"Expected 16 contact bins for {source}, found {n_bins}.")
        return [(float(lower), float(lower + 5)) for lower in range(0, 75, 5)] + [(75.0, None)]
    if source == "mistry_2021":
        if n_bins != 85:
            raise ValueError(f"Expected 85 contact bins for {source}, found {n_bins}.")
        return [(float(age), float(age + 1)) for age in range(0, 84)] + [(84.0, None)]
    raise ValueError(f"Unsupported epydemix contact source: {contacts_source!r}")


def load_epydemix_contact_matrix(
    epydemix_data_root: str | Path,
    population_name: str,
    contacts_source: str,
    *,
    layer: str = "all",
) -> np.ndarray:
    source = _normalize_epydemix_contact_source(contacts_source)
    matrix_path = _epydemix_resource_root(
        epydemix_data_root,
        "data",
        population_name,
        "contact_matrices",
        source,
        f"contacts_matrix_{layer}.csv",
    )
    matrix = pd.read_csv(matrix_path, header=None).to_numpy(dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError(f"Invalid epydemix contact matrix at {matrix_path!r}: shape {matrix.shape}")
    return matrix


def _population_by_model_group_and_source_bin(
    one_year_population: pd.DataFrame,
    source_age_ranges: list[tuple[float, float | None]],
) -> np.ndarray:
    model_bounds = [
        (0.0, 2.0 / 12.0),
        (2.0 / 12.0, 1.0),
        (1.0, 7.0),
        (7.0, 18.0),
        (18.0, 101.0),
    ]
    source_bounds = [
        (
            float(lower),
            float(101.0 if upper is None else upper),
        )
        for lower, upper in source_age_ranges
    ]
    ages = pd.to_numeric(one_year_population["AgeStart"], errors="coerce").fillna(0.0).to_numpy(dtype=float)
    values = pd.to_numeric(one_year_population["Value"], errors="coerce").fillna(0.0).to_numpy(dtype=float)

    bin_pop = np.zeros((len(model_bounds), len(source_bounds)), dtype=float)
    for age, population in zip(ages, values):
        age_lower = float(age)
        age_upper = float(age + 1.0)
        for model_idx, (model_lower, model_upper) in enumerate(model_bounds):
            for source_idx, (source_lower, source_upper) in enumerate(source_bounds):
                overlap = max(
                    0.0,
                    min(age_upper, model_upper, source_upper) - max(age_lower, model_lower, source_lower),
                )
                if overlap > 0.0:
                    bin_pop[model_idx, source_idx] += float(population) * overlap
    return bin_pop


def aggregate_contact_matrix_from_epydemix(
    contact_matrix: np.ndarray,
    one_year_population: pd.DataFrame,
    *,
    source_age_ranges: list[tuple[float, float | None]],
) -> tuple[list[list[float]], dict[str, float | bool]]:
    matrix = np.asarray(contact_matrix, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError(f"Contact matrix must be square; got shape {matrix.shape}")
    if len(source_age_ranges) != matrix.shape[0]:
        raise ValueError(
            "Contact matrix bin count does not match the provided age ranges: "
            f"{matrix.shape[0]} vs {len(source_age_ranges)}."
        )

    bin_pop = _population_by_model_group_and_source_bin(one_year_population, source_age_ranges)
    model_pop = np.maximum(bin_pop.sum(axis=1), 1e-12)
    source_pop = np.maximum(bin_pop.sum(axis=0), 1e-12)
    row_weights = bin_pop / model_pop[:, None]
    column_fractions = bin_pop / source_pop[None, :]
    aggregated = row_weights @ matrix @ column_fractions.T
    model_population = np.maximum(bin_pop.sum(axis=1), 1e-12)
    error_before = reciprocity_error(aggregated, model_population)
    balanced = balance_reciprocity(aggregated, model_population)
    error_after = reciprocity_error(balanced, model_population)
    return balanced.round(6).tolist(), {
        "reciprocity_correction_applied": True,
        "reciprocity_error_before": float(error_before),
        "reciprocity_error_after": float(error_after),
    }


def infer_seasonality(incidence: pd.DataFrame) -> dict[str, float]:
    df = incidence.loc[incidence["Cases"].gt(0)].copy()
    if df.empty:
        raise ValueError("Cannot infer seasonality from a surveillance series with no positive reported cases.")

    day_of_year = df["Date"].dt.dayofyear.clip(upper=365).to_numpy(dtype=float)
    theta = 2.0 * np.pi * (day_of_year - 1.0) / 365.0
    weights = df["Cases"].to_numpy(dtype=float)
    sin_sum = float(np.sum(weights * np.sin(theta)))
    cos_sum = float(np.sum(weights * np.cos(theta)))
    total = max(float(np.sum(weights)), 1e-9)
    concentration = min(1.0, np.sqrt(sin_sum**2 + cos_sum**2) / total)
    phase = (np.arctan2(sin_sum, cos_sum) * 365.0 / (2.0 * np.pi) + 1.0) % 365.0
    amplitude = float(np.clip(0.08 + 0.55 * concentration, 0.08, 0.35))
    return {
        "seasonal_amplitude": amplitude,
        "seasonal_phase": float(phase),
        "seasonal_concentration": float(concentration),
    }


def infer_multiyear_cycle(incidence: pd.DataFrame) -> dict[str, float]:
    annual = incidence.groupby("Year", as_index=False)["Cases"].sum().sort_values("Year")
    if len(annual) < 6:
        raise ValueError("Cannot assess multi-year cycle support from fewer than six annual observations.")

    values = annual["Cases"].to_numpy(dtype=float)
    years = annual["Year"].to_numpy(dtype=float)
    prominence = max(float(np.max(values)) * 0.10, 1.0)
    peak_idx, _ = find_peaks(values, distance=2, prominence=prominence)
    intervals = np.diff(years[peak_idx])
    plausible = intervals[(intervals >= 3.0) & (intervals <= 5.0)]
    if len(plausible) == 0:
        return {
            "multi_year_period_years": float("nan"),
            "multi_year_amplitude": 0.0,
            "multi_year_supported": False,
            "observed_peak_years": ";".join(str(int(years[i])) for i in peak_idx),
        }
    period = float(np.median(plausible))
    cv = float(np.std(values) / max(np.mean(values), 1e-9))
    amplitude = float(np.clip(0.06 + 0.08 * cv, 0.06, 0.16))
    return {
        "multi_year_period_years": period,
        "multi_year_amplitude": amplitude,
        "multi_year_supported": True,
        "observed_peak_years": ";".join(str(int(years[i])) for i in peak_idx),
    }


def observed_annual_incidence(incidence: pd.DataFrame, total_population: float) -> dict[str, float]:
    annual_cases = incidence.groupby("Year")["Cases"].sum().to_numpy(dtype=float)
    annual_incidence = annual_cases / max(total_population, 1e-9) * 100_000.0
    return {
        "observed_mean_annual_reported_incidence_per_100k": float(np.mean(annual_incidence)),
        "observed_peak_annual_reported_incidence_per_100k": float(np.max(annual_incidence)),
    }


def coverage_by_age(vaccine_df: pd.DataFrame, iso3: str, meta: dict[str, Any]) -> dict[str, float]:
    row = vaccine_df.loc[vaccine_df["CODE"].eq(iso3)]
    if row.empty:
        if "coverage_DTP1" not in meta or "coverage_DTP3" not in meta:
            raise ValueError(
                f"No vaccine coverage row found for {iso3}; provide explicit coverage_DTP1 and coverage_DTP3."
            )
        dtp1 = float(meta["coverage_DTP1"])
        dtp3 = float(meta["coverage_DTP3"])
    else:
        dtp1 = float(row["CoverageDTP1"].iloc[0]) / 100.0
        dtp3 = float(row["CoverageDTP3"].iloc[0]) / 100.0
    child_boosters = float(meta["child_booster_doses"])
    maternal_coverage = float(meta["maternal_coverage"])
    adolescent_booster = bool(meta["adolescent_booster"])

    infant_birth_protection = 0.02 + 0.55 * maternal_coverage
    partial_infant_series = 0.75 * dtp1 + 0.12 * dtp3 + 0.12 * maternal_coverage
    preschool_boost = 0.88 + 0.04 * min(child_boosters, 2.0)
    school_boost = 0.58 + 0.10 * min(child_boosters, 2.0) + (0.12 if adolescent_booster else 0.0)
    adult_proxy = 0.18 + 0.32 * maternal_coverage + (0.04 if adolescent_booster else 0.0)
    return {
        "infant_0_2m": float(np.clip(infant_birth_protection, 0.02, 0.75)),
        "infant_3_11m": float(np.clip(partial_infant_series, 0.0, 0.95)),
        "child_1_6y": float(np.clip(dtp3 * preschool_boost, 0.0, 0.98)),
        "school_7_17y": float(np.clip(dtp3 * school_boost, 0.0, 0.95)),
        "adult_18plus": float(np.clip(adult_proxy, 0.10, 0.75)),
    }


def build_profiles() -> tuple[
    dict[str, Any],
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
]:
    sources = load_data_sources()
    validate_data_sources(sources)
    reporting_rates = baseline_reporting_rates()
    wpp_csv = _resolve_path(sources["wpp_population_csv"])
    incidence_csv = _resolve_path(sources["pertussis_incidence_csv"])
    vaccine_csv = _resolve_path(sources["vaccine_data_csv"])
    epydemix_data_root = sources["epydemix_data_root"]
    year = int(sources["population_year"])
    vaccine_df = pd.read_csv(vaccine_csv)

    profiles: dict[str, Any] = {}
    population_rows = []
    seasonality_rows = []
    contact_rows = []
    contact_diagnostic_rows = []
    incidence_frames = []

    for country_code, meta in sources["countries"].items():
        key = meta["config_key"]
        iso3 = meta["iso3"]
        incidence = load_incidence(incidence_csv, country_code)
        incidence = incidence.assign(config_key=key, iso3=iso3)
        incidence_frames.append(incidence)

        one_year_population = load_wpp_one_year(wpp_csv, iso3=iso3, year=year)
        population = aggregate_wpp_population(wpp_csv, iso3=iso3, year=year)
        seasonality = infer_seasonality(incidence)
        cycle = infer_multiyear_cycle(incidence)
        vaccination = coverage_by_age(vaccine_df, iso3, meta)
        epydemix_country = str(meta["epydemix_population_name"]).replace(" ", "_")
        epydemix_source = _normalize_epydemix_contact_source(meta["epydemix_contacts_source"])
        raw_contact_matrix = load_epydemix_contact_matrix(
            epydemix_data_root,
            epydemix_country,
            epydemix_source,
            layer="all",
        )
        source_age_ranges = _epydemix_contact_age_ranges(epydemix_source, raw_contact_matrix.shape[0])
        contact_matrix, contact_diagnostics = aggregate_contact_matrix_from_epydemix(
            raw_contact_matrix,
            one_year_population,
            source_age_ranges=source_age_ranges,
        )
        total_population = sum(population.values())
        observed_incidence = observed_annual_incidence(incidence, total_population)
        birth_vaccinated = float(np.clip(0.02 + 0.55 * float(meta["maternal_coverage"]), 0.02, 0.75))
        transmission_overrides = {
            "seasonal_amplitude": float(seasonality["seasonal_amplitude"]),
            "seasonal_phase": float(seasonality["seasonal_phase"]),
            "multi_year_amplitude": float(cycle["multi_year_amplitude"]),
        }
        if bool(cycle["multi_year_supported"]):
            transmission_overrides["multi_year_period_years"] = float(cycle["multi_year_period_years"])

        population_rows.extend(
            {
                "country": key,
                "iso3": iso3,
                "year": year,
                "age_group": age_group,
                "population": value,
                "source": "UN WPP 2024 one-year age population",
                "source_type": "derived",
            }
            for age_group, value in population.items()
        )
        for source_idx, source_age in enumerate(AGE_GROUPS):
            for target_idx, target_age in enumerate(AGE_GROUPS):
                contact_rows.append(
                    {
                        "country": key,
                        "iso3": iso3,
                        "source_age_group": source_age,
                        "target_age_group": target_age,
                        "contacts_per_day": contact_matrix[source_idx][target_idx],
                        "source": (
                            f"epydemix-data {epydemix_source} "
                            "all-layer matrix aggregated with WPP age weights and reciprocity balanced"
                        ),
                        "source_type": "derived",
                    }
                )
        contact_diagnostic_rows.append(
            {
                "country": key,
                "iso3": iso3,
                **contact_diagnostics,
                "source_type": "derived",
            }
        )
        seasonality_rows.append(
            {
                "country": key,
                "iso3": iso3,
                **seasonality,
                **cycle,
                **observed_incidence,
                "source": "reported pertussis case time series",
                "source_type": "derived",
            }
        )

        profiles[key] = {
            "description": (
                f"Data-derived profile for {key}; WPP {year} population, "
                "reported pertussis surveillance-derived seasonality, epydemix-data contact matrix."
            ),
            "iso3": iso3,
            "population": {k: float(v) for k, v in population.items()},
            "total_population": float(total_population),
            "observed_incidence": observed_incidence,
            "vaccine_coverage": {k: float(v) for k, v in vaccination.items()},
            "source_types": {
                "population": "derived",
                "observed_incidence": "derived",
                "vaccine_coverage": "derived_or_explicit",
                "birth_entry": "derived_from_maternal_coverage",
                "reporting_rate": "declared_runtime_parameter",
                "seasonality": "derived",
                "multi_year_cycle": "derived",
                "contact_matrix": "derived",
            },
            "vaccine_schedule": {
                "vaccine_product": meta["vaccine_product"],
                "primary_doses": int(meta["primary_doses"]),
                "child_booster_doses": int(meta["child_booster_doses"]),
                "adolescent_booster": bool(meta["adolescent_booster"]),
                "maternal_program": bool(meta["maternal_program"]),
                "maternal_coverage": float(meta["maternal_coverage"]),
                "schedule_note": meta["schedule_note"],
                "source": "WHO Immunization Data Portal / WUENIC / JRF plus country schedule metadata",
            },
            "birth_entry": {"S": float(1.0 - birth_vaccinated), "V": birth_vaccinated},
            "reporting_rate": dict(reporting_rates),
            "transmission_overrides": transmission_overrides,
            "contact_reciprocity": contact_diagnostics,
            "contact_source": (
                f"epydemix-data {epydemix_source} "
                "country matrix aggregated to project age groups with population-weighted reciprocity correction"
            ),
            "contact_matrix": contact_matrix,
        }

    incidence_out = pd.concat(incidence_frames, ignore_index=True)
    return (
        profiles,
        pd.DataFrame(population_rows),
        pd.DataFrame(seasonality_rows),
        pd.DataFrame(contact_rows),
        pd.DataFrame(contact_diagnostic_rows),
        incidence_out,
    )


def main() -> None:
    profiles, population, seasonality, contacts, contact_diagnostics, incidence = build_profiles()
    project_path("data/processed").mkdir(parents=True, exist_ok=True)
    population.to_csv(project_path("data/processed/wpp_country_age_groups.csv"), index=False)
    seasonality.to_csv(project_path("data/processed/pertussis_incidence_seasonality.csv"), index=False)
    contacts.to_csv(project_path("data/processed/country_contact_matrices_5groups.csv"), index=False)
    contact_diagnostics.to_csv(project_path("data/processed/contact_matrix_reciprocity_diagnostics.csv"), index=False)
    incidence.to_csv(project_path("data/processed/pertussis_incidence_timeseries.csv"), index=False)

    with project_path("config/country_profiles.yaml").open("w", encoding="utf-8") as handle:
        yaml.dump(profiles, handle, Dumper=NoAliasDumper, sort_keys=False)


if __name__ == "__main__":
    main()
