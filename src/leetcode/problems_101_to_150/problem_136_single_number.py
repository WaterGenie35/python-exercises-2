class Solution:
    """
    Solution to LeetCode problem 136, NeetCode 150 - bit manipulation
    https://leetcode.com/problems/single-number/
    https://neetcode.io/problems/single-number

    Given a non-empty array of integers where every integer appears twice except one,
    return the integer that appears once.

    Must run in O(n) time and O(1) space.
    """

    def single_number(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor


def test_solution() -> None:
    solution = Solution()
    assert solution.single_number([3, 2, 3]) == 2
    assert solution.single_number([7, 6, 6, 7, 8]) == 8
