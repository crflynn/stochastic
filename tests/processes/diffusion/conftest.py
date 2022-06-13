"""Diffusion process testing."""
import pytest


# Floating point arithmetic comparison threshold
@pytest.fixture(params=[10**-10])
def threshold(request):
    return request.param


@pytest.fixture(params=[1])
def t(request):
    return request.param


@pytest.fixture(params=[16])
def n(request):
    return request.param


@pytest.fixture(params=[1])
def initial(request):
    return request.param


@pytest.fixture(params=[1])
def speed(request):
    return request.param


@pytest.fixture(params=[1])
def drift(request):
    return request.param


@pytest.fixture(params=[1])
def mean(request):
    return request.param


@pytest.fixture(params=[1])
def vol(request):
    return request.param


@pytest.fixture(params=[1])
def volexp(request):
    return request.param
