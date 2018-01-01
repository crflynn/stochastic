"""Cox-Ingersoll-Ross process."""
import numpy as np

from stochastic.diffusion.ornstein_uhlenbeck import OrnsteinUhlenbeckProcess


class CoxIngersollRossProcess(OrnsteinUhlenbeckProcess):
    r"""Cox-Ingersoll-Ross process.

    A model for instantaneous interest rate.

    The process :math:`X_t` that satisfies the following stochastic
    differential equation with Wiener process :math:`W_t`:

    .. math::

        dX_t = \theta X_t (\mu - t) dt + \sigma \sqrt(X_t)dW_t

    Realizations are generated using the Euler-Maruyama method.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param float speed: the speed of reversion, or :math:`\theta` above
    :param float mean: the mean of the process, or :math:`\mu` above
    :param float vol: volatility coefficient of the process, or :math:`\sigma`
        above
    """

    def __init__(self, t=1, speed=1, mean=1, vol=1):
        super().__init__(t, speed, mean, vol)

    def _volatility(self, arg):
        """Volatility term."""
        return np.sqrt(arg)


class CIRProcess(CoxIngersollRossProcess):
    """Alias for CoxIngersollRossProcess."""

    pass
