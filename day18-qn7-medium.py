# 2487. Remove Nodes From Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        stack = []
        while curr.next:
            stack.append(curr)
            if curr.next.val > curr.val:
                while stack and stack[-1].val < curr.next.val:
                    stack.pop()
                    if stack:
                        stack[-1].next = curr.next
                    else:
                        head = curr.next
            curr = curr.next
        return head
                
                
