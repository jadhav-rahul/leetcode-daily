# Problem Name: Maximum Depth of Binary Tree
# Platform: LeetCode
# Topic: Tree, Recursion, Depth-First Search (DFS)
# Difficulty: Easy
#
# Approach:
# - Use recursion to calculate the depth of left and right subtrees
# - Base case: if node is None, return 0
# - Recursively compute depth of left and right children
# - Return 1 + max(left_depth, right_depth)
#
# Time Complexity: O(n)
# Space Complexity: O(h)  (h = height of the tree due to recursion stack)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)