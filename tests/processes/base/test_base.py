import pytest

from stochastic.processes.base import BaseProcess
from stochastic.processes.base import BaseSequenceProcess
from stochastic.processes.base import BaseTimeProcess


def test_base_process(end, n):
    with pytest.raises(TypeError):
        _ = BaseProcess()


def test_base_sequence_process(end, n):
    with pytest.raises(TypeError):
        _ = BaseSequenceProcess()


def test_base_time_process(end, n):
    with pytest.raises(TypeError):
        _ = BaseTimeProcess()
