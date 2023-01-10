# Problem Number: 100
# Problem Name: Same Tree
# Difficulty: Easy
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def sameTree(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val == q.val:
                return sameTree(p.left,q.left) and sameTree(p.right,q.right)
            else:
                return False

        return sameTree(p,q)