"""Inverse Gaussian process."""
import inspect

import numpy as np

from stochastic.processes.base import BaseTimeProcess
from stochastic.utils.validation import check_positive_number


class InverseGaussianProcess(BaseTimeProcess):
    r"""Inverse Gaussian process.

    .. image:: _static/inverse_gaussian.png
        :scale: 50%

    An inverse Gaussian process has independent increments which follow an
    inverse Gaussian distribution with parameters defined by a monotonically
    increasing function, :math:`\Gamma(t)`. E.g. for increment :math:`[s, t]`:

    :math:`\mathcal{IG}(\Gamma(t) - \Gamma(s), \eta(\Gamma(t) - \Gamma(s))^2)`

    Uses a method for generating inverse Gaussian variates from:

    * Michael, John R., William R. Schucany, and Roy W. Haas. "Generating
      random variates using transformations with multiple roots." The
      American Statistician 30, no. 2 (1976): 88-90.

    :param callable mean: a callable with one argument :math:`\Gamma(t)` such
        that :math:`\Gamma(t') > \Gamma(t) \forall t' > t`. Default is the
        identity function.
    :param float scale: scale factor of the shape parameter of the inverse
        gaussian, or :math:`\eta` from the above equation.
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, mean=None, scale=1, t=1, rng=None):
        super().__init__(t=t, rng=rng)
        if mean is None:
            self.mean = lambda x: x
        else:
            self.mean = mean
        self.scale = scale
        self._n = None
        self._ms = None

    def __str__(self):
        s = "Inverse Gaussian process with mean {m} and scale {s} on interval [0, {t}]."
        return s.format(t=str(self.t), m=str(self.mean.__name__), s=str(self.scale))

    def __repr__(self):
        return "InverseGaussianProcess(mean={m}, scale={s}, t={t})".format(
            t=str(self.t), m=str(self.mean.__name__), s=str(self.scale)
        )

    @property
    def mean(self):
        """Mean function."""
        return self._mean

    @mean.setter
    def mean(self, value):
        try:
            num_args = len(inspect.signature(value).parameters)
        except Exception:
            raise ValueError("Mean must be a function of one argument.")
        if not callable(value) or num_args != 1:
            raise ValueError("Mean must be a function of one argument.")
        self._mean = value

    @property
    def scale(self):
        """Scale parameter."""
        return self._scale

    @scale.setter
    def scale(self, value):
        check_positive_number(value, "Scale")
        self._scale = value

    def _check_mean(self, left, right):
        """Check the validity of the mean function."""
        delta = self.mean(right) - self.mean(left)
        if delta <= 0:
            raise ValueError("Mean must be monotonically increasing.")
        return delta

    def _sample_inverse_gaussian_process(self, n):
        """Generate a realization of the inverse Gaussian process.

        Generate an inverse Gaussian process realization with n increments.
        """
        if self._n != n:
            self._set_times(n)
            self._ms = []
            for k in range(n):
                self._ms.append(self._check_mean(self._times[k], self._times[k + 1]))
            self._ms = np.array(self._ms)

        ls = np.array([self.scale * m**2 for m in self._ms])

        gn = self.rng.normal(size=n)
        ys = gn**2

        xs = (
            self._ms
            + self._ms**2 * ys / 2 / ls
            - self._ms
            / 2
            / ys
            * np.sqrt(4 * self._ms * ls * ys + self._ms**2 * ys**2)
        )

        zs = self.rng.uniform(size=n)

        ign = []
        for z, x, m in zip(zs, xs, self._ms):
            if z <= m / (m + x):
                ign.append(x)
            else:
                ign.append(m**2 / x)

        ig = np.array(ign).cumsum()
        ig = np.insert(ig, [0], 0)
        return ig

    def sample(self, n):
        """Generate a realization.

        :param int n: the number of increments to generate
        """
        return self._sample_inverse_gaussian_process(n)

    def _sample_inverse_gaussian_process_at(self, times):
        """Generate an inverse Gaussian process at specified times."""
        n = len(times) - 1
        if times[0] != 0:
            times = np.concatenate(([0], times))

        ms = []
        for k in range(n):
            ms.append(self._check_mean(times[k], times[k + 1]))
        ms = np.array(ms)

        ls = np.array([self.scale * m**2 for m in ms])

        gn = self.rng.normal(size=n)
        ys = gn**2

        xs = (
            ms
            + ms**2 * ys / 2 / ls
            - ms / 2 / ys * np.sqrt(4 * ms * ls * ys + ms**2 * ys**2)
        )

        zs = self.rng.uniform(size=n)

        ign = []
        for z, x, m in zip(zs, xs, ms):
            if z <= m / (m + x):
                ign.append(x)
            else:
                ign.append(m**2 / x)

        ig = np.array(ign).cumsum()
        if times[0] == 0:
            ig = np.insert(ig, 0, [0])

        return ig

    def sample_at(self, times):
        """Generate a realization using specified times.

        :param times: a vector of increasing time values at which to generate
            the realization
        """
        return self._sample_inverse_gaussian_process_at(times)
