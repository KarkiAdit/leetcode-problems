# 103. Binary Tree Zigzag level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        leveled_orders = [[root.val]]
        queue = [root] if root else []
        order = -1
        while queue:
            this_level_nodes = queue.copy()
            this_level_vals = []
            for node in this_level_nodes:
                if node.left:
                    this_level_vals.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    this_level_vals.append(node.right.val)
                    queue.append(node.right)   
                queue.pop(0)
            if this_level_vals:
                if order == -1:
                    this_level_vals = this_level_vals[::-1]
                leveled_orders.append(this_level_vals)
            order *= -1
        return leveled_orders
            


