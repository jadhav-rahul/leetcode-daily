# Problem Name: Max Number of K-Sum Pairs
# Platform: LeetCode
# Topic: Array, Hashing
# Difficulty: Medium
#
# Approach:
# - Use a hash map to store frequencies of numbers
# - For each number, check if its complement (k - num) exists
# - If yes, form a pair and decrease frequency
# - Otherwise, store the current number in the map
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        freq = {}

        for num in nums:
            need = k - num

            if freq.get(need, 0) > 0:
                ans += 1
                freq[need] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1

        return ans
