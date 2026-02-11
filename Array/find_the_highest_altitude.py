# Problem Name: Find the Highest Altitude
# Platform: LeetCode
# Topic: Array, Prefix Sum
# Difficulty: Easy
#
# Approach:
# - Start with altitude = 0
# - Traverse the gain array and keep adding values
# - Track the maximum altitude reached during traversal
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        max_altitude = 0

        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)

        return max_altitude
