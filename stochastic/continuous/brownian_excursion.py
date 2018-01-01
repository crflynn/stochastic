"""Brownian excursion."""
import numpy as np

from stochastic.continuous.brownian_bridge import BrownianBridge


class BrownianExcursion(BrownianBridge):
    """Brownian excursion.

    A Brownian excursion is a Brownian bridge from (0, 0) to (t, 0) which is
    conditioned to be nonnegative on the interval [0, 1].

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    """

    def __init__(self, t=1):
        super().__init__(t)

    def __str__(self):
        return "Brownian excursion"""

    def __repr__(self):
        return "BrownianExcursion()"

    def _sample_brownian_excursion(self, n, zero=True):
        """Generate a Brownian excursion."""
        brownian_bridge = self._sample_brownian_bridge(n)
        idx_min = np.argmin(brownian_bridge)
        return np.array(
            [brownian_bridge[idx_min + idx % n] - brownian_bridge[idx_min]
             for idx in range(n + 1)]
        )

    def sample(self, n, zero=True):
        """Generate a Brownian excursion."""
        return self._sample_brownian_excursion(n)

    def sample_at(self, times):
        """TODO"""
        raise NotImplementedError
