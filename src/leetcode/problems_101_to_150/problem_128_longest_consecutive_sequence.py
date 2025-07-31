class Solution:
    """
    Solution to LeetCode problem 128, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/longest-consecutive-sequence/
    https://neetcode.io/problems/longest-consecutive-sequence

    Given an integer array, return the length of the longest consecutive sequence
    that can be formed using elements from the array.
    The algorithm must run in O(n) time.
    """

    def longest_consecutive(self, nums: list[int]) -> int:
        longest_from_num: dict[int, int] = {}
        longest = 0
        for num in nums:
            if num in longest_from_num and longest_from_num[num] > 0:
                continue

            prev = num - 1
            next = num + 1
            if prev not in longest_from_num:
                longest_from_num[prev] = 0
            if next not in longest_from_num:
                longest_from_num[next] = 0
            new_length = longest_from_num[prev] + 1 + longest_from_num[next]
            longest = max(longest, new_length)
            longest_from_num[num] = new_length

            # Sufficient to keep sequence start/end updated
            # as num in-between existing sequence doesn't contribute
            seq_start = num - longest_from_num[prev]
            seq_end = num + longest_from_num[next]
            longest_from_num[seq_start] = new_length
            longest_from_num[seq_end] = new_length

        return longest


def test_solution() -> None:
    solution = Solution()
    assert solution.longest_consecutive([2, 20, 4, 10, 3, 4, 5]) == 4
    assert solution.longest_consecutive([0, 3, 2, 5, 4, 6, 1, 1]) == 7
    assert solution.longest_consecutive([3, 1, 2, -10, 6, 9, 8, 5, 7, -20, 4]) == 9
