"""Test the base classes."""
import pytest

from stochastic.utils.validation import check_increments
from stochastic.utils.validation import check_nonnegative_number
from stochastic.utils.validation import check_numeric
from stochastic.utils.validation import check_numeric_or_single_arg_callable
from stochastic.utils.validation import check_positive_integer
from stochastic.utils.validation import check_positive_number


def test_check_positive_integer(increments_fixture):
    if not isinstance(increments_fixture, int):
        with pytest.raises(TypeError):
            check_positive_integer(increments_fixture)
    elif increments_fixture <= 0:
        with pytest.raises(ValueError):
            check_positive_integer(increments_fixture)
    else:
        assert check_positive_integer(increments_fixture) is None


def test_check_numeric(number_fixture, parameter_name_fixture):
    if not isinstance(number_fixture, (int, float)):
        with pytest.raises(TypeError):
            check_numeric(number_fixture, parameter_name_fixture)
    else:
        assert check_numeric(number_fixture, parameter_name_fixture) is None


def test_check_positive_number(positive_number_fixture, parameter_name_fixture):
    if positive_number_fixture <= 0:
        with pytest.raises(ValueError):
            check_positive_number(positive_number_fixture, parameter_name_fixture)
    else:
        assert (
            check_positive_number(positive_number_fixture, parameter_name_fixture)
            is None
        )


def test_check_nonnegative_number(nonnegative_number_fixture, parameter_name_fixture):
    if nonnegative_number_fixture < 0:
        with pytest.raises(ValueError):
            check_nonnegative_number(nonnegative_number_fixture, parameter_name_fixture)
    else:
        assert (
            check_nonnegative_number(nonnegative_number_fixture, parameter_name_fixture)
            is None
        )


def test_check_numeric_or_single_arg_callable():
    with pytest.raises(ValueError):
        check_numeric_or_single_arg_callable(lambda x, y: 5)
    with pytest.raises(ValueError):
        check_numeric_or_single_arg_callable("test")
    check_numeric_or_single_arg_callable(5)
    check_numeric_or_single_arg_callable(lambda x: 5)


def test_check_increments():
    with pytest.raises(ValueError):
        check_increments([-1, 0, 1])
    with pytest.raises(ValueError):
        check_increments([0, 2, 1])
    check_increments([0, 1, 2])
