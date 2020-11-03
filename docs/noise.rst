Noise Processes
===============

The :py:mod:`stochastic.processes.noise` module provides classes for generating
noise processes.

Gaussian increments

* :py:class:`stochastic.processes.noise.GaussianNoise`
* :py:class:`stochastic.processes.noise.FractionalGaussianNoise`

Colored noise

* :py:class:`stochastic.processes.noise.BlueNoise`
* :py:class:`stochastic.processes.noise.BrownianNoise`
* :py:class:`stochastic.processes.noise.ColoredNoise`
* :py:class:`stochastic.processes.noise.RedNoise`
* :py:class:`stochastic.processes.noise.PinkNoise`
* :py:class:`stochastic.processes.noise.VioletNoise`
* :py:class:`stochastic.processes.noise.WhiteNoise`

Gaussian increments
~~~~~~~~~~~~~~~~~~~

Noise processes which are increments of their continuous counterparts.

.. autoclass:: stochastic.processes.noise.GaussianNoise
    :members: t, sample, sample_at, times

.. autoclass:: stochastic.processes.noise.FractionalGaussianNoise
    :members: t, hurst, sample, times

Colored noise
~~~~~~~~~~~~~

Signals with spectral densities proportional to the power law.

.. autoclass:: stochastic.processes.noise.BlueNoise
    :members: t, sample, times

.. autoclass:: stochastic.processes.noise.BrownianNoise
    :members: t, sample, times

.. autoclass:: stochastic.processes.noise.ColoredNoise
    :members: t, beta, sample, times

.. autoclass:: stochastic.processes.noise.RedNoise
    :members: t, sample, times

.. autoclass:: stochastic.processes.noise.PinkNoise
    :members: t, sample, times

.. autoclass:: stochastic.processes.noise.VioletNoise
    :members: t, sample, times

.. autoclass:: stochastic.processes.noise.WhiteNoise
    :members: t, sample, times
