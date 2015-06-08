# problem description: https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        if not root: return []
        stk = []
        stk.append(root)
        res = []
        
        while stk:
            curr = stk.pop()
            res.append(curr.val)
            if curr.right: stk.append(curr.right)
            if curr.left: stk.append(curr.left)

        return res
