# Problem Name: Maximum Number of Vowels in a Substring of Given Length
# Platform: LeetCode
# Topic: String, Sliding Window
# Difficulty: Medium
#
# Approach:
# - Count vowels in the first window of size k
# - Slide the window by removing the left character and adding the right character
# - Update the maximum vowel count at each step
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = "AEIOUaeiou"
        ans = 0

        # Count vowels in the first window
        for ch in s[:k]:
            if ch in vowels:
                ans += 1

        max_ans = ans
        back = 0
        front = k

        # Slide the window
        while front < len(s):
            if s[back] in vowels:
                ans -= 1
            if s[front] in vowels:
                ans += 1

            max_ans = max(max_ans, ans)
            back += 1
            front += 1

        return max_ans
