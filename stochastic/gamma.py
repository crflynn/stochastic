import numpy as np


class GammaProcess(object):
    """
    A Gamma process (discretely sampled) is the summation of stationary
    independent increments which are distributed as gamma random variables.

    args:
        T (float) = end time of process
        mean (float) = mean value of the process at t=1
        variance (float) = variance of the process at t=1
    """

    def __init__(self, T=1, mean=1, variance=1):
        self.mean = mean
        self.variance = variance
        self.T = T

    @property
    def T(self):
        return self._T

    @T.setter
    def T(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Time end value must be a positive number.')
        if value <= 0:
            raise ValueError('Time end value must be positive.')
        self._T = float(value)

    @property
    def mean(self):
        return self._mean

    @mean.setter
    def mean(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Mean parameter must be a positive number.')
        if value <= 0:
            raise ValueError('Mean parameter must be positive.')
        self._mean = float(value)

    @property
    def variance(self):
        return self._variance

    @variance.setter
    def variance(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Variance parameter must be a positive number.')
        if value <= 0:
            raise ValueError('Variance parameter must be positive.')
        self._variance = float(value)

    def __str__(self):
        return 'Gamma process with mean = {} and variance = {}.'.format(self.mean, self.variance)

    def __repr__(self):
        return self.__str__()

    def _check_increments(self, n):
        if not isinstance(n, int):
            raise TypeError('Number of increments must be an int.')
        if n <= 0:
            raise ValueError('Number of increments must be positive.')

    def _check_zero(self, zero):
        if not isinstance(zero, bool):
            raise TypeError('Zero inclusion flag must be a boolean.')

    def _check_number(self, value, name):
        if not isinstance(value, (int, float)):
            raise TypeError(name + ' value must be a number.')

    def sample(self, n, zero=True):
        """
        Returns a sample of a Gamma process with n increments from time
        t = 0 to time t = T.

        args:
            n (int) = the number of increments
            zero (bool) = boolean flag to include G_0 = 0 in the sample
        """
        self._check_increments(n)
        self._check_zero(zero)
        delta_t = self.T / n

        shape = self.mean**2 * delta_t / self.variance
        scale = self.variance / self.mean

        if zero:
            return np.concatenate(([0], np.cumsum(np.random.gamma(shape=shape, scale=scale, size=n))))
        else:
            return np.cumsum(np.random.gamma(shape=shape, scale=scale, size=n))

    def sample_at(self, times):
        """
        Returns a sample of a Gamma process at specified times.

        args:
            times (array of floats) = an array of time values for the
                Gamma process sample. Times must be positive and
                monotonically increasing. May include 0 as a time.
        """

        increments = np.diff(times)
        if np.any([t < 0 for t in times]):
            raise ValueError(' Times must be nonnegative.')
        if np.any([t <= 0 for t in increments]):
            raise ValueError(' Times must be strictly monotonically increasing.')

        s = []
        if times[0] == 0:
            s.append(0)
            increments = increments[1:]
        else:
            increments = np.concatenate((times[:1], increments))

        scale = self.variance / self.mean
        shape_coef = self.mean**2 / self.variance

        for inc in increments:
            s.append(np.random.gamma(shape=shape_coef * inc, scale=scale))

        return np.cumsum(s)

    def times(self, n, zero=True):
        """
        Return the values of t corresponding to a sample of n increments
        If zero is true, the sample includes t=0.
        """
        self._check_increments(n)
        self._check_zero(zero)

        return self._linspace(self.T, n, zero)

    def _linspace(self, end, n, zero=True):
        if zero:
            return np.linspace(0, end, n + 1)
        else:
            return np.linspace(1.0 * end / n, end, n)
