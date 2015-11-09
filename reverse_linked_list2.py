# problem description: https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in xrange(m-1): pre = pre.next
        start = pre.next
        # curr is posistion we actually start reverse
        curr = start.next
        
        i = 0
        while i < n-m:
            start.next = curr.next
            curr.next = pre.next
            pre.next = curr
            curr = start.next
            i += 1
            
        return dummy.next
