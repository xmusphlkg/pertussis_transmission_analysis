from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np


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
    contact_matrix: np.ndarray
    vaccine: dict[str, float]
    rates: dict[str, float]
    transmission: dict[str, float]
    treatment: dict[str, Any]
    pep: dict[str, float]
    initial: dict[str, Any]
    demography: dict[str, Any]
    routine_vaccination: dict[str, Any]
    importation: dict[str, Any]
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
        vaccine = {key: float(value) for key, value in config.get("vaccine", {}).items() if key.startswith("VE_")}
        if not vaccine:
            vaccine = {"VE_sus": 0.0, "VE_sym": 0.0, "VE_inf": 0.0, "VE_dur": 0.0}

        coverage = np.array([record.get("vaccine_coverage", 0.0) for record in age_records], dtype=float)
        if sum(vaccine.values()) == 0:
            coverage = np.zeros_like(coverage)

        reporting_multiplier = float(config.get("reporting_multiplier", 1.0))
        reporting = np.array([record.get("reporting_rate", 0.0) for record in age_records], dtype=float)
        reporting = np.clip(reporting * reporting_multiplier, 0.0, 1.0)

        rows = config["contact_matrix"]["rows"]
        contact_matrix = np.array(rows, dtype=float)
        if contact_matrix.shape != (len(age_groups), len(age_groups)):
            raise ValueError("Contact matrix dimensions must match age groups.")

        natural_history = config["natural_history"]
        rates = {
            "latent": 1.0 / float(natural_history["latent_duration"]),
            "recovery_symptomatic": 1.0 / float(natural_history["infectious_duration_symptomatic"]),
            "recovery_asymptomatic": 1.0 / float(natural_history["infectious_duration_asymptomatic"]),
            "waning_natural": 1.0 / float(natural_history["recovered_immunity_duration"]),
            "waning_vaccine": 1.0 / float(natural_history["vaccine_protection_duration"]),
        }
        rates.update(config.get("rates", {}))

        symptom_probability = np.array(
            [record.get("symptom_probability", 0.4) for record in age_records],
            dtype=float,
        )

        return cls(
            raw=config,
            analysis=analysis,
            scenario=scenario,
            vaccine_scenario=vaccine_scenario,
            resistance_scenario=resistance_scenario,
            intervention=intervention,
            age_groups=age_groups,
            population=population,
            vaccine_coverage=np.clip(coverage, 0.0, 1.0),
            symptom_probability=np.clip(symptom_probability, 0.0, 1.0),
            reporting_rate=reporting,
            contact_matrix=contact_matrix,
            vaccine=vaccine,
            rates=rates,
            transmission=config["transmission"],
            treatment=config["treatment"],
            pep=config["PEP"],
            initial=config["initial_conditions"],
            demography=config.get("demography", {"enabled": False}),
            routine_vaccination=config.get("routine_vaccination", {"enabled": False}),
            importation=config.get("importation", {"enabled": False}),
            reporting_time_variation=config.get("reporting_time_variation", {}),
            reporting_multiplier=reporting_multiplier,
            metadata=metadata or {},
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
