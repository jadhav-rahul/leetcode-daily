# Problem Name: Reverse Vowels of a String
# Platform: LeetCode
# Topic: String, Two Pointers
# Difficulty: Easy
#
# Approach:
# - Use two pointers from start and end
# - Move pointers until vowels are found
# - Swap vowels and continue
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        s = list(s)
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1

            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)
