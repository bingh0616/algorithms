# problem description: https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        first, second = head, head.next
        
        while second:
            first.next = second.next
            second.next = first
            pre.next = second
            pre = first
            first = first.next
            if not first: break
            second = first.next
            
        return dummy.next
