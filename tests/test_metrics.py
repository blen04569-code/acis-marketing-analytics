import numpy as np
import pandas as pd


def calculate_pure_premium(
    total_loss: float, total_exposure_years: float
) -> float:
    if total_exposure_years <= 0:
        return 0.0
    return total_loss / total_exposure_years


def test_pure_premium_calculation():
    # Test typical portfolio baseline
    assert calculate_pure_premium(500000, 1000) == 500.0
    # Test zero exposure safety limit
    assert calculate_pure_premium(15000, 0) == 0.0