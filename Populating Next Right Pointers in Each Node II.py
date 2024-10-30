# 117. Populating Next Righ Pointers in Each Node II

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
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None
        queue = [root]
        while queue:
            curr_level_max = len(queue)
            prev = None
            for _ in range(curr_level_max):
                curr = queue.pop(0)
                if prev:
                    prev.next = curr
                prev = curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root
