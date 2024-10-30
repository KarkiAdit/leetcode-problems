# 199. Binary Tree Right Side View


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right_side_vals = []
        queue = [root]
        while queue:
            size = len(queue)
            this_level_nodes = []
            for _ in range(size):
                curr = queue.pop(0)
                this_level_nodes.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            right_side_vals.append(this_level_nodes[-1])
        return right_side_vals
