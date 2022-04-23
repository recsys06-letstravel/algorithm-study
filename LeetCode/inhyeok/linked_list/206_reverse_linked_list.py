# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            node, prev = next, node

        return prev
