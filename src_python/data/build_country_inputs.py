from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml
from scipy.signal import find_peaks

from src_python.utils.io import load_yaml, project_path


AGE_GROUPS = (
    "infant_0_2m",
    "infant_3_11m",
    "child_1_6y",
    "school_7_17y",
    "adult_18plus",
)


BASE_CONTACT_MATRIX = [
    [5.5, 2.2, 1.2, 0.5, 1.0],
    [1.8, 6.2, 2.6, 0.8, 1.2],
    [0.7, 2.1, 9.0, 2.8, 1.4],
    [0.3, 0.8, 3.0, 10.5, 2.6],
    [0.4, 0.7, 1.3, 2.5, 6.0],
]

PREM_CONTACT_BINS = tuple(range(0, 80, 5))


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


REPORTING_DEFAULTS = {
    "infant_0_2m": 0.60,
    "infant_3_11m": 0.50,
    "child_1_6y": 0.25,
    "school_7_17y": 0.10,
    "adult_18plus": 0.05,
}


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
    if settings_path.exists():
        settings = load_yaml(settings_path)
        sources = settings.get("runtime", {}).get("data_sources")
        if sources:
            return sources
    return load_yaml(project_path("config/data_sources.yaml"))


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
        raise ValueError(f"No PertussisIncidence rows found for {country_code}.")
    df["Date"] = pd.to_datetime(df["Date"])
    df["Cases"] = pd.to_numeric(df["Cases"], errors="coerce").fillna(0.0)
    return df


