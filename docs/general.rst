General Usage
=============


Processes
---------

This package offers a number of common discrete-time, continuous-time, and
noise process objects for generating realizations of stochastic processes as
``numpy`` arrays.

The diffusion processes are approximated using the Euler–Maruyama method.

Some analysis functions are also offered: NHPP rate estimation methods, 2D Kolmogorov-Smirnov testing.

Here are the currently supported processes and how to access their classes:

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
    * MultifractionalBrownianMotion
    * PoissonProcess
    * MixedPoissonProcess
    * NHPP
    * SquaredBesselProcess
    * VarianceGammaProcess
    * WienerProcess

  * diffusion

    * ConstantElasticityVarianceProcess (or CEVProcess)
    * CoxIngersollRossProcess (or CIRProcess)
    * OrnsteinUhlenbeckProcess (or OUProcess)
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

Here are the analysis functions:
    
   * analysis
    
    * ks2d1s
    * ks2d2s
    * NHPPLeemisEst
    * NHPPMangkuEst
    
Usage patterns
--------------


The sample() method
~~~~~~~~~~~~~~~~~~~

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


The sample_at() method
~~~~~~~~~~~~~~~~~~~~~~

Some continuous processes also provide a ``sample_at()`` method, in which a
sequence of time values can be passed at which the object will generate a
realization. This method ignores the parameter, ``t``, specified on
instantiation.


.. code-block:: python

    from stochastic.continuous import BrownianMotion


    bm = BrownianMotion(t=1, drift=1, scale=1)
    times = [0, 3, 10, 11, 11.2, 20]
    s = sample_at(times)


The times() method
~~~~~~~~~~~~~~~~~~

Continuous-time processes also provide a method ``times()`` which generates the
time values (using ``numpy.linspace``) corresponding to a realization of ``n``
steps. This is particularly useful for plotting your samples.

.. code-block:: python

    import matplotlib.pyplot as plt
    from stochastic.continuous import FractionalBrownianMotion


    fbm = FractionalBrownianMotion(t=1, hurst=0.7)
    s = fbm.sample(32)
    times = fbm.times(32)

    plt.plot(times, s)
    plt.show()


The algorithm option
~~~~~~~~~~~~~~~~~~~~

Some processes provide an optional parameter ``algorithm``, in which one can
specify which algorithm to use to generate the realization using the
``sample()`` or ``sample_at()`` methods. See class-specific documentation for
implementations.


.. code-block:: python

    from stochastic.noise import FractionalGaussianNoise


    fgn = FractionalGaussianNoise(t=1, hurst=0.6)
    s = fgn.sample(32, algorithm='hosking')
