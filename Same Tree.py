# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def evaluate_nodes(curr_t1, curr_t2):
            # Both null nodes
            if not curr_t1 and not curr_t2:
                return True
            # One of the nodes present while the other not
            if (curr_t1 and not curr_t2) or (curr_t2 and not curr_t1):
                return False
            # For both non-null nodes
            if curr_t1.val == curr_t2.val:
                # See node to left from the current node for both trees
                if not evaluate_nodes(curr_t1.left, curr_t2.left):
                    return False
                # See node to right from the current node for both trees
                if not evaluate_nodes(curr_t1.right, curr_t2.right):
                    return False
            else:
                return False
            return True
        return evaluate_nodes(p, q)