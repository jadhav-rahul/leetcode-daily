# Problem Name: Binary Tree Level Order Traversal
# Platform: LeetCode
# Topic: Tree, Breadth-First Search (BFS), Queue
# Difficulty: Medium
#
# Approach:
# - Use a queue to perform Breadth-First Search (BFS)
# - Start by adding the root node to the queue
# - For each level:
#     1. Record the number of nodes currently in the queue
#     2. Process those nodes and collect their values
#     3. Add their left and right children to the queue
# - Append the values of each level to the result
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            levelSize = len(q)
            level = []

            for _ in range(levelSize):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(level)

        return res