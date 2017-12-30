"""Brownian motion and derivative processes."""
import numpy as np

from stochastic.base import Continuous


class GaussianNoise(Continuous):
    """Gaussian noise process."""

    def __init__(self, t=1):
        self.t = t

    def __str__(self):
        return "Gaussian noise generator on interval [0, {t}]".format(
            t=str(self.t))

    def __repr__(self):
        return "GaussianNoise(t={t})".format(t=str(self.t))

    def _sample_gaussian_noise(self, n, zero=False):
        """Generate a realization of Gaussian noise.

        Generate a Gaussian noise realization with n increments.
        """
        self._check_increments(n)
        delta_t = 1.0 * self.t / n

        noise = np.random.normal(scale=np.sqrt(delta_t), size=n)

        if zero:
            noise = np.insert(noise, [0], 0)

        return noise

    def _sample_gaussian_noise_at(self, times, zero=False):
        """Generate Gaussian noise increments at specified times from zero."""
        if np.any([t < 0 for t in times]):
            raise ValueError("Times must be nonnegative.")

        if times[0] != 0:
            times = np.concatenate(([0], times))
        increments = np.diff(times)

        if np.any([t <= 0 for t in increments]):
            raise ValueError(
                "Times must be strictly monotonically increasing.")

        noise = np.array(
            [np.random.normal(scale=np.sqrt(inc)) for inc in increments])

        if zero:
            noise = np.insert(noise, [0], 0)

        return noise

    def sample(self, n):
        """Generate a realization of Gaussian noise.

        Generate a Gaussian noise realization with n increments.
        """
        return self._sample_gaussian_noise(n)

    def sample_at(self, times):
        """Generate Gaussian noise increments at specified times from zero."""
        return self._sample_gaussian_noise_at(times)


class BrownianMotion(GaussianNoise):
    """Brownian motion.

    A Brownian motion (discretely sampled) has independent and identically
    distributed Gaussian increments with variance equal to increment length.
    """

    def __init__(self, t=1, drift=0, scale=1):
        super().__init__(t)
        self.drift = drift
        self.scale = scale

    def __str__(self):
        if self.drift == 0 and self.scale == 1:
            s = "Standard Brownian motion on interval [0, {t}]".format(
                t=self.t)
            return s
        s = ("Brownian motion with drift {d} and scale {s} on interval "
             "[0, {t}].")
        return s.format(
            t=str(self.t),
            d=str(self.drift),
            s=str(self.scale)
        )

    def __repr__(self):
        if self.drift == 0 and self.scale == 1:
            return "BrownianMotion(t={t})".format(t=self.t)
        return "BrownianMotion(t={t}, drift={d}, scale={s})".format(
            t=str(self.t),
            d=str(self.drift),
            s=str(self.scale)
        )

    @property
    def drift(self):
        """Drift parameter."""
        return self._drift

    @drift.setter
    def drift(self, value):
        self._check_number(value, "Drift")
        self._drift = value

    @property
    def scale(self):
        """Scale parameter."""
        return self._scale

    @scale.setter
    def scale(self, value):
        self._check_positive_number(value, "Scale")
        self._scale = value

    def _sample_brownian_motion(self, n, zero=True):
        """Generate a realization of Brownian Motion.

        Generate a Brownian motion realization with n increments. If zero is
        True then include W_0 = 0.
        """
        self._check_zero(zero)

        line = self._linspace(self.drift, n, zero)
        bm = np.cumsum(self.scale * self._sample_gaussian_noise(n, zero))

        return line + bm

    def sample(self, n, zero=True):
        """Generate a realization of Brownian Motion.

        Generate a Brownian motion realization with n increments. If zero is
        True then include W_0 = 0.
        """
        return self._sample_brownian_motion(n, zero)

    def _sample_brownian_motion_at(self, times, zero=True):
        """Generate a Brownian motion at specified times."""
        return np.cumsum(self._sample_gaussian_noise_at(times, zero))

    def sample_at(self, times, zero=True):
        """Generate a Brownian motion at specified times."""
        return self._sample_brownian_motion_at(times)


