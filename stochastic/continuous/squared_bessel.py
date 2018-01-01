"""Squared Bessel process."""
import numpy as np

from stochastic.continuous.bessel import BesselProcess


class SquaredBesselProcess(BesselProcess):
    r"""Squared Bessel process.

    The square of a Bessel process: :math:`\|\mathbf{W}_t\|^2`.

    The Bessel process is the Euclidean norm of an :math:`n`-dimensional
    Wiener process, e.g. :math:`\|\mathbf{W}_t\|`

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
        """Generate a realization.

        :param int n: the number of increments to generate
        :param bool zero: if True, include :math:`t=0`
        """
        return self._sample_squared_bessel_process(n, zero)
