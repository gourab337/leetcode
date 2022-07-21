# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        if not head:
            return None
        left, right = head, head
        stop = False
        def reverse(right, m, n):
            nonlocal left, stop
            if n == 1:
                return
            right= right.next
            if m>1:
                left = left.next
            reverse(right, m-1, n-1)
            if left == right or left == right.next:
                stop = True
            if stop is not True:
                left.val, right.val = right.val, left.val
                #right is automatically taken care of by backtracking
                left = left.next
        
        reverse(right,m,n)
        return head
            
