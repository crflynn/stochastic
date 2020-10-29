from inspect import signature
from numbers import Number

import numpy as np

from stochastic.base import Continuous
from stochastic.noise import GaussianNoise


class DiffusionProcess(Continuous):
    r"""Generalized diffusion process.

    A base process for more specific diffusion processes.

    The process :math:`X_t` that satisfies the following
    stochastic differential equation with Wiener process :math:`W_t`:

    .. math::

        dX_t = \theta_t (\mu_t - X_t) dt + \sigma_t X_t^{\gamma_t} dW_t

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
    :param func volexp: volatility exponent of the process, or :math:`\gamma_t`
        above
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    """

    def __init__(self, speed=1, mean=0, vol=1, volexp=0, t=1):
        super().__init__(t)
        self.speed = speed
        self.mean = mean
        self.vol = vol
        self.volexp = volexp
        self.gn = GaussianNoise(t)

    def __str__(self):
        return "Diffusion process with speed={s}, mean={m}, vol={v}, volexp={e} on [0, {t}]".format(
            s=str(self.speed), m=str(self.mean), v=str(self.vol), e=str(self.volexp), t=str(self.t)
        )

    def __repr__(self):
        return "Diffusion(speed={s}, mean={m}, vol={v}, volexp={e} t={t})".format(
            s=str(self.speed), m=str(self.mean), v=str(self.vol), e=str(self.volexp), t=str(self.t)
        )

    def _default_const(self, value):
        def const(t):
            return value

        return const

    def _check_numeric_or_single_arg_callable(self, value, varname):
        is_numeric = isinstance(value, Number)
        is_callable = callable(value)
        if is_callable and len(signature(value).parameters) != 1:
            raise ValueError(f"{varname} callable must have a single argument")
        if not is_numeric and not is_callable:
            raise ValueError(f"{varname} must be numeric or a single argument callable")

    def _ensure_callable(self, value):
        if not callable(value):
            return self._default_const(value)
        return value

    @property
    def speed(self):
        """Speed, or :math:`\theta_t`."""
        return self._speed

    @speed.setter
    def speed(self, value):
        self._check_numeric_or_single_arg_callable(value, "speed")
        self._speed = self._ensure_callable(value)

    @property
    def mean(self):
        r"""Mean, or :math:`\mu_t`."""
        return self._mean

    @mean.setter
    def mean(self, value):
        self._check_numeric_or_single_arg_callable(value, "mean")
        self._mean = self._ensure_callable(value)

    @property
    def vol(self):
        r"""Volatility, or :math:`\sigma_t`."""
        return self._vol

    @vol.setter
    def vol(self, value):
        self._check_numeric_or_single_arg_callable(value, "vol")
        self._vol = self._ensure_callable(value)

    @property
    def volexp(self):
        r"""Volatility exponent, or :math:`\gamma_t`."""
        return self._volexp

    @volexp.setter
    def volexp(self, value):
        self._check_numeric_or_single_arg_callable(value, "volexp")
        self._volexp = self._ensure_callable(value)

    def _sample(self, n, initial=1.0):
        """Generate a realization of a Vasicek process."""
        self._check_increments(n)
        self._check_number(initial, "Initial")

        delta_t = 1.0 * self.t / n
        gns = self.gn.sample(n)

        s = [initial]
        t = 0
        for k in range(n):
            t += delta_t
            initial += (
                self._speed(t) * (self._mean(t) - initial) * delta_t
                + self._vol(t) * initial ** self._volexp(initial) * gns[k]
            )
            s.append(initial)

        return np.array(s)

    def sample(self, n, initial=1.0):
        """Generate a realization.

        :param int n: the number of increments to generate
        :param float initial: the initial value of the process
        """
        return self._sample(n, initial)
