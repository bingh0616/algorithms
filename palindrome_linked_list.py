# problem description: https://leetcode.com/problems/palindrome-linked-list/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None: return True
        fast, slow = head, head
        while fast:
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
                slow = slow.next
        slow.next = self.reverse(slow.next)
        a, b = head, slow.next
        while b and a.val == b.val:
            a = a.next
            b = b.next
            
        return b is None
        
    
    def reverse(self, head):
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre
        
