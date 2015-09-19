# problem description: https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # use a PQ to solve this problem
        pop = heapq.heappop
        push = heapq.heappush
        pq = []
        
        dummy = ListNode(0)
        pre = dummy
        
        for l in lists:
            if l: push(pq, (l.val, l))
        
        while pq:
            pre.next = pop(pq)[1]
            if pre.next.next:
                push(pq, (pre.next.next.val, pre.next.next))
            pre = pre.next
        
        return dummy.next
