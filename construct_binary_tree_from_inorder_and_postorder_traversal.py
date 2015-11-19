# problem description: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        mp = {}
        for i in xrange(len(inorder)):
            mp[inorder[i]] = i
        return self.helper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1, mp)

    
    def helper(self, inorder, ist, ie, postorder, pst, pe, mp):
        if ist > ie: return None
        root_val = postorder[pe]
        root_in_idx = mp[root_val]
        left_len = root_in_idx-ist
        
        root = TreeNode(root_val)
        root.left = self.helper(inorder, ist, root_in_idx-1, postorder, pst, pst+left_len-1, mp)
        root.right = self.helper(inorder, root_in_idx+1, ie, postorder, pst+left_len, pe-1, mp)
        return root
