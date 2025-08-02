def solution() -> None:
    """
    Solution to Project Euler problem 6
    https://projecteuler.net/problem=6

    Find the difference between the sum of the squares of the first 100 natural
    numbers and the square of the sum.
    """
    print(sum_square_difference(lte_bound=100))


def sum_square_difference(lte_bound: int) -> int:
    sum_of_squares = 0
    square_of_sum = int((lte_bound * (lte_bound + 1) / 2) ** 2)
    for n in range(lte_bound + 1):
        sum_of_squares += n**2
    return abs(sum_of_squares - square_of_sum)


def test_solution() -> None:
    assert sum_square_difference(lte_bound=10) == 2_640
    assert sum_square_difference(lte_bound=100) == 25_164_150
