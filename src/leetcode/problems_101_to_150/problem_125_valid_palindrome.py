from math import ceil


class Solution:
    """
    Solution to LeetCode problem 125, NeetCode 150 - two pointers
    https://leetcode.com/problems/valid-palindrome/
    https://neetcode.io/problems/is-palindrome

    Check if the given string is a palindrome.
    Case-insensitive and ignore all non-alphanumeric characters.
    """

    a = ord("a")
    z = ord("z")
    A = ord("A")
    Z = ord("Z")
    num_0 = ord("0")
    num_9 = ord("9")

    def is_palindrome(self, string: str) -> bool:
        alphanumeric = []
        for s in string:
            c = ord(s)
            if (self.a <= c and c <= self.z) or (self.A <= c and c <= self.Z) or (self.num_0 <= c and c <= self.num_9):
                alphanumeric.append(s.lower())
        for head in range(ceil(len(alphanumeric) / 2)):
            tail = (len(alphanumeric) - head) - 1
            if alphanumeric[head] != alphanumeric[tail]:
                return False
        return True


def test_solution() -> None:
    solution = Solution()
    assert solution.is_palindrome("")
    assert solution.is_palindrome(" ")
    assert solution.is_palindrome("a!")
    assert solution.is_palindrome("0aA0")
    assert solution.is_palindrome("Was it a car or a cat I saw?")
    assert not solution.is_palindrome("tab a cat")
