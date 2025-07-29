class Solution:
    """
    Solution to LeetCode problem 242, NeetCode 150 - Array & Hashing
    https://leetcode.com/problems/valid-anagram/
    https://neetcode.io/problems/is-anagram

    Given 2 strings, return true iff they are anagrams of each other.
    Strings are an anagram of each other iff they contain the same number of
    characters regardless of order.
    """

    def is_anagram(self, s: str, t: str) -> bool:
        char_freq: dict[str, int] = {}
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
        for char in t:
            if char not in char_freq or char_freq[char] == 0:
                return False
            char_freq[char] -= 1
            if char_freq[char] == 0:
                del char_freq[char]
        return len(char_freq) == 0


def test_solution() -> None:
    solution = Solution()
    assert solution.is_anagram("racecar", "carrace")
    assert not solution.is_anagram("jar", "jam")
