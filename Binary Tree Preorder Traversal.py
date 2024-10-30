# 144. Binary Tree Preorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre_ordered = []
        if not root:
            return pre_ordered

        def pre_order(root):
            pre_ordered.append(root.val)
            left = root.left
            right = root.right
            # Traverse left
            if left:
                pre_order(left)
            # Traverse right
            if right:
                pre_order(right)

        pre_order(root)
        return pre_ordered
