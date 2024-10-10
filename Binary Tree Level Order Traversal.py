# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        leveled_nodes = [[root.val]]
        while len(queue) > 0:
            queue_before_append = queue.copy()
            this_level_vals = []
            for node in queue_before_append:
                if node.left:
                    this_level_vals.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    this_level_vals.append(node.right.val)
                    queue.append(node.right)
                queue.pop(0)
            if this_level_vals:
                leveled_nodes.append(this_level_vals) 
        return leveled_nodes

                



        