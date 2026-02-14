# Problem Name: Determine if Two Strings Are Close
# Platform: LeetCode
# Topic: String, Hashing
# Difficulty: Medium
#
# Approach:
# - If lengths differ, return False
# - Check if both strings contain the same set of characters
# - Count frequency of each character using Counter
# - Compare sorted frequency values of both strings
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)

from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        occ1 = Counter(word1)
        occ2 = Counter(word2)

        return sorted(occ1.values()) == sorted(occ2.values())
