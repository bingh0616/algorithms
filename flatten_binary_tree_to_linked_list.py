# Given a binary tree, flatten it to a linked list in-place
# for example, Given [1,2,5,3,4,#,6] to [1,#,2,#,#,#,3,...] (only have right child)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            left_last = root.left
            while left_last.right:
                left_last = left_last.right
            left_last.right = root.right
            root.right = root.left
            root.left = None
