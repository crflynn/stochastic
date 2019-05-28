"""Vasicek tests."""
import pytest

from stochastic.diffusion import VasicekProcess


def test_ornstein_uhlenbeck_str_repr(speed, mean, vol, t):
    instance = VasicekProcess(speed, mean, vol, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)
