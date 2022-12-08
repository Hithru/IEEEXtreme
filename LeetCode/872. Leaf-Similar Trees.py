# Problem Number: 872
# Problem Name: Leaf-Similar Trees
# Difficulty: Easy
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1_leaves = []
        tree2_leaves = []
        self.addLeaves(root1, tree1_leaves)
        self.addLeaves(root2, tree2_leaves)

        return tree1_leaves == tree2_leaves

    def addLeaves(self, node, leaves_list):
        if not node.right and not node.left:
            leaves_list.append(node.val)

        if node.left:
            self.addLeaves(node.left, leaves_list)

        if node.right:
            self.addLeaves(node.right, leaves_list)

        return