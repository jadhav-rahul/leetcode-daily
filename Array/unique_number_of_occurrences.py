# Problem Name: Unique Number of Occurrences
# Platform: LeetCode
# Topic: Array, Hashing
# Difficulty: Easy
#
# Approach:
# - Use a hash map to count the frequency of each number
# - Store all frequencies
# - Check if all frequencies are unique using a set
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        return len(freq.values()) == len(set(freq.values()))
