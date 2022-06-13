stochastic
==========

|build| |rtd| |codecov| |pypi| |pyversions|

.. |build| image:: https://github.com/crflynn/stochastic/actions/workflows/build.yml/badge.svg
    :target: https://github.com/crflynn/stochastic/actions

.. |rtd| image:: https://img.shields.io/readthedocs/stochastic.svg
    :target: http://stochastic.readthedocs.io/en/latest/

.. |codecov| image:: https://codecov.io/gh/crflynn/stochastic/branch/master/graphs/badge.svg
    :target: https://codecov.io/gh/crflynn/stochastic

.. |pypi| image:: https://img.shields.io/pypi/v/stochastic.svg
    :target: https://pypi.python.org/pypi/stochastic

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/stochastic.svg
    :target: https://pypi.python.org/pypi/stochastic


Stochastic is a python package for generating realizations of
stochastic processes.

Installation
------------

Stochastic is available on `pypi <https://pypi.python.org/pypi>`_ and can be
installed using ``pip``:

.. code-block:: bash

   pip install stochastic

Dependencies
------------

Stochastic depends on ``numpy`` for most calculations and ``scipy`` for
certain random variable generation.

Compatibility
-------------

Stochastic is tested on Python versions 3.6, 3.7, and 3.8.

Performance
-----------

This package uses ``numpy`` and ``scipy`` wherever possible for faster
computation. For improved performance under Monte Carlo simulation, some
classes will store results of intermediate computations for faster generation
on subsequent simulations.

Documentation
-------------


.. toctree::
   :maxdepth: 2

   general
   random
   continuous
   diffusion
   discrete
   noise
   sources
   notes



Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
