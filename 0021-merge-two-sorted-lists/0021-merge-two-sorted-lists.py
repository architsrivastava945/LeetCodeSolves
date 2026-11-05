# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            newhead = list1
            newhead.next = self.mergeTwoLists(list1.next, list2)
        else:
            newhead = list2
            newhead.next = self.mergeTwoLists(list1, list2.next)
        return newhead
