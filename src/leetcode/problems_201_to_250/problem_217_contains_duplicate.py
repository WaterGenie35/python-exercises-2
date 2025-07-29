class Solution:
    """
    Solution to LeetCode problem 217, NeetCode 150 - Array & Hashing
    https://leetcode.com/problems/contains-duplicate/
    https://neetcode.io/problems/duplicate-integer

    Given an array of integers, return True iff the array contains duplicate.
    """

    def contains_duplicate(self, nums: list[int]) -> bool:
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


def test_solution() -> None:
    solution = Solution()
    assert solution.contains_duplicate([1, 2, 3, 1])
    assert not solution.contains_duplicate([1, 2, 3, 4])
    assert solution.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
