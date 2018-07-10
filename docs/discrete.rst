Discrete-time Processes
=======================

The :py:mod:`nhppy.discrete` module provides classes for generating
discrete-time nhppy processes.

* :py:class:`nhppy.discrete.BernoulliProcess`
* :py:class:`nhppy.discrete.ChineseRestaurantProcess`
* :py:class:`nhppy.discrete.MarkovChain`
* :py:class:`nhppy.discrete.MoranProcess`
* :py:class:`nhppy.discrete.RandomWalk`

.. autoclass:: nhppy.discrete.BernoulliProcess
    :members: p, sample

.. autoclass:: nhppy.discrete.ChineseRestaurantProcess
    :members: discount, strength, sample, sample_partition, sequence_to_partition, partition_to_sequence

.. autoclass:: nhppy.discrete.MarkovChain
    :members: transition, initial, sample

.. autoclass:: nhppy.discrete.MoranProcess
    :members: n_max, sample

.. autoclass:: nhppy.discrete.RandomWalk
    :members: steps, weights, p, sample, sample_increments