class BrownianBridge(BrownianMotion):
    """Brownian bridge."""

    def __init__(self, t=1, b=0):
        super().__init__(t, drift=0, scale=1)
        self.b = b

    def __str__(self):
        return "Brownian bridge from 0 to {b} on [0, {t}]".format(
            t=str(self.t),
            b=str(self.b)
        )

    def __repr__(self):
        if self.t == 1:
            return "BrownianBridge(b={b})".format(
                t=str(self.t),
                b=str(self.b)
            )
        return "BrownianBridge(t={t}, b={b})".format(
            t=str(self.t),
            b=str(self.b),
        )

    def _sample_brownian_bridge(self, n, b=0, zero=True):
        """Generate a realization of a Brownian bridge."""
        self._check_number(b, "Time end")
        self._check_zero(zero)

        bm = self._sample_brownian_motion(n, zero)
        times = self.times(n, zero)

        return bm + times * (b - bm[-1]) / self.t

    def sample(self, n, b=0, zero=True):
        """Generate a realization of a Brownian bridge."""
        return self._sample_brownian_bridge(n, b, zero)

    # TODO
    # def sample_at(self, times):
    #     pass


class BrownianExcursion(BrownianBridge):
    """Brownian excursion."""

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Brownian excursion"""

    def __repr__(self):
        return "BrownianExcursion()"

    def _sample_brownian_excursion(self, n, zero=True):
        """Generate a Brownian excursion."""
        brownian_bridge = self._sample_brownian_bridge(n)
        idx_min = np.argmin(brownian_bridge)
        return np.array(
            [brownian_bridge[idx_min + idx % n] - brownian_bridge[idx_min]
             for idx in range(n + 1)]
        )

    def sample(self, n, zero=True):
        """Generate a Brownian excursion."""
        return self._sample_brownian_excursion(n)

    # TODO
    # def sample_at(self, times)
        # pass


class BrownianMeander(BrownianMotion):
    """Brownian meander process."""

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Brownian meander"""

    def __repr__(self):
        return "BrownianMeander()"

    def _sample_brownian_meander(self, n, b=None):
        """Generate a Brownian meander realization.

        Williams, 1970, or Imhof, 1984.
        """
        if b is None:
            b = np.sqrt(2 * np.random.exponential())
        else:
            self._check_number(b, "Right endpoint")
            if b < 0:
                raise ValueError("Right endpoint must be nonnegative.")
        bridge_1 = self._sample_brownian_bridge()
        bridge_2 = self._sample_brownian_bridge()
        bridge_3 = self._sample_brownian_bridge()
        times = self.times(n)

        return np.sqrt(
            (b * times + bridge_1) ** 2 + bridge_2 ** 2 + bridge_3 ** 2
        )

    def sample(self, n, b=None):
        """Generate a Brownian meander realization."""
        return self._sample_brownian_meander(b)

    # TODO
    # def sample_at(self):
    #     pass


class GeometricBrownianMotion(Continuous):
    """Geometric Brownian motion process."""

    def __init__(self, t=1, drift=0, volatility=1):
        super().__init__(t)
        # TODO add getter setter to ensure bm is standard
        self._brownian_motion = BrownianMotion(self.t)
        self.drift = drift
        self.volatility = volatility

    @property
    def drift(self):
        """Geometric Brownian motion drift parameter."""
        return self._drift

    @drift.setter
    def drift(self, value):
        self._check_number(value, "Drift")
        self._drift = value

    @property
    def volatility(self):
        """Geometric Brownian motion volatility parameter."""
        return self._volatility

    @volatility.setter
    def volatility(self, value):
        self._check_positive_number(value, "Volatility")
        self._volatility = value

    def _sample_geometric_brownian_motion(self, n, initial=1, zero=True):
        """Generate a realization of geometric Brownian motion."""
        self._check_increments(n)
        self._check_positive_number(initial, "Initial")
        self._check_zero(zero)

        line = self._linspace(self.drift - self.volatility ** 2 / 2.0, n, zero)
        noise = self.volatility * self._brownian_motion.sample(n, zero)

        return initial * np.exp(line + noise)

    def sample(self, n, initial=1, zero=True):
        """Generate a realization of geometric Brownian motion."""
        return self._sample_geometric_brownian_motion(n, initial, zero)

    # TODO
    # def sample_at(self, times):
    #     pass


class BesselProcess(Continuous):
    """Bessel process."""

    def __init__(self, t=1, dim=1):
        super().__init__(t)
        self.brownian_motions = []
        self.dim = dim
        for k in range(self.dim):
            self.brownian_motions.append(BrownianMotion(self.t))

    @property
    def dim(self):
        """Dimensions."""
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
        """Generate a realization of a Bessel process."""
        return self._sample_bessel_process(n, zero)
