"""Test ColoredNoise."""
# flake8: noqa
import pytest

from stochastic.noise import ColoredNoise


def test_colored_noise_str_repr(t):
    instance = ColoredNoise(t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_colored_noise_sample(t, n, beta):
    instance = ColoredNoise(t)
    s = instance.sample(n)
    assert len(s) == n + 1
