"""
Loader for FNO v2 experiment results.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

# Default data directory (relative to project root)
DEFAULT_DATA_DIR = Path(__file__).resolve().parent.parent / "results"


def load_config(data_dir: str | Path | None = None) -> dict[str, Any]:
    """Load experiment configuration and best hyperparameters."""
    data_dir = Path(data_dir or DEFAULT_DATA_DIR)
    with open(data_dir / "config.json", encoding="utf-8") as f:
        return json.load(f)


def load_models_table(data_dir: str | Path | None = None) -> pd.DataFrame:
    """Load model comparison table (NLL, RPS, MAE, top5_hit)."""
    data_dir = Path(data_dir or DEFAULT_DATA_DIR)
    return pd.read_csv(data_dir / "tableau_modeles.csv")


def load_comparisons(data_dir: str | Path | None = None) -> pd.DataFrame:
    """Load statistical comparisons vs baselines."""
    data_dir = Path(data_dir or DEFAULT_DATA_DIR)
    return pd.read_csv(data_dir / "comparaisons.csv")


def load_points_test(data_dir: str | Path | None = None) -> pd.DataFrame:
    """Load per-point NLL on the test set."""
    data_dir = Path(data_dir or DEFAULT_DATA_DIR)
    return pd.read_csv(data_dir / "points_test.csv")


def load_next_draw(data_dir: str | Path | None = None) -> pd.DataFrame:
    """Load next-draw summary statistics."""
    data_dir = Path(data_dir or DEFAULT_DATA_DIR)
    return pd.read_csv(data_dir / "prochain_tirage.csv")


def load_distributions(data_dir: str | Path | None = None) -> pd.DataFrame:
    """Load full probability distributions for the next draw (rows = columns, cols = values 1..50)."""
    data_dir = Path(data_dir or DEFAULT_DATA_DIR)
    return pd.read_csv(data_dir / "prochain_tirage_distributions.csv", index_col=0)


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
