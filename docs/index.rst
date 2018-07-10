.. nhppy documentation master file, created by
   sphinx-quickstart on Sun Dec 31 20:50:28 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

nhppy
==========

|travis| |rtd| |codecov| |pypi| |pyversions|


.. |travis| image:: https://img.shields.io/travis/crflynn/nhppy.svg
    :target: https://travis-ci.org/crflynn/nhppy

.. |rtd| image:: https://img.shields.io/readthedocs/nhppy.svg
    :target: http://nhppy.readthedocs.io/en/latest/

.. |codecov| image:: https://codecov.io/gh/crflynn/nhppy/branch/master/graphs/badge.svg
    :target: https://codecov.io/gh/crflynn/nhppy

.. |pypi| image:: https://img.shields.io/pypi/v/nhppy.svg
    :target: https://pypi.python.org/pypi/nhppy

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/nhppy.svg
    :target: https://pypi.python.org/pypi/nhppy


Stochastic is a python package for generating realizations of
nhppy processes.

Installation
------------

Stochastic is a python package available on
`pypi <https://pypi.python.org/pypi>`_ and can be installed using ``pip``:

.. code-block:: bash

   pip install nhppy

Dependencies
------------

Stochastic depends on ``numpy`` for most calculations and ``scipy`` for
certain random variable generation.

Compatibility
-------------

Stochastic is tested on Python versions 2.7, 3.4, 3.5, and 3.6.

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
   base
   discrete
   noise
   continuous
   diffusion
   analysis
   notes



Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
