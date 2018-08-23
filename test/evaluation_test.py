import sys
import os
import numpy as np
from pytest import approx
sys.path.append(os.path.join('..', 'src'))
sys.path.append(os.path.join('src'))
import evaluation


def test_calculates_nwrmsle_for_perfect_match():
    estimate = np.array([1, 2, 3])
    actual = np.array([1, 2, 3])
    weights = np.array([1, 1, 1])
    calculated_nwrmsle = evaluation.nwrmsle(estimate, actual, weights)

    assert calculated_nwrmsle == 0.0


def test_calculates_nwrmsle_for_imperfect_match():
    estimate = np.array([0, 0, 0])
    actual = np.array([1, 1, 1])
    weights = np.array([1, 1, 1])
    calculated_nwrmsle = evaluation.nwrmsle(estimate, actual, weights)

    # Assert by-hand calculation of nwrmsle is reasonably close to python calculation
    assert approx(calculated_nwrmsle, 0.69314718)
