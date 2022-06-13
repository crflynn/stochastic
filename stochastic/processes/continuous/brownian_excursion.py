"""Brownian excursion."""
import numpy as np

from stochastic.processes.continuous import BrownianBridge


class BrownianExcursion(BrownianBridge):
    r"""Brownian excursion.

    .. image:: _static/brownian_excursion.png
        :scale: 50%

    A Brownian excursion is a Brownian bridge from (0, 0) to (t, 0) which is
    conditioned to be nonnegative on the interval [0, t].

    Generated using method by

    * Biane, Philippe. "Relations entre pont et excursion du mouvement
      Brownien reel." Ann. Inst. Henri Poincare 22, no. 1 (1986): 1-7.

    * Vervaat, Wim. "A relation between Brownian bridge and Brownian
      excursion." The Annals of Probability (1979): 143-149.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, t=1, rng=None):
        super().__init__(t=t, rng=rng)

    def __str__(self):
        return "Brownian excursion on [0, {t}]".format(t=str(self.t))

    def __repr__(self):
        return "BrownianExcursion(t={t})".format(t=str(self.t))

    def _sample_brownian_excursion(self, n):
        """Generate a Brownian excursion."""
        brownian_bridge = self._sample_brownian_bridge(n)
        idx_min = np.argmin(brownian_bridge)
        s = np.array(
            [
                brownian_bridge[(idx_min + idx) % n] - brownian_bridge[idx_min]
                for idx in range(n + 1)
            ]
        )
        return s

    def _sample_brownian_excursion_at(self, times):
        """Generate a Brownian excursion."""
        if times[0] != 0:
            zero = False
            times = np.array([0] + list(times))
        else:
            zero = True
        brownian_bridge = self._sample_brownian_bridge_at(times)
        idx_min = np.argmin(brownian_bridge)
        n = len(brownian_bridge)
        s = np.array(
            [
                brownian_bridge[(idx_min + idx) % (n - 1)] - brownian_bridge[idx_min]
                for idx in range(n)
            ]
        )
        if zero:
            return s
        else:
            return s[1:]

    def sample(self, n):
        """Generate a realization.

        :param int n: the number of increments to generate.
        """
        return self._sample_brownian_excursion(n)

    def sample_at(self, times):
        """Generate a realization using specified times.

        :param times: a vector of increasing time values at which to generate
            the realization
        """
        return self._sample_brownian_excursion_at(times)
