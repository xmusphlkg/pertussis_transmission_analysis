from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

import pandas as pd
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def project_path(*parts: str | Path) -> Path:
    return PROJECT_ROOT.joinpath(*map(Path, parts))


def load_yaml(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    return data or {}


def deep_update(base: dict[str, Any], updates: dict[str, Any] | None) -> dict[str, Any]:
    out = deepcopy(base)
    if not updates:
        return out
    for key, value in updates.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = deep_update(out[key], value)
        else:
            out[key] = deepcopy(value)
    return out


def set_by_dotted_path(config: dict[str, Any], path: str, value: Any) -> None:
    node = config
    parts = path.split(".")
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = value


def ensure_output_dirs() -> None:
    for relative in [
        "outputs/simulations",
        "outputs/summaries",
        "outputs/figures",
        "outputs/tables",
        "outputs/metadata",
        "manuscript_notes",
    ]:
        project_path(relative).mkdir(parents=True, exist_ok=True)


def write_dataframe(df: pd.DataFrame, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".parquet":
        df.to_parquet(path, index=False)
        df.to_csv(path.with_suffix(".csv"), index=False)
        return
    if path.suffix == ".csv":
        df.to_csv(path, index=False)
        try:
            df.to_parquet(path.with_suffix(".parquet"), index=False)
        except Exception:
            pass
        return
    raise ValueError(f"Unsupported output suffix for {path}")


def read_table(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if path.suffix == ".parquet" and path.exists():
        return pd.read_parquet(path)
    if path.exists():
        return pd.read_csv(path)
    csv_path = path.with_suffix(".csv")
    if csv_path.exists():
        return pd.read_csv(csv_path)
    raise FileNotFoundError(path)
