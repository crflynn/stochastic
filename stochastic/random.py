import numpy as np

_default_rng = np.random.default_rng()

#: The default random number generator for the stochastic package
generator = _default_rng


def use_randomstate(rng=None):
    """Use the legacy numpy RandomState generator as default for stochastic.

    Sets the default random number generator for stochastic processes to
    the legacy ``np.random``.

    :param numpy.random.RandomState rng: a RandomState instance to use as the
        default random number generator for stochastic.
    """
    global generator
    if rng is not None and not isinstance(rng, np.random.RandomState):
        raise TypeError("rng must be of type np.random.RandomState")
    generator = rng or np.random


def use_generator(rng=None):
    """Use the new numpy Generator as default for stochastic.

    Sets the default random number generator for stochastic processes to
    the newer ``np.random.default_rng()``.

    .. note::

        This is the default generator and
        there is no need to call this function unless returning to the default
        after switching away from it.

    :param numpy.random.Generator rng: a Generator instance to use as the
        default random number generator for stochastic.
    """
    global generator
    if rng is not None and not isinstance(rng, np.random.Generator):
        raise TypeError("rng must be of type np.random.Generator")
    generator = rng or _default_rng


def seed(value):
    """Sets the seed for numpy legacy or ``default_rng`` generators.

    If using the legacy generator, this will call ``numpy.random.seed(value)``.
    Otherwise a new random number generator is created using
    ``numpy.random.default_rng(value)``.
    """
    global generator
    if generator == np.random:
        np.random.seed(value)
    else:
        generator = np.random.default_rng(value)
