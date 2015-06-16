# problem description: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        curr = head
        
        while curr:
            tmp = curr
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if tmp == curr:
                pre = pre.next
            else:
                pre.next = curr.next
            curr = curr.next
            
        
        return dummy.next
