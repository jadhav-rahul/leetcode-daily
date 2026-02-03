# Problem Name: Can Place Flowers
# Platform: LeetCode
# Topic: Array, Greedy
# Difficulty: Easy
#
# Approach:
# - Traverse the flowerbed
# - For each empty plot, check left and right plots
# - Place a flower if both sides are empty
# - Decrease n and return early if n becomes zero
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = (i == 0) or flowerbed[i - 1] == 0
                right = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0

                if left and right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True

        return n <= 0
