"""Discrete-time process testing."""
import numpy as np
import pytest
import scipy.stats as ss


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


@pytest.fixture(params=[1])
def initial(request):
    return request.param


# BernoulliProcess
@pytest.fixture(params=[0.5])
def p(request):
    return request.param


@pytest.fixture(params=[0.5, "0.5", 2, -0.5])
def p_fixture(request):
    return request.param


# ChineseRestaurantProcess
@pytest.fixture(params=[0])
def discount(request):
    return request.param


@pytest.fixture(params=[1])
def strength(request):
    return request.param


@pytest.fixture(params=[2, -1, 0.7])
def discount_fixture(request):
    return request.param


@pytest.fixture(params=[1.1, -2])
def strength_fixture(request):
    return request.param


# MarkovChain
@pytest.fixture(params=[[[0.25, 0.75], [0.4, 0.6]]])
def transition(request):
    return request.param


@pytest.fixture(params=[[0.25, 0.75], None])
def initial(request):
    return request.param


# MoranProcess
@pytest.fixture(params=[0, 0.1])
def maximum_fixture(request):
    return request.param


@pytest.fixture(params=[0, 1.1])
def n_fixture(request):
    return request.param


@pytest.fixture(params=[-1, 1.1])
def start_fixture(request):
    return request.param


@pytest.fixture(params=[1])
def start(request):
    return request.param


@pytest.fixture(params=[5])
def maximum(request):
    return request.param


# RandomWalk
@pytest.fixture(params=[[-1, 1]])
def steps(request):
    return request.param


@pytest.fixture(params=[[1, 1], None])
def weights(request):
    return request.param


@pytest.fixture(params=[[], ["1"], [[1, 2], [3, 4]]])
def steps_fixture(request):
    return request.param


@pytest.fixture(params=[[1], [-1, -1], [[1, 2], [3, 4]]])
def weights_fixture(request):
    return request.param


# Dirichlet process
@pytest.fixture(params=[None, np.random.uniform, ss.cauchy().rvs, 1])
def base(request):
    return request.param


@pytest.fixture(params=[-1, 0, 0.1, 1, 100])
def alpha(request):
    return request.param
