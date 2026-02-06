# Problem Name: Move Zeroes
# Platform: LeetCode
# Topic: Array, Two Pointers
# Difficulty: Easy

# Approach:
# - Use a write pointer to track the position for the next non-zero element
# - Traverse the array and swap non-zero elements with the write position
# - This moves all zeroes to the end while maintaining relative order
#
# Time Complexity: O(n)
# Space Complexity: O(1) (in-place modification)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[write] = nums[write], nums[i]
                write += 1
        return nums