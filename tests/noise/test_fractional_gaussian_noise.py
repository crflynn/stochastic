"""Test FractionalGaussianNoise."""
import pytest

from stochastic.noise import FractionalGaussianNoise
from stochastic.noise import fractional_gaussian_noise


def test_fractional_gaussian_noise_str_repr(hurst, t):
    instance = FractionalGaussianNoise(hurst, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_fractional_gaussian_noise_hurst(hurst_fixture, t):
    with pytest.raises((ValueError, TypeError)):
        instance = FractionalGaussianNoise(hurst_fixture, t)


def test_fractional_gaussian_noise_algorithm(t, n, algorithm_fixture):
    instance = FractionalGaussianNoise(0.7, t)
    with pytest.raises(ValueError):
        s = instance.sample(n, algorithm_fixture)


def test_fractional_gaussian_noise_sample(hurst, t, algorithm, n, zero):
    instance = FractionalGaussianNoise(hurst, t)
    s = instance.sample(n, algorithm)
    assert len(s) == n
