# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head: return head
        # node, prev, ans = head, None, head.next
        # while node and node.next:
        #     adj = node.next
        #     if prev: 
        #         prev.next = adj
        #     adj.next, node.next = node, adj.next # swap
        #     node, prev = node.next, node

        node = head
        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next

        return head

