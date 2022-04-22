# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None: return None
        root = start = ListNode(None)
        root.next = head
        for _ in range(left - 1):
            start = start.next
        end = start.next
        for _ in range(right - left):  # 3 times
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp

        return root.next
