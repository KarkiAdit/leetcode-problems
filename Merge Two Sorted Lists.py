# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        def traverse(node_l1, node_l2, tail):
            # Both linked list out of range
            if not node_l1 and not node_l2:
                return 
            # Second linked list out of range
            if not node_l2:
                tail.next = node_l1
                traverse(node_l1.next, None, node_l1)
            # First linked list out of range
            elif not node_l1:
                tail.next = node_l2
                traverse(None, node_l2.next, node_l2)
            # Both lists have nodes
            elif node_l1.val < node_l2.val:
                tail.next = node_l1
                traverse(node_l1.next, node_l2, node_l1)
            else:
                tail.next = node_l2
                traverse(node_l1, node_l2.next, node_l2)
        traverse(list1, list2, dummy_head)
        return dummy_head.next
        