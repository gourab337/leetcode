# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper (node = head):
            if not (node and node.next):
                return node
            first, second = node, node.next
            first.next = helper(node.next.next)
            second.next = first
            return second
        return helper()
        