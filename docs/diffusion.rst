Diffusion Models
================

The :py:mod:`nhppy.diffusion` module provides classes for generating
(discretely sampled) continous-time diffusion processes using the
Euler–Maruyama method.

* :py:class:`nhppy.diffusion.ConstantElasticityVarianceProcess`
* :py:class:`nhppy.diffusion.CoxIngersollRossProcess`
* :py:class:`nhppy.diffusion.OrnsteinUhlenbeckProcess`
* :py:class:`nhppy.diffusion.VasicekProcess`

.. autoclass:: nhppy.diffusion.ConstantElasticityVarianceProcess
    :members: t, sample, times

.. autoclass:: nhppy.diffusion.CEVProcess


.. autoclass:: nhppy.diffusion.CoxIngersollRossProcess
    :members: t, sample, times

.. autoclass:: nhppy.diffusion.CIRProcess


.. autoclass:: nhppy.diffusion.OrnsteinUhlenbeckProcess
    :members: t, sample, times

.. autoclass:: nhppy.diffusion.OUProcess


.. autoclass:: nhppy.diffusion.VasicekProcess
    :members: t, sample, times
