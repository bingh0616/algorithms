# problem description: https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(range(1, n+1))
    
    def helper(self, A):
        if not A: return [None]
        res = []
        for i in xrange(len(A)):
            for l in self.helper(A[:i]):
                for r in self.helper(A[i+1:]):
                    root = TreeNode(A[i])
                    root.left = l
                    root.right = r
                    res.append(root)
                    
        return res
