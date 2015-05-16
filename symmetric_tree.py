# problem description: https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive solution
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root: return True
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)

# iterative solution
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root: return True
        left_s, right_s = [root.left], [root.right]
        while left_s and right_s:
            l, r = left_s.pop(), right_s.pop()
            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return False
            left_s.append(l.left)
            left_s.append(l.right)
            right_s.append(r.right)
            right_s.append(r.left)
            
        return True
