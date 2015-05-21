# problem description: https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        lh, rh = ListNode(0), ListNode(0)
        l, r = lh, rh
        
        curr = head
        while curr:
            if curr.val < x:
                l.next = curr
                l = l.next
            else:
                r.next = curr
                r = r.next
            curr = curr.next
        l.next = rh.next
        r.next = None
        return lh.next
