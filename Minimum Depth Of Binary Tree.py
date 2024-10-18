# 111. Minimum Depth of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, min_depth, count):
            # Count the current node
            count += 1
            if not node.left and not node.right:
                return min(min_depth, count)
            # Traverse left
            if node.left:
                min_depth = dfs(node.left, min_depth, count)
            # Traverse right
            if node.right:
                min_depth = dfs(node.right, min_depth, count)
            return min_depth

        return dfs(root, 10**5 + 1, 0)
