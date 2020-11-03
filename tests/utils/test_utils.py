import numpy as np

from stochastic.utils import ensure_single_arg_constant_function
from stochastic.utils import generate_times
from stochastic.utils import single_arg_constant_function


def test_generate_times(end, n):
    ls = generate_times(end, n)
    assert (ls == np.linspace(0, end, n + 1)).all()


def test_single_arg_constant_function():
    const = single_arg_constant_function(4)
    assert callable(const)
    assert const(1) == 4


def test_ensure_single_arg_constant_function():
    const = ensure_single_arg_constant_function(4)
    assert callable(const)
    assert const(1) == 4
    func = ensure_single_arg_constant_function(lambda x: 5)
    assert callable(func)
    assert func(1) == 5
