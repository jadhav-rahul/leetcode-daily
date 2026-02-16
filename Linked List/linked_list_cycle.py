# Problem Name: Linked List Cycle
# Platform: LeetCode
# Topic: Linked List, Two Pointers
# Difficulty: Easy
#
# Approach:
# - Use two pointers (slow and fast)
# - Move slow by one step and fast by two steps
# - If there is a cycle, they will eventually meet
# - If fast reaches the end, there is no cycle
#
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
