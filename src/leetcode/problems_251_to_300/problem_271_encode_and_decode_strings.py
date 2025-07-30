class Solution:
    """
    Solution to LeetCode problem 271, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/encode-and-decode-strings/ (pay-walled)
    https://neetcode.io/problems/string-encode-and-decode

    Design an algorithm to encode a list of strings to a single string and a
    corresponding algorithm to decode a string back to the original list.
    """

    separator = "␟"  # unit separator

    def encode(self, strs: list[str]) -> str:
        prefix = f"{len(strs)}{Solution.separator}"
        return f"{prefix}{Solution.separator.join(strs)}"

    def decode(self, s: str) -> list[str]:
        parts = s.split(Solution.separator)
        length = int(parts[0])
        if length == 0:
            return []
        return parts[1:]


def test_solution() -> None:
    solution = Solution()
    list_1: list[str] = ["we", "say", ":", "yes"]
    assert solution.decode(solution.encode(list_1)) == list_1
    list_2: list[str] = []
    assert solution.decode(solution.encode(list_2)) == list_2
    list_3: list[str] = ["foo"]
    assert solution.decode(solution.encode(list_3)) == list_3
    list_4: list[str] = [""]
    assert solution.decode(solution.encode(list_4)) == list_4
