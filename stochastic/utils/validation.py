from inspect import signature
from numbers import Number

import numpy as np


def check_positive_integer(n, name=""):
    """Ensure that the number is a positive integer."""
    if not isinstance(n, int):
        raise TypeError(f"{name} must be an integer.")
    if n <= 0:
        raise ValueError(f"{name} must be positive.")


def check_numeric(value, name=""):
    """Ensure that the value is numeric."""
    if not isinstance(value, Number):
        raise TypeError(f"{name} value must be a number.")


def check_positive_number(value, name=""):
    """Ensure that the value is a positive number."""
    check_numeric(value, name)
    if value <= 0:
        raise ValueError(f"{name} value must be positive.")


def check_nonnegative_number(value, name=""):
    """Ensure that the value is a nonnegative number"""
    check_numeric(value, name)
    if value < 0:
        raise ValueError(f"{name} value must be nonnegative.")


def check_increments(times):
    increments = np.diff(times)
    if np.any([t < 0 for t in times]):
        raise ValueError("Times must be nonnegative.")
    if np.any([t <= 0 for t in increments]):
        raise ValueError("Times must be strictly increasing.")
    return increments


def times_to_increments(times):
    """Ensure a positive, monotonically increasing sequence."""
    return check_increments(times)


def check_numeric_or_single_arg_callable(value, name=""):
    """Ensure a numeric of single arg callable."""
    is_numeric = isinstance(value, Number)
    is_callable = callable(value)
    if is_callable and len(signature(value).parameters) != 1:
        raise ValueError(f"{name} callable must have a single argument")
    if not is_numeric and not is_callable:
        raise ValueError(f"{name} must be numeric or a single argument callable")
