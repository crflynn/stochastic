import numpy as np


class BrownianMotion(object):
    """
    A Brownian motion (discretely sampled) has independent and identically
    distributed Gaussian increments with variance equal to increment length.

    args:
        T (float) = end time of process

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

    def __init__(self, T=1):
        self.T = T

    def __str__(self):
        return 'Brownian motion generator on interval [0, {}].'.format(self.T)

    def __repr__(self):
        return self.__str__()

    @property
    def T(self):
        return self._T

    @T.setter
    def T(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Time end value must be a number.')
        if value <= 0:
            raise ValueError('Time end value must be positive.')
        self._T = float(value)

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
        Generate a Brownian motion sample of n increments
        If zero is true, the sample includes W_0 = 0.
        """
        self._check_increments(n)
        self._check_zero(zero)
        delta_t = self.T / n

        if zero:
            return np.concatenate(([0], np.cumsum(np.random.normal(scale=np.sqrt(delta_t), size=n))))
        else:
            return np.cumsum(np.random.normal(scale=np.sqrt(delta_t), size=n))

    def sample_noise(self, n):
        """
        Generate a Gaussian noise sample of n increments
        """
        self._check_increments(n)
        delta_t = self.T / n

        return np.random.normal(scale=np.sqrt(delta_t), size=n)

    def sample_bridge(self, n, b=0, zero=True):
        """
        Generate a Brownian bridge sample of n increments from W_0 = 0
        to time t which has value b. If zero is true, the sample
        includes W_0 = 0.
        """
        self._check_number(b, 'End')
        b = float(b)
        self._check_zero(zero)

        line = self._linspace(b, n, zero)
        bm = self.sample(n, zero)
        times = self.times(n, zero)

        return line + (bm - times * bm)

    def sample_drift(self, n, drift, volatility, zero=True):
        """
        Generate a Brownian motion with drift sample of n increments from
        drift and volatility values. If zero is true,
        the sample includes W_0=0.
        """
        self._check_increments(n)
        self._check_number(drift, 'Drift')
        self._check_number(volatility, 'Volatility')
        if volatility < 0:
            raise ValueError('Volatility must be nonnegative.')
        self._check_zero(zero)

        line = self._linspace(drift, n, zero)
        bm = volatility * self.sample(n, zero)

        return line + bm

    def sample_geometric(self, n, drift, volatility, initial=1, zero=True):
        """
        Generate a geometric Brownian motion sample of n increments from
        initial value S_0=initial, with drift and volatility. If zero is true,
        the sample includes W_0=initial.
        """
        self._check_increments(n)
        self._check_number(drift, 'Drift')
        self._check_number(volatility, 'Volatility')
        if volatility < 0:
            raise ValueError('Volatility must be nonnegative.')
        self._check_number(initial, 'Initial')
        if initial <= 0:
            raise ValueError('Initial value must be positive.')
        self._check_zero(zero)

        line = self._linspace(1.0 * drift - volatility ** 2 / 2, n, zero)
        noise = volatility * self.sample(n, zero)

        return initial * np.exp(line + noise)

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
