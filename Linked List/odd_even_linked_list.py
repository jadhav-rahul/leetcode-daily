# Problem Name: Odd Even Linked List
# Platform: LeetCode
# Topic: Linked List
# Difficulty: Medium
#
# Approach:
# - Separate nodes into odd and even position lists
# - Maintain two pointers for odd and even traversal
# - Re-link odd nodes together and even nodes together
# - Attach even list at the end of odd list
#
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        Hodd = head
        Heven = head.next
        oddcur = head
        evencur = head.next

        while oddcur.next and evencur and evencur.next:
            oddcur.next = oddcur.next.next
            evencur.next = evencur.next.next
            oddcur = oddcur.next
            evencur = evencur.next

        oddcur.next = Heven
        return Hodd
