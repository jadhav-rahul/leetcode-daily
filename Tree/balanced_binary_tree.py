# Problem Name: Balanced Binary Tree
# Platform: LeetCode
# Topic: Tree, Recursion, Depth-First Search (DFS)
# Difficulty: Easy
#
# Approach:
# - Use a recursive function to compute the height of each subtree
# - For every node, calculate height of left and right subtrees
# - If the difference in heights is greater than 1, the tree is not balanced
# - Use a shared variable to track whether the tree remains balanced
#
# Time Complexity: O(n)
# Space Complexity: O(h)  (h = height of tree due to recursion stack)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def height(self, root, ans):
        if root is None:
            return 0

        left = self.height(root.left, ans)
        right = self.height(root.right, ans)

        if abs(left - right) > 1:
            ans[0] = False

        return 1 + max(left, right)

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        ans = [True]
        self.height(root, ans)
        return ans[0]