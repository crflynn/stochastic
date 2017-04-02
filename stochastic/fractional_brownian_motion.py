import numpy as np
from warnings import warn


class FractionalBrownianMotion(object):
    """
    A fractional Brownian motion (discretely sampled) has correlated Gaussian
    increments defined by Hurst parameter H. When H == 1/2, the process
    is a standard Brownian motion. When H > 1/2, the increments are
    positively correlated. When H < 1/2, the increments are negatively
    correlated.

    args:
        t (float) = end time of process

    methods:

    sample
        args:
            n (int) = number of increments in the sample
            zero (bool) = flag to include W_t=0
        returns:
            (list) of values of the Brownian motion sample

    times
        args:
            n (int) = number of increments in the sample
            zero (bool) = flag to include t_0=0
        returns:
            (list) of times corresponding the Brownian motion sample
    """

    def __init__(self, T=1, H=0.5, method='daviesharte'):
        self.T = T
        self.H = H
        methods = {'daviesharte': self._daviesharte,
                   'cholesky': self._cholesky,
                   'hosking': self._hosking
                   }

        try:
            self._method = methods[method]
        except KeyError:
            raise ValueError('Method must be \'daviesharte\', \'hosking\' '
                             'or \'cholesky\'')

    def __str__(self):
        return 'Fractional Brownian motion on interval [0, {}] and Hurst ' \
               'parameter H = {} using {} method.'.format(
                   self.T, self.H, self._method)

    def __repr__(self):
        return self.__str__()

    @property
    def T(self):
        return self._T

    @T.setter
    def T(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Time end value must be a number.')
        if value <= 0:
            raise ValueError('Time end value must be positive.')
        self._T = float(value)

    @property
    def H(self):
        return self._H

    @H.setter
    def H(self, value):
        if not isinstance(value, (float)):
            raise TypeError('Hurst value must be a number.')
        if value <= 0 or value >= 1:
            raise ValueError('Hurst value must be in interval (0,1).')
        self._H = float(value)

    def _autocovariance(self, H, k):
        """
        Autocovariance function for fractional Gaussian noise.
        args:
            H (float): Hurst parameter, between 0 and 1 exclusive.
            k (float): Distance between increments.
        returns:
            (float): The autocovariance for a fgn for parameters H, k
        """
        return 0.5 * (abs(k - 1) ** (2 * H) - 2 * abs(k) ** (2 * H) +
                      abs(k + 1) ** (2 * H))

    def _check_zero(self, zero):
        if not isinstance(zero, bool):
            raise TypeError('Zero inclusion flag must be a boolean.')

    def _check_input(self, n, H, T):
        if not isinstance(n, int) or n <= 0:
            raise ValueError('Number of increments must be a positive integer')
        if not isinstance(H, (float)) or H <= 0 or H >= 1:
            raise ValueError('Hurst parameter must be in interval (0, 1).')
        if not isinstance(T, (int, float)) or T <= 0:
            raise ValueError('Length of fbm must be greater than 0.')

    def _check_increments(self, n):
        if not isinstance(n, int):
            raise TypeError('Number of increments must be an int.')
        if n <= 0:
            raise ValueError('Number of increments must be positive.')

    def sample(self, n):
        return self._method(n, self.H, self.T)

    def times(self, n, zero=True):
        self._check_increments(n)
        self._check_zero(zero)

        return self._linspace(self.T, n, zero)

    def _daviesharte(self, n, H=0.5, T=1):
        """
        Uses Davies and Harte method (exact method) from:
        Davies, Robert B., and D. S. Harte. "Tests for Hurst effect." Biometrika
        74, no. 1 (1987): 95-101.
        args:
            n (int): The number of increments for the fbm.
            H (float): Hurst parameter, between 0 and 1 exclusive.
            T (float): The length of the realization, nonnegative.
        returns:
            fbm (list(float)): A fbm realization from t=0 to t=T of length n+1.
            fgn (list(float)): The corresponding fgn realization of length n.
            t (list(float)): A list of time values associated with the fbm.
        raises:
            TypeError: if the input n is nonnegative or non-integer
            ValueError: if the Hurst parameter is outside (0,1) or T is negative
        """

        # Input checking
        self._check_input(n, H, T)

        # For scaling to interval [0, T]
        increment = float(T) / n
        scale = increment ** H

        fgn = np.random.normal(0.0, 1.0, n)

        # If H = 0.5 then just generate a standard Brownian motion, otherwise
        # proceed with the Davies Harte method
        if H == 0.5:
            pass
        else:
            # Generate first row of circulant matrix
            row_component = [self._autocovariance(H, i) for i in range(1, n)]
            reverse_component = [row_component[-i] for i in range(1, n)]
            row = [self._autocovariance(H, 0)] + row_component + \
                [0] + reverse_component

            # Get eigenvalues of circulant matrix
            # Discard imaginary part (should all be zero in theory so imaginary
            # part will be very small)
            eigenvals = np.fft.fft(row).real
            if np.any([ev < 0 for ev in eigenvals]):
                warn('Combination of increments n and Hurst value H invalid for \
                      Davies-Harte method. Reverting to Hosking method. Try \
                      increasing n or decreasing H')
                return self._hosking(n, H, T)

            # Generate second sequence of i.d.d. standard normals
            fgn2 = np.random.normal(0.0, 1.0, n)

            # Resulting sequence from matrix multiplication of positive definite
            # sqrt(C) matrix with fgn sample can be simulated in this way.
            w = np.zeros(2 * n, dtype=complex)
            for i in range(2 * n):
                if i == 0:
                    w[i] = np.sqrt(eigenvals[i] / (2 * n)) * fgn[i]
                elif i < n:
                    w[i] = np.sqrt(eigenvals[i] / (4 * n)) * \
                        (fgn[i] + 1j * fgn2[i])
                elif i == n:
                    w[i] = np.sqrt(eigenvals[i] / (2 * n)) * fgn2[0]
                else:
                    w[i] = np.sqrt(eigenvals[i] / (4 * n)) * \
                        (fgn[2 * n - i] - 1j * fgn2[2 * n - i])

            # Resulting z is fft of sequence w. Discard small imaginary part (z
            # should be real in theory).
            z = np.fft.fft(w)
            fgn = z[:n].real

        # Scale to interval [0, T]
        fgn *= scale

        # Take cumulative sum, return fbm, fgn, timesteps
        fbm = fgn.cumsum()
        fbm = np.insert(fbm, [0], 0)
        # t = np.linspace(0, T, n + 1)

        # return fbm, fgn, t
        return fbm

    def _cholesky(self, n, H=0.5, T=1):
        """
        Uses Cholesky decomposition method (exact method) from:
        Asmussen, S. (1998). Stochastic simulation with a view towards stochastic
        processes. University of Aarhus. Centre for Mathematical Physics and
        Stochastics (MaPhySto)[MPS].
        Hosking's method performs the same operations directly rather than taking
        a Cholesky decomposition of the covariance matrix.
        args:
            n (int): The number of increments for the fbm.
            H (float): Hurst parameter, between 0 and 1 exclusive.
            T (float): The length of the realization, nonnegative.
        returns:
            fbm (list(float)): A fbm realization from t=0 to t=T of length n+1.
            fgn (list(float)): The corresponding fgn realization of length n.
            t (list(float)): A list of time values associated with the fbm.
        raises:
            TypeError: if the input n is nonnegative or non-integer
            ValueError: if the Hurst parameter is outside (0,1) or T is negative
        """

        # Input checking
        self._check_input(n, H, T)

        # For scaling to interval [0, T]
        increment = float(T) / n
        scale = increment ** H

        fgn = np.random.normal(0.0, 1.0, n)

        # If H = 0.5 then just generate a standard Brownian motion, otherwise
        # proceed with the Cholesky method
        if H == 0.5:
            pass
        else:
            # Generate covariance matrix
            G = np.matrix(np.zeros([n, n]))
            for i in range(n):
                for j in range(i + 1):
                    G[i, j] = self._autocovariance(H, i - j)

            # Cholesky decomposition
            C = np.linalg.cholesky(G)

            # Generate fgn
            fgn = C * np.matrix(fgn).T
            fgn = np.squeeze(np.asarray(fgn))

        # Scale to interval [0, T]
        fgn *= scale

        # Take cumulative sum, return fbm, fgn, timesteps
        fbm = fgn.cumsum()
        fbm = np.insert(fbm, [0], 0)
        # t = np.linspace(0, T, n + 1)

        # return fbm, fgn, t
        return fbm

    def _hosking(self, n, H=0.5, T=1):
        """
        Method of generation is Hosking's method (exact method) from his paper:
        Hosking, J. R. (1984). Modeling persistence in hydrological time series
        using fractional differencing. Water resources research, 20(12),
        1898-1908.
        Hosking's method generates a fractional Gaussian noise (fgn) realization.
        The cumulative sum of this realization gives a fbm.
        args:
            n (int): The number of increments for the fbm.
            H (float): Hurst parameter, between 0 and 1 exclusive.
            T (float): The length of the realization, nonnegative.
        returns:
            fbm (list(float)): A fbm realization from t=0 to t=T of length n+1.
            fgn (list(float)): The corresponding fgn realization of length n.
            t (list(float)): A list of time values associated with the fbm.
        raises:
            TypeError: if the input n is nonnegative or non-integer
            ValueError: if the Hurst parameter is outside (0,1) or T is negative
        """

        # Input checking
        self._check_input(n, H, T)

        # For scaling to interval [0, T]
        increment = float(T) / n
        scale = increment ** H

        gn = np.random.normal(0.0, 1.0, n)

        # If H = 0.5 then just generate a standard Brownian motion, otherwise
        # proceed with Hosking's method
        if H == 0.5:
            fgn = gn
            del gn
        else:
            # Initializations
            fgn = np.zeros(n)
            phi = np.zeros(n)
            psi = np.zeros(n)
            cov = np.array([self._autocovariance(H, i) for i in range(n)])

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
                v *= (1 - phi[i - 1] * phi[i - 1])
                for j in range(i):
                    fgn[i] += phi[j] * fgn[i - j - 1]
                fgn[i] += np.sqrt(v) * gn[i]

        # Scale to interval [0, T]
        fgn *= scale

        # Take cumulative sum, return fbm, fgn, timesteps
        fbm = fgn.cumsum()
        fbm = np.insert(fbm, [0], 0)
        # t = np.linspace(0, T, n + 1)

        # return fbm, fgn, t
        return fbm

    def _linspace(self, end, n, zero=True):
        if zero:
            return np.linspace(0, end, n + 1)
        else:
            return np.linspace(1.0 * end / n, end, n)
