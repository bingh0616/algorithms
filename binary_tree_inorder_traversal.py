# problem description: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        if not root: return []
        stk = [root]
        visited = set()
        res = []
        while stk:
            curr = stk[-1]
            if curr.left and curr.left not in visited:
                stk.append(curr.left)
            else:
                res.append(stk.pop().val)
                if curr.right: stk.append(curr.right)
            visited.add(curr)
        return res
