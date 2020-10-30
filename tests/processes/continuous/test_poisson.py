"""Test PoissonProcess."""
import pytest

from stochastic.processes.continuous import PoissonProcess


def test_poisson_process_str_repr(rate):
    instance = PoissonProcess(rate)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_poisson_process_sample(rate, n_fixture, length):
    instance = PoissonProcess(rate)
    if n_fixture is None and length is None:
        with pytest.raises(ValueError):
            s = instance.sample(n_fixture, length)
    elif length is not None and n_fixture is None:
        s = instance.sample(n_fixture, length)
        assert s[-1] >= length
    else:  # n_fixture is not None:
        s = instance.sample(n_fixture, length)
        assert len(s) == n_fixture + 1


def test_poisson_process_times(rate, n):
    instance = PoissonProcess(rate)
    with pytest.raises(AttributeError):
        _ = instance.times(n)
