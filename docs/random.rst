Random Number Generation
========================

Numpy's random number generation
--------------------------------

Stochastic relies on `numpy <https://numpy.org/doc/stable/reference/random/index.html>`__ for random number generation. Since numpy 1.17, the newer ``Generator`` objects provide improved performance:

.. note::

    From numpy docs: The Generator’s normal, exponential and gamma functions use 256-step Ziggurat methods which are 2-10 times faster than NumPy’s Box-Muller or inverse CDF implementations.

By default, the stochastic package uses numpy's faster `Generator <https://numpy.org/doc/stable/reference/random/generator.html#random-generator>`__ random number generation. With a function call, we can change the default back to the `legacy random number generation <https://numpy.org/doc/stable/reference/random/legacy.html#legacy>`__, which uses `RandomState <https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState>`__ objects.

If no ``rng`` arg is passed when instantiating process instances, each instance will reference the ``stochastic.random`` module's ``generator`` attribute for random number generation.

Examples
--------

Changing the default random number generation on instances without specified ``rng``:

.. code-block:: python

    from stochastic.processes import GaussianNoise
    from stochastic import random

    gn = GaussianNoise()
    print(gn.rng)
    # Generator(PCG64)

    # use the legacy random number generator
    random.use_randomstate()

    print(gn.rng)
    # <module 'numpy.random' from '/path/to/site-packages/numpy/random/__init__.py'>

    # use the newer Generator
    random.use_generator()

    print(gn.rng)
    # Generator(PCG64)


Setting the seed value:

.. code-block:: python

    from stochastic.processes import GaussianNoise
    from stochastic import random

    gn = GaussianNoise()
    print(gn.rng)
    # Generator(PCG64)

    random.seed(42)
    print(gn.rng.bit_generator.state)
    # {'bit_generator': 'PCG64', 'state': {'state': 274674114334540486603088602300644985544, 'inc': 332724090758049132448979897138935081983}, 'has_uint32': 0, 'uinteger': 0}
    print(gn.sample(4))
    # [ 0.15235854 -0.51999205  0.3752256   0.47028236]

    random.seed(42)
    print(gn.rng.bit_generator.state)
    # {'bit_generator': 'PCG64', 'state': {'state': 274674114334540486603088602300644985544, 'inc': 332724090758049132448979897138935081983}, 'has_uint32': 0, 'uinteger': 0}
    print(gn.sample(4))
    # [ 0.15235854 -0.51999205  0.3752256   0.47028236]


Passing `custom generators <https://numpy.org/doc/stable/reference/random/bit_generators/index.html>`__ to process instances at instantiation:

.. code-block:: python

    from numpy.random import Generator
    from numpy.random import PCG64
    from stochastic.processes import GaussianNoise
    from stochastic import random

    generator = Generator(PCG64(seed=42))

    gn = GaussianNoise(rng=generator)
    # generator specific to this gaussian noise instance
    print(gn.rng.bit_generator.state)
    # {'bit_generator': 'PCG64', 'state': {'state': 274674114334540486603088602300644985544, 'inc': 332724090758049132448979897138935081983}, 'has_uint32': 0, 'uinteger': 0}

    # stochastic's global generator, different from the one attached to `gn`
    print(random.generator.bit_generator.state)
    # {'bit_generator': 'PCG64', 'state': {'state': 228239801863081385502825691348763076514, 'inc': 61631449755775032062670113901777656135}, 'has_uint32': 0, 'uinteger': 0}


Documentation
-------------

.. automodule:: stochastic.random
   :members:

