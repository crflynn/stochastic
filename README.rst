stochastic
==========

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

Here are the currently supported processes:

Continuous-time
~~~~~~~~~~~~~~~

* Bessel process
* Brownian bridge
* Brownian excursion
* Brownian meander
* Brownian motion
* Cauchy process
* Fractional Brownian motion
* Gamma process
* Geometric Brownian motion
* Poisson process
* Squared Bessel process
* Variance gamma process
* Wiener process

Diffusion models
~~~~~~~~~~~~~~~~

* Constant elasticity of variance (CEV) process
* Cox-Ingersoll-Ross (CIR) process
* Ornstein-Uhlenbeck (OU) process
* Vasicek process

Discrete-time
~~~~~~~~~~~~~

* Bernoulli process
* Chinese restaurant process
* Markov chain
* Moran process
* Random walk

Noise
~~~~~

* Gaussian noise
* Fractional Gaussian noise


Package Access Structure
------------------------

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

        * GaussianNoise
        * FractionalGaussianNoise

Usage
-----

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

Some continuous processes also provide a ``sample_at()`` method, in which a
sequence of time values can be passed at which the object will generate a
realization. This method ignores the parameter, ``t``, specified on
instantiation.


.. code-block:: python

    from stochastic.continuous import BrownianMotion


    bm = BrownianMotion(t=1, drift=1, scale=1)
    times = [0, 3, 10, 11, 11.2, 20]
    s = sample_at(times)


Continuous processes also provide a method ``times()`` which generates the time
values (using ``numpy.linspace``) corresponding to a realization of ``n``
steps. This is particularly useful for plotting your samples.


.. code-block:: python

    import matplotlib.pyplot as plt
    from stochastic.continuous import FractionalBrownianMotion


    fbm = FractionalBrownianMotion(t=1, hurst=0.7)
    s = fbm.sample(32)
    times = fbm.times(32)

    plt.plot(times, s)
    plt.show()


Some processes provide an optional parameter ``algorithm``, in which one can
specify which algorithm to use to generate the realization using the
``sample()`` or ``sample_at()`` methods. See the documentation for
process-specific implementations.


.. code-block:: python

    from stochastic.noise import FractionalGaussianNoise


    fgn = FractionalGaussianNoise(t=1, hurst=0.6)
    s = fgn.sample(32, algorithm='hosking')
