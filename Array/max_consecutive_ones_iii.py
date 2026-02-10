# Problem Name: Max Consecutive Ones III
# Platform: LeetCode
# Topic: Array, Sliding Window
# Difficulty: Medium
#
# Approach:
# - Use a sliding window with two pointers
# - Expand the window by moving the right pointer
# - Count the number of zeroes in the current window
# - If zeroes exceed k, shrink the window from the left
# - Track the maximum window size where zeroes ≤ k
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        back = 0
        zeroes = 0
        ans = 0

        for front in range(len(nums)):
            if nums[front] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[back] == 0:
                    zeroes -= 1
                back += 1

            ans = max(ans, front - back + 1)

        return ans
