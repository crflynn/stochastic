"""Bessel process."""
import numpy as np

from stochastic.processes.continuous.brownian_motion import BrownianMotion
from stochastic.utils.validation import check_positive_integer


class BesselProcess(BrownianMotion):
    r"""Bessel process.

    .. image:: _static/bessel_process.png
        :scale: 50%

    The Bessel process is the Euclidean norm of an :math:`n`-dimensional
    Wiener process, e.g. :math:`\|\mathbf{W}_t\|`

    Generate Bessel process realizations using :py:attr:`dim` independent
    Brownian motion processes on the interval :math:`[0,t]`

    :param int dim: the number of underlying independent Brownian motions to
        use
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, dim=1, t=1, rng=None):
        super().__init__(t=t, rng=rng)
        self.dim = dim

    def __str__(self):
        return "Bessel process of {d} Wiener processes on [0, {t}]".format(
            t=str(self.t), d=str(self.dim)
        )

    def __repr__(self):
        return "BesselProcess(dim={d}, t={t})".format(t=str(self.t), d=str(self.dim))

    @property
    def dim(self):
        """Dimensions, or independent Brownian motions."""
        return self._dim

    @dim.setter
    def dim(self, value):
        if not isinstance(value, int):
            raise TypeError("Dimension must be a positive integer.")
        if value < 1:
            raise ValueError("Dimension must be positive.")
        self._dim = value

    def _sample_bessel_process(self, n):
        """Generate a realization of a Bessel process."""
        check_positive_integer(n)
        samples = [self._sample_brownian_motion(n) for _ in range(self.dim)]
        return np.array([np.linalg.norm(coord) for coord in zip(*samples)])

    def _sample_bessel_process_at(self, times):
        """Generate a realization of a Bessel process."""
        samples = [self._sample_brownian_motion_at(times) for _ in range(self.dim)]
        return np.array([np.linalg.norm(coord) for coord in zip(*samples)])

    def sample(self, n):
        """Generate a realization.

        :param int n: the number of increments to generate
        """
        return self._sample_bessel_process(n)

    def sample_at(self, times):
        """Generate a realization using specified times.

        :param times: a vector of increasing time values at which to generate
            the realization
        """
        return self._sample_bessel_process_at(times)
