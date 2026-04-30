from __future__ import annotations

from dataclasses import dataclass

import numpy as np


COMPARTMENTS: tuple[str, ...] = (
    "S",
    "V",
    "E_S",
    "E_R",
    "I_S_sym",
    "I_S_asym",
    "I_R_sym",
    "I_R_asym",
    "T_S",
    "T_R",
    "R",
)


@dataclass(frozen=True)
class StateIndex:
    age_groups: tuple[str, ...]

    @property
    def n_age(self) -> int:
        return len(self.age_groups)

    @property
    def n_compartments(self) -> int:
        return len(COMPARTMENTS)

    @property
    def size(self) -> int:
        return self.n_age * self.n_compartments

    def index(self, age: int | str, compartment: str) -> int:
        age_idx = self.age_groups.index(age) if isinstance(age, str) else age
        comp_idx = COMPARTMENTS.index(compartment)
        return age_idx * self.n_compartments + comp_idx

    def reshape(self, y: np.ndarray) -> np.ndarray:
        return np.asarray(y, dtype=float).reshape((self.n_age, self.n_compartments))

    def flatten(self, state: np.ndarray) -> np.ndarray:
        return np.asarray(state, dtype=float).reshape(self.size)

    def compartment(self, state: np.ndarray, name: str) -> np.ndarray:
        return self.reshape(state)[:, COMPARTMENTS.index(name)]
