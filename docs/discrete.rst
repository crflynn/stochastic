Discrete-time Processes
=======================

The :py:mod:`stochastic.processes.discrete` module provides classes for generating
discrete-time stochastic processes.

* :py:class:`stochastic.processes.discrete.BernoulliProcess`
* :py:class:`stochastic.processes.discrete.ChineseRestaurantProcess`
* :py:class:`stochastic.processes.discrete.DirichletProcess`
* :py:class:`stochastic.processes.discrete.MarkovChain`
* :py:class:`stochastic.processes.discrete.MoranProcess`
* :py:class:`stochastic.processes.discrete.RandomWalk`

.. autoclass:: stochastic.processes.discrete.BernoulliProcess
    :members: p, sample

.. autoclass:: stochastic.processes.discrete.ChineseRestaurantProcess
    :members: discount, strength, sample, sample_partition, sequence_to_partition, partition_to_sequence

.. autoclass:: stochastic.processes.discrete.DirichletProcess
    :members: base, alpha, sample

.. autoclass:: stochastic.processes.discrete.MarkovChain
    :members: transition, initial, sample

.. autoclass:: stochastic.processes.discrete.MoranProcess
    :members: maximum, sample

.. autoclass:: stochastic.processes.discrete.RandomWalk
    :members: steps, weights, p, sample, sample_increments
