"""Ornstein-Uhlenbeck tests."""
from stochastic.diffusion.ornstein_uhlenbeck import OrnsteinUhlenbeckProcess


def test_ornstein_uhlenbeck_str_repr(speed, vol, t):
    instance = OrnsteinUhlenbeckProcess(speed, vol, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_ornstein_uhlenbeck_sample(speed, vol, t, n, initial, threshold):
    instance = OrnsteinUhlenbeckProcess(speed, vol, t)
    s = instance.sample(n, initial)
    assert len(s) == n + 1
