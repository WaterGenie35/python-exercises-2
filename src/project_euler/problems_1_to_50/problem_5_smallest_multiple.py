from utils.maths.prime import primes


def solution() -> None:
    """
    Solution to Project Euler problem 5
    https://projecteuler.net/problem=5

    Find the smallest positive number that is evenly divisible by all numbers
    from 1 to 20.
    """
    print(evenly_divisible_up_to(lte_bound=20))


def evenly_divisible_up_to(lte_bound: int) -> int:
    # Least common multiple
    # Corresponds to the product of largest prime powers of each prime in the
    # prime factorisation of each number <= lte_bound.
    # https://en.wikipedia.org/wiki/Least_common_multiple#Using_prime_factorization
    prime_factors = primes(lte_bound)
    largest_prime_powers = {prime: 0 for prime in prime_factors}
    for n in range(2, lte_bound + 1):
        remaining = n
        for factor in prime_factors:
            power = 0
            while remaining % factor == 0:
                power += 1
                remaining //= factor
            if power > largest_prime_powers[factor]:
                largest_prime_powers[factor] = power
    lcm = 1
    for prime, power in largest_prime_powers.items():
        lcm *= prime**power
    return lcm


def _brute_force_evenly_divisible_up_to(lte_bound: int) -> int:
    head = lte_bound
    while True:
        evenly_divisible = True
        for divisor in range(2, lte_bound + 1):
            if head % divisor != 0:
                evenly_divisible = False
                break
        if evenly_divisible:
            return head
        head += lte_bound


def test_solution() -> None:
    assert evenly_divisible_up_to(lte_bound=10) == 2_520
    assert evenly_divisible_up_to(lte_bound=20) == 232_792_560
