# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_node, l1_prev = l1, None
        l1_num = ""
        while l1_node:
            l1_next, l1_node.next = l1_node.next, l1_prev
            l1_node, l1_prev = l1_next, l1_node

        while l1_prev:
            l1_num += str(l1_prev.val)
            l1_prev = l1_prev.next

        l2_node, l2_prev = l2, None
        l2_num = ""
        while l2_node:
            l2_next, l2_node.next = l2_node.next, l2_prev
            l2_node, l2_prev = l2_next, l2_node

        while l2_prev:
            l2_num += str(l2_prev.val)
            l2_prev = l2_prev.next

        result = list(map(int, str(int(l2_num) + int(l1_num))))  # 807

        prev = None
        for val in result:
            node = ListNode(val)
            node.next = prev
            prev = node

        return node

