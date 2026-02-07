# Problem Name: Max Number of K-Sum Pairs
# Platform: LeetCode
# Topic: Array, Two Pointers
# Difficulty: Medium
#
# Approach:
# - Sort the array
# - Use two pointers from start and end
# - If sum equals k, count the pair and move both pointers
# - If sum is less than k, move left pointer
# - If sum is greater than k, move right pointer
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i = 0
        j = len(nums) - 1
        ans = 0

        while i < j:
            total = nums[i] + nums[j]

            if total == k:
                ans += 1
                i += 1
                j -= 1
            elif total < k:
                i += 1
            else:
                j -= 1

        return ans
