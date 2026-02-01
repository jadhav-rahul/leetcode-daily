# Problem: Minimum Cost
# Platform: LeetCode
# Approach: Sort remaining elements and pick smallest
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution(object):
    def minimumCost(self, nums):
        first = nums[0]
        nums = sorted(nums[1:])
        return first + sum(nums[:2])