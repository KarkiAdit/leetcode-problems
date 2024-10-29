# 116. Populating Next Right Pointers in Each Node

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        head = root
        while root:
            curr, root = root, root.left
            while curr:
                if root:
                    curr.left.next = curr.right
                    if curr.next:
                        curr.right.next = curr.next.left
                curr = curr.next
        return head
