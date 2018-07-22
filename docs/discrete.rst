Discrete-time Processes
=======================

The :py:mod:`stochastic.discrete` module provides classes for generating
discrete-time stochastic processes.

* :py:class:`stochastic.discrete.BernoulliProcess`
* :py:class:`stochastic.discrete.ChineseRestaurantProcess`
* :py:class:`stochastic.discrete.MarkovChain`
* :py:class:`stochastic.discrete.MoranProcess`
* :py:class:`stochastic.discrete.RandomWalk`

.. autoclass:: stochastic.discrete.BernoulliProcess
    :members: p, sample

.. autoclass:: stochastic.discrete.ChineseRestaurantProcess
    :members: discount, strength, sample, sample_partition, sequence_to_partition, partition_to_sequence

.. autoclass:: stochastic.discrete.MarkovChain
    :members: transition, initial, sample

.. autoclass:: stochastic.discrete.MoranProcess
    :members: maximum, sample

.. autoclass:: stochastic.discrete.RandomWalk
    :members: steps, weights, p, sample, sample_increments
