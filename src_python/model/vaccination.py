from __future__ import annotations

import numpy as np


def vaccinated_infection_share(susceptible: np.ndarray, vaccinated: np.ndarray, ve_sus: float) -> np.ndarray:
    effective_vaccinated = np.maximum(vaccinated, 0.0) * max(0.0, 1.0 - ve_sus)
    effective_total = np.maximum(susceptible, 0.0) + effective_vaccinated
    return np.divide(
        effective_vaccinated,
        effective_total,
        out=np.zeros_like(effective_total, dtype=float),
        where=effective_total > 0,
    )


def symptomatic_probability(
    base_probability: np.ndarray,
    infection_from_susceptible: np.ndarray,
    infection_from_vaccinated: np.ndarray,
    ve_sym: float,
) -> np.ndarray:
    unvaccinated_sym = np.clip(base_probability, 0.0, 1.0)
    vaccinated_sym = np.clip(base_probability * (1.0 - ve_sym), 0.0, 1.0)
    total = infection_from_susceptible + infection_from_vaccinated
    weighted = infection_from_susceptible * unvaccinated_sym + infection_from_vaccinated * vaccinated_sym
    fallback = 0.5 * (unvaccinated_sym + vaccinated_sym)
    return np.divide(weighted, total, out=fallback.copy(), where=total > 0)


def infectiousness_multiplier(vaccine_origin_share: np.ndarray, ve_inf: float) -> np.ndarray:
    return np.clip(1.0 - vaccine_origin_share * ve_inf, 0.0, 1.0)


def recovery_rate_multiplier(vaccine_origin_share: np.ndarray, ve_dur: float) -> np.ndarray:
    duration_multiplier = np.clip(1.0 - vaccine_origin_share * ve_dur, 0.05, None)
    return 1.0 / duration_multiplier
