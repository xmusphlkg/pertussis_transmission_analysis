from __future__ import annotations

import numpy as np


def vaccine_susceptibility(ve_sus: float, *, relative_effect: float = 1.0) -> float:
    return max(0.0, 1.0 - max(0.0, relative_effect) * ve_sus)


def origin_relative_effect(origin: str, *, waned_relative_effect: float = 0.35) -> float:
    if origin == "recent":
        return 1.0
    if origin == "waned":
        return float(np.clip(waned_relative_effect, 0.0, 1.0))
    return 0.0


def origin_symptomatic_probability(
    base_probability: np.ndarray,
    ve_sym: float,
    origin: str,
    *,
    waned_relative_effect: float = 0.35,
) -> np.ndarray:
    effect = origin_relative_effect(origin, waned_relative_effect=waned_relative_effect)
    return np.clip(np.asarray(base_probability, dtype=float) * (1.0 - ve_sym * effect), 0.0, 1.0)


def origin_infectiousness_multiplier(
    ve_inf: float,
    origin: str,
    *,
    waned_relative_effect: float = 0.35,
) -> float:
    effect = origin_relative_effect(origin, waned_relative_effect=waned_relative_effect)
    return float(np.clip(1.0 - ve_inf * effect, 0.0, 1.0))


def origin_recovery_rate_multiplier(
    ve_dur: float,
    origin: str,
    *,
    waned_relative_effect: float = 0.35,
) -> float:
    effect = origin_relative_effect(origin, waned_relative_effect=waned_relative_effect)
    duration_multiplier = max(0.05, 1.0 - ve_dur * effect)
    return 1.0 / duration_multiplier


def vaccinated_infection_share(
    susceptible: np.ndarray,
    vaccinated_recent: np.ndarray,
    ve_sus: float,
    vaccinated_waned: np.ndarray | None = None,
    *,
    waned_relative_effect: float = 0.35,
) -> np.ndarray:
    recent = np.maximum(vaccinated_recent, 0.0) * vaccine_susceptibility(ve_sus)
    if vaccinated_waned is None:
        effective_waned = np.zeros_like(recent, dtype=float)
        protected_waned = effective_waned
    else:
        effective_waned = np.maximum(vaccinated_waned, 0.0) * vaccine_susceptibility(
            ve_sus,
            relative_effect=waned_relative_effect,
        )
        protected_waned = effective_waned * np.clip(waned_relative_effect, 0.0, 1.0)
    effective_total = np.maximum(susceptible, 0.0) + recent + effective_waned
    protected_equivalent = recent + protected_waned
    return np.divide(
        protected_equivalent,
        effective_total,
        out=np.zeros_like(effective_total, dtype=float),
        where=effective_total > 0,
    )


def symptomatic_probability(
    base_probability: np.ndarray,
    infection_from_susceptible: np.ndarray,
    infection_from_vaccinated: np.ndarray,
    ve_sym: float,
    infection_from_waned: np.ndarray | None = None,
    *,
    waned_relative_effect: float = 0.35,
) -> np.ndarray:
    unvaccinated_sym = np.clip(base_probability, 0.0, 1.0)
    vaccinated_sym = np.clip(base_probability * (1.0 - ve_sym), 0.0, 1.0)
    if infection_from_waned is None:
        total = infection_from_susceptible + infection_from_vaccinated
        weighted = infection_from_susceptible * unvaccinated_sym + infection_from_vaccinated * vaccinated_sym
    else:
        waned_effect = np.clip(waned_relative_effect, 0.0, 1.0)
        waned_sym = np.clip(base_probability * (1.0 - ve_sym * waned_effect), 0.0, 1.0)
        total = infection_from_susceptible + infection_from_vaccinated + infection_from_waned
        weighted = (
            infection_from_susceptible * unvaccinated_sym
            + infection_from_vaccinated * vaccinated_sym
            + infection_from_waned * waned_sym
        )
    zero_exposure_estimate = 0.5 * (unvaccinated_sym + vaccinated_sym)
    return np.divide(weighted, total, out=zero_exposure_estimate.copy(), where=total > 0)


def infectiousness_multiplier(vaccine_origin_share: np.ndarray, ve_inf: float) -> np.ndarray:
    return np.clip(1.0 - vaccine_origin_share * ve_inf, 0.0, 1.0)


def recovery_rate_multiplier(vaccine_origin_share: np.ndarray, ve_dur: float) -> np.ndarray:
    duration_multiplier = np.clip(1.0 - vaccine_origin_share * ve_dur, 0.05, None)
    return 1.0 / duration_multiplier
