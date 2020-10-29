"""Test ColoredNoise."""


def test_colored_noise_str_repr(t, colored_noise_class):
    instance = colored_noise_class(t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_colored_noise_sample(t, n, beta, colored_noise_class):
    instance = colored_noise_class(t)
    s = instance.sample(n)
    assert len(s) == n + 1
