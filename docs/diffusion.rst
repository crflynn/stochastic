Diffusion Models
================

The :py:mod:`stochastic.diffusion` module provides classes for generating
(discretely sampled) continous-time diffusion processes using the
Euler–Maruyama method.

* :py:class:`stochastic.diffusion.DiffusionProcess`
* :py:class:`stochastic.diffusion.ConstantElasticityVarianceProcess`
* :py:class:`stochastic.diffusion.CoxIngersollRossProcess`
* :py:class:`stochastic.diffusion.OrnsteinUhlenbeckProcess`
* :py:class:`stochastic.diffusion.VasicekProcess`

.. autoclass:: stochastic.diffusion.DiffusionProcess
    :members: t, sample, times


.. autoclass:: stochastic.diffusion.ConstantElasticityVarianceProcess
    :members: t, sample, times


.. autoclass:: stochastic.diffusion.CoxIngersollRossProcess
    :members: t, sample, times


.. autoclass:: stochastic.diffusion.OrnsteinUhlenbeckProcess
    :members: t, sample, times


.. autoclass:: stochastic.diffusion.VasicekProcess
    :members: t, sample, times
