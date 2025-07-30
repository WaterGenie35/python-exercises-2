class Solution:
    """
    Solution to LeetCode problem 238, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/product-of-array-except-self/
    https://neetcode.io/problems/products-of-array-discluding-self

    Given an integer array, return an array of the same size where the ith output
    element is the product of every integer in the array except the ith element.
    Assume that the products fit in a 32-bit integer.
    Solve in O(n) with no division.
    """

    def product_except_self(self, nums: list[int]) -> list[int]:
        length = len(nums)
        from_left = [1] * length
        from_right = [1] * length
        products = [1] * length

        head = nums[0]
        for i in range(1, length):
            from_left[i] = head
            head *= nums[i]
        head = nums[-1]
        for i in reversed(range(length - 1)):
            from_right[i] = head
            head *= nums[i]

        for i in range(length):
            products[i] = from_left[i] * from_right[i]
        return products


def test_solution() -> None:
    solution = Solution()
    assert solution.product_except_self([1, 2, 4, 6]) == [48, 24, 12, 8]
    assert solution.product_except_self([-1, 0, 1, 2, 3]) == [0, -6, 0, 0, 0]
