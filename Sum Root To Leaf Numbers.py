# 129. Sum Root to Leaf Numbers


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total_sum = 0

        def pre_order(root, path_sum):
            path_sum = path_sum * 10 + root.val
            if not root.left and not root.right:
                self.total_sum += path_sum
                return
            left = root.left
            right = root.right
            if left:
                pre_order(left, path_sum)
            if right:
                pre_order(right, path_sum)

        pre_order(root, 0)
        return self.total_sum
