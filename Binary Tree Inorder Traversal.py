# 94. Binary Tree Inorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        in_ordered = []

        def dfs_traverse(node):
            if node.left:
                dfs_traverse(node.left)
            in_ordered.append(node.val)
            if node.right:
                dfs_traverse(node.right)

        dfs_traverse(root)
        return in_ordered
