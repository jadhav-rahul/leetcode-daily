# Problem Name: Product of Array Except Self
# Platform: LeetCode
# Topic: Array, Prefix Sum
# Difficulty: Medium
#
# Approach:
# - Create an answer array initialized with 1
# - Traverse from left to right to store prefix product for each index
# - Traverse from right to left to multiply suffix product
# - Final array contains product of all elements except itself
#
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output array)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = 1
        ans = [1] * n

        # Prefix product
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # Suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
