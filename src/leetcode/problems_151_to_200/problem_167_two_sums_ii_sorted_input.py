class Solution:
    """
    Solution to LeetCode problem 167, NeetCode 150 - two pointers
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
    https://neetcode.io/problems/two-integer-sum-ii

    Given an integer array sorted in non-decreasing order, return 1-based indices
    i, j such that i < j and the ith and jth element sum to the target number.
    Assume a unique solution exists.
    """

    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        head = 0
        tail = len(numbers) - 1
        current_sum = numbers[head] + numbers[tail]
        while current_sum != target:
            if current_sum < target:
                head += 1
            else:
                tail -= 1
            current_sum = numbers[head] + numbers[tail]
        return [head + 1, tail + 1]


def test_solution() -> None:
    solution = Solution()
    assert solution.two_sum([-1, 0], -1) == [1, 2]
    assert solution.two_sum([1, 2, 3, 4], 3) == [1, 2]
    assert solution.two_sum([0, 0, 1, 2, 5, 9, 10, 11], 16) == [5, 8]
