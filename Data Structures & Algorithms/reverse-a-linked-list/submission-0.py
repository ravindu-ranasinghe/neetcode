# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        result = []
        curr = head
        if not head:
            return None 
        while curr is not None:
            stack.append(curr)
            curr = curr.next
        
        nh = stack.pop()
        curr = nh
        while len(stack) > 0:
            next = stack.pop()
            curr.next = next
            curr = next
        
        curr.next = None
        
        return nh

        