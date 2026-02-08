# Problem Name: Maximum Average Subarray I
# Platform: LeetCode
# Topic: Array, Sliding Window
# Difficulty: Easy
#
# Approach:
# - Calculate the sum of the first window of size k
# - Slide the window by removing the left element and adding the next element
# - Track the maximum window sum
# - Divide the maximum sum by k to get the average
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        back = 0
        front = k
        window_sum = sum(nums[back:front])
        max_sum = window_sum

        while front < len(nums):
            window_sum = window_sum - nums[back] + nums[front]
            max_sum = max(max_sum, window_sum)
            back += 1
            front += 1

        return float(max_sum) / k
