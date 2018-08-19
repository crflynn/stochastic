Continuous-time Processes
=========================

The :py:mod:`stochastic.continuous` module provides classes for generating
(discretely sampled) continuous-time stochastic processes.

* :py:class:`stochastic.continuous.BesselProcess`
* :py:class:`stochastic.continuous.BrownianBridge`
* :py:class:`stochastic.continuous.BrownianExcursion`
* :py:class:`stochastic.continuous.BrownianMeander`
* :py:class:`stochastic.continuous.BrownianMotion`
* :py:class:`stochastic.continuous.CauchyProcess`
* :py:class:`stochastic.continuous.FractionalBrownianMotion`
* :py:class:`stochastic.continuous.GammaProcess`
* :py:class:`stochastic.continuous.GeometricBrownianMotion`
* :py:class:`stochastic.continuous.InverseGaussianProcess`
* :py:class:`stochastic.continuous.MixedPoissonProcess`
* :py:class:`stochastic.continuous.MultifractionalBrownianMotion`
* :py:class:`stochastic.continuous.PoissonProcess`
* :py:class:`stochastic.continuous.SquaredBesselProcess`
* :py:class:`stochastic.continuous.VarianceGammaProcess`
* :py:class:`stochastic.continuous.WienerProcess`


.. autoclass:: stochastic.continuous.BesselProcess
    :members: t, sample, sample_at, times

.. autoclass:: stochastic.continuous.BrownianBridge
    :members: t, b, sample, sample_at, times

.. autoclass:: stochastic.continuous.BrownianExcursion
    :members: t, sample, sample_at, times

.. autoclass:: stochastic.continuous.BrownianMeander
    :members: t, sample, sample_at, times

.. autoclass:: stochastic.continuous.BrownianMotion
    :members: t, drift, scale, sample, sample_at, times

.. autoclass:: stochastic.continuous.CauchyProcess
    :members: t, sample, sample_at, times

.. autoclass:: stochastic.continuous.FractionalBrownianMotion
    :members: t, hurst, sample, times

.. autoclass:: stochastic.continuous.GammaProcess
    :members: t, mean, variance, rate, scale, sample, sample_at, times

.. autoclass:: stochastic.continuous.GeometricBrownianMotion
    :members: t, drift, volatility, sample, sample_at, times

.. autoclass:: stochastic.continuous.InverseGaussianProcess
    :members: t, mean, scale, sample, sample_at, times

.. autoclass:: stochastic.continuous.MixedPoissonProcess
    :members: rate, rate_func, rate_args, rate_kwargs, sample

.. autoclass:: stochastic.continuous.MultifractionalBrownianMotion
    :members: t, hurst, sample, times

.. autoclass:: stochastic.continuous.PoissonProcess
    :members: rate, sample

.. autoclass:: stochastic.continuous.SquaredBesselProcess
    :members: t, dim, sample, sample_at

.. autoclass:: stochastic.continuous.VarianceGammaProcess
    :members: t, drift, variance, scale, sample, sample_at

.. autoclass:: stochastic.continuous.WienerProcess
    :members: t, sample, sample_at, times
