"""Continuous-time process tests."""
# flake8: noqa
import numpy as np
import pytest


# Floating point arithmetic comparison threshold
@pytest.fixture(params=[np.array([[0,1,2,3,4,5,6],[0,0.5,0.75,0,0,0,0],[0,10,20,50,100,0,0]]).T])
def AllReal2D(request):
    return request.param
