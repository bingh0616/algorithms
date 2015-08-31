# problem description: https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # set the node's value to be next, loop until hit the end, then delete the last one
        while node.next:
            node.val = node.next.val
            if not node.next.next: break
            node = node.next
            
        node.next = None
