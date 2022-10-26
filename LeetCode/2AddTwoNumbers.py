# Problem Number: 2
# Problem Name: Add Two Numbers
# Difficulty: Medium
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_number = str(l1.val)
        second_number = str(l2.val)
        first = l1.next
        second = l2.next
        while first != None or second != None:
            if first != None:
                first_number += str(first.val)

                first = first.next

            if second != None:
                second_number += str(second.val)
                second = second.next

        answer = str(int(first_number[::-1]) + int(second_number[::-1]))[::-1]

        root_node = ListNode(int(answer[0]), None)

        previous_node = root_node
        for k in range(1, len(answer)):
            new_node = ListNode(int(answer[k]), None)
            previous_node.next = new_node
            previous_node = new_node

        return root_node
