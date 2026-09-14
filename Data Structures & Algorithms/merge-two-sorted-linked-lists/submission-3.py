# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        tail = dummy
        c1 = list1
        c2 = list2
        while c1 is not None and c2 is not None:
            if c1.val > c2.val:
                tail.next = c2
                c2 = c2.next
            else:
                tail.next = c1
                c1 = c1.next
            tail = tail.next

        if c1 is not None:
            tail.next = c1
            c1 = c1.next
        if c2 is not None:
            tail.next = c2
            c2 = c2.next
        return dummy.next

        