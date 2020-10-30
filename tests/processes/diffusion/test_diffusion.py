"""Diffusion process tests."""
from stochastic.processes.diffusion import DiffusionProcess


def test_diffusion_process_str_repr(speed, mean, vol, volexp, t):
    instance = DiffusionProcess(speed, mean, vol, volexp, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_diffusion_process_sample(speed, mean, vol, volexp, t, n, initial, threshold):
    instance = DiffusionProcess(speed, mean, vol, volexp, t)
    s = instance.sample(n, initial)
    assert len(s) == n + 1
