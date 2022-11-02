# Problem Number: 21
# Problem Name: Merged Two Sorted List
# Difficulty: Easy
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2

        if list2 == None:
            return list1
        if list1.val < list2.val:
            root_node = ListNode(list1.val, None)
            first = list1.next
            second = list2
        else:
            root_node = ListNode(list2.val, None)
            first = list1
            second = list2.next

        previous_node = root_node
        while first != None or second != None:

            if first == None:
                answer = second.val
                second = second.next

            elif second == None:
                answer = first.val
                first = first.next
            else:
                if first.val < second.val:
                    answer = first.val
                    first = first.next
                else:
                    answer = second.val
                    second = second.next
            new_node = ListNode(answer, None)
            previous_node.next = new_node
            previous_node = new_node
        return root_node
