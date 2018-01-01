"""Geometric Brownian motion."""
import numpy as np

from stochastic.base import Continuous
from stochastic.continuous.brownian_motion import BrownianMotion


class GeometricBrownianMotion(Continuous):
    """Geometric Brownian motion process."""

    def __init__(self, t=1, drift=0, volatility=1):
        super().__init__(t)
        # TODO add getter setter to ensure bm is standard
        self._brownian_motion = BrownianMotion(self.t)
        self.drift = drift
        self.volatility = volatility

    @property
    def drift(self):
        """Geometric Brownian motion drift parameter."""
        return self._drift

    @drift.setter
    def drift(self, value):
        self._check_number(value, "Drift")
        self._drift = value

    @property
    def volatility(self):
        """Geometric Brownian motion volatility parameter."""
        return self._volatility

    @volatility.setter
    def volatility(self, value):
        self._check_positive_number(value, "Volatility")
        self._volatility = value

    def _sample_geometric_brownian_motion(self, n, initial=1, zero=True):
        """Generate a realization of geometric Brownian motion."""
        self._check_increments(n)
        self._check_positive_number(initial, "Initial")
        self._check_zero(zero)

        line = self._linspace(self.drift - self.volatility ** 2 / 2.0, n, zero)
        noise = self.volatility * self._brownian_motion.sample(n, zero)

        return initial * np.exp(line + noise)

    def sample(self, n, initial=1, zero=True):
        """Generate a realization of geometric Brownian motion."""
        return self._sample_geometric_brownian_motion(n, initial, zero)

    # TODO
    # def sample_at(self, times):
    #     pass
