# 114. Flatten Binary Tree to Linked List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Flatten the root node and return list tail
        def dfs(root):
            if not root:
                return None
            left_tail = dfs(root.left)
            right_tail = dfs(root.right)

            if root.left:
                left_tail.right = root.right
                root.right = root.left
                root.left = None

            return right_tail if right_tail else left_tail if left_tail else root

        dfs(root)
