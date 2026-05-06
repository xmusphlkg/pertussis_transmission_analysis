from __future__ import annotations

from dataclasses import dataclass, field
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
        if np.any(population <= 0.0):
            raise ValueError("Age-group populations must be positive.")
        vaccine_config = _require_config_value(config, "vaccine", context="model config")
        vaccine = {key: float(vaccine_config[key]) for key in ("VE_sus", "VE_sym", "VE_inf", "VE_dur")}
        _require_probability_values("vaccine efficacy", np.array(list(vaccine.values()), dtype=float))

        coverage = np.array([record["vaccine_coverage"] for record in age_records], dtype=float)
        _require_probability_values("vaccine coverage", coverage)
        if sum(vaccine.values()) == 0:
            coverage = np.zeros_like(coverage)

        reporting_multiplier = float(_require_config_value(config, "reporting_multiplier", context="model config"))
        if not np.isfinite(reporting_multiplier) or reporting_multiplier < 0.0:
            raise ValueError("reporting_multiplier must be finite and non-negative.")
        reporting = np.array([record["reporting_rate"] for record in age_records], dtype=float)
        _require_probability_values("reporting rate", reporting)
        reporting = np.clip(reporting * reporting_multiplier, 0.0, 1.0)

        rows = config["contact_matrix"]["rows"]
        contact_matrix = np.array(rows, dtype=float)
        if contact_matrix.shape != (len(age_groups), len(age_groups)):
            raise ValueError("Contact matrix dimensions must match age groups.")
        if np.any(contact_matrix < 0.0):
            raise ValueError("Contact matrix entries must be non-negative.")
        contact_metadata = {}
        correction = config["contact_matrix"]["reciprocity_correction"]
        if bool(correction["enabled"]):
            before = reciprocity_error(contact_matrix, population)
            contact_matrix = balance_reciprocity(contact_matrix, population)
            after = reciprocity_error(contact_matrix, population)
            tolerance = float(correction["tolerance"])
            if after > tolerance:
                raise ValueError(
                    f"Contact reciprocity correction failed tolerance: after={after:.6g}, tolerance={tolerance:.6g}."
                )
            contact_metadata = {
                "contact_reciprocity_error_before": before,
                "contact_reciprocity_error_after": after,
                "contact_reciprocity_tolerance": tolerance,
            }

        natural_history = config["natural_history"]
        _require_positive_values(
            "natural history durations",
            np.array(
                [
                    natural_history["latent_duration"],
                    natural_history["infectious_duration_symptomatic"],
                    natural_history["infectious_duration_asymptomatic"],
                    natural_history["recovered_immunity_duration"],
                    natural_history["vaccine_protection_duration"],
                ],
                dtype=float,
            ),
        )
        immunity_model = config["immunity_model"]
        waned_vaccine_duration = float(immunity_model["waned_vaccine_duration"])
        _require_positive_values("waned vaccine duration", np.array([waned_vaccine_duration], dtype=float))
        _validate_immunity_model(immunity_model, age_groups)
        rates = {
            "latent": 1.0 / float(natural_history["latent_duration"]),
            "recovery_symptomatic": 1.0 / float(natural_history["infectious_duration_symptomatic"]),
            "recovery_asymptomatic": 1.0 / float(natural_history["infectious_duration_asymptomatic"]),
            "waning_natural": 1.0 / float(natural_history["recovered_immunity_duration"]),
            "waning_vaccine": 1.0 / float(natural_history["vaccine_protection_duration"]),
            "waning_vaccine_waned": 1.0 / waned_vaccine_duration if waned_vaccine_duration > 0 else 0.0,
        }
        rates.update(config.get("rates", {}))
        _require_nonnegative_values("transition rates", np.array(list(rates.values()), dtype=float))
        _require_nonnegative_values(
            "transmission parameters",
            np.array(
                [
                    config["transmission"]["beta_S"],
                    config["transmission"]["seasonal_amplitude"],
                    config["transmission"]["multi_year_amplitude"],
                ],
                dtype=float,
            ),
        )
        _validate_transmission(config["transmission"])
        _validate_treatment(config["treatment"])
        _validate_pep(config["PEP"])
        _validate_initial_conditions(config["initial_conditions"])
        _validate_importation(config["importation"], age_groups)
        _validate_demography(config["demography"])
        _validate_routine_vaccination(config["routine_vaccination"])

        symptom_probability = np.array(
            [record["symptom_probability"] for record in age_records],
            dtype=float,
        )
        _require_probability_values("symptom probability", symptom_probability)

        config_metadata = {
            key: value
            for key, value in config["metadata"].items()
            if isinstance(value, (str, int, float, bool, np.number))
        }

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
            immunity_model=immunity_model,
            observation_model=config["observation_model"],
            resistance=config["resistance"],
            demography=config["demography"],
            routine_vaccination=config["routine_vaccination"],
            importation=config["importation"],
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

        start_time = float(self.reporting_time_variation["start_time"])
        end_time = float(self.reporting_time_variation["end_time"])
        start_multiplier = float(self.reporting_time_variation["start_multiplier"])
        end_multiplier = float(self.reporting_time_variation["end_multiplier"])
        if end_time <= start_time:
            multiplier = end_multiplier
        else:
            progress = np.clip((float(t) - start_time) / (end_time - start_time), 0.0, 1.0)
            multiplier = start_multiplier + progress * (end_multiplier - start_multiplier)
        return np.clip(self.reporting_rate * multiplier, 0.0, 1.0)

    def observation_probabilities_at(self, t: float) -> dict[str, np.ndarray]:
        """Return age-specific observation cascade probabilities at time t.

        When no explicit split is supplied, `reporting_rate` remains the final
        symptomatic-case reporting probability for backward-compatible runs.
        """

        final_reporting = self.reporting_rate_at(t)
        ones = np.ones_like(final_reporting)
        care = self._observation_component(
            ("care_seeking_rate", "care_seeking_probability", "symptomatic_to_care_probability"),
            reference=ones,
        )
        testing = self._observation_component(
            ("testing_rate", "testing_probability", "care_to_test_probability"),
            reference=ones,
        )
        test_reporting = self._observation_component(
            ("test_reporting_rate", "test_reporting_probability", "test_to_report_probability"),
            reference=final_reporting,
        )
        reported = np.clip(care * testing * test_reporting, 0.0, 1.0)
        return {
            "care": care,
            "testing": testing,
            "test_reporting": test_reporting,
            "reported": reported,
        }

    def _observation_component(self, names: tuple[str, ...], *, reference: np.ndarray) -> np.ndarray:
        components = self.observation_model.get("components", {})
        raw = None
        for name in names:
            if name in self.observation_model:
                raw = self.observation_model[name]
                break
            if isinstance(components, dict) and name in components:
                raw = components[name]
                break
        if raw is None:
            return np.clip(np.asarray(reference, dtype=float), 0.0, 1.0)
        if isinstance(raw, dict):
            missing = [age for age in self.age_groups if age not in raw]
            if missing:
                raise ValueError(f"Observation component is missing age groups: {missing}")
            values = np.array([float(raw[age]) for age in self.age_groups], dtype=float)
        elif isinstance(raw, (list, tuple, np.ndarray)):
            values = np.asarray(raw, dtype=float)
            if values.size != len(self.age_groups):
                raise ValueError("Observation component arrays must match age group count.")
        else:
            values = np.repeat(float(raw), len(self.age_groups))
        return np.clip(values, 0.0, 1.0)


