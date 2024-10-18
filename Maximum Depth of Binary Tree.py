# 104. Maximum Depth of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs_traverse(node, curr_max, count):
            # Count the current node
            count += 1
            curr_max = max(count, curr_max)
            # Traverse to left node
            if node.left:
                curr_max = dfs_traverse(node.left, curr_max, count)
            # Traverse to right node
            if node.right:
                curr_max = dfs_traverse(node.right, curr_max, count)
            return curr_max

        return dfs_traverse(root, 0, 0)
