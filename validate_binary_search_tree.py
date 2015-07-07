# problem description: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def __init__(self):
        self.pre = None
    def isValidBST(self, root):
        if not root: return True
        left_res = self.isValidBST(root.left)
        if left_res:
            if self.pre and self.pre.val >= root.val:
                return False
            self.pre = root
            return self.isValidBST(root.right)
        return False
