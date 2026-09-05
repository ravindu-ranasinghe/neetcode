# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        x = ListNode() #dummy
        x.next = head
        c = x
        while c.next: #technically x.next.next
            if c.next.val == val: #comparing x.next.next to val
                c.next = c.next.next #skipping node 
            else:
                c = c.next #advance as usual
        return x.next 

            

        