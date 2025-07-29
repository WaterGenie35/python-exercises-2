def solution() -> None:
    """
    Solution to Project Euler problem 2
    https://projecteuler.net/problem=2

    Find the sum of even fibonacci numbers below 4_000_000.
    Start the fibonacci sequence with 1 and 2.
    """
    print(sum_of_even_fibonacci(lt_bound=4_000_000))


def sum_of_even_fibonacci(lt_bound: int) -> int:
    # Let e(n) be the nth even Fibonacci term
    # e(n) = f(3n-1) by induction on P(k): f(3k-2) is odd and f(3k-1) is even
    # e(n) = 4e(n-1) + e(n-2) by algebra
    # Here, e(1) = f(2) = 2 and e(2) = f(5) = 8
    if lt_bound <= 2:
        return 0
    if lt_bound <= 8:
        return 2
    total = 2
    prev = 2
    head = 8
    while head < lt_bound:
        total += head
        tmp = head
        head = (4 * head) + prev
        prev = tmp
    return total


def test_solution() -> None:
    assert sum_of_even_fibonacci(0) == 0
    assert sum_of_even_fibonacci(1) == 0
    assert sum_of_even_fibonacci(2) == 0
    assert sum_of_even_fibonacci(3) == 2
    assert sum_of_even_fibonacci(8) == 2
    assert sum_of_even_fibonacci(9) == 10
    assert sum_of_even_fibonacci(4_000_000) == 4_613_732
