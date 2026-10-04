"""
Analysis helpers for FNO v2 results.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def rank_models(
    models: pd.DataFrame,
    metric: str = "NLL",
    ascending: bool = True,
) -> pd.DataFrame:
    """Return models ranked by a given metric."""
    df = models.copy()
    df = df.sort_values(metric, ascending=ascending).reset_index(drop=True)
    df["rank"] = np.arange(1, len(df) + 1)
    return df


def significant_wins(
    comparisons: pd.DataFrame,
    alpha: float = 0.05,
) -> pd.DataFrame:
    """
    Filter comparisons where FNO is significantly better
    (negative delta + p_fdr < alpha).
    """
    df = comparisons.copy()
    mask = (df["delta"] < 0) & (df["p_fdr"] < alpha)
    return df.loc[mask].sort_values("p_fdr")


def mean_nll_by_model(points: pd.DataFrame) -> pd.Series:
    """Compute mean NLL per model from the points_test table."""
    nll_cols = [c for c in points.columns if c.startswith("nll_")]
    return points[nll_cols].mean().sort_values()


def nll_by_fold(points: pd.DataFrame) -> pd.DataFrame:
    """Mean NLL per model and fold."""
    nll_cols = [c for c in points.columns if c.startswith("nll_")]
    return points.groupby("pli")[nll_cols].mean()


def nll_by_column(points: pd.DataFrame) -> pd.DataFrame:
    """Mean NLL per model and column (feature)."""
    nll_cols = [c for c in points.columns if c.startswith("nll_")]
    return points.groupby("colonne")[nll_cols].mean()


def expected_value_from_dist(dist_row: pd.Series) -> float:
    """Compute expectation from a probability distribution over 1..N."""
    values = np.arange(1, len(dist_row) + 1)
    return float(np.sum(values * dist_row.values))


def entropy(dist_row: pd.Series) -> float:
    """Shannon entropy of a discrete distribution."""
    p = dist_row.values.astype(float)
    p = p[p > 0]
    return float(-np.sum(p * np.log(p)))


def summary_report(
    models: pd.DataFrame,
    comparisons: pd.DataFrame,
    points: pd.DataFrame,
    alpha: float = 0.05,
) -> str:
    """Generate a short text summary of the main findings."""
    ranked = rank_models(models, "NLL")
    best = ranked.iloc[0]
    wins = significant_wins(comparisons, alpha=alpha)
    mean_nll = mean_nll_by_model(points)

    lines = [
        "=== FNO v2 – Summary ===",
        f"Best model by NLL : {best['modele']} ({best['NLL']:.4f})",
        f"Significant wins  : {len(wins)} (FDR < {alpha})",
        "",
        "Mean NLL on test set:",
    ]
    for name, val in mean_nll.items():
        lines.append(f"  {name:<28} {val:.4f}")
    return "\n".join(lines)
