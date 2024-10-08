# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def navigate_path(curr_node, path_sum):
            if curr_node:
                path_sum += curr_node.val
                if not curr_node.left and not curr_node.right:
                    return path_sum == targetSum
                # If there is a valid left path
                if curr_node.left and navigate_path(curr_node.left, path_sum):
                    return True
                # If there is a valid right path
                if curr_node.right and navigate_path(curr_node.right, path_sum):
                    return True            
            # No valid right or left path or tree is empty
            return False
        return navigate_path(root, 0)

        
        