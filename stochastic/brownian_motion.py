import numpy as np


class BrownianMotion(object):
    """
    A Brownian motion (discretely sampled) has independent and identically
    distributed Gaussian increments with variance equal to increment length.

    args:
        delta (float) = increment length

    methods:

    sample
        args:
            n (int) = number of increments in the sample
            zero (bool) = flag to include W_t=0
        returns:
            (list) of values of the Brownian motion sample

    times
        args:
            n (int) = number of increments in the sample
            zero (bool) = flag to include t_0=0
        returns:
            (list) of times corresponding the Brownian motion sample
    """

    def __init__(self, delta=1):
        self.delta = delta

    @property
    def delta(self):
        return self._delta

    @delta.setter
    def delta(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Increment size must be a number.')
        if value <= 0:
            raise ValueError('Increment size must be positive.')
        self._delta = value

    def sample(self, n, zero=True):
        """
        Generate a Brownian motion sample of n increments
        If zero is true, the sample includes W_0 = 0
        """
        if not isinstance(n, int):
            raise TypeError('Number of increments must be an int.')
        if n <= 0:
            raise ValueError('Number of increments must be positive.')
        if not isinstance(zero, bool):
            raise TypeError('Zero inclusion flag must be a boolean.')

        if zero:
            return np.concatenate(([0], np.cumsum(np.random.normal(scale=self.delta, size=n))))
        else:
            return np.cumsum(np.random.normal(scale=self.delta, size=n))

    def times(self, n, zero=True):
        """
        Return the values of t corresponding to a sample of n increments
        If zero is true, the sample includes t=0
        """
        if not isinstance(n, int):
            raise TypeError('Number of increments must be an int.')
        if n <= 0:
            raise ValueError('Number of increments must be positive.')
        if not isinstance(zero, bool):
            raise TypeError('Zero inclusion flag must be a boolean.')

        if zero:
            return np.linspace(0, n * self.delta, n + 1)
        else:
            return np.linspace(self.delta, n * self.delta, n)