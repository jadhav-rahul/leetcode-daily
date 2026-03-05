# Problem Name: Single Number
# Platform: LeetCode
# Topic: Array, Bit Manipulation
# Difficulty: Easy
#
# Approach:
# - Use XOR operation
# - XOR of a number with itself becomes 0
# - XOR of a number with 0 remains the number
# - All duplicate numbers cancel out, leaving the single number
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for num in nums:
            result ^= num

        return result
