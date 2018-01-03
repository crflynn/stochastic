"""Discrete-time process testing."""
# flake8: noqa
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
