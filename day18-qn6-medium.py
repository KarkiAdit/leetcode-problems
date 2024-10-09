# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def analyze_and_swap_adjacent_nodes(prev, curr, next):
            # No further swaps needed
            if not next or not curr:
                return
            if prev is None:
                nonlocal head
                head = next
            else:
                prev.next = next
            temp = next.next
            next.next = curr
            curr.next = temp
            if curr.next and curr.next.next:
                analyze_and_swap_adjacent_nodes(curr, curr.next, curr.next.next)
            else:
                return
        if head and head.next:
            analyze_and_swap_adjacent_nodes(None, head, head.next)
        return head