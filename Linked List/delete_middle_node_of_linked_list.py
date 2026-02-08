# Problem Name: Delete the Middle Node of a Linked List
# Platform: LeetCode
# Topic: Linked List, Two Pointers
# Difficulty: Medium
#
# Approach:
# - Use two pointers (slow and fast)
# - Move slow by one step and fast by two steps
# - Maintain a previous pointer to track the node before slow
# - When fast reaches the end, slow will be at the middle node
# - Delete the middle node by updating previous.next
#
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head
