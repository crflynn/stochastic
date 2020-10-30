"""Base classes."""
from abc import ABC
from abc import abstractmethod

from stochastic.utils import generate_times
from stochastic.utils.validation import check_positive_integer
from stochastic.utils.validation import check_positive_number


class BaseProcess(ABC):
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

    def __init__(self, t=1):
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
