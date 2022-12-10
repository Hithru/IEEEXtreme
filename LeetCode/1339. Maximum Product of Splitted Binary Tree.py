# Problem Number: 1339
# Problem Name: Maximum Product of Splitted Binary Tree
# Difficulty: Medium

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        table = {}

        def sumOfNode(node, level, path):

            node_sum = 0
            if not node:
                return node_sum
            elif node.val in table:
                return table[node.val]
            else:
                node_sum += node.val
                node_sum += sumOfNode(node.right, level + 1, "R")
                node_sum += sumOfNode(node.left, level + 1, "L")
                table[str(node.val) + "_" + str(level) + path] = node_sum
                return node_sum

        root = sumOfNode(root, 0, "M")
        max_product = 0

        for value in table.values():
            product = (root - value) * value
            if product > max_product:
                max_product = product
        return max_product % (10 ** 9 + 7)