def infer_seasonality(incidence: pd.DataFrame) -> dict[str, float]:
    df = incidence.loc[incidence["Cases"].gt(0)].copy()
    if df.empty:
        return {"seasonal_amplitude": 0.12, "seasonal_phase": 30.0}

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
        return {"multi_year_period_years": 4.0, "multi_year_amplitude": 0.08}

    values = annual["Cases"].to_numpy(dtype=float)
    years = annual["Year"].to_numpy(dtype=float)
    prominence = max(float(np.max(values)) * 0.10, 1.0)
    peak_idx, _ = find_peaks(values, distance=2, prominence=prominence)
    intervals = np.diff(years[peak_idx])
    plausible = intervals[(intervals >= 3.0) & (intervals <= 5.0)]
    period = float(np.median(plausible)) if len(plausible) else 4.0
    cv = float(np.std(values) / max(np.mean(values), 1e-9))
    amplitude = float(np.clip(0.06 + 0.08 * cv, 0.06, 0.16))
    return {
        "multi_year_period_years": period,
        "multi_year_amplitude": amplitude,
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
        dtp1 = float(meta.get("fallback_DTP1", 0.95))
        dtp3 = float(meta.get("fallback_DTP3", 0.90))
        child_boosters = float(meta.get("child_booster_doses", 1))
    else:
        dtp1 = float(row["CoverageDTP1"].iloc[0]) / 100.0
        dtp3 = float(row["CoverageDTP3"].iloc[0]) / 100.0
        child_boosters = float(meta.get("child_booster_doses", row.get("GENERALY", pd.Series([1])).iloc[0]))
    maternal_coverage = float(meta.get("maternal_coverage", 0.0))
    adolescent_booster = bool(meta.get("adolescent_booster", False))

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


def _model_age_population_by_prem_bin(one_year_population: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, record in one_year_population.iterrows():
        age = int(record["AgeStart"])
        value = float(record["Value"])
        prem_bin = min((age // 5) * 5, 75)
        if age == 0:
            rows.extend(
                [
                    {"age_group": "infant_0_2m", "prem_bin": prem_bin, "population": value * 0.25},
                    {"age_group": "infant_3_11m", "prem_bin": prem_bin, "population": value * 0.75},
                ]
            )
        elif 1 <= age <= 6:
            rows.append({"age_group": "child_1_6y", "prem_bin": prem_bin, "population": value})
        elif 7 <= age <= 17:
            rows.append({"age_group": "school_7_17y", "prem_bin": prem_bin, "population": value})
        else:
            rows.append({"age_group": "adult_18plus", "prem_bin": prem_bin, "population": value})
    return pd.DataFrame(rows)


def _prem_bin_label(lower: int) -> str:
    return f"[{lower:02d},{lower + 5:02d})"


def aggregate_contact_matrix(
    contact_df: pd.DataFrame,
    one_year_population: pd.DataFrame,
    *,
    country_key: str,
) -> list[list[float]]:
    country_contacts = contact_df.loc[contact_df["country"].eq(country_key)].copy()
    if country_contacts.empty:
        return BASE_CONTACT_MATRIX

    labels = [_prem_bin_label(lower) for lower in PREM_CONTACT_BINS]
    fine = (
        country_contacts.pivot_table(
            index="source_age_bin",
            columns="target_age_bin",
            values="contacts_per_day",
            aggfunc="mean",
        )
        .reindex(index=labels, columns=labels)
        .fillna(0.0)
        .to_numpy(dtype=float)
    )
    overlap = _model_age_population_by_prem_bin(one_year_population)
    bin_pop = (
        overlap.pivot_table(index="age_group", columns="prem_bin", values="population", aggfunc="sum")
        .reindex(index=AGE_GROUPS, columns=PREM_CONTACT_BINS)
        .fillna(0.0)
        .to_numpy(dtype=float)
    )
    model_pop = np.maximum(bin_pop.sum(axis=1), 1e-12)
    fine_pop = np.maximum(bin_pop.sum(axis=0), 1e-12)
    row_weights = bin_pop / model_pop[:, None]
    column_fractions = bin_pop / fine_pop[None, :]
    aggregated = row_weights @ fine @ column_fractions.T
    return aggregated.round(6).tolist()


def build_profiles() -> tuple[dict[str, Any], pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    sources = load_data_sources()
    wpp_csv = _resolve_path(sources["wpp_population_csv"])
    incidence_csv = _resolve_path(sources["pertussis_incidence_csv"])
    vaccine_csv = _resolve_path(sources["vaccine_data_csv"])
    contact_csv = _resolve_path(sources["contact_matrix_csv"])
    year = int(sources.get("analysis_year", 2023))
    vaccine_df = pd.read_csv(vaccine_csv)
    contact_df = pd.read_csv(contact_csv)

    profiles: dict[str, Any] = {}
    population_rows = []
    seasonality_rows = []
    contact_rows = []
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
        contact_matrix = aggregate_contact_matrix(contact_df, one_year_population, country_key=key)
        total_population = sum(population.values())
        observed_incidence = observed_annual_incidence(incidence, total_population)
        birth_vaccinated = float(np.clip(0.02 + 0.55 * float(meta.get("maternal_coverage", 0.0)), 0.02, 0.75))

        population_rows.extend(
            {
                "country": key,
                "iso3": iso3,
                "year": year,
                "age_group": age_group,
                "population": value,
                "source": "UN WPP 2024 one-year age population",
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
                            f"Prem/contactdata {meta.get('contactdata_source', 'unknown')} "
                            "matrix aggregated with WPP age weights"
                        ),
                    }
                )
        seasonality_rows.append(
            {
                "country": key,
                "iso3": iso3,
                **seasonality,
                **cycle,
                **observed_incidence,
                "source": "PertussisIncidence reported case time series",
            }
        )

        profiles[key] = {
            "description": (
                f"Data-derived profile for {key}; WPP {year} population, "
                "PertussisIncidence-derived seasonality, Prem/contactdata-derived contact matrix."
            ),
            "iso3": iso3,
            "population": {k: float(v) for k, v in population.items()},
            "total_population": float(total_population),
            "observed_incidence": observed_incidence,
            "vaccine_coverage": {k: float(v) for k, v in vaccination.items()},
            "vaccine_schedule": {
                "vaccine_product": meta.get("vaccine_product", "unknown"),
                "primary_doses": int(meta.get("primary_doses", 3)),
                "child_booster_doses": int(meta.get("child_booster_doses", 0)),
                "adolescent_booster": bool(meta.get("adolescent_booster", False)),
                "maternal_program": bool(meta.get("maternal_program", False)),
                "maternal_coverage": float(meta.get("maternal_coverage", 0.0)),
                "schedule_note": meta.get("schedule_note", ""),
                "source": "WHO Immunization Data Portal / WUENIC / JRF plus country schedule metadata",
            },
            "birth_entry": {"S": float(1.0 - birth_vaccinated), "V": birth_vaccinated},
            "reporting_rate": REPORTING_DEFAULTS,
            "transmission_overrides": {
                "seasonal_amplitude": float(seasonality["seasonal_amplitude"]),
                "seasonal_phase": float(seasonality["seasonal_phase"]),
                "multi_year_amplitude": float(cycle["multi_year_amplitude"]),
                "multi_year_period_years": float(cycle["multi_year_period_years"]),
            },
            "contact_source": (
                f"Prem/contactdata {meta.get('contactdata_source', 'unknown')} "
                "country matrix aggregated to project age groups"
            ),
            "contact_matrix": contact_matrix,
        }

    incidence_out = pd.concat(incidence_frames, ignore_index=True)
    return (
        profiles,
        pd.DataFrame(population_rows),
        pd.DataFrame(seasonality_rows),
        pd.DataFrame(contact_rows),
        incidence_out,
    )


def main() -> None:
    profiles, population, seasonality, contacts, incidence = build_profiles()
    project_path("data/processed").mkdir(parents=True, exist_ok=True)
    population.to_csv(project_path("data/processed/wpp_country_age_groups.csv"), index=False)
    seasonality.to_csv(project_path("data/processed/pertussis_incidence_seasonality.csv"), index=False)
    contacts.to_csv(project_path("data/processed/country_contact_matrices_5groups.csv"), index=False)
    incidence.to_csv(project_path("data/processed/pertussis_incidence_timeseries.csv"), index=False)

    with project_path("config/country_profiles.yaml").open("w", encoding="utf-8") as handle:
        yaml.dump(profiles, handle, Dumper=NoAliasDumper, sort_keys=False)


if __name__ == "__main__":
    main()
