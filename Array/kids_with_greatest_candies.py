# Problem Name: Kids With the Greatest Number of Candies
# Platform: LeetCode
# Topic: Array
# Difficulty: Easy
#
# Approach:
# - Find the maximum candies among all kids
# - For each kid, check if candies + extraCandies is at least max
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans = []
        maxCandy = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandy:
                ans.append(True)
            else:
                ans.append(False)

        return ans
