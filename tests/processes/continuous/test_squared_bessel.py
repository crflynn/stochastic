"""Test SquaredBesselProcess."""
import pytest

from stochastic.processes.continuous import SquaredBesselProcess


def test_squared_bessel_str_repr(dim, t):
    instance = SquaredBesselProcess(dim, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_squared_bessel_init(dim_fixture, t):
    if not isinstance(dim_fixture, int):
        with pytest.raises(TypeError):
            _ = SquaredBesselProcess(dim_fixture, t)
    elif dim_fixture < 1:
        with pytest.raises(ValueError):
            _ = SquaredBesselProcess(dim_fixture, t)
    else:
        _ = SquaredBesselProcess(dim_fixture, t)


def test_squared_bessel_sample(dim, t, n):
    instance = SquaredBesselProcess(dim, t)
    s = instance.sample(n)
    assert len(s) == n + 1


def test_squared_bessel_sample_at(dim, t, times):
    instance = SquaredBesselProcess(dim, t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
