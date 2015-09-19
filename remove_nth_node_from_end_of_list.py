# problem description: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head: return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        l = 0
        while head:
            head = head.next
            l += 1
        
        for i in xrange(l-n):
            pre = pre.next
        
        curr = pre.next
        pre.next = curr.next
        return dummy.next
