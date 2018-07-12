"""Vasicek tests."""
# flake8: noqa
import pytest

from stochastic.diffusion import VasicekProcess


def test_ornstein_uhlenbeck_str_repr(t, speed, mean, vol):
    instance = VasicekProcess(t, speed, mean, vol)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)
