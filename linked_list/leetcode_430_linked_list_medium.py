"https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/"

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head):
        if not head:
            return None
        
        dummy = Node(0)
        curr = dummy
        stack = [head]

        while stack:
            node = stack.pop()
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
            curr.next = node
            node.prev = curr
            curr = curr.next
            node.child = None
            
        dummy.next.prev = None
        return dummy.next



        
        return head
