# Given the head of a singly linked list, return true if it is a palindrome.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #         temp_list = []
        #         while head is not None:
        #             temp_list.append(head.val)
        #             head = head.next

        #         if temp_list == temp_list[::-1]:
        #             return True
        #         return False

        # original linked list
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev