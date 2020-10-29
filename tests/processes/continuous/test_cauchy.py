"""Test CauchyProcess."""

from stochastic.processes.continuous import CauchyProcess


def test_cauchy_process_str_repr(t):
    instance = CauchyProcess(t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_cauchy_process_sample(t, n, threshold):
    instance = CauchyProcess(t)
    s = instance.sample(n)
    assert len(s) == n + 1


def test_cauchy_process_sample_at(t, times, threshold):
    instance = CauchyProcess(t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
