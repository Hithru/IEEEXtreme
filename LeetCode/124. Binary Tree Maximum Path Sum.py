# Problem Number: 124
# Problem Name: Binary Tree Maximum Path Sum
# Difficulty: Hard
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maximum_path = [-float('inf')]
        def maxPath(node: Optional[TreeNode],maximum_path):

            if node is None:
                return 0

            left_side = maxPath(node.left,maximum_path)
            right_side = maxPath(node.right,maximum_path)

            max_only_one_side = max(max(left_side,right_side)+node.val,node.val)

            max_consider_final = max(max_only_one_side,left_side+right_side+node.val)
            if max_consider_final > maximum_path[0]:
                maximum_path[0] = max_consider_final

            return max_only_one_side

        maxPath(root,maximum_path)
        return maximum_path[0]