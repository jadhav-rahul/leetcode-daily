# Problem Name: Find Pivot Index
# Platform: LeetCode
# Topic: Array, Prefix Sum
# Difficulty: Easy
#
# Approach:
# - Compute the total sum of the array
# - Traverse the array while maintaining left_sum
# - For each index, check:
#     left_sum == total_sum - left_sum - nums[i]
# - If true, return the index
# - Otherwise, update left_sum
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1
