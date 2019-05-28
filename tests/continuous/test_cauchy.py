"""Test CauchyProcess."""
import pytest

from stochastic.continuous import CauchyProcess


def test_cauchy_process_str_repr(t):
    instance = CauchyProcess(t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_cauchy_process_sample(t, n, zero, threshold):
    instance = CauchyProcess(t)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)


def test_cauchy_process_sample_at(t, times, threshold):
    instance = CauchyProcess(t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
