# Problem Name: Container With Most Water
# Platform: LeetCode
# Topic: Array, Two Pointers
# Difficulty: Medium
#
# Approach:
# - Use two pointers starting from both ends of the array
# - Calculate the area formed by the two pointers
# - Move the pointer with the smaller height to try to increase area
# - Keep track of the maximum area found
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = 0
        b = len(height) - 1
        ans = 0

        while a < b:
            dist = b - a
            if height[a] < height[b]:
                ans = max(ans, height[a] * dist)
                a += 1
            else:
                ans = max(ans, height[b] * dist)
                b -= 1

        return ans
