# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        i = list1
        j = list2
        if not i:
            return j
        if not j:
            return i

        if i.val < j.val:
            newhead = i
            i = i.next
        else:
            newhead = j
            j = j.next
        
        curr = newhead
        while i and j:
            if i.val < j.val:
                curr.next = i
                i = i.next
                curr = curr.next
            else:
                curr.next = j
                j = j.next
                curr = curr.next
            
        curr.next = j if j else i

        return newhead
