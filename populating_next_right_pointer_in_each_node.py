# problem description: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None: return
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                if root.next:
                    root.left.next = root.next.left if root.next.left else root.next.right
        if root.right:
            if root.next:
                root.right.next = root.next.left if root.next.left else root.next.right
        self.connect(root.left)
        self.connect(root.right)
