# Problem Name: Greatest Common Divisor of Strings
# Platform: LeetCode
# Topic: String, Mathematics
# Difficulty: Easy
#
# Approach:
# - If str1 + str2 != str2 + str1, no common divisor exists
# - Compute GCD of lengths of both strings
# - The substring of length gcd(len(str1), len(str2)) is the answer
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        gcd_length = gcd(len(str1), len(str2))

        return str1[:gcd_length]
