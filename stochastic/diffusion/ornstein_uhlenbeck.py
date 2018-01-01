"""Ornstein-Uhlenbeck process."""
import numpy as np

from stochastic.base import Continuous
from stochastic.noise.gaussian_noise import GaussianNoise


class OrnsteinUhlenbeckProcess(Continuous):
    """Cox-Ingersoll-Ross process."""

    def __init__(self, t=1, speed=1, mean=1, vol=1):
        super().__init__(t)
        self.speed = speed
        self.mean = mean
        self.vol = vol
        self.gn = GaussianNoise(t)

    @property
    def speed(self):
        """Speed of reversion."""
        return self._speed

    @speed.setter
    def speed(self, value):
        self._check_positive_number(value)
        self._speed = value

    @property
    def mean(self):
        """Mean of process."""
        return self._mean

    @mean.setter
    def mean(self, value):
        self._check_number(value)
        self._mean = value

    @property
    def vol(self):
        """Volatility parameter."""
        return self._vol

    @vol.setter
    def vol(self, value):
        self._check_positive_number(value)
        self._vol = value

    def _volatility(self, arg):
        """Volatility coefficient.

        This method is overridden in subclasses for more specific stochastic
        volatility processes.
        """
        return 1

    def _sample(self, n, start, zero=True):
        """Generate a realization of a Ornstein-Uhlenbeck process."""
        self._check_increments(n)
        self._check_zero(zero)
        self._check_number(start)

        delta_t = 1.0 * self.t / n
        gns = self.gn.sample(n)

        s = []
        if zero:
            s.append(start)
        for k in range(n):
            start += self.speed * (self.mean - start) * delta_t + \
                self.vol * self._volatility * gns[k]
            s.append(start)

        return np.array(s)

    def sample(self, n, start, zero=True):
        """Generate a realization of a Ornstein-Uhlenbeck process."""
        return self._sample(n, start, zero)


class OUProcess(OrnsteinUhlenbeckProcess):
    """Alias for OrnsteinUhlenbeckProcess."""

    pass
