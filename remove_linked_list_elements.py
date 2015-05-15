# problem description: https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        pre = ListNode(0)
        pre.next = head
        dummy = pre
        while head:
            if head.val == val:
                pre.next = head.next
                head = pre.next
            else:
                head = head.next
                pre = pre.next
                
        return dummy.next
