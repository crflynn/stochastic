"""Brownian bridge."""
from stochastic.continuous.brownian_motion import BrownianMotion


class BrownianBridge(BrownianMotion):
    """Brownian bridge."""

    def __init__(self, t=1, b=0):
        super().__init__(t, drift=0, scale=1)
        self.b = b

    def __str__(self):
        return "Brownian bridge from 0 to {b} on [0, {t}]".format(
            t=str(self.t),
            b=str(self.b)
        )

    def __repr__(self):
        if self.t == 1:
            return "BrownianBridge(b={b})".format(
                t=str(self.t),
                b=str(self.b)
            )
        return "BrownianBridge(t={t}, b={b})".format(
            t=str(self.t),
            b=str(self.b),
        )

    def _sample_brownian_bridge(self, n, b=0, zero=True):
        """Generate a realization of a Brownian bridge."""
        self._check_number(b, "Time end")
        self._check_zero(zero)

        bm = self._sample_brownian_motion(n, zero)
        times = self.times(n, zero)

        return bm + times * (b - bm[-1]) / self.t

    def sample(self, n, b=0, zero=True):
        """Generate a realization of a Brownian bridge."""
        return self._sample_brownian_bridge(n, b, zero)

    # TODO
    # def sample_at(self, times):
    #     pass
