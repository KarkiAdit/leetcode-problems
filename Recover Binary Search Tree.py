# 99. Recover Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.previous = TreeNode(float("-inf"))

        def inorder(root):
            if not root:
                return
            # Inorder -> traverse(left) -> root -> traverse(right)
            inorder(root.left)
            # Check if the BST condition is still valid
            if self.previous.val > root.val:
                if not self.first:
                    self.first = self.previous
                self.second = root
            # Update the previous everytime
            self.previous = root
            # Traverse right
            inorder(root.right)

        inorder(root)
        # Swap the values
        self.first.val, self.second.val = self.second.val, self.first.val
