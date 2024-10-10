# 98. Validate Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Unoptimized O(n) additional space solution - using (in-order traversal)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        in_ordered = []

        def traverse_and_validate(node):
            if node.left:
                traverse_and_validate(node.left)
            in_ordered.append(node.val)
            if node.right:
                traverse_and_validate(node.right)

        traverse_and_validate(root)
        size = len(in_ordered)
        if size == 1:
            return root
        for j in range(1, size):
            if in_ordered[j - 1] < in_ordered[j]:
                continue
            else:
                return False
        return True


# Optimized O(1) space solution using pre-order traversal
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse_and_validate(node, low=float("-inf"), high=float("inf")):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return traverse_and_validate(
                node.left, low, node.val
            ) and traverse_and_validate(node.right, node.val, high)

        return traverse_and_validate(root)
