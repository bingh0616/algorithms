# problem description: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        pre, curr = head, head.next
        
        while curr:
            if pre.val == curr.val:
                curr = curr.next
            else:
                pre.next = curr
                pre = curr
                curr = curr.next
        pre.next = curr
        return dummy.next
        
# 10.28.2015
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        dummy = ListNode(0)
        dummy.next = head
        pre, curr = dummy, head
        while curr.next:
            if curr.val == curr.next.val:
                pre.next = curr.next
            else:
                pre = pre.next
            curr = curr.next
        
        return dummy.next
