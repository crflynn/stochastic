"""Squared Bessel process."""
import numpy as np

from stochastic.processes.continuous.bessel import BesselProcess
from stochastic.utils.validation import check_positive_integer


class SquaredBesselProcess(BesselProcess):
    r"""Squared Bessel process.

    .. image:: _static/squared_bessel_process.png
        :scale: 50%

    The square of a Bessel process: :math:`\|\mathbf{W}_t\|^2`.

    The Bessel process is the Euclidean norm of an :math:`n`-dimensional
    Wiener process, e.g. :math:`\|\mathbf{W}_t\|`

    :param int dim: the number of underlying independent Brownian motions to
        use
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    """

    def _sample_squared_bessel_process(self, n):
        """Generate a realization of a squared Bessel process."""
        check_positive_integer(n)

        samples = [self._sample_brownian_motion(n) for _ in range(self.dim)]

        return np.array([sum(map(lambda x: x**2, coord)) for coord in zip(*samples)])

    def _sample_squared_bessel_process_at(self, times):
        """Generate a realization of a squared Bessel process."""
        samples = [self._sample_brownian_motion_at(times) for _ in range(self.dim)]

        return np.array([sum(map(lambda x: x**2, coord)) for coord in zip(*samples)])

    def sample(self, n):
        """Generate a realization.

        :param int n: the number of increments to generate
        """
        return self._sample_squared_bessel_process(n)

    def sample_at(self, times):
        """Generate a realization using specified times.

        :param times: a vector of increasing time values at which to generate
            the realization
        """
        return self._sample_squared_bessel_process_at(times)
