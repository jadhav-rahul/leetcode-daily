# Problem Name: Reverse Linked List
# Platform: LeetCode
# Topic: Linked List
# Difficulty: Easy
#
# Approach:
# - Use three pointers: prev, curr, and front
# - Reverse the link of each node while traversing
# - Move pointers forward until the list ends
# - Return prev as the new head of the reversed list
#
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head

        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        return prev
