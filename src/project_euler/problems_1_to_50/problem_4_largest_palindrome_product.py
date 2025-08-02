from utils.string import is_palindrome
from utils.typing import Nullable


def solution() -> None:
    """
    Solution to Project Euler problem 4
    https://projecteuler.net/problem=4

    Find the largest palindrome that is a product of two 3-digit numbers.
    """
    print(largest_palindrome_product_from_digits(3))


def largest_palindrome_product_from_digits(digits: int) -> Nullable[int]:
    largest: float | int = float('-inf')

    upper_bound = (10**digits) - 1
    lower_bound = 10 ** (digits - 1)

    for term_1 in range(upper_bound, lower_bound - 1, -1):
        for term_2 in range(term_1, lower_bound - 1, -1):
            product = term_1 * term_2
            if is_palindrome(str(product)) and product > largest:
                largest = product

    if isinstance(largest, float):
        return None
    return largest


def test_solution() -> None:
    assert largest_palindrome_product_from_digits(2) == 90_09
    assert largest_palindrome_product_from_digits(3) == 906_609
