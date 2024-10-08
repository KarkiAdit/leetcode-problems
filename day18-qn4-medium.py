# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = ListNode()
        curr_tail = dummy_head
        while l1 or l2 or carry:
            if not l1 and not l2:
                curr_sum = carry
            elif not l1:
                curr_sum = carry + l2.val
            elif not l2:
                curr_sum = carry + l1.val
            else:
                curr_sum = carry + l1.val + l2.val
            new_node = ListNode(curr_sum % 10)
            curr_tail.next = new_node
            curr_tail = new_node
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            carry = curr_sum // 10
        return dummy_head.next



        

