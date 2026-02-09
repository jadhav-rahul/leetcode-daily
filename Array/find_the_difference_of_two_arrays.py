# Problem Name: Find the Difference of Two Arrays
# Platform: LeetCode
# Topic: Array, Hashing
# Difficulty: Easy
#
# Approach:
# - Convert both arrays into sets to remove duplicates
# - Find elements present in nums1 but not in nums2
# - Find elements present in nums2 but not in nums1
# - Return both results as a list of lists
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        a = list(set(nums1) - set(nums2))
        b = list(set(nums2) - set(nums1))
        return [a, b]
