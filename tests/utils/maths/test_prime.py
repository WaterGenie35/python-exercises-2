from utils.maths.prime import is_prime, primes


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


def test_primes() -> None:
    assert primes(lte_bound=1) == []
    assert primes(lte_bound=2) == [2]
    assert primes(lte_bound=10) == [2, 3, 5, 7]
    assert primes(lte_bound=11) == [2, 3, 5, 7, 11]
    assert primes(lte_bound=75) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
