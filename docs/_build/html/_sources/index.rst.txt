.. stochastic documentation master file, created by
   sphinx-quickstart on Sun Dec 31 20:50:28 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

stochastic
==========

Stochastic is a python package for generating realizations of
stochastic processes.

.. warning::

    This package is currently in development and not all functionality
    may be properly tested or documented. Additionally, some processes use
    methods which are approximate rather than exact. Use this software package at
    your own risk.

Installation
------------

Stochastic is a python package available on
`pypi <https://pypi.python.org/pypi>`_ and can be installed using ``pip``:

.. code-block:: bash

   pip install stochastic

Dependencies
------------

Stochastic depends on ``numpy`` for most calculations and ``scipy`` for
certain random variable generation.

Compatibility
-------------

Stochastic is tested on Python versions...

Documentation
-------------


.. toctree::
   :maxdepth: 1

   general
   base
   discrete
   noise
   continuous
   diffusion
   notes



Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
