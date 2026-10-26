# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        prev = None
        curr = head
        forward = head.next

        while forward != None:
            curr.next = prev
            prev = curr
            curr = forward
            forward = forward.next

        curr.next = prev
        return curr