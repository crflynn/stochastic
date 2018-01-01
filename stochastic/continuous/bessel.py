"""Bessel process."""
import numpy as np

from stochastic.base import Continuous
from stochastic.continuous.brownian_motion import BrownianMotion


class BesselProcess(Continuous):
    r"""Bessel process.

    The Bessel process is the Euclidean norm of an :math:`n`-dimensional
    Wiener process, e.g. :math:`\|\mathbf{W}_t\|`

    Generate Bessel process realizations using :py:attr:`dim` independent
    Brownian motion processes on the interval :math:`[0,t]`

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param int dim: the number of underlying independent Brownian motions to
        use
    """

    def __init__(self, t=1, dim=1):
        super().__init__(t)
        self.brownian_motions = []
        self.dim = dim
        for k in range(self.dim):
            self.brownian_motions.append(BrownianMotion(self.t))

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

    def _sample_bessel_process(self, n, zero=True):
        """Generate a realization of a Bessel process."""
        self._check_increments(n)
        self._check_zero(zero)

        samples = [bm.sample(n, zero) for bm in self.brownian_motions]

        return np.array([np.linalg.norm(coord) for coord in zip(*samples)])

    def sample(self, n, zero=True):
        """Generate a realization.

        :param int n: the number of increments to generate
        :param bool zero: if True, include :math:`t=0`
        """
        return self._sample_bessel_process(n, zero)
