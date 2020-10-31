"""Base classes."""
from abc import ABC
from abc import abstractmethod

import numpy as np

from stochastic import random
from stochastic.utils import generate_times
from stochastic.utils.validation import check_positive_integer
from stochastic.utils.validation import check_positive_number


class BaseProcess(ABC):
    def __init__(self, rng=None):
        self.rng = rng

    @property
    def rng(self):
        if self._rng is None:
            return random.generator
        return self._rng

    @rng.setter
    def rng(self, value):
        if value is None:
            self._rng = None
        elif isinstance(value, (np.random.RandomState, np.random.Generator)):
            self._rng = value
        else:
            raise TypeError("rng must be of type `numpy.random.Generator`")

    @abstractmethod
    def sample(self, n):  # pragma: no cover
        pass


class BaseSequenceProcess(BaseProcess, ABC):
    pass


class BaseTimeProcess(BaseProcess, ABC):
    """Base class to be subclassed to most process classes.

    Contains properties and functions related to times and continuous-time
    processes.
    """

    def __init__(self, t=1, rng=None):
        super().__init__(rng=rng)
        self.t = t
        self._n = None
        self._times = None

    @property
    def t(self):
        """End time of the process."""
        return self._t

    @t.setter
    def t(self, value):
        check_positive_number(value, "Time end")
        self._t = float(value)

    def _set_times(self, n):
        if self._n != n:
            check_positive_integer(n)
            self._n = n
            self._times = generate_times(self.t, n)

    def times(self, n):
        """Generate times associated with n increments on [0, t].

        :param int n: the number of increments
        """
        self._set_times(n)
        return self._times