def _require_probability_values(name: str, values: np.ndarray) -> None:
    if not np.isfinite(values).all() or np.any((values < 0.0) | (values > 1.0)):
        raise ValueError(f"{name} values must be finite probabilities in [0, 1].")


def _require_config_value(mapping: dict[str, Any], key: str, *, context: str) -> Any:
    if key not in mapping or mapping[key] in (None, ""):
        raise ValueError(f"{context} must define {key!r}.")
    return mapping[key]


def _require_positive_values(name: str, values: np.ndarray) -> None:
    if not np.isfinite(values).all() or np.any(values <= 0.0):
        raise ValueError(f"{name} must be finite positive values.")


def _require_nonnegative_values(name: str, values: np.ndarray) -> None:
    if not np.isfinite(values).all() or np.any(values < 0.0):
        raise ValueError(f"{name} must be finite non-negative values.")


def _validate_transmission(transmission: dict[str, Any]) -> None:
    _require_probability_values(
        "seasonal transmission amplitude",
        np.array(
            [
                transmission["seasonal_amplitude"],
                transmission["multi_year_amplitude"],
            ],
            dtype=float,
        ),
    )
    _require_nonnegative_values(
        "transmission multipliers",
        np.array(
            [
                transmission["fitness_R"],
                transmission["relative_infectiousness_asymptomatic"],
                transmission["multi_year_period_years"],
            ],
            dtype=float,
        ),
    )


