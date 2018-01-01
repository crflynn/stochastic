"""Brownian meander."""
import numpy as np

from stochastic.continuous.brownian_motion import BrownianMotion


class BrownianMeander(BrownianMotion):
    """Brownian meander process."""

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Brownian meander"""

    def __repr__(self):
        return "BrownianMeander()"

    def _sample_brownian_meander(self, n, b=None):
        """Generate a Brownian meander realization.

        Williams, 1970, or Imhof, 1984.
        """
        if b is None:
            b = np.sqrt(2 * np.random.exponential())
        else:
            self._check_number(b, "Right endpoint")
            if b < 0:
                raise ValueError("Right endpoint must be nonnegative.")
        bridge_1 = self._sample_brownian_bridge()
        bridge_2 = self._sample_brownian_bridge()
        bridge_3 = self._sample_brownian_bridge()
        times = self.times(n)

        return np.sqrt(
            (b * times + bridge_1) ** 2 + bridge_2 ** 2 + bridge_3 ** 2
        )

    def sample(self, n, b=None):
        """Generate a Brownian meander realization."""
        return self._sample_brownian_meander(b)

    # TODO
    # def sample_at(self):
    #     pass
