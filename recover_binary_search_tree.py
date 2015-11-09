# problem description: https://leetcode.com/problems/recover-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.pre = None
        self.first = None
        self.second = None
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val
    def traverse(self, root):
        if not root: return
        self.traverse(root.left)
        if self.pre and self.pre.val > root.val:
            self.first = self.first if self.first else self.pre
            self.second = root
        self.pre = root
        self.traverse(root.right)
