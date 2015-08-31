# problem description: https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left_depth, right_depth = 0, 0
        p = root
        while p:
            p = p.left
            left_depth += 1
        p = root
        while p:
            p = p.right
            right_depth += 1
        
        if left_depth == right_depth:
            return (1 << left_depth) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
