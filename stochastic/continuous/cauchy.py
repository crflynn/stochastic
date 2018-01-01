"""Cauchy processes."""
import numpy as np
from scipy.stats import levy

from stochastic.base import Continuous
from stochastic.continuous.brownian_motion import BrownianMotion


class CauchyProcess(Continuous):
    """Symmetric Cauchy process."""

    def __init__(self, t=1):
        super().__init__(t)
        self.brownian_motion = BrownianMotion(t)

    def _sample_cauchy_process(self, n, zero=True):
        """Generate a realization of a Cauchy process."""
        self._check_increments(n)
        self._check_zero(zero)

        delta_t = 1.0 * self.t / n
        times = np.cumsum(levy.rvs(loc=0, scale=delta_t ** 2 / 2, size=n))

        return self.brownian_motion.sample_at(times, zero=zero)

    def sample(self, n, zero=True):
        """Generate a realization of a Cauchy process."""
        return self._sample_cauchy_process(n, zero)
