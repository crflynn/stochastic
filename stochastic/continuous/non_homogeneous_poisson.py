"""Poisson processes."""
import numpy as np
import scipy.optimize
import scipy.integrate

from stochastic.base import Checks
import matplotlib.pyplot as plt
import sys

class NonHomogeneousPoissonProcess(Checks):
    r"""Non-homogeneous Poisson process.

    .. image:: _static/non_homogeneous_poisson_process.png
    :scale: 50%

    A Poisson process whose rate :math:`\lambda` is a function of time or the
    underlying data space :math:`\lambda\to\lambda(t)`.

    2. Note: This class can be used to create a Cox process by injecting a
    :math:`\lambda(t)` matrix generated using another stochastic process.

    :param callable rate_func: the rate function
    :param tuple rate_args: positional args for ``rate_func``
    :param dict rate_kwargs: keyword args for ``rate_func``
    """

    def __init__(self, rate_func, rate_args=(), rate_kwargs={}):
        self.rate_func = rate_func
        self.rate_args = rate_args
        self.rate_kwargs = rate_kwargs

    def __str__(self):
        return "Non-homogeneous Poisson process with rate function of time."

    def __repr__(self):
        return "NonHomogeneousPoissonProcess(" \
            "rate_func={rf}, rate_args={ra}, rate_kwargs={rkw})".format(
                rf=str(self.rate_func),
                ra=str(self.rate_args),
                rkw=str(self.rate_kwargs)
            )

    @property
    def rate_func(self):
        """Current rate's distribution."""
        return self._rate_func

    @rate_func.setter
    def rate_func(self, value):
        if not callable(value):
            raise ValueError("Rate function must be a callable.")
        self._rate_func = value

    @property
    def rate_args(self):
        """Positional arguments for the rate function."""
        return self._rate_args

    @rate_args.setter
    def rate_args(self, value):
        if not isinstance(value, (list, tuple)):
            raise ValueError("Rate args must be a list or tuple.")
        self._rate_args = value

    @property
    def rate_kwargs(self):
        """Keyword arguments for the rate function."""
        return self._rate_kwargs

    @rate_kwargs.setter
    def rate_kwargs(self, value):
        if not isinstance(value, dict):
            raise ValueError("Rate kwargs must be a dict.")
        self._rate_kwargs = value

    def _wrapper_kwargs(self, *args, **kwargs):
        """Wrapper function, because kwargs cannot be passed to
        scipy.integrate.quad.
        """
        def func(x):
            return self.rate_func(x, *args, **kwargs)
        return(func)

    def _invert_rate_func(self, func_to_wrap, time):
        def func(x):
            return np.abs(time - scipy.integrate.quad(func_to_wrap, 0, x)[0])
        return func

    def _sample_nhpp_order(self, n=None, length=None, zero=True):
        return

    def _sample_nhpp_inversion(self, n=None, length=None, zero=True):
        """Generate a realization of a Non-Homogeneous Poisson process using
        the inversion algorithm. Only 1D. First, event times of homogeneous
        poisson process are generated. Then, the expectation function, the
        integral of the rate function, is used to transform these event times.
        """
        if n is not None:
                times = np.array([0])
                means = np.array([0])
                while len(means) < n:
                    mean = 0
                    while (mean == means[-1]) | (mean == 0):
                        time = -np.log(np.random.uniform())
                        wrapped_rate_func = self._wrapper_kwargs(
                                                            *self.rate_args,
                                                            **self.rate_kwargs)
                        inverted = self._invert_rate_func(wrapped_rate_func,
                                                          times[-1])
                        mean = scipy.optimize.minimize(inverted,
                                                       times[-1]+time,
                                                       bounds = ((means[-1],
                                                                  np.inf),)).x
                        # print(wrapped_rate_func(times[-1]))
                        # print(mean, means[-1], time, times[-1])
                    times = np.append(times, time+times[-1])
                    means = np.append(means, mean)
        if length is not None:
            times = np.array([0])
            means = np.array([0])
            while means[-1] < length:
                mean = 0
                while (mean == means[-1]) | (mean == 0):
                    wrapped_rate_func = self._wrapper_kwargs(*self.rate_args,
                                                             **self.rate_kwargs)
                    inverted = self._invert_rate_func(wrapped_rate_func,
                                                      times[-1])
                    mean = scipy.optimize.minimize(inverted,
                                                   times[-1],
                                                   bounds = ((means[-1],
                                                              np.inf),)).x
                    times = np.append(times,
                                      times[-1] + np.random.exponential())
                means = np.append(means, mean)
        return(means[1-zero:])

    def _sample_nhpp_thinning(self, n=None, length=None, zero=True):
        """Generate a realization of a Non-Homogeneous Poisson process using
        the thinning or acceptance/rejection algorithm. Points are generated
        using a computed max rate, then accepted with a probability
        proportional to the rate function.
        """
        thinned = np.array([0])
        wrapped_rate_func = self._wrapper_kwargs(*self.rate_args, **self.rate_kwargs)
        if n is not None:
            self._check_increments(n)
            inverted = self._invert_rate_func(wrapped_rate_func, n)
            mean_time_at_n = scipy.optimize.minimize(inverted,
                                                     n,
                                                     bounds = ((0, np.inf),)).x
            def to_minimize(x): return(-wrapped_rate_func(x))
            rate_max =  wrapped_rate_func(scipy.optimize.minimize(to_minimize, 0, bounds=((0, mean_time_at_n*5),)).x)
            unthinned = 0
            while len(thinned) < n:
                unthinned = unthinned - np.log(np.random.uniform())/rate_max
                if np.random.uniform() <= self.rate_func(unthinned)/rate_max:
                    thinned = np.append(thinned, unthinned)
            return(thinned[1-zero:])
        elif length is not None:
            self._check_positive_number(length, "Sample length")
            def to_minimize(x): return(-wrapped_rate_func(x))
            rate_max =  wrapped_rate_func(scipy.optimize.minimize(to_minimize, 0, bounds=((0, length),)).x)
            unthinned = 0
            while unthinned < length:
                unthinned = unthinned - np.log(np.random.uniform())/rate_max
                if np.random.uniform() <= self.rate_func(unthinned)/rate_max:
                    thinned = np.append(thinned, unthinned)
            return(thinned[1-zero:])
        else:
            raise ValueError("Must provide argument n.")

    def sample(self, n=None, length=None, zero=True, algo='inversion'):
        """Generate a realization.

        :param int n: the number of points to simulate
        """
        if algo == 'thinning':
            return(self._sample_nhpp_thinning(n, length, zero))
        elif algo == 'inversion':
            return(self._sample_nhpp_inversion(n, length, zero))
        elif algo == 'order':
            return(self._sample_nhpp_order(n, length, zero))
        else:
            raise ValueError("Argument algo must be 'thinning', 'order' or 'inversion'.")
    def times(self, *args, **kwargs):
        """Disallow times for this process."""
        raise AttributeError(
        "NonHomogeneousPoissonProcess object has no attribute times.")
