"""Cox-Ingersoll-Ross process."""
import numpy as np

from stochastic.diffusion.ornstein_uhlenbeck import OrnsteinUhlenbeckProcess


class CoxIngersollRossProcess(OrnsteinUhlenbeckProcess):
    """Cox-Ingersoll-Ross process."""

    def __init__(self, t=1, speed=1, mean=1, vol=1):
        super().__init__(t, speed, mean, vol)

    def _volatility(self, arg):
        """Volatility term."""
        return np.sqrt(arg)


class CIRProcess(CoxIngersollRossProcess):
    """Alias for CoxIngersollRossProcess."""

    pass
