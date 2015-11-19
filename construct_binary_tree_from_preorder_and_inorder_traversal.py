# problem description: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        mp = {}
        for i in xrange(len(inorder)):
            mp[inorder[i]] = i
        return self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, mp)
    
    def helper(self, preorder, pl, pr, inorder, il, ir, mp):
        if pl > pr:
            return None
        root = TreeNode(preorder[pl])
        root_pre_idx = mp[root.val]
        root.left = self.helper(preorder, pl+1, pl+1+(root_pre_idx-1-il), inorder, il, root_pre_idx-1, mp)
        root.right = self.helper(preorder, pl+1+(root_pre_idx-1-il)+1, pr, inorder, root_pre_idx+1, ir, mp)
        return root
