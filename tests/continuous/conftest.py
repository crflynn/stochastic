"""Continuous-time process tests."""
# flake8: noqa
import numpy as np
import pytest


# Floating point arithmetic comparison threshold
@pytest.fixture(params=[10**-10])
def threshold(request):
    return request.param

# Common
@pytest.fixture(params=[1])
def t(request):
    return request.param

@pytest.fixture(params=[16])
def n(request):
    return request.param

@pytest.fixture(params=[True, False])
def zero(request):
    return request.param

# Generate some random times for the sample_at() method
times_random = np.cumsum(np.abs(np.random.normal(size=16)))
times_random_zero = np.cumsum([0] + list(np.abs(np.random.normal(size=16))))

@pytest.fixture(params=[times_random, times_random_zero])
def times(request):
    return request.param

# Bessel
@pytest.fixture(params=[0, 1, 1.1])
def dim_fixture(request):
    return request.param

@pytest.fixture(params=[3])
def dim(request):
    return request.param

# BrownianBridge
@pytest.fixture(params=[3, 0, None])
def b(request):
    return request.param

# BrownianMotion
@pytest.fixture(params=[0, 1])
def drift(request):
    return request.param

@pytest.fixture(params=[1])
def scale(request):
    return request.param

# FractionalBrownianMotion
@pytest.fixture(params=[0.2, 0.5, 0.7])
def hurst(request):
    return request.param

# GammaProcess
@pytest.fixture(params=[1, None])
def mean_fixture(request):
    return request.param

@pytest.fixture(params=[1, None])
def scale_fixture(request):
    return request.param

@pytest.fixture(params=[1, None])
def rate_fixture(request):
    return request.param

@pytest.fixture(params=[1, None])
def variance_fixture(request):
    return request.param

@pytest.fixture(params=[1])
def mean(request):
    return request.param

@pytest.fixture(params=[1])
def variance(request):
    return request.param

# GeometricBrownianMotion
@pytest.fixture(params=[1])
def volatility(request):
    return request.param

@pytest.fixture(params=[1])
def initial(request):
    return request.param

# PoissonProcess
@pytest.fixture(params=[16, None])
def n_fixture(request):
    return request.param

@pytest.fixture(params=[1, None])
def length(request):
    return request.param

@pytest.fixture(params=[1])
def rate(request):
    return request.param
    
# MixedPoissonProcess
@pytest.fixture(params=[np.random.uniform])
def ratedist(request):
    return request.param

@pytest.fixture(params=[[1,100],[1,10]])
def ratedistparams(request):
    return request.param
    
