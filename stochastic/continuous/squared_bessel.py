"""Squared Bessel process."""
import numpy as np

from stochastic.continuous.bessel import BesselProcess


class SquaredBesselProcess(BesselProcess):
    """Squared Bessel process.

    The square of a Bessel process.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param int dim: the number of underlying independent Brownian motions to
        use
    """

    def _sample_squared_bessel_process(self, n, zero=True):
        """Generate a realization of a squared Bessel process."""
        self._check_increments(n)
        self._check_zero(zero)

        samples = [bm.sample(n, zero) for bm in self.brownian_motions]

        return np.array([
            sum(map(lambda x: x**2, coord))
            for coord in zip(*samples)
        ])

    def sample(self, n, zero=True):
        """Generate a realization of a squared Bessel process.

        :param int n: the number of increments to generate
        :param bool zero: if True, include :math:`t=0`
        """
        return self._sample_squared_bessel_process(n, zero)
