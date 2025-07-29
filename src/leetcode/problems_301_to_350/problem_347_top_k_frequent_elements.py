class Solution:
    """
    Solution to LeetCode problem 347, NeetCode 150 - arrays & hashing
    https://leetcode.com/problems/top-k-frequent-elements/
    https://neetcode.io/problems/top-k-elements-in-list

    Given an integer array and an integer k, return the k most frequent elements
    in the array.
    Assume the k most frequent elements are unique.
    The k most frequent elements can be in any order in the output.
    """

    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        # O(n) with bucket sort:
        # 1 round to get frequencies
        # 1 round to each frequency to numbers with that frequency
        # 1 round to go through frequencies from largest to smallest
        freq = {}
        max_freq = float('-inf')
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
            max_freq = max(max_freq, freq[num])
        if isinstance(max_freq, float):
            return []

        num_with_freq = {}
        for num, count in freq.items():
            if count not in num_with_freq:
                num_with_freq[count] = [num]
            else:
                num_with_freq[count].append(num)

        top_k = []
        nums_included = 0
        print(num_with_freq)
        for i in reversed(range(1, max_freq + 1)):
            print(i)
            if i in num_with_freq:
                for num in num_with_freq[i]:
                    top_k.append(num)
                    nums_included += 1
                    if nums_included >= k:
                        return top_k
        return top_k


def test_solution() -> None:
    solution = Solution()
    assert sorted(solution.top_k_frequent([7, 7], 1)) == sorted([7])
    assert sorted(solution.top_k_frequent([1, 2, 2, 3, 3, 3], 2)) == sorted([2, 3])
