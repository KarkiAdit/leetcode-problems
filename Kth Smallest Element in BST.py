# 230. Kth Smallest Element in BST


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inordered = []

        def dfs(root):
            if not root:
                return
            # Traverse the left subtree
            if root.left:
                dfs(root.left)
            # Process the root
            inordered.append(root.val)
            # Traverse the right subtree
            if root.right:
                dfs(root.right)

        dfs(root)
        return inordered[k - 1]
