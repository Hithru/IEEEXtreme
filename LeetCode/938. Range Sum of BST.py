# Problem Number: 938
# Problem Name: Range Sum of BST
# Difficulty: Easy
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    final_sum = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.addToSum(root, low, high)

        return self.final_sum

    def addToSum(self, node, low, high):
        if low <= node.val <= high:
            self.final_sum += node.val

        if node.val >= low:
            if node.left:
                self.addToSum(node.left, low, high)

        if node.val <= high:
            if node.right:
                self.addToSum(node.right, low, high)

        return

