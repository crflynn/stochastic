"""Moran process tests."""
import pytest

from stochastic.processes.discrete import MoranProcess


def test_moran_process_str_repr(maximum):
    instance = MoranProcess(maximum)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_moran_process_sample(maximum, n, start):
    instance = MoranProcess(maximum)
    s = instance.sample(n, start)
    assert len(s) <= n
    states = list(range(maximum + 1))
    for state in s:
        assert state in states


def test_moran_process_probability(maximum_fixture):
    with pytest.raises((ValueError, TypeError)):
        instance = MoranProcess(maximum_fixture)


def test_moran_process_n(n, n_fixture):
    instance = MoranProcess(20)
    with pytest.raises((ValueError, TypeError)):
        s = instance.sample(n_fixture, 5)


def test_moran_process_(n, start_fixture):
    instance = MoranProcess(20)
    with pytest.raises((ValueError, TypeError)):
        s = instance.sample(20, start_fixture)
