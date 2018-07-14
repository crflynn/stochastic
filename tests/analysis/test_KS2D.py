"""Test Estimation."""
# flake8: noqa
import pytest
import numpy as np
from stochastic.analysis import ks2d1s
from stochastic.analysis import ks2d2s




def test_ks2d1s(points2d,distarr2d,distfunc2d):
    # with pytest.raises(AttributeError):
    # ks2d1s(points2d,distarr2d)
    ks2d1s(points2d,distfunc2d)
