"""Tests for analysis helpers."""
from __future__ import annotations

from pathlib import Path

from fno_v2 import (
    load_models_table,
    load_comparisons,
    load_points_test,
    rank_models,
    significant_wins,
    mean_nll_by_model,
)

DATA = Path(__file__).resolve().parent.parent / "results"


def test_rank_models():
    models = load_models_table(DATA)
    ranked = rank_models(models, metric="NLL")
    assert ranked.iloc[0]["rank"] == 1
    assert ranked["NLL"].is_monotonic_increasing


def test_significant_wins():
    comps = load_comparisons(DATA)
    wins = significant_wins(comps, alpha=0.05)
    assert "p_fdr" in wins.columns
    if not wins.empty:
        assert (wins["p_fdr"] < 0.05).all()
        assert (wins["delta"] < 0).all()


def test_mean_nll_by_model():
    points = load_points_test(DATA)
    means = mean_nll_by_model(points)
    assert len(means) >= 5
