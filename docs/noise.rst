Noise Processes
===============

The :py:mod:`stochastic.noise` module provides classes for generating
noise processes.

* :py:class:`stochastic.noise.GaussianNoise`
* :py:class:`stochastic.noise.FractionalGaussianNoise`

.. autoclass:: stochastic.noise.GaussianNoise
    :members: t, sample, sample_at, times

.. autoclass:: stochastic.noise.FractionalGaussianNoise
    :members: t, hurst, sample, times
