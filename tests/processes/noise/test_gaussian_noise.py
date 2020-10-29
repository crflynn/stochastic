"""Test GaussianNoise."""
from stochastic.processes.noise import GaussianNoise


def test_gaussian_noise_str_repr(t):
    instance = GaussianNoise(t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_gaussian_noise_sample(t, n):
    instance = GaussianNoise(t)
    s = instance.sample(n)
    assert len(s) == n


def test_gaussian_noise_sample_at(t, times):
    instance = GaussianNoise(t)
    s = instance.sample_at(times)
    if times[0] == 0:
        assert len(s) == len(times) - 1
    else:
        assert len(s) == len(times)
