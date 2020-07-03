"""Test the base classes."""
import pytest

from stochastic.base import Checks


def test_check_increments(increments_fixture):
    checks = Checks()
    if not isinstance(increments_fixture, int):
        with pytest.raises(TypeError):
            checks._check_increments(increments_fixture)
    elif increments_fixture <= 0:
        with pytest.raises(ValueError):
            checks._check_increments(increments_fixture)
    else:
        assert checks._check_increments(increments_fixture) is None


def test_check_number(number_fixture, parameter_name_fixture):
    checks = Checks()
    if not isinstance(number_fixture, (int, float)):
        with pytest.raises(TypeError):
            checks._check_number(number_fixture, parameter_name_fixture)
    else:
        assert checks._check_number(number_fixture, parameter_name_fixture) is None


def test_check_positive_number(positive_number_fixture, parameter_name_fixture):
    checks = Checks()
    if positive_number_fixture <= 0:
        with pytest.raises(ValueError):
            checks._check_positive_number(positive_number_fixture, parameter_name_fixture)
    else:
        assert checks._check_positive_number(positive_number_fixture, parameter_name_fixture) is None


def test_check_nonnegative_number(nonnegative_number_fixture, parameter_name_fixture):
    checks = Checks()
    if nonnegative_number_fixture < 0:
        with pytest.raises(ValueError):
            checks._check_nonnegative_number(nonnegative_number_fixture, parameter_name_fixture)
    else:
        assert checks._check_nonnegative_number(nonnegative_number_fixture, parameter_name_fixture) is None


def test_check_zero(zero_fixture):
    checks = Checks()
    if not isinstance(zero_fixture, bool):
        with pytest.raises(TypeError):
            checks._check_zero(zero_fixture)
    else:
        assert checks._check_zero(zero_fixture) is None
