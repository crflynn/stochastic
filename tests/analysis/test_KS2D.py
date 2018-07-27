"""Test Estimation."""
# flake8: noqa
import pytest
import numpy as np
from stochastic.analysis import ks2d1s
from stochastic.analysis import ks2d2s

def test_ks2d1s(points2d,distarr2d,distfunc2d):
    # with pytest.raises(AttributeError):
    # ks2d1s(points2d,distarr2d)
    d,prob=ks2d1s(points2d,distfunc2d)
    assert isinstance(d, float)
    assert 0.<=d<=1.
    assert isinstance(prob, float)
    assert 0.<=prob<=1.

def test_ks2d2s(points2d):
    d,prob=ks2d2s(points2d,-points2d)
    assert isinstance(d, float)
    assert 0.<=d<=1.
    assert isinstance(prob, float)
    assert 0.<=prob<=1.
