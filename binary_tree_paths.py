# problem description: https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        curr = [str(root.val)]
        path = []
        self.helper(root, curr, path)
        return path
    def helper(self, root, curr, path):
        if not root.left and not root.right:
            path.append('->'.join(curr))
        
        else:
            if root.left:
                curr.append(str(root.left.val))
                self.helper(root.left, curr, path)
                curr.pop()
            if root.right:
                curr.append(str(root.right.val))
                self.helper(root.right, curr, path)
                curr.pop()
