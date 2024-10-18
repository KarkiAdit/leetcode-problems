# 113. Path Sum II


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        paths = []

        def dfs(node, curr_path_sum, curr_path):
            if not node.left and not node.right and curr_path_sum == targetSum:
                this_path = []
                for elem in curr_path:
                    this_path.append(elem)
                paths.append(this_path)
            if node.left:
                curr_val = node.left.val
                curr_path.append(curr_val)
                dfs(node.left, curr_path_sum + curr_val, curr_path)
                left_val = curr_path.pop()
            if node.right:
                curr_val = node.right.val
                curr_path.append(curr_val)
                dfs(node.right, curr_path_sum + curr_val, curr_path)
                curr_path.pop()

        dfs(root, root.val, [root.val])
        return paths
