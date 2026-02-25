# Problem Name: Subsets
# Platform: LeetCode
# Topic: Backtracking, Recursion
# Difficulty: Medium
#
# Approach:
# - Use recursion to generate all subsets
# - At each index, choose:
#     1. Include the current element
#     2. Exclude the current element
# - When index reaches end of array, add current subset to result
#
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n) (recursion stack)

class Solution(object):

    def allsubsets(self, i, n, nums, ans, result):
        if i >= n:
            result.append(list(ans))
            return

        # Include current element
        ans.append(nums[i])
        self.allsubsets(i + 1, n, nums, ans, result)

        # Exclude current element
        ans.pop()
        self.allsubsets(i + 1, n, nums, ans, result)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []
        result = []

        self.allsubsets(0, n, nums, ans, result)
        return result