# Problem Name: String Compression
# Platform: LeetCode
# Topic: String, Two Pointers
# Difficulty: Medium
#
# Approach:
# - Use two pointers to group consecutive characters
# - Count frequency of each character
# - Write the character and its count (if > 1) back into the array
# - Use a write pointer to modify the array in-place
#
# Time Complexity: O(n)
# Space Complexity: O(1) (in-place modification)

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        i = 0
        j = 0
        write = 0

        while j < n and i < n:
            count = 0

            # Count consecutive characters
            while j < n and chars[j] == chars[i]:
                count += 1
                j += 1

            # Write character
            chars[write] = chars[i]
            write += 1

            # Write count if greater than 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

            i = j

        return write
