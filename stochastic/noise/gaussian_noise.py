"""Gaussian Noise."""
import numpy as np

from stochastic.base import Continuous


class GaussianNoise(Continuous):
    """Gaussian noise process."""

    def __init__(self, t=1):
        self.t = t

    def __str__(self):
        return "Gaussian noise generator on interval [0, {t}]".format(
            t=str(self.t))

    def __repr__(self):
        return "GaussianNoise(t={t})".format(t=str(self.t))

    def _sample_gaussian_noise(self, n, zero=False):
        """Generate a realization of Gaussian noise.

        Generate a Gaussian noise realization with n increments.
        """
        self._check_increments(n)
        delta_t = 1.0 * self.t / n

        noise = np.random.normal(scale=np.sqrt(delta_t), size=n)

        if zero:
            noise = np.insert(noise, [0], 0)

        return noise

    def _sample_gaussian_noise_at(self, times, zero=False):
        """Generate Gaussian noise increments at specified times from zero."""
        if np.any([t < 0 for t in times]):
            raise ValueError("Times must be nonnegative.")

        if times[0] != 0:
            times = np.concatenate(([0], times))
        increments = np.diff(times)

        if np.any([t <= 0 for t in increments]):
            raise ValueError(
                "Times must be strictly monotonically increasing.")

        noise = np.array(
            [np.random.normal(scale=np.sqrt(inc)) for inc in increments])

        if zero:
            noise = np.insert(noise, [0], 0)

        return noise

    def sample(self, n):
        """Generate a realization of Gaussian noise.

        Generate a Gaussian noise realization with n increments.
        """
        return self._sample_gaussian_noise(n)

    def sample_at(self, times):
        """Generate Gaussian noise increments at specified times from zero."""
        return self._sample_gaussian_noise_at(times)
