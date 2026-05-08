from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from typing import Any

import numpy as np

from src_python.model.contact_matrix import balance_reciprocity, reciprocity_error


@dataclass(frozen=True)
class PreparedParameters:
    raw: dict[str, Any]
    analysis: str
    scenario: str
    vaccine_scenario: str
    resistance_scenario: str
    intervention: str
    age_groups: tuple[str, ...]
    population: np.ndarray
    vaccine_coverage: np.ndarray
    symptom_probability: np.ndarray
    reporting_rate: np.ndarray
    pep_detection_rate: np.ndarray
    contact_matrix: np.ndarray
    vaccine: dict[str, float]
    rates: dict[str, float]
    transmission: dict[str, float]
    treatment: dict[str, Any]
    pep: dict[str, float]
    initial: dict[str, Any]
    immunity_model: dict[str, Any]
    observation_model: dict[str, Any]
    resistance: dict[str, Any]
    demography: dict[str, Any]
    routine_vaccination: dict[str, Any]
    importation: dict[str, Any]
    calendar: dict[str, Any]
    calendar_start_date: date | None
    reporting_time_variation: dict[str, float] = field(default_factory=dict)
    reporting_multiplier: float = 1.0
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_config(
        cls,
        config: dict[str, Any],
        *,
        analysis: str,
        scenario: str,
        vaccine_scenario: str = "",
        resistance_scenario: str = "",
        intervention: str = "",
        metadata: dict[str, Any] | None = None,
    ) -> "PreparedParameters":
        age_records = config["age_groups"]
        age_groups = tuple(record["label"] for record in age_records)
        population = np.array([record["population"] for record in age_records], dtype=float)
        if not np.isfinite(population).all() or np.any(population <= 0.0):
            raise ValueError("Age-group populations must be finite and > 0.")

        vaccine = {key: float(value) for key, value in config.get("vaccine", {}).items() if key.startswith("VE_")}
        if not vaccine:
            vaccine = {"VE_sus": 0.0, "VE_sym": 0.0, "VE_inf": 0.0, "VE_dur": 0.0}
        _validate_probability_values(vaccine.values(), "Vaccine efficacy values")

        coverage = _probability_array(
            [record.get("vaccine_coverage", 0.0) for record in age_records],
            "Age-group vaccine coverage",
        )
        if sum(vaccine.values()) == 0:
            coverage = np.zeros_like(coverage)

        reporting_multiplier = float(config.get("reporting_multiplier", 1.0))
        reporting_base = _probability_array(
            [record.get("reporting_rate", 0.0) for record in age_records],
            "Age-group reporting rates",
        )
        pep_detection = _probability_array(
            [record.get("pep_detection_rate", record.get("reporting_rate", 0.0)) for record in age_records],
            "Age-group PEP detection rates",
        )
        reporting = reporting_base
        reporting = np.clip(reporting * reporting_multiplier, 0.0, 1.0)

        rows = config["contact_matrix"]["rows"]
        contact_matrix = np.array(rows, dtype=float)
        if contact_matrix.shape != (len(age_groups), len(age_groups)):
            raise ValueError("Contact matrix dimensions must match age groups.")
        if not np.isfinite(contact_matrix).all() or np.any(contact_matrix < 0.0):
            raise ValueError("Contact matrix entries must be finite and non-negative.")
        contact_metadata = {}
        correction = config.get("contact_matrix", {}).get("reciprocity_correction", {})
        if correction.get("enabled", False):
            before = reciprocity_error(contact_matrix, population)
            contact_matrix = balance_reciprocity(contact_matrix, population)
            after = reciprocity_error(contact_matrix, population)
            contact_metadata = {
                "contact_reciprocity_error_before": before,
                "contact_reciprocity_error_after": after,
            }

        natural_history = config["natural_history"]
        immunity_model = config.get("immunity_model", {})
        waned_vaccine_duration = float(
            immunity_model.get(
                "waned_vaccine_duration",
                natural_history.get("waned_vaccine_duration", natural_history["vaccine_protection_duration"]),
            )
        )
        rates = {
            "latent": 1.0 / float(natural_history["latent_duration"]),
            "recovery_symptomatic": 1.0 / float(natural_history["infectious_duration_symptomatic"]),
            "recovery_asymptomatic": 1.0 / float(natural_history["infectious_duration_asymptomatic"]),
            "waning_natural": 1.0 / float(natural_history["recovered_immunity_duration"]),
            "waning_vaccine": 1.0 / float(natural_history["vaccine_protection_duration"]),
            "waning_vaccine_waned": 1.0 / waned_vaccine_duration if waned_vaccine_duration > 0 else 0.0,
            "waning_maternal": 1.0 / float(natural_history.get("maternal_protection_duration", 90.0)),
        }
        rates.update(config.get("rates", {}))

        symptom_probability = _probability_array(
            [record.get("symptom_probability", 0.4) for record in age_records],
            "Age-group symptom probabilities",
        )

        config_metadata = {
            key: value
            for key, value in config.get("metadata", {}).items()
            if isinstance(value, (str, int, float, bool, np.number))
        }
        calendar = config.get("calendar", {})
        calendar_start_date = _parse_calendar_start_date(calendar)

        return cls(
            raw=config,
            analysis=analysis,
            scenario=scenario,
            vaccine_scenario=vaccine_scenario,
            resistance_scenario=resistance_scenario,
            intervention=intervention,
            age_groups=age_groups,
            population=population,
            vaccine_coverage=coverage,
            symptom_probability=symptom_probability,
            reporting_rate=reporting,
            pep_detection_rate=pep_detection,
            contact_matrix=contact_matrix,
            vaccine=vaccine,
            rates=rates,
            transmission=config["transmission"],
            treatment=config["treatment"],
            pep=config["PEP"],
            initial=config["initial_conditions"],
            immunity_model=immunity_model,
            observation_model=config.get("observation_model", {}),
            resistance=config.get("resistance", {}),
            demography=config.get("demography", {"enabled": False}),
            routine_vaccination=config.get("routine_vaccination", {"enabled": False}),
            importation=config.get("importation", {"enabled": False}),
            calendar=calendar,
            calendar_start_date=calendar_start_date,
            reporting_time_variation=config.get("reporting_time_variation", {}),
            reporting_multiplier=reporting_multiplier,
            metadata={**config_metadata, **contact_metadata, **(metadata or {})},
        )

    @property
    def total_population(self) -> float:
        return float(self.population.sum())

    @property
    def infant_age_groups(self) -> set[str]:
        return {"infant_0_2m", "infant_3_11m"}

    def reporting_rate_at(self, t: float) -> np.ndarray:
        if not self.reporting_time_variation:
            return self.reporting_rate

        start_time = float(self.reporting_time_variation.get("start_time", self.raw["simulation"]["start_time"]))
        end_time = float(self.reporting_time_variation.get("end_time", self.raw["simulation"]["end_time"]))
        start_multiplier = float(self.reporting_time_variation.get("start_multiplier", 1.0))
        end_multiplier = float(self.reporting_time_variation.get("end_multiplier", 1.0))
        if end_time <= start_time:
            multiplier = end_multiplier
        else:
            progress = np.clip((float(t) - start_time) / (end_time - start_time), 0.0, 1.0)
            multiplier = start_multiplier + progress * (end_multiplier - start_multiplier)
        return np.clip(self.reporting_rate * multiplier, 0.0, 1.0)

    def pep_detection_rate_at(self, t: float) -> np.ndarray:
        return self.pep_detection_rate

    def calendar_date_at(self, t: float) -> date | None:
        if self.calendar_start_date is None:
            return None
        start_time = float(self.raw["simulation"].get("start_time", 0.0))
        return self.calendar_start_date + timedelta(days=float(t) - start_time)

    def calendar_year_at(self, t: float) -> int | None:
        calendar_date = self.calendar_date_at(t)
        return calendar_date.year if calendar_date else None

    def calendar_day_of_year_at(self, t: float) -> float:
        calendar_date = self.calendar_date_at(t)
        if calendar_date is None:
            return float(t % 365.0)
        return float(min(calendar_date.timetuple().tm_yday, 365))


def _validate_probability_values(values: Any, label: str) -> None:
    arr = np.asarray(list(values), dtype=float)
    if not np.isfinite(arr).all() or np.any((arr < 0.0) | (arr > 1.0)):
        raise ValueError(f"{label} must be finite probabilities within [0, 1].")


def _probability_array(values: Any, label: str) -> np.ndarray:
    arr = np.asarray(list(values), dtype=float)
    if not np.isfinite(arr).all() or np.any((arr < 0.0) | (arr > 1.0)):
        raise ValueError(f"{label} must be finite probabilities within [0, 1].")
    return arr


def _parse_calendar_start_date(calendar: dict[str, Any]) -> date | None:
    if not calendar or not bool(calendar.get("enabled", False)):
        return None
    value = calendar.get("analysis_start_date", calendar.get("start_date"))
    if not value:
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    return datetime.strptime(str(value), "%Y-%m-%d").date()
