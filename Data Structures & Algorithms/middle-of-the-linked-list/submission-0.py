# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = head
        n = 0 
        while c:
            n+=1 # increment counter 
            c = c.next #advance head
        t = n // 2 
        c = head #reinitlize head
        for i in range(t):
            c = c.next
        return c
        