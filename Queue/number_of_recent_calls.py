# Problem Name: Number of Recent Calls
# Platform: LeetCode
# Topic: Queue, Sliding Window
# Difficulty: Easy
#
# Approach:
# - Use a deque to store timestamps
# - For each ping(t):
#     1. Add current timestamp to the queue
#     2. Remove timestamps less than (t - 3000)
# - The size of the queue represents the number of valid recent calls
#
# Time Complexity:
# - Amortized O(1) per ping
# Space Complexity: O(n)

from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.q = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)

        while self.q and self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)
