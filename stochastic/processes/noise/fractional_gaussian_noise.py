"""Fractional Gaussian noise."""
from functools import lru_cache

import numpy as np

from stochastic.processes.base import BaseTimeProcess
from stochastic.utils.validation import check_positive_integer


def _fgn_autocovariance(hurst, n):
    """Autocovariance function for fGn."""
    ns_2h = np.arange(n + 1) ** (2 * hurst)
    return np.insert((ns_2h[:-2] - 2 * ns_2h[1:-1] + ns_2h[2:]) / 2, 0, 1)


def _fgn_dh_sqrt_eigenvals(hurst, n):
    """Square-roots of normalized circulant matrix eigenvalues for fGn."""
    return np.fft.irfft(_fgn_autocovariance(hurst, n))[:n] ** (1 / 2)


class FractionalGaussianNoise(BaseTimeProcess):
    """Fractional Gaussian noise process.

    .. image:: _static/fractional_gaussian_noise.png
        :scale: 50%

    Generate sequences of fractional Gaussian noise.

    Hosking's method:

    * Hosking, Jonathan RM. "Modeling persistence in hydrological time series
      using fractional differencing." Water resources research 20, no. 12 (1984): 1898-1908.

    Davies Harte method:

    * Davies, Robert B., and D. S. Harte. "Tests for Hurst effect." Biometrika
      74, no. 1 (1987): 95-101.

    :param float hurst: The Hurst parameter value in :math:`(0,1)`.
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, hurst=0.5, t=1, rng=None):
        super().__init__(t=t, rng=rng)
        self.hurst = hurst
        self._autocovariance = lru_cache(1)(_fgn_autocovariance)
        self._dh_sqrt_eigenvals = lru_cache(1)(_fgn_dh_sqrt_eigenvals)

    def __str__(self):
        return "Fractional Gaussian noise with Hurst {h} on [0, {t}].".format(
            h=self.hurst, t=self.t
        )

    def __repr__(self):
        return "FractionalGaussianNoise(hurst={h}, t={t})".format(
            t=str(self.t), h=str(self.hurst)
        )

    @property
    def hurst(self):
        """Hurst parameter."""
        return self._hurst

    @hurst.setter
    def hurst(self, value):
        if not isinstance(value, float):
            raise TypeError("Hurst value must be a number on interval (0,1).")
        if value <= 0 or value >= 1:
            raise ValueError("Hurst value must be in interval (0,1).")
        self._hurst = value

    def _daviesharte(self, n):
        """Generate a fractional Gaussian noise using davies-harte method.

        Uses Davies and Harte method (exact method) from:
        Davies, Robert B., and D. S. Harte. "Tests for Hurst effect."
        Biometrika 74, no. 1 (1987): 95-101.
        """
        check_positive_integer(n)

        # For scaling to interval [0, T]
        increment = self.t / n
        scale = increment**self.hurst

        # If H = 0.5 then just generate a standard Brownian motion, otherwise
        # proceed with the Davies Harte method
        if self.hurst == 0.5:
            return self.rng.normal(scale=scale, size=n)

        else:
            # Generate some more fGns to use power-of-two FFTs for speed.
            m = 2 ** (n - 2).bit_length() + 1
            sqrt_eigenvals = self._dh_sqrt_eigenvals(self.hurst, m)

            # irfft results will be normalized by (2(m-1))**(3/2) but we only
            # want to normalize by 2(m-1)**(1/2).
            scale *= 2 ** (1 / 2) * (m - 1)

            w = self.rng.normal(scale=scale, size=2 * m).view(complex)
            w[0] = w[0].real * 2 ** (1 / 2)
            w[-1] = w[-1].real * 2 ** (1 / 2)

            # Resulting z is fft of sequence w.
            return np.fft.irfft(sqrt_eigenvals * w)[:n]

    def _hosking(self, n):
        """Generate fractional Gaussian noise using Hosking's method.

        Method of generation is Hosking's method (exact method) from his paper:
        Hosking, J. R. (1984). Modeling persistence in hydrological time series
        using fractional differencing. Water resources research, 20(12),
        1898-1908.

        Hosking's method generates a fractional Gaussian noise (fGn)
        realization. The cumulative sum of this realization gives a fBm.
        """
        # For scaling to interval [0, T]
        increment = self.t / n
        scale = increment**self.hurst

        gn = self.rng.normal(0.0, 1.0, n)

        # If H = 0.5 then just generate a standard Brownian motion, otherwise
        # proceed with Hosking's method
        if self.hurst == 0.5:
            fgn = gn
        else:
            # Initializations
            fgn = np.zeros(n)
            phi = np.zeros(n)
            psi = np.zeros(n)
            cov = self._autocovariance(self.hurst, n)

            # First increment from stationary distribution
            fgn[0] = gn[0]
            v = 1
            phi[0] = 0

            # Generates fgn realization with n increments of size 1
            for i in range(1, n):
                phi[i - 1] = cov[i]
                for j in range(i - 1):
                    psi[j] = phi[j]
                    phi[i - 1] -= psi[j] * cov[i - j - 1]
                phi[i - 1] /= v
                for j in range(i - 1):
                    phi[j] = psi[j] - phi[i - 1] * psi[i - j - 2]
                v *= 1 - phi[i - 1] * phi[i - 1]
                for j in range(i):
                    fgn[i] += phi[j] * fgn[i - j - 1]
                fgn[i] += np.sqrt(v) * gn[i]

        # Scale to interval [0, T]
        fgn *= scale

        return fgn

    def _sample_fractional_gaussian_noise(self, n, algorithm="daviesharte"):
        """Generate a realization of fractional Gaussian noise."""
        if algorithm == "daviesharte":
            return self._daviesharte(n)
        elif algorithm == "hosking":
            return self._hosking(n)
        else:
            raise ValueError("Algorithm must be daviesharte or hosking.")

    def sample(self, n, algorithm="daviesharte"):
        """Generate a realization of fractional Gaussian noise.

        :param int n: number of increments to generate
        :param str algorithm: either 'daviesharte' or 'hosking' algorithms
        """
        return self._sample_fractional_gaussian_noise(n, algorithm)
