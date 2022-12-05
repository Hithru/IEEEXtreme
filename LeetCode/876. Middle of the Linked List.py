# Problem Number: 876
# Problem Name: Middle of the Linked List
# Difficulty: Easy
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = [head]
        node = head
        while node.next:
            node = node.next
            values.append(node)


        return values[len(values)//2]