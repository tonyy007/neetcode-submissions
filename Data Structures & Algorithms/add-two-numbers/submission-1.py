# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        head = l1
        exp = 1
        while head is not None:
            num1 += (head.val * exp)
            exp *= 10
            head = head.next
        head = l2
        exp = 1
        while head is not None:
            num2 += (head.val * exp)
            exp *= 10
            head = head.next
        
        total = num1 + num2
        return_node = ListNode(total % 10)
        curr = return_node
        total = total // 10
        while total > 0:
            getNum = total %10
            new_node = ListNode(getNum)
            curr.next = new_node
            curr = new_node
            total = total//10
        return return_node
