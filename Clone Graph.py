# 133. Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        marked = {}

        def dfs(node):
            cloned_node = Node(node.val)
            marked[node.val] = cloned_node
            for neighbor in node.neighbors:
                if neighbor.val in marked:
                    cloned_node.neighbors.append(marked[neighbor.val])
                else:
                    cloned_node.neighbors.append(dfs(neighbor))
            return cloned_node

        return dfs(node)
