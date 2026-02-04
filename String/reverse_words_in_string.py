# Problem Name: Reverse Words in a String
# Platform: LeetCode
# Topic: String
# Difficulty: Medium
#
# Approach:
# - Split the string into individual words using split()
# - Reverse the list of words
# - Join the words using a single space
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        return " ".join(words)
