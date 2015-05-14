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