def _validate_treatment(treatment: dict[str, Any]) -> None:
    _require_nonnegative_values(
        "treatment rates",
        np.array(
            [
                treatment["treatment_rate_symptomatic"],
                treatment["treatment_rate_asymptomatic"],
            ],
            dtype=float,
        ),
    )
    for strain_key in ("sensitive", "resistant"):
        if strain_key not in treatment:
            raise ValueError(f"Missing treatment configuration for {strain_key}.")
        _require_range_values(
            f"{strain_key} treatment reductions",
            np.array(
                [
                    treatment[strain_key]["infectious_duration_reduction"],
                    treatment[strain_key]["infectiousness_reduction"],
                ],
                dtype=float,
            ),
            low=0.0,
            high=0.95,
        )


def _validate_pep(pep: dict[str, Any]) -> None:
    _require_probability_values(
        "PEP probabilities",
        np.array(
            [
                pep["coverage_household_contacts"],
                pep["effectiveness_sensitive"],
                pep["effectiveness_resistant"],
            ],
            dtype=float,
        ),
    )
    _require_positive_values("PEP activation prevalence", np.array([pep["activation_prevalence"]], dtype=float))


def _validate_initial_conditions(initial: dict[str, Any]) -> None:
    _require_nonnegative_values(
        "initial infection seeds",
        np.array(
            [
                initial["initial_exposed_per_100k"],
                initial["initial_infectious_per_100k"],
            ],
            dtype=float,
        ),
    )
    _require_probability_values(
        "initial resistance prevalence",
        np.array([initial["initial_resistance_prevalence"]], dtype=float),
    )
    seed_distribution = initial["seed_age_distribution"]
    _require_nonnegative_values("seed age distribution", np.array(list(seed_distribution.values()), dtype=float))


def _validate_importation(importation: dict[str, Any], age_groups: tuple[str, ...]) -> None:
    if "enabled" not in importation:
        raise ValueError("importation must define 'enabled'.")
    _require_nonnegative_values(
        "importation rate",
        np.array([importation["rate_per_100k_per_year"]], dtype=float),
    )
    _require_probability_values(
        "importation resistant fraction",
        np.array([importation["resistant_fraction"]], dtype=float),
    )
    age_distribution = importation["age_distribution"]
    missing = [age for age in age_groups if age not in age_distribution]
    if missing:
        raise ValueError(f"Importation age distribution is missing age groups: {missing}")
    _require_nonnegative_values(
        "importation age distribution",
        np.array([age_distribution[age] for age in age_groups], dtype=float),
    )


def _validate_demography(demography: dict[str, Any]) -> None:
    if "enabled" not in demography:
        raise ValueError("demography must define 'enabled'.")
    if not bool(demography["enabled"]):
        return
    durations = demography["age_bin_durations_years"]
    _require_positive_values("demography age-bin durations", np.array(list(durations.values()), dtype=float))
    birth_entry = demography["birth_entry"]
    _require_nonnegative_values("demography birth-entry weights", np.array(list(birth_entry.values()), dtype=float))


def _validate_routine_vaccination(routine_vaccination: dict[str, Any]) -> None:
    if "enabled" not in routine_vaccination:
        raise ValueError("routine_vaccination must define 'enabled'.")
    if not bool(routine_vaccination["enabled"]):
        return
    _require_nonnegative_values(
        "routine vaccination relaxation rate",
        np.array([routine_vaccination["target_relaxation_rate_per_year"]], dtype=float),
    )


def _validate_immunity_model(immunity_model: dict[str, Any], age_groups: tuple[str, ...]) -> None:
    _require_probability_values(
        "waned relative vaccine effect",
        np.array([immunity_model["waned_relative_effect"]], dtype=float),
    )
    _require_probability_values(
        "initial recent vaccine fraction",
        np.array([immunity_model["initial_recent_fraction"]], dtype=float),
    )
    by_age = immunity_model["initial_recent_fraction_by_age"]
    missing = [age for age in age_groups if age not in by_age]
    if missing:
        raise ValueError(f"Age-specific initial recent vaccine fractions are missing age groups: {missing}")
    _require_probability_values(
        "age-specific initial recent vaccine fractions",
        np.array([by_age[age] for age in age_groups], dtype=float),
    )


def _require_range_values(name: str, values: np.ndarray, *, low: float, high: float) -> None:
    if not np.isfinite(values).all() or np.any((values < low) | (values > high)):
        raise ValueError(f"{name} values must be finite and within [{low}, {high}].")
