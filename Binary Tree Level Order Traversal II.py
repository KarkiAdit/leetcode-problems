# 107. Binary Tree Level Order Traversal II


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverse(self, curr_level_order):
        start = 0
        end = len(curr_level_order) - 1
        while start < end:
            curr_level_order[start], curr_level_order[end] = (
                curr_level_order[end],
                curr_level_order[start],
            )
            end -= 1
            start += 1

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        curr_level_order = []
        # Do level order traverse normally
        while queue:
            this_level_nodes = queue.copy()
            this_level_vals = []
            for node in this_level_nodes:
                queue.pop(0)
                this_level_vals.append(node.val)
                # Add the left node
                if node.left:
                    queue.append(node.left)
                # Add the right node
                if node.right:
                    queue.append(node.right)
            if this_level_vals:
                curr_level_order.append(this_level_vals)
        self.reverse(curr_level_order)
        return curr_level_order
