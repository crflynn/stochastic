"""Gamma process."""
import numpy as np

from stochastic.base import Continuous


class GammaProcess(Continuous):
    """Gamma process.

    A Gamma process (discretely sampled) is the summation of stationary
    independent increments which are distributed as gamma random variables.

    args:
        T (float) = end time of process
        mean (float) = mean value of the process at t=1
        variance (float) = variance of the process at t=1
    """

    def __init__(self, t=1, mean=1, variance=1, rate=None, scale=None):
        super().__init__(t)
        if mean is None or variance is None:
            self.rate = rate
            self.scale = scale
            self.mean = 1.0 * self.rate / self.scale
            self.variance = 1.0 * self.mean / self.scale
            # self.variance = 1.0 * self.rate / self.scale ** 2
        if rate is None or scale is None:
            self.mean = mean
            self.variance = variance
            self.rate = mean ** 2.0 / variance
            self.scale = 1.0 * mean / variance

    def __str__(self):
        return ("Gamma process with rate = {r} and "
                "scale = {s} on [0, {t}].").format(
                    t=str(self.t),
                    r=str(self.rate),
                    s=str(self.scale)
        )

    def __repr__(self):
        return "GammaProcess(t={t}, rate={r}, scale={s})".format(
            t=str(self.t),
            r=str(self.rate),
            s=str(self.scale)
        )

    @property
    def mean(self):
        """Mean increase per unit time."""
        return self._mean

    @mean.setter
    def mean(self, value):
        self._check_positive_number(value, "Mean parameter")
        self._mean = float(value)

    @property
    def rate(self):
        """Rate of jump arrivals."""
        return self._rate

    @rate.setter
    def rate(self, value):
        self._check_positive_number(value, "Rate parameter")
        self._rate = value

    @property
    def scale(self):
        """Scale parameter."""
        return self._scale

    @scale.setter
    def scale(self, value):
        self._check_positive_number(value, "Scale parameter")
        self._scale = value

    @property
    def variance(self):
        """Variance of increase per unit time."""
        return self._variance

    @variance.setter
    def variance(self, value):
        self._check_positive_number(value, "Variance parameter")
        self._variance = value

    def _sample_gamma_process(self, n, zero=True):
        """Sample a Gamma process."""
        self._check_increments(n)
        self._check_zero(zero)
        delta_t = 1.0 * self.t / n

        shape = 1.0 * self.mean ** 2 * delta_t / self.variance
        scale = 1.0 * self.variance / self.mean

        samples = np.cumsum(np.random.gamma(shape=shape, scale=scale, size=n))

        if zero:
            return np.concatenate(([0], samples))
        else:
            return samples

    def _sample_gamma_process_at(self, times):
        """Sample a Gamma process at specific times."""
        increments = np.diff(times)
        if np.any([t < 0 for t in times]):
            raise ValueError("Times must be nonnegative.")
        if np.any([t <= 0 for t in increments]):
            raise ValueError("Times must be strictly increasing.")

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

    def sample(self, n, zero=True):
        """Generate a realization of a Gamma process."""
        return self._sample_gamma_process(n, zero)


class VarianceGammaProcess(Continuous):
    """Variance Gamma process."""

    def __init__(self, t=1, drift=0, variance=1, scale=1):
        super().__init__(t)
        self.drift = drift
        self.variance = variance
        self.scale = scale

    @property
    def drift(self):
        """Drift parameter."""
        return self._drift

    @drift.setter
    def drift(self, value):
        self._check_number(value, "Drift")
        self._drift = value

    @property
    def variance(self):
        """Variance parameter."""
        return self._variance

    @variance.setter
    def variance(self, value):
        self._check_positive_number(value, "Variance")
        self._variance = value

    @property
    def scale(self):
        """Scale parameter."""
        return self._scale

    @scale.setter
    def scale(self, value):
        self._check_positive_number(value, "Scale")
        self._scale = value

    def _sample_variance_gamma_process(self, n, zero=True):
        """Generate a realization of a variance gamma process."""
        self._check_increments(n)
        self._check_zero(zero)

        delta_t = 1.0 * self.t / n
        shape = delta_t / self.variance
        scale = self.variance

        gammas = np.random.gamma(shape=shape, scale=scale, size=n)
        gn = np.random.normal(size=n)

        increments = self.drift * gammas + self.scale * np.sqrt(gammas) * gn

        samples = np.cumsum(increments)

        if zero:
            return np.concatenate(([0], samples))
        else:
            return samples

    def sample(self, n, zero=True):
        """Generate a realization of a variance gamma process."""
        return self._sample_variance_gamma_process(n, zero)
