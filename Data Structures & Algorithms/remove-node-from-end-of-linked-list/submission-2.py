# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        #elif n == 1:

        i = 0
        lead = head
        while i < n:
            lead = lead.next
            i += 1
        rear = head

        if lead is None:
            return head.next
        while lead.next is not None:
            rear = rear.next
            lead = lead.next
        
        rear.next = rear.next.next
        if n == 1:
            rear.next = None
        return head