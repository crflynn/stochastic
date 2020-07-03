import numpy as np
import pytest

from stochastic.base import Continuous


def test_check_times(end, n, zero, mocker):
    continuous = Continuous(end)
    mocker.patch("stochastic.base.Continuous.times")
    assert continuous._n is None
    continuous._check_times(n, zero)
    assert continuous._n == n
    assert continuous.times.called


def test_linspace(end, n, zero):
    continuous = Continuous(end)
    ls = continuous._linspace(end, n, zero)
    if zero:
        assert (ls == np.linspace(0, end, n + 1)).all()
    else:
        assert (ls == np.linspace(1.0 * end / n, end, n)).all()


def test_sample(end, n):
    continuous = Continuous(end)
    with pytest.raises(NotImplementedError):
        continuous.sample(n)


def test_times(end, n, zero, mocker):
    continuous = Continuous(end)
    mocker.patch("stochastic.base.Continuous._linspace")
    continuous.times(n, zero)
    assert continuous._linspace.called


def test_check_time_sequence(end, times_fixture):
    continuous = Continuous(end)
    if np.any(np.array(times_fixture) < 0) or np.any(np.diff(times_fixture) <= 0):
        with pytest.raises(ValueError):
            continuous._check_time_sequence(times_fixture)
    else:
        continuous._check_time_sequence(times_fixture)
