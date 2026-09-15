# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #split list
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        #reverse list
        second = slow.next
        slow.next = None
        prev = None
        while second is not None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        while head and prev:
            left = head.next
            right = prev.next
            head.next = prev
            head = left
            prev.next = head
            prev = right
            # left = head.next
            # right = prev.next
