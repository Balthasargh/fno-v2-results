"""
Loader for FNO v2 experiment results.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

_PKG_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_DATA_DIR = _PKG_ROOT / "results"


def _resolve(data_dir: str | Path | None) -> Path:
    return Path(data_dir) if data_dir is not None else DEFAULT_DATA_DIR


def load_config(data_dir: str | Path | None = None) -> dict[str, Any]:
    """Load experiment configuration and best hyperparameters."""
    path = _resolve(data_dir) / "config.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_models_table(data_dir: str | Path | None = None) -> pd.DataFrame:
    """Load model comparison table (NLL, RPS, MAE, top5_hit)."""
    return pd.read_csv(_resolve(data_dir) / "tableau_modeles.csv")


def load_comparisons(data_dir: str | Path | None = None) -> pd.DataFrame:
    """Load statistical comparisons versus baselines."""
    return pd.read_csv(_resolve(data_dir) / "comparaisons.csv")


def load_points_test(data_dir: str | Path | None = None) -> pd.DataFrame:
    """Load per-point NLL on the test set."""
    return pd.read_csv(_resolve(data_dir) / "points_test.csv")


def load_next_draw(data_dir: str | Path | None = None) -> pd.DataFrame:
    """Load next-draw summary statistics."""
    return pd.read_csv(_resolve(data_dir) / "prochain_tirage.csv")


def load_distributions(data_dir: str | Path | None = None) -> pd.DataFrame:
    """Load full probability distributions for the next draw."""
    return pd.read_csv(
        _resolve(data_dir) / "prochain_tirage_distributions.csv",
        index_col=0,
    )


def load_all(data_dir: str | Path | None = None) -> dict[str, Any]:
    """Load every result file into a dictionary."""
    return {
        "config": load_config(data_dir),
        "models": load_models_table(data_dir),
        "comparisons": load_comparisons(data_dir),
        "points_test": load_points_test(data_dir),
        "next_draw": load_next_draw(data_dir),
        "distributions": load_distributions(data_dir),
    }
