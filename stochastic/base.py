"""Base classes."""
import numpy as np


class Sequence(object):
    """Base class for sequence processes."""

    def _check_increments(self, n):
        if not isinstance(n, int):
            raise TypeError("Number of increments must be an integer.")
        if n <= 0:
            raise ValueError("Number of increments must be positive.")

    def _check_number(self, value, name):
        if not isinstance(value, (int, float)):
            raise TypeError(name + " value must be a number.")

    def _check_positive_number(self, value, name):
        self._check_number(value, name)
        if value <= 0:
            raise ValueError(name + " value must be positive.")

    def _check_nonnegative_number(self, value, name):
        self._check_number(value, name)
        if value < 0:
            raise ValueError(name + " value must be nonnegative.")

    def _check_zero(self, zero):
        if not isinstance(zero, bool):
            raise TypeError("Zero inclusion flag must be a boolean.")


class Process(Sequence):
    """Generic process class."""

    def _linspace(self, end, n, zero=True):
        """Generate a linspace from 0 to end for n increments."""
        if zero:
            return np.linspace(0, end, n + 1)
        else:
            return np.linspace(1.0 * end / n, end, n)

    def times(self, n, zero=True):
        """Generate times associated with n increments on [0, t].

        :param int n: the number of increments
        :param bool zero: if True, include :math:`t=0`
        """
        self._check_increments(n)
        self._check_zero(zero)

        return self._linspace(self.t, n, zero)


class Continuous(Process):
    """Continuous stochastic process class to be subclassed."""

    def __init__(self, t=1):
        self.t = t

    @property
    def t(self):
        """End time of the process."""
        return self._t

    @t.setter
    def t(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Time end value must be a number.")
        if value <= 0:
            raise ValueError("Time end value must be positive.")
        self._t = float(value)

    def sample(self, *args, **kwargs):
        """Sample the process."""
        raise NotImplementedError
