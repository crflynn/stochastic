"""Noise process tests."""
import numpy as np
import pytest

from stochastic.processes.noise import BlueNoise
from stochastic.processes.noise import BrownianNoise
from stochastic.processes.noise import ColoredNoise
from stochastic.processes.noise import PinkNoise
from stochastic.processes.noise import RedNoise
from stochastic.processes.noise import VioletNoise
from stochastic.processes.noise import WhiteNoise


# Floating point arithmetic comparison threshold
@pytest.fixture(params=[10**-10])
def threshold(request):
    return request.param


# Common
@pytest.fixture(params=[1])
def t(request):
    return request.param


@pytest.fixture(params=[16, 17])  # even and odd for colored noise fft
def n(request):
    return request.param


# Generate some random times for the sample_at() method
times_random = np.cumsum(np.abs(np.random.normal(size=16)))
times_random_zero = np.cumsum([0] + list(np.abs(np.random.normal(size=16))))


@pytest.fixture(params=[times_random, times_random_zero])
def times(request):
    return request.param


# FractionalGaussianNoise
@pytest.fixture(params=[0.2, 0.5, 0.7])
def hurst(request):
    return request.param


@pytest.fixture(params=[1, 1.1])
def hurst_fixture(request):
    return request.param


@pytest.fixture(params=["daviesharte", "hosking"])
def algorithm(request):
    return request.param


@pytest.fixture(params=["badalgorithm"])
def algorithm_fixture(request):
    return request.param


# ColoredNoise
@pytest.fixture(params=[-3, -2, -1, 0, 1, 2, 3, 0.5, -0.5])
def beta(request):
    return request.param


@pytest.fixture(
    params=[
        ColoredNoise,
        WhiteNoise,
        PinkNoise,
        RedNoise,
        BrownianNoise,
        BlueNoise,
        VioletNoise,
    ]
)
def colored_noise_class(request):
    return request.param
