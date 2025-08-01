class Solution:
    """
    Solution to LeetCode problem 49, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/group-anagrams/
    https://neetcode.io/problems/anagram-groups

    Given an array of strings, return a list of lists where each sublist contain
    strings in the input array that are anagrams of each other.
    Strings are an anagram of each other iff they contain the same number of
    characters regardless of order.
    The sublists can be in any order, and the strings in each sublists can be
    in any order.
    """

    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        groups: dict[tuple[int, ...], list[str]] = {}
        index_offset = ord('a')
        for s in strs:
            char_freq = [0] * 26
            for char in s:
                index = ord(char) - index_offset
                char_freq[index] += 1
            key: tuple[int, ...] = tuple(char_freq)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return list(groups.values())


def sorted_inner(groups: list[list[str]]) -> list[list[str]]:
    inner = []
    for group in groups:
        inner.append(sorted(group))
    return sorted(inner)


def test_solution() -> None:
    solution = Solution()
    assert sorted_inner(solution.group_anagrams([])) == sorted_inner([])
    assert sorted_inner(solution.group_anagrams(["x"])) == sorted_inner([["x"]])
    assert sorted_inner(solution.group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"])) == sorted_inner(
        [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
    )
