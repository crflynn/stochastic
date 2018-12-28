stochastic
==========

|travis| |rtd| |codecov| |pypi| |pyversions|


.. |travis| image:: https://img.shields.io/travis/crflynn/stochastic.svg
    :target: https://travis-ci.org/crflynn/stochastic

.. |rtd| image:: https://img.shields.io/readthedocs/stochastic.svg
    :target: http://stochastic.readthedocs.io/en/latest/

.. |codecov| image:: https://codecov.io/gh/crflynn/stochastic/branch/master/graphs/badge.svg
    :target: https://codecov.io/gh/crflynn/stochastic

.. |pypi| image:: https://img.shields.io/pypi/v/stochastic.svg
    :target: https://pypi.python.org/pypi/stochastic

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/stochastic.svg
    :target: https://pypi.python.org/pypi/stochastic


A python package for generating realizations of common
(and perhaps some less common) stochastic processes, with some optimization
for repeated simulation.

Installation
------------

The ``stochastic`` package is available on pypi and can be installed using pip

.. code-block:: shell

    pip install stochastic

Dependencies
~~~~~~~~~~~~

Stochastic uses ``numpy`` for many calculations and ``scipy`` for sampling
specific random variables.

Processes
---------

This package offers a number of common discrete-time, continuous-time, and
noise process objects for generating realizations of stochastic processes as
``numpy`` arrays.

The diffusion processes are approximated using the Euler–Maruyama method.

Here are the currently supported processes and their class references within
the package.

* stochastic

    * continuous

        * BesselProcess
        * BrownianBridge
        * BrownianExcursion
        * BrownianMeander
        * BrownianMotion
        * CauchyProcess
        * FractionalBrownianMotion
        * GammaProcess
        * GeometricBrownianMotion
        * InverseGaussianProcess
        * MixedPoissonProcess
        * MultifractionalBrownianMotion
        * PoissonProcess
        * SquaredBesselProcess
        * VarianceGammaProcess
        * WienerProcess

    * diffusion

        * ConstantElasticityVarianceProcess
        * CoxIngersollRossProcess
        * OrnsteinUhlenbeckProcess
        * VasicekProcess

    * discrete

        * BernoulliProcess
        * ChineseRestaurantProcess
        * MarkovChain
        * MoranProcess
        * RandomWalk

    * noise

        * BlueNoise
        * BrownianNoise
        * ColoredNoise
        * PinkNoise
        * RedNoise
        * VioletNoise
        * WhiteNoise
        * FractionalGaussianNoise
        * GaussianNoise

Usage patterns
--------------

Sampling
~~~~~~~~

To use ``stochastic``, import the process you want and instantiate with the
required parameters. Every process class has a ``sample`` method for generating
realizations. The ``sample`` methods accept a parameter ``n`` for the quantity
of steps in the realization, but others (Poisson, for instance) may take
additional parameters. Parameters can be accessed as attributes of the
instance.

.. code-block:: python

    from stochastic.discrete import BernoulliProcess


    bp = BernoulliProcess(p=0.6)
    s = bp.sample(16)
    success_probability = bp.p


Continuous processes provide a default parameter, ``t``, which indicates the
maximum time of the process realizations. The default value is 1. The sample
method will generate ``n`` equally spaced increments on the
interval ``[0, t]``.

Sampling at specific times
~~~~~~~~~~~~~~~~~~~~~~~~~~

Some continuous processes also provide a ``sample_at()`` method, in which a
sequence of time values can be passed at which the object will generate a
realization. This method ignores the parameter, ``t``, specified on
instantiation.


.. code-block:: python

    from stochastic.continuous import BrownianMotion


    bm = BrownianMotion(drift=1, scale=1, t=1)
    times = [0, 3, 10, 11, 11.2, 20]
    s = bm.sample_at(times)

Sample times
~~~~~~~~~~~~

Continuous processes also provide a method ``times()`` which generates the time
values (using ``numpy.linspace``) corresponding to a realization of ``n``
steps. This is particularly useful for plotting your samples.


.. code-block:: python

    import matplotlib.pyplot as plt
    from stochastic.continuous import FractionalBrownianMotion


    fbm = FractionalBrownianMotion(hurst=0.7, t=1)
    s = fbm.sample(32)
    times = fbm.times(32)

    plt.plot(times, s)
    plt.show()


Specifying an algorithm
~~~~~~~~~~~~~~~~~~~~~~~

Some processes provide an optional parameter ``algorithm``, in which one can
specify which algorithm to use to generate the realization using the
``sample()`` or ``sample_at()`` methods. See the documentation for
process-specific implementations.


.. code-block:: python

    from stochastic.noise import FractionalGaussianNoise


    fgn = FractionalGaussianNoise(hurst=0.6, t=1)
    s = fgn.sample(32, algorithm='hosking')
