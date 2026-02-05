# Problem Name: Increasing Triplet Subsequence
# Platform: LeetCode
# Topic: Array, Greedy
# Difficulty: Medium
#
# Approach:
# - Maintain two variables to store the smallest and second smallest values
# - Traverse the array:
#   - Update first if current number is smaller or equal
#   - Else update second if current number is smaller or equal
#   - If a number greater than both is found, triplet exists
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
