# problem description: https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if k == 0 or not head: return head
        l = 0
        
        curr = head
        while curr:
            curr = curr.next
            l += 1
        
        k %= l
        tmp = l-k
        
        prev = head
        while tmp > 1:
            prev = prev.next
            tmp -= 1
            
        last = prev
        
        while last and last.next:
            last = last.next
        last.next = head
        head = prev.next
        prev.next = None
        
        return head

# 10.14.2015
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        n = 1
        curr = head
        while curr.next:
            n += 1
            curr = curr.next
        k %= n
        last = curr
        curr = head
        for i in xrange(n-k-1):
            curr = curr.next
        last.next = head
        head = curr.next
        curr.next = None
        return head
