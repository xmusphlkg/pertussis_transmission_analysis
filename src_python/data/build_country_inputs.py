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
    amplitude = float(np.clip(0.04 + 0.08 * cv, 0.05, 0.18))
    return {
        "multi_year_period_years": period,
        "multi_year_amplitude": amplitude,
        "observed_peak_years": ";".join(str(int(years[i])) for i in peak_idx),
    }


def coverage_by_age(vaccine_df: pd.DataFrame, iso3: str) -> dict[str, float]:
    row = vaccine_df.loc[vaccine_df["CODE"].eq(iso3)]
    if row.empty:
        dtp1 = 0.85
        dtp3 = 0.80
    else:
        dtp1 = float(row["CoverageDTP1"].iloc[0]) / 100.0
        dtp3 = float(row["CoverageDTP3"].iloc[0]) / 100.0
    return {
        "infant_0_2m": min(0.12, 0.10 * dtp1),
        "infant_3_11m": min(0.95, 0.75 * dtp1 + 0.15 * dtp3),
        "child_1_6y": min(0.98, dtp3),
        "school_7_17y": min(0.95, 0.78 * dtp3),
        "adult_18plus": min(0.75, max(0.20, 0.40 * dtp3)),
    }


def build_profiles() -> tuple[dict[str, Any], pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    sources = load_yaml(project_path("config/data_sources.yaml"))
    wpp_csv = _resolve_path(sources["wpp_population_csv"])
    incidence_csv = _resolve_path(sources["pertussis_incidence_csv"])
    vaccine_csv = _resolve_path(sources["vaccine_data_csv"])
    year = int(sources.get("analysis_year", 2023))
    vaccine_df = pd.read_csv(vaccine_csv)

    profiles: dict[str, Any] = {}
    population_rows = []
    seasonality_rows = []
    incidence_frames = []

    for country_code, meta in sources["countries"].items():
        key = meta["config_key"]
        iso3 = meta["iso3"]
        incidence = load_incidence(incidence_csv, country_code)
        incidence = incidence.assign(config_key=key, iso3=iso3)
        incidence_frames.append(incidence)

        population = aggregate_wpp_population(wpp_csv, iso3=iso3, year=year)
        seasonality = infer_seasonality(incidence)
        cycle = infer_multiyear_cycle(incidence)
        vaccination = coverage_by_age(vaccine_df, iso3)
        total_population = sum(population.values())

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
        seasonality_rows.append(
            {
                "country": key,
                "iso3": iso3,
                **seasonality,
                **cycle,
                "source": "PertussisIncidence reported case time series",
            }
        )

        profiles[key] = {
            "description": (
                f"Data-derived profile for {key}; WPP {year} population, "
                "PertussisIncidence-derived seasonality, synthetic contact matrix placeholder."
            ),
            "iso3": iso3,
            "population": {k: float(v) for k, v in population.items()},
            "total_population": float(total_population),
            "vaccine_coverage": {k: float(v) for k, v in vaccination.items()},
            "birth_entry": {"S": 0.95, "V": 0.05},
            "reporting_rate": REPORTING_DEFAULTS,
            "transmission_overrides": {
                "seasonal_amplitude": float(seasonality["seasonal_amplitude"]),
                "seasonal_phase": float(seasonality["seasonal_phase"]),
                "multi_year_amplitude": float(cycle["multi_year_amplitude"]),
                "multi_year_period_years": float(cycle["multi_year_period_years"]),
            },
            "contact_source": "synthetic_placeholder_matrix_until_country_contact_data_are_added",
            "contact_matrix": BASE_CONTACT_MATRIX,
        }

    incidence_out = pd.concat(incidence_frames, ignore_index=True)
    return profiles, pd.DataFrame(population_rows), pd.DataFrame(seasonality_rows), incidence_out


def main() -> None:
    profiles, population, seasonality, incidence = build_profiles()
    project_path("data/processed").mkdir(parents=True, exist_ok=True)
    population.to_csv(project_path("data/processed/wpp_country_age_groups.csv"), index=False)
    seasonality.to_csv(project_path("data/processed/pertussis_incidence_seasonality.csv"), index=False)
    incidence.to_csv(project_path("data/processed/pertussis_incidence_timeseries.csv"), index=False)

    with project_path("config/country_profiles.yaml").open("w", encoding="utf-8") as handle:
        yaml.dump(profiles, handle, Dumper=NoAliasDumper, sort_keys=False)


if __name__ == "__main__":
    main()
