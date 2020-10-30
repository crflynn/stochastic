"""Vasicek tests."""
from stochastic.processes.diffusion import VasicekProcess


def test_vasicek_str_repr(speed, mean, vol, t):
    instance = VasicekProcess(speed, mean, vol, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)
