"""Fractional Gaussian noise."""
import logging

import numpy as np

from stochastic.base import Continuous


class FractionalGaussianNoise(Continuous):
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

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param float hurst: The Hurst parameter value in :math:`(0,1)`.
    """

    def __init__(self, t=1, hurst=0.5):
        super(FractionalGaussianNoise, self).__init__(t)
        self.hurst = hurst
        self._n = None
        self._eigenvals = None
        self._cov = None

    def __str__(self):
        return "Fractional Gaussian noise with Hurst {h} on [0, {t}].".format(
            h=self.hurst,
            t=self.t
        )

    def __repr__(self):
        return "FractionalGaussianNoise(t={t}, hurst={h})".format(
            t=str(self.t),
            h=str(self.hurst)
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

    def _autocovariance(self, k):
        """Autocovariance function for fractional Gaussian noise."""
        return 0.5 * (abs(k - 1) ** (2 * self.hurst) - 2 *
                      abs(k) ** (2 * self.hurst) +
                      abs(k + 1) ** (2 * self.hurst))

    def _daviesharte(self, n):
        """Generate a fractional Gaussian noise using davies-harte method.

        Uses Davies and Harte method (exact method) from:
        Davies, Robert B., and D. S. Harte. "Tests for Hurst effect."
        Biometrika 74, no. 1 (1987): 95-101.
        """
        self._check_increments(n)

        # For scaling to interval [0, T]
        increment = 1.0 * self.t / n
        scale = increment ** self.hurst

        fgn = np.random.normal(0.0, 1.0, n)

        # If H = 0.5 then just generate a standard Brownian motion, otherwise
        # proceed with the Davies Harte method
        if self.hurst == 0.5:
            pass
        else:
            if self._n != n:
                self._n = n
                # Generate first row of circulant matrix
                row_component = [self._autocovariance(i) for i in range(1, n)]
                reverse_component = [row_component[-i] for i in range(1, n)]
                row = [self._autocovariance(0)] + row_component + \
                    [0] + reverse_component

                # Get eigenvalues of circulant matrix
                # Discard imaginary part (should all be zero in theory so
                # imaginary part will be very small)
                self._eigenvals = np.fft.fft(row).real

            if np.any([ev < 0 for ev in self._eigenvals]):
                logging.warning(
                    "Combination of increments n and Hurst value "
                    "H invalid for Davies-Harte method. Reverting to Hosking "
                    "method. Try increasing n or decreasing H")
                return self._hosking(n)

            # Generate second sequence of i.d.d. standard normals
            fgn2 = np.random.normal(0.0, 1.0, n)

            # Resulting sequence from matrix multiplication of positive
            # definite sqrt(C) matrix with fgn sample can be simulated
            # this way.
            w = np.zeros(2 * n, dtype=complex)
            for i in range(2 * n):
                if i == 0:
                    w[i] = np.sqrt(self._eigenvals[i] / (2 * n)) * fgn[i]
                elif i < n:
                    w[i] = np.sqrt(self._eigenvals[i] / (4 * n)) * \
                        (fgn[i] + 1j * fgn2[i])
                elif i == n:
                    w[i] = np.sqrt(self._eigenvals[i] / (2 * n)) * fgn2[0]
                else:
                    w[i] = np.sqrt(self._eigenvals[i] / (4 * n)) * \
                        (fgn[2 * n - i] - 1j * fgn2[2 * n - i])

            # Resulting z is fft of sequence w. Discard small imaginary part (z
            # should be real in theory).
            z = np.fft.fft(w)
            fgn = z[:n].real

        # Scale to interval [0, T]
        fgn *= scale

        return fgn

    def _hosking(self, n):
        """Generate fractional Gaussian noise using Hosking"s method.

        Method of generation is Hosking"s method (exact method) from his paper:
        Hosking, J. R. (1984). Modeling persistence in hydrological time series
        using fractional differencing. Water resources research, 20(12),
        1898-1908.

        Hosking"s method generates a fractional Gaussian noise (fGn)
        realization. The cumulative sum of this realization gives a fBm.
        """
        # For scaling to interval [0, T]
        increment = 1.0 * self.t / n
        scale = increment ** self.hurst

        gn = np.random.normal(0.0, 1.0, n)

        # If H = 0.5 then just generate a standard Brownian motion, otherwise
        # proceed with Hosking"s method
        if self.hurst == 0.5:
            fgn = gn
        else:
            # Initializations
            fgn = np.zeros(n)
            phi = np.zeros(n)
            psi = np.zeros(n)
            if self._n != n or self._cov is None:
                self._cov = np.array([self._autocovariance(i)
                                      for i in range(n)])

            # First increment from stationary distribution
            fgn[0] = gn[0]
            v = 1
            phi[0] = 0

            # Generates fgn realization with n increments of size 1
            for i in range(1, n):
                phi[i - 1] = self._cov[i]
                for j in range(i - 1):
                    psi[j] = phi[j]
                    phi[i - 1] -= psi[j] * self._cov[i - j - 1]
                phi[i - 1] /= v
                for j in range(i - 1):
                    phi[j] = psi[j] - phi[i - 1] * psi[i - j - 2]
                v *= (1 - phi[i - 1] * phi[i - 1])
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
