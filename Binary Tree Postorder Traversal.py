# 145. Binary Tree Postorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        num_list = []

        def dfs(root):
            if not root:
                return None
            left = dfs(root.left)
            right = dfs(root.right)
            if left:
                num_list.append(left.val)
            elif right:
                num_list.append(right.val)
            else:
                num_list.append(root.val)

        dfs(root)
        return num_list
