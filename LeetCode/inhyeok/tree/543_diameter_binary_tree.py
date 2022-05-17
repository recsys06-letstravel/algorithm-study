# Definition for a binary tree node.
from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    longest_diameter: int = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dfs(node):
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest_diameter = max(self.longest_diameter, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.longest_diameter
