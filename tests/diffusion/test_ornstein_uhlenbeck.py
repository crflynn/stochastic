"""Ornstein-Uhlenbeck tests."""
import pytest

from stochastic.diffusion import OrnsteinUhlenbeckProcess


def test_ornstein_uhlenbeck_str_repr(speed, mean, vol, t):
    instance = OrnsteinUhlenbeckProcess(speed, mean, vol, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_ornstein_uhlenbeck_sample(speed, mean, vol, t, n, initial, zero, threshold):
    instance = OrnsteinUhlenbeckProcess(speed, mean, vol, t)
    s = instance.sample(n, initial, zero)
    assert len(s) == n + int(zero)
