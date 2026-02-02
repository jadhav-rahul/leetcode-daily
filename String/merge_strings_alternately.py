# Problem Name: Merge Strings Alternately
# Platform: LeetCode
# Topic: String, Two Pointers
# Difficulty: Easy
#
# Approach:
# - Use two pointers to traverse both strings
# - Append characters alternately to the result
# - Append remaining characters after one string ends
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        j = 0
        res = ""

        while i < len(word1) and j < len(word2):
            res += word1[i] + word2[j]
            i += 1
            j += 1

        res += word1[i:]
        res += word2[j:]

        return res
