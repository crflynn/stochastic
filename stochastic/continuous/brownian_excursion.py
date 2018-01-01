"""Brownian excursion."""
import numpy as np

from stochastic.continuous.brownian_bridge import BrownianBridge


class BrownianExcursion(BrownianBridge):
    """Brownian excursion."""

    def __init__(self):
        super().__init__()

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

    # TODO
    # def sample_at(self, times)
        # pass
