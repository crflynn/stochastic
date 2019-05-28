"""Gaussian Noise."""
import numpy as np

from stochastic.base import Continuous


class GaussianNoise(Continuous):
    """Gaussian noise process.

    .. image:: _static/gaussian_noise.png
        :scale: 50%

    Generate a sequence of Gaussian random variables.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    """

    def __init__(self, t=1):
        super(GaussianNoise, self).__init__(t)

    def __str__(self):
        return "Gaussian noise generator on interval [0, {t}]".format(t=str(self.t))

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
        if times[0] != 0:
            times = np.concatenate(([0], times))
        increments = self._check_time_sequence(times)

        noise = np.array([np.random.normal(scale=np.sqrt(inc)) for inc in increments])

        if zero:
            noise = np.insert(noise, [0], 0)

        return noise

    def sample(self, n):
        """Generate a realization of Gaussian noise.

        Generate a Gaussian noise realization with n increments.

        :param int n: the number of increments to generate.
        """
        return self._sample_gaussian_noise(n)

    def sample_at(self, times):
        """Generate Gaussian noise increments at specified times from zero.

        :param times: a vector of increasing time values for which to generate
            noise increments.
        """
        return self._sample_gaussian_noise_at(times)
