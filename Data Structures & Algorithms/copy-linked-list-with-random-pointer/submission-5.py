"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        curr = head
        nodes = {}
        while curr is not None:
            copy = Node(curr.val)
            nodes[curr] = copy
            curr = curr.next
        curr = head
        #print(nodes)
        while curr is not None:
            copy = nodes[curr]
            if curr.next is None:
                copy.next = None
            else:
                copy.next = nodes[curr.next]
            
            if curr.random is None:
                copy.random = None
            else:
                copy.random = nodes[curr.random]
            curr = curr.next

        # curr = nodes[head]
        # while curr is not None:
        #     print(curr.val, curr)
        #     curr = curr.next
        return nodes[head]