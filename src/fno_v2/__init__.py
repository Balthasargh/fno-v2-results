"""
FNO v2 Results – Analysis toolkit for Fourier Neural Operator experiments.
"""
from .loader import (
    load_all,
    load_config,
    load_models_table,
    load_comparisons,
    load_points_test,
    load_next_draw,
    load_distributions,
)
from .analysis import (
    rank_models,
    significant_wins,
    mean_nll_by_model,
    expected_value_from_dist,
    entropy,
)

__version__ = "0.2.0"
__all__ = [
    "load_all",
    "load_config",
    "load_models_table",
    "load_comparisons",
    "load_points_test",
    "load_next_draw",
    "load_distributions",
    "rank_models",
    "significant_wins",
    "mean_nll_by_model",
    "expected_value_from_dist",
    "entropy",
]
