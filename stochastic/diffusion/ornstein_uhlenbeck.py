"""Ornstein-Uhlenbeck process."""
import numpy as np

from stochastic.base import Continuous
from stochastic.noise.gaussian_noise import GaussianNoise


class OrnsteinUhlenbeckProcess(Continuous):
    r"""Ornstein-Uhlenbeck process.

    .. image:: _static/ornstein_uhlenbeck_process.png
        :scale: 50%

    The process :math:`X_t` that satisfies the following stochastic
    differential equation with Wiener process :math:`W_t`:

    .. math::

        dX_t = \theta X_t (\mu - t) dt + \sigma dW_t

    Realizations are generated using the Euler-Maruyama method.

    :param float speed: the speed of reversion, or :math:`\theta` above
    :param float mean: the mean of the process, or :math:`\mu` above
    :param float vol: volatility coefficient of the process, or :math:`\sigma`
        above
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    """

    def __init__(self, speed=1, mean=1, vol=1, t=1):
        super(OrnsteinUhlenbeckProcess, self).__init__(t)
        self.speed = speed
        self.mean = mean
        self.vol = vol
        self.gn = GaussianNoise(t)

    def __str__(self):
        return "Ornstein-Uhlenbeck process with speed={s}, mean={m}, vol={v} on [0, {t}]".format(
            s=str(self.speed), m=str(self.mean), v=str(self.vol), t=str(self.t)
        )

    def __repr__(self):
        return "OrnsteinUhlenbeckProcess(speed={s}, mean={m}, vol={v}, t={t})".format(
            s=str(self.speed), m=str(self.mean), v=str(self.vol), t=str(self.t)
        )

    @property
    def speed(self):
        """Speed of reversion."""
        return self._speed

    @speed.setter
    def speed(self, value):
        self._check_number(value, "Speed")
        self._speed = value

    @property
    def mean(self):
        """Mean of process."""
        return self._mean

    @mean.setter
    def mean(self, value):
        self._check_number(value, "Mean")
        self._mean = value

    @property
    def vol(self):
        """Volatility parameter."""
        return self._vol

    @vol.setter
    def vol(self, value):
        self._check_number(value, "Vol")
        self._vol = value

    def _volatility(self, arg):
        """Volatility coefficient.

        This method is overridden in subclasses for more specific stochastic
        volatility processes.
        """
        return 1

    def _sample(self, n, initial=1, zero=True):
        """Generate a realization of a Ornstein-Uhlenbeck process."""
        self._check_increments(n)
        self._check_zero(zero)
        self._check_number(initial, "Initial")

        delta_t = 1.0 * self.t / n
        gns = self.gn.sample(n)

        s = []
        if zero:
            s.append(initial)
        for k in range(n):
            initial += self.speed * (self.mean - initial) * delta_t + self.vol * self._volatility(initial) * gns[k]
            s.append(initial)

        return np.array(s)

    def sample(self, n, initial=1, zero=True):
        """Generate a realization.

        :param int n: the number of increments to generate
        :param float initial: the initial value of the process
        :param bool zero: if True, include :math:`t=0`
        """
        return self._sample(n, initial, zero)


class OUProcess(OrnsteinUhlenbeckProcess):
    """Alias for OrnsteinUhlenbeckProcess."""

    pass
