from utils.maths.prime import is_prime


def test_is_prime() -> None:
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(65_537)
    assert is_prime(87_178_291_199)
    # assert is_prime(3_331_113_965_338_635_107)

    assert not is_prime(-3)
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(65_535)
    assert not is_prime(87_178_291_197)
    # assert not is_prime(3_331_113_965_338_635_109)
