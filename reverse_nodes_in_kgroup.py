# problem description: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        p = head
        i = 0
        while i<k and p:
            p = p.next
            i += 1
        if i == k:
            right = self.reverseKGroup(p, k)
            
            while i>0:
                nxt = head.next
                head.next = right
                right = head
                head = nxt
                i -= 1
            head = right
        return head
