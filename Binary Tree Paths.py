# 257. Binary Tree Paths


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        paths = []

        def bfs(root, curr_path):
            curr_val = str(root.val)
            if not root.left and not root.right:
                paths.append(curr_path + curr_val)
            curr_path += curr_val + "->"
            if root.left:
                bfs(root.left, curr_path)
            if root.right:
                bfs(root.right, curr_path)

        bfs(root, "")
        return paths
