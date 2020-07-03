"""Test BesselProcess."""
import pytest

from stochastic.continuous import BesselProcess


def test_bessel_str_repr(dim, t):
    instance = BesselProcess(dim, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_bessel_init(dim_fixture, t):
    if not isinstance(dim_fixture, int):
        with pytest.raises(TypeError):
            instance = BesselProcess(dim_fixture, t)
    elif dim_fixture < 1:
        with pytest.raises(ValueError):
            instance = BesselProcess(dim_fixture, t)
    else:
        instance = BesselProcess(dim_fixture, t)


def test_bessel_sample(dim, t, n, zero):
    instance = BesselProcess(dim, t)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)


def test_bessel_sample_at(dim, t, times):
    instance = BesselProcess(dim, t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
