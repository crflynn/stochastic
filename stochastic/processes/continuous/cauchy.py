"""Cauchy processes."""
import numpy as np
from scipy.stats import levy

from stochastic.processes.continuous.brownian_motion import BrownianMotion
from stochastic.utils.validation import check_positive_integer


class CauchyProcess(BrownianMotion):
    """Symmetric Cauchy process.

    .. image:: _static/cauchy_process.png
        :scale: 50%

    The symmetric Cauchy process is a Brownian motion with a Levy subordinator
    using location parameter 0 and scale parameter :math:`t^2/2`.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, t=1, rng=None):
        super().__init__(t=t, rng=rng)

    def _sample_cauchy_process(self, n):
        """Generate a realization of a Cauchy process."""
        check_positive_integer(n)

        delta_t = 1.0 * self.t / n
        times = np.cumsum(levy.rvs(loc=0, scale=delta_t**2 / 2, size=n))
        times = np.insert(times, 0, [0])
        return self._sample_brownian_motion_at(times)

    def _sample_cauchy_process_at(self, times):
        """Generate a realization of a Cauchy process."""
        if times[0] != 0:
            zero = False
            times = np.insert(times, 0, [0])
        else:
            zero = True

        deltas = np.diff(times)
        levys = [
            levy.rvs(loc=0, scale=d**2 / 2, size=1, random_state=self.rng)
            for d in deltas
        ]
        ts = np.cumsum(levys)

        if zero:
            ts = np.insert(ts, 0, [0])

        return self._sample_brownian_motion_at(ts)

    def sample(self, n):
        """Generate a realization.

        :param int n: the number of increments to generate.
        """
        return self._sample_cauchy_process(n)

    def sample_at(self, times):
        """Generate a realization using specified times.

        :param times: a vector of increasing time values at which to generate
            the realization
        """
        return self._sample_cauchy_process_at(times)
