# problem description: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        la, lb = 0, 0
        curr = headA
        while curr:
            curr = curr.next
            la += 1
        curr = headB
        while curr:
            curr = curr.next
            lb += 1
        if la >= lb:
            diff = la-lb
            for i in range(diff):
                headA = headA.next
        else:
            diff = lb-la
            for i in range(diff):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None
