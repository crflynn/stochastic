"""Ornstein-Uhlenbeck process."""
from stochastic.processes.diffusion.vasicek import VasicekProcess


class OrnsteinUhlenbeckProcess(VasicekProcess):
    r"""Ornstein-Uhlenbeck process.

    .. image:: _static/ornstein_uhlenbeck_process.png
        :scale: 50%

    The process :math:`X_t` that satisfies the following stochastic
    differential equation with Wiener process :math:`W_t`:

    .. math::

        dX_t = - \theta X_t dt + \sigma dW_t

    Realizations are generated using the Euler-Maruyama method.

    .. note::

        Since the family of diffusion processes have parameters which
        generalize to functions of ``t``, parameter attributes will be returned
        as callables, even if they are initialized as constants. e.g. a
        ``speed`` parameter of 1 accessed from an instance attribute will return
        a function which accepts a single argument and always returns 1.

    :param float speed: the speed of reversion, or :math:`\theta` above
    :param float vol: volatility coefficient of the process, or :math:`\sigma`
        above
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, speed=1, vol=1, t=1, rng=None):
        super().__init__(speed=speed, mean=0, vol=vol, t=t, rng=None)

    def __str__(self):
        return "Ornstein-Uhlenbeck process with speed={s}, vol={v} on [0, {t}]".format(
            s=str(self.speed), m=str(self.mean), v=str(self.vol), t=str(self.t)
        )

    def __repr__(self):
        return "OrnsteinUhlenbeckProcess(speed={s}, vol={v}, t={t})".format(
            s=str(self.speed), m=str(self.mean), v=str(self.vol), t=str(self.t)
        )
