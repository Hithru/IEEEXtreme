# Problem Number: 1026
# Problem Name: Maximum Difference Between Node and Ancestor
# Difficulty: Medium
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        maximum_difference = [0]

        self.findMaxDifference(root.val,root.val,maximum_difference,root)
        return maximum_difference[-1]


    def findMaxDifference(self,minimum_yet,maximum_yet,value_list,node):

        if abs(maximum_yet-node.val) > value_list[-1]:
            value_list.append(abs(maximum_yet-node.val))

        if abs(minimum_yet-node.val) > value_list[-1]:
            value_list.append(abs(minimum_yet-node.val))

        if node.val <minimum_yet:
            minimum_yet = node.val
        if node.val > maximum_yet:
            maximum_yet = node.val

        if node.right:
            self.findMaxDifference(minimum_yet,maximum_yet,value_list,node.right)
        if node.left:
            self.findMaxDifference(minimum_yet,maximum_yet,value_list,node.left)

        return
