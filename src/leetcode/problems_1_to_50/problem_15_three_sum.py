from utils.list import sorted_nested


class Solution:
    """
    Solution to LeetCode problem 15, NeetCode 150 - two pointers
    https://leetcode.com/problems/3sum/
    https://neetcode.io/problems/three-integer-sum

    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    where each triplet sums up to 0 and i, j, and k are distinct.
    The output must not contain duplicate triplets.
    """

    def three_sum(self, nums: list[int]) -> list[list[int]]:
        triplets: set[tuple[int, int, int]] = set()
        sorted_nums = sorted(nums)
        for i in range(len(nums) - 2):
            nums_i = sorted_nums[i]
            if nums_i > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                nums_j = sorted_nums[j]
                nums_k = sorted_nums[k]
                total = nums_i + nums_j + nums_k
                if total > 0:
                    k -= 1
                    continue
                if total < 0:
                    j += 1
                    continue
                triplets.add((nums_i, nums_j, nums_k))
                j += 1

        return [list(triplet) for triplet in triplets]


def test_solution() -> None:
    solution = Solution()
    assert sorted_nested(solution.three_sum([-1, 0, 1, 2, -1, -4])) == sorted_nested([[-1, -1, 2], [-1, 0, 1]])
    assert solution.three_sum([0, 1, 1]) == []
    assert solution.three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert sorted_nested(solution.three_sum([-2, 0, 1, 1, 2])) == sorted_nested([[-2, 0, 2], [-2, 1, 1]])
