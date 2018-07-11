Noise Processes
===============

The :py:mod:`stochastic.noise` module provides classes for generating
noise processes.

Gaussian increments

* :py:class:`stochastic.noise.GaussianNoise`
* :py:class:`stochastic.noise.FractionalGaussianNoise`

Colored noise

* :py:class:`stochastic.noise.BlueNoise`
* :py:class:`stochastic.noise.BrownianNoise`
* :py:class:`stochastic.noise.ColoredNoise`
* :py:class:`stochastic.noise.RedNoise`
* :py:class:`stochastic.noise.PinkNoise`
* :py:class:`stochastic.noise.VioletNoise`
* :py:class:`stochastic.noise.WhiteNoise`

Gaussian increments
~~~~~~~~~~~~~~~~~~~

Noise processes which are increments of their continuous counterparts.

.. autoclass:: stochastic.noise.GaussianNoise
    :members: t, sample, sample_at, times

.. autoclass:: stochastic.noise.FractionalGaussianNoise
    :members: t, hurst, sample, times

Colored noise
~~~~~~~~~~~~~

Signals with spectral densities proportional to the power law.

.. autoclass:: stochastic.noise.BlueNoise
    :members: t, sample, times

.. autoclass:: stochastic.noise.BrownianNoise
    :members: t, sample, times

.. autoclass:: stochastic.noise.ColoredNoise
    :members: t, beta, sample, times

.. autoclass:: stochastic.noise.RedNoise
    :members: t, sample, times

.. autoclass:: stochastic.noise.PinkNoise
    :members: t, sample, times

.. autoclass:: stochastic.noise.VioletNoise
    :members: t, sample, times

.. autoclass:: stochastic.noise.WhiteNoise
    :members: t, sample, times
