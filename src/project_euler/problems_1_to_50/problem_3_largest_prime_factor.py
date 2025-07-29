from math import floor, sqrt

from utils.maths.prime import is_prime
from utils.typing import Nullable


def solution() -> None:
    """
    Solution to Project Euler problem 3
    https://projecteuler.net/problem=3

    Find the largest prime factor of 600_851_475_143
    """
    print(largest_prime_factor(600_851_475_143))


def largest_prime_factor(num: int) -> Nullable[int]:
    largest: float | int = float('-inf')
    if num % 2 == 0:
        largest = 2
    head = 3
    lte_bound = floor(sqrt(num))
    while head <= lte_bound:
        if num % head == 0:
            pair = num // head
            if is_prime(pair):
                return pair
            if is_prime(head):
                largest = head
        head += 2

    if isinstance(largest, float):
        return None
    return largest


def test_solution() -> None:
    assert largest_prime_factor(13_195) == 29
    assert largest_prime_factor(600_851_475_143) == 6_857
