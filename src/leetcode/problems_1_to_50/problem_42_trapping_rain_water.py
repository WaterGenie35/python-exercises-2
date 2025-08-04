class Solution:
    """
    Solution to LeetCode problem 42, NeetCode 150 - two pointers
    https://leetcode.com/problems/trapping-rain-water/
    https://neetcode.io/problems/trapping-rain-water

    prompt
    """

    def trap(self, height: list[int]) -> int:
        area = 0
        width = len(height)
        left_wall = [0] * width
        right_wall = [0] * width

        current_highest = 0
        for i in range(width):
            current_highest = max(current_highest, height[i])
            left_wall[i] = current_highest
        current_highest = 0
        for i in reversed(range(width)):
            current_highest = max(current_highest, height[i])
            right_wall[i] = current_highest

        for i in range(width):
            lowest_wall = min(left_wall[i], right_wall[i])
            seafloor = height[i]
            if lowest_wall <= seafloor:
                continue
            area += lowest_wall - seafloor
        return area


def test_solution() -> None:
    solution = Solution()
    assert solution.trap([4, 2, 0, 3, 2, 5]) == 9
    assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
