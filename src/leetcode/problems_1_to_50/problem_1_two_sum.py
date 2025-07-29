class Solution:
    """
    Solution to LeetCode problem 1, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/two-sum/
    https://neetcode.io/problems/two-integer-sum

    Given an array of integers and a target integer, return 2 different indices
    such that the corresponding integers in the array sum to the target integer.
    Assume that a unique solution exists.
    Provide the smaller index first.
    """

    def two_sum(self, nums: list[int], target: int) -> tuple[int, int]:
        num_index: dict[int, int] = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_index:
                return (num_index[complement], index)
            num_index[num] = index
        # Never happen by assumption:
        return (-1, -1)


def test_solution() -> None:
    solution = Solution()
    assert solution.two_sum([3, 4, 5, 6], 7) == (0, 1)
    assert solution.two_sum([4, 5, 6], 10) == (0, 2)
    assert solution.two_sum([5, 5], 10) == (0, 1)
