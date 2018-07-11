"""Test FractionalGaussianNoise."""
# flake8: noqa
import pytest

from stochastic.noise import FractionalGaussianNoise
from stochastic.noise import fractional_gaussian_noise


def test_fractional_gaussian_noise_str_repr(t, hurst):
    instance = FractionalGaussianNoise(t, hurst)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_fractional_gaussian_noise_hurst(t, hurst_fixture):
    with pytest.raises((ValueError, TypeError)):
        instance = FractionalGaussianNoise(t, hurst_fixture)

def test_fractional_gaussian_noise_algorithm(t, n, algorithm_fixture):
    instance = FractionalGaussianNoise(t, 0.7)
    with pytest.raises(ValueError):
        s = instance.sample(n, algorithm_fixture)

def test_fractional_gaussian_noise_fallback(t, mocker):
    instance = FractionalGaussianNoise(t, 0.99)  # high hurst
    mocker.patch('stochastic.noise.fractional_gaussian_noise.logging')
    s = instance.sample(8, 'daviesharte')  # low n, with daviesharte, fallback to hosking
    assert fractional_gaussian_noise.logging.warning.called

def test_fractional_gaussian_noise_sample(t, hurst, algorithm, n, zero):
    instance = FractionalGaussianNoise(t, hurst)
    s = instance.sample(n, algorithm)
    assert len(s) == n
