"""Diffusion process testing."""
import pytest


# Floating point arithmetic comparison threshold
@pytest.fixture(params=[10 ** -10])
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


# OrnsteinUhlenbeckProcess
@pytest.fixture(params=[1])
def speed(request):
    return request.param


@pytest.fixture(params=[1])
def mean(request):
    return request.param


@pytest.fixture(params=[1])
def vol(request):
    return request.param


# CEVProcess
@pytest.fixture(params=[1])
def mu(request):
    return request.param


@pytest.fixture(params=[1])
def sigma(request):
    return request.param


@pytest.fixture(params=[1])
def gamma(request):
    return request.param
