
# Problem Name: Maximum Twin Sum of a Linked List
# Platform: LeetCode
# Topic: Linked List, Two Pointers
# Difficulty: Medium
#
# Approach:
# - Use slow and fast pointers to find the middle of the list
# - Reverse the second half of the linked list
# - Traverse both halves simultaneously
# - Compute and track the maximum twin sum
#
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow = head
        fast = head

        # Step 1: Find middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow

        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        # Step 3: Calculate twin sum
        first = head
        second = prev
        max_sum = 0

        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
