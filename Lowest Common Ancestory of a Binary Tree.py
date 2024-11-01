# 236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(root):
            if not root:
                return None
            elif root == p or root == q:
                return root
            # Traverse through left and right
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right

        return dfs(root)
