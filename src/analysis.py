"""
Analysis helpers for FNO v2 results.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def rank_models(models: pd.DataFrame, metric: str = "NLL", ascending: bool = True) -> pd.DataFrame:
    """Return models ranked by a given metric."""
    df = models.copy()
    df = df.sort_values(metric, ascending=ascending).reset_index(drop=True)
    df["rank"] = np.arange(1, len(df) + 1)
    return df


def significant_wins(comparisons: pd.DataFrame, alpha: float = 0.05) -> pd.DataFrame:
    """
    Filter comparisons where FNO is significantly better (negative delta + p_fdr < alpha).
    Assumes delta = FNO - baseline (negative means FNO better for NLL/RPS).
    """
    df = comparisons.copy()
    mask = (df["delta"] < 0) & (df["p_fdr"] < alpha)
    return df.loc[mask].sort_values("p_fdr")


def mean_nll_by_model(points: pd.DataFrame) -> pd.Series:
    """Compute mean NLL per model from the points_test table."""
    nll_cols = [c for c in points.columns if c.startswith("nll_")]
    return points[nll_cols].mean().sort_values()


def expected_value_from_dist(dist_row: pd.Series) -> float:
    """Compute expectation from a probability distribution over 1..50."""
    values = np.arange(1, len(dist_row) + 1)
    return float(np.sum(values * dist_row.values))


def entropy(dist_row: pd.Series) -> float:
    """Shannon entropy of a discrete distribution."""
    p = dist_row.values
    p = p[p > 0]
    return float(-np.sum(p * np.log(p)))
