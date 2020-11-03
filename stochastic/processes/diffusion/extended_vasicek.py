from stochastic.processes.diffusion.diffusion import DiffusionProcess


class ExtendedVasicekProcess(DiffusionProcess):
    r"""Extended Vasicek process.

    A model for future interest rates.

    .. image:: _static/extended_vasicek_process.png
        :scale: 50%

    The ExtendedVasicek process :math:`X_t` that satisfies the following
    stochastic differential equation with Wiener process :math:`W_t`:

    .. math::

        dX_t = \theta_t (\mu_t - X_t) dt + \sigma_t dW_t

    Realizations are generated using the Euler-Maruyama method.

    .. note::

        Since the family of diffusion processes have parameters which
        generalize to functions of ``t``, parameter attributes will be returned
        as callables, even if they are initialized as constants. e.g. a
        ``speed`` parameter of 1 accessed from an instance attribute will return
        a function which accepts a single argument and always returns 1.

    :param func speed: the speed of reversion, or :math:`\theta_t` above
    :param func mean: the mean of the process, or :math:`\mu_t` above
    :param func vol: volatility coefficient of the process, or :math:`\sigma_t`
        above
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, speed=1, mean=0, vol=1, t=1, rng=None):
        super().__init__(speed=speed, mean=mean, vol=vol, volexp=0, t=t, rng=rng)

    def __str__(self):
        return "Extended Vasicek process with speed={s}, mean={m}, vol={v} on [0, {t}]".format(
            s=str(self.speed), m=str(self.mean), v=str(self.vol), t=str(self.t)
        )

    def __repr__(self):
        return "ExtendedVasicekProcess(speed={s}, mean={m}, vol={v}, t={t})".format(
            s=str(self.speed), m=str(self.mean), v=str(self.vol), t=str(self.t)
        )
