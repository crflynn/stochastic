"""Ornstein-Uhlenbeck tests."""
# flake8: noqa
import pytest

from stochastic.diffusion import OrnsteinUhlenbeckProcess


def test_ornstein_uhlenbeck_str_repr(t, speed, mean, vol):
    instance = OrnsteinUhlenbeckProcess(t, speed, mean, vol)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_ornstein_uhlenbeck_sample(t, speed, mean, vol, n, initial, zero, threshold):
    instance = OrnsteinUhlenbeckProcess(t, speed, mean, vol)
    s = instance.sample(n, initial, zero)
    assert len(s) == n + int(zero)
