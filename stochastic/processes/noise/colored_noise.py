"""Colored noise."""
import numpy as np

from stochastic.processes.base import BaseTimeProcess
from stochastic.utils.validation import check_numeric
from stochastic.utils.validation import check_positive_integer


class ColoredNoise(BaseTimeProcess):
    r"""Colored noise processes.

    .. image:: _static/colored_noise.png
        :scale: 50%

    Also referred to as power law noise, colored noise refers to noise
    processes with power law spectral density. That is, their spectral density
    per unit bandwidth is proportional to :math:`(1/f)^\beta`, where
    :math:`f` is frequency with exponent :math:`\beta`.

    Uses the algorithm from:

    * Timmer, J., and M. Koenig. "On generating power law noise."
      Astronomy and Astrophysics 300 (1995): 707.

    Generates a normalized power-law spectral noise.

    :param float beta: the power law exponent for the spectral density, with 0
        being white noise, 1 being pink noise, 2 being red noise (Brownian
        noise), -1 being blue noise, -2 being violet noise. Default is 0
        (white noise).
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, beta=0, t=1, rng=None):
        super().__init__(t=t, rng=rng)
        self.beta = beta
        self._n = None
        self._half = None
        self._frequencies = None
        self._scale = None

    def __str__(self):
        return (
            "Colored noise generator with exponent "
            + "{beta} on interval [0, {t}]".format(beta=str(self.beta), t=str(self.t))
        )

    def __repr__(self):
        return "ColoredNoise(beta={beta}, t={t})".format(
            beta=str(self.beta), t=str(self.t)
        )

    @property
    def beta(self):
        """Power law exponent."""
        return self._beta

    @beta.setter
    def beta(self, value):
        check_numeric(value, "beta")
        self._beta = value

    def _sample_colored_noise(self, n):
        """Generate colored noise increments at specified times from zero."""
        check_positive_integer(n)
        n = n + 1
        if self._n != n:
            self._n = n

            self._half = (n + 1) // 2
            self._frequencies = np.fft.fftfreq(n, self.t)
            self._scale = [
                np.sqrt(0.5 * (1 / w) ** self.beta)
                for w in self._frequencies[1 : self._half]
            ]

        gn_real = np.random.normal(size=self._half - 1)
        gn_imag = np.random.normal(size=self._half - 1)
        fft = self._scale * (gn_real + 1j * gn_imag)

        if n % 2 == 0:
            f = np.concatenate(
                (
                    [0],
                    fft,
                    [
                        np.sqrt(0.5 * (1 / -self._frequencies[self._half]) ** self.beta)
                        * np.random.normal()
                    ],
                    np.conj(fft)[::-1],
                )
            )
        else:
            f = np.concatenate(([0], fft, np.conj(fft)[::-1]))

        return np.fft.ifft(f).real / np.std(f)

    def sample(self, n):
        """Generate a realization of colored noise.

        Generate a colored noise realization with n increments.

        :param int n: the number of increments to generate.
        """
        return self._sample_colored_noise(n)


class PinkNoise(ColoredNoise):
    r"""Pink (flicker) noise.

    .. image:: _static/pink_noise.png
        :scale: 50%

    Colored noise, or power law noise with spectral density exponent
    :math:`\beta = 1`.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, t=1, rng=None):
        super().__init__(beta=1, t=t, rng=rng)


class WhiteNoise(ColoredNoise):
    r"""White noise.

    .. image:: _static/white_noise.png
        :scale: 50%

    Colored noise, or power law noise with spectral density exponent
    :math:`\beta = 0`.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, t=1, rng=None):
        super().__init__(beta=0, t=t, rng=rng)


class RedNoise(ColoredNoise):
    r"""Red (Brownian) noise.

    .. image:: _static/red_noise.png
        :scale: 50%

    Colored noise, or power law noise with spectral density exponent
    :math:`\beta = 2`.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, t=1, rng=None):
        super().__init__(beta=2, t=t, rng=rng)


class BrownianNoise(RedNoise):
    r"""Brownian (red) noise.

    .. image:: _static/red_noise.png
        :scale: 50%

    Colored noise, or power law noise with spectral density exponent
    :math:`\beta = 2`.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """
    pass


class BlueNoise(ColoredNoise):
    r"""Blue noise.

    .. image:: _static/blue_noise.png
        :scale: 50%

    Colored noise, or power law noise with spectral density exponent
    :math:`\beta = -1`.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, t=1, rng=None):
        super().__init__(beta=-1, t=t, rng=rng)


class VioletNoise(ColoredNoise):
    r"""Violet noise.

    .. image:: _static/violet_noise.png
        :scale: 50%

    Colored noise, or power law noise with spectral density exponent
    :math:`\beta = -2`.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, t=1, rng=None):
        super().__init__(beta=-2, t=t, rng=rng)
