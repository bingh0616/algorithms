# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}

    def reverseList(self, head):
        if not head: return head
        self.last = None
        return self.reverse(head)
        
    def reverse(self, head):
        if not head.next:
            self.last = head
            return head
        res = self.reverse(head.next)
        self.last.next = head
        self.last = head
        self.last.next = None
        return res

