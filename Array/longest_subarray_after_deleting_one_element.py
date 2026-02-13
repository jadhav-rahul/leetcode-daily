# Problem Name: Longest Subarray of 1's After Deleting One Element
# Platform: LeetCode
# Topic: Array, Sliding Window
# Difficulty: Medium
#
# Approach:
# - Use a sliding window with two pointers
# - Allow at most one zero inside the window
# - If zero count exceeds one, shrink the window from the left
# - Since one element must be deleted, window length is (front - back)
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        back = 0
        zero_count = 0
        ans = 0

        for front in range(len(nums)):
            if nums[front] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[back] == 0:
                    zero_count -= 1
                back += 1

            ans = max(ans, front - back)

        return ans
