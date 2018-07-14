"""Test Estimation."""
# flake8: noqa
import pytest
import numpy as np
from stochastic.analysis import NHPPLeemisEst

def test_NHPPLeemisEst(AllReal2D):
    AllEventsT, GammaEstNoNan =  NHPPLeemisEst(AllReal2D)
    assert isinstance(AllEventsT, np.ndarray)
    assert isinstance(GammaEstNoNan, np.ndarray)
    assert len(GammaEstNoNan)==len(AllEventsT)
    