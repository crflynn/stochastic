Continuous-time Processes
=========================

The :py:mod:`nhppy.continuous` module provides classes for generating
(discretely sampled) continuous-time nhppy processes.

* :py:class:`nhppy.continuous.BesselProcess`
* :py:class:`nhppy.continuous.BrownianBridge`
* :py:class:`nhppy.continuous.BrownianExcursion`
* :py:class:`nhppy.continuous.BrownianMeander`
* :py:class:`nhppy.continuous.BrownianMotion`
* :py:class:`nhppy.continuous.CauchyProcess`
* :py:class:`nhppy.continuous.FractionalBrownianMotion`
* :py:class:`nhppy.continuous.GammaProcess`
* :py:class:`nhppy.continuous.GeometricBrownianMotion`
* :py:class:`nhppy.continuous.PoissonProcess`
* :py:class:`nhppy.continuous.MixedPoissonProcess`
* :py:class:`nhppy.continuous.NHPP`
* :py:class:`nhppy.continuous.SquaredBesselProcess`
* :py:class:`nhppy.continuous.VarianceGammaProcess`
* :py:class:`nhppy.continuous.WienerProcess`


.. autoclass:: nhppy.continuous.BesselProcess
    :members: t, sample, sample_at, times

.. autoclass:: nhppy.continuous.BrownianBridge
    :members: t, b, sample, sample_at, times

.. autoclass:: nhppy.continuous.BrownianExcursion
    :members: t, sample, sample_at, times

.. autoclass:: nhppy.continuous.BrownianMeander
    :members: t, sample, sample_at, times

.. autoclass:: nhppy.continuous.BrownianMotion
    :members: t, drift, scale, sample, sample_at, times

.. autoclass:: nhppy.continuous.CauchyProcess
    :members: t, sample, sample_at, times

.. autoclass:: nhppy.continuous.FractionalBrownianMotion
    :members: t, hurst, sample, times

.. autoclass:: nhppy.continuous.GammaProcess
    :members: t, mean, variance, rate, scale, sample, sample_at, times

.. autoclass:: nhppy.continuous.GeometricBrownianMotion
    :members: t, drift, volatility, sample, sample_at, times

.. autoclass:: nhppy.continuous.PoissonProcess
    :members: rate, sample
    
.. autoclass:: nhppy.continuous.MixedPoissonProcess
    :members: rate, sample

.. autoclass:: nhppy.continuous.NHPP
    :members: rate, sample
    
    
.. autoclass:: nhppy.continuous.SquaredBesselProcess
    :members: t, dim, sample, sample_at

.. autoclass:: nhppy.continuous.VarianceGammaProcess
    :members: t, drift, variance, scale, sample, sample_at

.. autoclass:: nhppy.continuous.WienerProcess
    :members: t, sample, sample_at, times
