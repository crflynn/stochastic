Continuous-time Processes
=========================

The :py:mod:`stochastic.processes.continuous` module provides classes for generating
discretely sampled continuous-time stochastic processes.

* :py:class:`stochastic.processes.continuous.BesselProcess`
* :py:class:`stochastic.processes.continuous.BrownianBridge`
* :py:class:`stochastic.processes.continuous.BrownianExcursion`
* :py:class:`stochastic.processes.continuous.BrownianMeander`
* :py:class:`stochastic.processes.continuous.BrownianMotion`
* :py:class:`stochastic.processes.continuous.CauchyProcess`
* :py:class:`stochastic.processes.continuous.FractionalBrownianMotion`
* :py:class:`stochastic.processes.continuous.GammaProcess`
* :py:class:`stochastic.processes.continuous.GeometricBrownianMotion`
* :py:class:`stochastic.processes.continuous.InverseGaussianProcess`
* :py:class:`stochastic.processes.continuous.MixedPoissonProcess`
* :py:class:`stochastic.processes.continuous.MultifractionalBrownianMotion`
* :py:class:`stochastic.processes.continuous.PoissonProcess`
* :py:class:`stochastic.processes.continuous.SquaredBesselProcess`
* :py:class:`stochastic.processes.continuous.VarianceGammaProcess`
* :py:class:`stochastic.processes.continuous.WienerProcess`


.. autoclass:: stochastic.processes.continuous.BesselProcess
    :members: t, sample, sample_at, times

.. autoclass:: stochastic.processes.continuous.BrownianBridge
    :members: t, b, sample, sample_at, times

.. autoclass:: stochastic.processes.continuous.BrownianExcursion
    :members: t, sample, sample_at, times

.. autoclass:: stochastic.processes.continuous.BrownianMeander
    :members: t, sample, sample_at, times

.. autoclass:: stochastic.processes.continuous.BrownianMotion
    :members: t, drift, scale, sample, sample_at, times

.. autoclass:: stochastic.processes.continuous.CauchyProcess
    :members: t, sample, sample_at, times

.. autoclass:: stochastic.processes.continuous.FractionalBrownianMotion
    :members: t, hurst, sample, times

.. autoclass:: stochastic.processes.continuous.GammaProcess
    :members: t, mean, variance, rate, scale, sample, sample_at, times

.. autoclass:: stochastic.processes.continuous.GeometricBrownianMotion
    :members: t, drift, volatility, sample, sample_at, times

.. autoclass:: stochastic.processes.continuous.InverseGaussianProcess
    :members: t, mean, scale, sample, sample_at, times

.. autoclass:: stochastic.processes.continuous.MixedPoissonProcess
    :members: rate, rate_func, rate_args, rate_kwargs, sample

.. autoclass:: stochastic.processes.continuous.MultifractionalBrownianMotion
    :members: t, hurst, sample, times

.. autoclass:: stochastic.processes.continuous.PoissonProcess
    :members: rate, sample

.. autoclass:: stochastic.processes.continuous.SquaredBesselProcess
    :members: t, dim, sample, sample_at

.. autoclass:: stochastic.processes.continuous.VarianceGammaProcess
    :members: t, drift, variance, scale, sample, sample_at

.. autoclass:: stochastic.processes.continuous.WienerProcess
    :members: t, sample, sample_at, times
