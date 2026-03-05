# Problem Name: Rotate String
# Platform: LeetCode
# Topic: String
# Difficulty: Easy
#
# Approach:
# - If lengths differ, rotation is not possible
# - Concatenate the string with itself (s + s)
# - If goal is a substring of (s + s), then it is a valid rotation
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        return goal in (s + s)
