# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head == None):
            return False
        # turtle, rabbit = head.next, head.next.next
        turtle, rabbit = head, head
        while(rabbit != None and rabbit.next != None):
            rabbit = rabbit.next.next
            turtle = turtle.next
            if(turtle == rabbit):
                return True
        return False


