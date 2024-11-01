# 226. Invert Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            if not root or (not root.left and not root.right):
                return
            if root.left and root.right:
                root.left, root.right = root.right, root.left
            elif root.left:
                root.right = root.left
                root.left = None
            elif root.right:
                root.left = root.right
                root.right = None
            bfs(root.left)
            bfs(root.right)

        bfs(root)
        return root
