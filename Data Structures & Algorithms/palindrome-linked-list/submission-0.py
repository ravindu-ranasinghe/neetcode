# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        c = head
        x = []
        while c:
            x.append(c.val)
            c = c.next
        return x == x[::-1]

        