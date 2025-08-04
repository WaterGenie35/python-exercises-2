class Solution:
    """
    Solution to LeetCode problem 11, NeetCode 150 - two pointers
    https://leetcode.com/problems/container-with-most-water/
    https://neetcode.io/problems/max-water-container

    Given an interger array of heights of each bar, return the maximum amount of
    area defined by the rectangle whose height is the minimum of the 2 chosen bars
    and whose width is the difference between the indices.
    """

    def max_area(self, heights: list[int]) -> int:
        area = 0
        head = 0
        tail = len(heights) - 1
        while head < tail:
            height_head = heights[head]
            height_tail = heights[tail]
            height = min(height_head, height_tail)
            width = tail - head
            new_area = width * height
            area = max(area, new_area)

            if height_head <= height_tail:
                head += 1
            else:
                tail -= 1
        return area


def test_solution() -> None:
    solution = Solution()
    assert solution.max_area([2, 2, 2]) == 4
    assert solution.max_area([1, 7, 2, 5, 4, 7, 3, 6]) == 36
