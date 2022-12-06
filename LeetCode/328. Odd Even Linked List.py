# Problem Number: 328
# Problem Name: Odd Even Linked List
# Difficulty: Medium
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head

        node = head
        oddHead = head
        finalEvenHead = head.next
        evenHead = node.next
        node = node.next

        i = 1
        while node.next:
            if i % 2 == 1:
                oddHead.next = node.next
                oddHead = oddHead.next
            else:
                evenHead.next = node.next
                evenHead = evenHead.next
            node = node.next
            i += 1

        if evenHead.next:
            evenHead.next = None

        oddHead.next = finalEvenHead

        return head
