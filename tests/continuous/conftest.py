"""Continuous-time process tests."""
# flake8: noqa
import math

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

# InverseGaussianProcess
def mean_func_monotonic(t):
    return t

def mean_func_not_monotonic(t):
    return 1

def mean_func_no_args():
    return 1

@pytest.fixture(params=[mean_func_monotonic, None])
def mean_func(request):
    return request.param

@pytest.fixture(params=[mean_func_not_monotonic, mean_func_no_args, 1])
def mean_func_invalid(request):
    return request.param

# MultifractionalBrownianMotion
def hurst_const(t):
    return 0.5

def hurst_sin(t):
    return math.sin(t) / 3 + 0.5

@pytest.fixture(params=[None, hurst_const, hurst_sin])
def hurst_func(request):
    return request.param

def hurst_too_many_args(t, u):
    return 0.5

def hurst_out_of_range(t):
    return 1.1

@pytest.fixture(params=[0.5, hurst_too_many_args, hurst_out_of_range])
def hurst_invalid(request):
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
    
# NHPP
@pytest.fixture(params=[lambda x:2.*x**2.])
def lambda_func1D(request):
    return request.param

@pytest.fixture(params=[np.arange(0, 100)])
def lambda_arr1D(request):
    return request.param

@pytest.fixture(params=[np.array([[0, 100]])])
def boundaries1D(request):
    return request.param

@pytest.fixture(params=[lambda x1, x2:6.*x1*x2**2.])
def lambda_func2D(request):
    return request.param

@pytest.fixture(params=[np.array([[1, 2, 3, 4], [4, 5, 6, 7], [5, 6, 7, 8]])])
def lambda_arr2D(request):
    return request.param

@pytest.fixture(params=[np.array([[0, 3], [0, 2]])])
def boundaries2D(request):
    return request.param

@pytest.fixture(params=[lambda x1, x2, x3:x1+2*x2**2+3*x3**3])
def lambda_func3D(request):
    return request.param

@pytest.fixture(params=[np.array([[[1, 2, 3, 4], [4, 5, 6, 7], [5, 6, 7, 8]],
    [[7, 8, 9, 5], [10, 11, 12, 5], [5, 6, 7, 8]]])])
def lambda_arr3D(request):
    return request.param

@pytest.fixture(params=[np.array([[0, 1], [0, 2], [0, 3]])])
def boundaries3D(request):
    return request.param
