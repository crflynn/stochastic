import numpy as np


def generate_times(end, n):
    """Generate a linspace from 0 to end for n increments."""
    return np.linspace(0, end, n + 1)


def single_arg_constant_function(value):
    """Generate a single argument function which returns a constant value."""
    return lambda x: value


def ensure_single_arg_constant_function(value):
    """Convert the passed value into a const function if not one already."""
    if not callable(value):
        return single_arg_constant_function(value)
    return value
