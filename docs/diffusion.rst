Diffusion Models
================

The :py:mod:`stochastic.processes.diffusion` module provides classes for generating
discretely sampled continous-time diffusion processes using the
Euler–Maruyama method.

* :py:class:`stochastic.processes.diffusion.DiffusionProcess`
* :py:class:`stochastic.processes.diffusion.ConstantElasticityVarianceProcess`
* :py:class:`stochastic.processes.diffusion.CoxIngersollRossProcess`
* :py:class:`stochastic.processes.diffusion.OrnsteinUhlenbeckProcess`
* :py:class:`stochastic.processes.diffusion.VasicekProcess`

.. autoclass:: stochastic.processes.diffusion.DiffusionProcess
    :members: t, sample, times


.. autoclass:: stochastic.processes.diffusion.ConstantElasticityVarianceProcess
    :members: t, sample, times


.. autoclass:: stochastic.processes.diffusion.CoxIngersollRossProcess
    :members: t, sample, times


.. autoclass:: stochastic.processes.diffusion.OrnsteinUhlenbeckProcess
    :members: t, sample, times


.. autoclass:: stochastic.processes.diffusion.VasicekProcess
    :members: t, sample, times
