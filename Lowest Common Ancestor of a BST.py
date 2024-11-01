# 235. Lowest Common Ancestor of a Binary Search Tree

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
        if not root:
            return None
        self.is_found = False

        def bfs(root):
            if self.is_found:
                return root
            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                self.is_found = True
                return root
            if p.val < root.val and q.val < root.val:
                left = bfs(root.left)
                if left:
                    return left
            if p.val > root.val and q.val > root.val:
                right = bfs(root.right)
                if right:
                    return right

        return bfs(root)
