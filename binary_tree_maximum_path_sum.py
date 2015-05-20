# problem description: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        curr_max = [-2**31]
        self.helper(root, curr_max)
        return curr_max[0]
    
    def helper(self, root, curr_max):
        if not root: return 0
        left = self.helper(root.left, curr_max)
        right = self.helper(root.right, curr_max)
        
        ret = root.val+max(left, right)
        curr_max[0] = max(root.val+left+right, curr_max[0])
        return ret if ret > 0 else 0
