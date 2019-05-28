"""Test SquaredBesselProcess."""
import pytest

from stochastic.continuous import SquaredBesselProcess


def test_squared_bessel_str_repr(dim, t):
    instance = SquaredBesselProcess(dim, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_squared_bessel_init(dim_fixture, t):
    if not isinstance(dim_fixture, int):
        with pytest.raises(TypeError):
            instance = SquaredBesselProcess(dim_fixture, t)
    elif dim_fixture < 1:
        with pytest.raises(ValueError):
            instance = SquaredBesselProcess(dim_fixture, t)
    else:
        instance = SquaredBesselProcess(dim_fixture, t)


def test_squared_bessel_sample(dim, t, n, zero):
    instance = SquaredBesselProcess(dim, t)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)


def test_squared_bessel_sample_at(dim, t, times):
    instance = SquaredBesselProcess(dim, t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
