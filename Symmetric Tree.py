# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse_graph(node_left, node_right):
            if (not node_left and node_right) or (not node_right and node_left):
                return False
            if node_left and node_right:
                if node_left.val == node_right.val:
                    if not traverse_graph(node_left.left, node_right.right):
                        return False
                    if not traverse_graph(node_left.right, node_right.left):
                        return False
                    return True
                else:
                    return False
            return True
        return traverse_graph(root, root)
        