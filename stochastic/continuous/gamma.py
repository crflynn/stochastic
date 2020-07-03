"""Gamma process."""
import numpy as np

from stochastic.base import Continuous


class GammaProcess(Continuous):
    """Gamma process.

    .. image:: _static/gamma_process.png
        :scale: 50%

    A Gamma process (discretely sampled) is the summation of stationary
    independent increments which are distributed as gamma random variables.
    This class supports instantiation using the mean/variance parametrization
    or the rate/scale parametrization.

    :param float mean: mean increase per unit time; supply with
        :py:attr:`variance`
    :param float variance: variance of increase per unit time; supply with
        :py:attr:`mean`
    :param float rate: the rate of jump arrivals; supply with :py:attr:`scale`
    :param float scale: the size of the jumps; supple with :py:attr:`rate`
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    """

    def __init__(self, mean=None, variance=None, rate=None, scale=None, t=1):
        super(GammaProcess, self).__init__(t)
        if rate is None and scale is None:
            self.mean = mean
            self.variance = variance
            self.rate = mean ** 2.0 / variance
            self.scale = 1.0 * mean / variance
        elif mean is None and variance is None:
            self.rate = rate
            self.scale = scale
            self.mean = 1.0 * self.rate / self.scale
            self.variance = 1.0 * self.mean / self.scale
            # self.variance = 1.0 * self.rate / self.scale ** 2
        else:
            raise ValueError("Invalid parametrization. Must provide either mean and variance or rate and scale.")

    def __str__(self):
        return "Gamma process with rate = {r} and scale = {s} on [0, {t}].".format(
            t=str(self.t), r=str(self.rate), s=str(self.scale)
        )

    def __repr__(self):
        return "GammaProcess(rate={r}, scale={s}, t={t})".format(t=str(self.t), r=str(self.rate), s=str(self.scale))

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
        """Scale parameter for jump sizes."""
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
        s = []
        if times[0] != 0:
            times = np.insert(times, 0, [0])
        else:
            s.append(0)
        increments = self._check_time_sequence(times)

        scale = self.variance / self.mean
        shape_coef = self.mean ** 2 / self.variance

        for inc in increments:
            s.append(np.random.gamma(shape=shape_coef * inc, scale=scale))

        return np.cumsum(s)

    def sample(self, n, zero=True):
        """Generate a realization.

        :param int n: the number of increments to generate
        :param bool zero: if True, include :math:`t=0`
        """
        return self._sample_gamma_process(n, zero)

    def sample_at(self, times):
        """Generate a realization at specified times.

        :param int times: the times at which to generate the realization
        """
        return self._sample_gamma_process_at(times)
