# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next == None:
            return head
        
        rear = head
        
        current = head.next
        forward = current.next
        rear.next = None
        while forward is not None:
            current.next = rear
            rear = current
            current = forward
            forward = forward.next
            
        current.next = rear
        
        return current
        
