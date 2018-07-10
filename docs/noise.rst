Noise Processes
===============

The :py:mod:`nhppy.noise` module provides classes for generating
noise processes.

* :py:class:`nhppy.noise.GaussianNoise`
* :py:class:`nhppy.noise.FractionalGaussianNoise`

.. autoclass:: nhppy.noise.GaussianNoise
    :members: t, sample, sample_at, times

.. autoclass:: nhppy.noise.FractionalGaussianNoise
    :members: t, hurst, sample, times
