# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}

    # iteration version
    def postorderTraversal(self, root):
        if not root:
            return []
        res = []
        visited = set()
        stack = [root]
        while stack:
            node = stack[-1]
            left_valid = node.left and node.left not in visited
            right_valid = node.right and node.right not in visited
            if not left_valid and not right_valid:
                tmp = stack.pop()
                res.append(tmp.val)
                visited.add(tmp)
            if right_valid:
                stack.append(node.right)
            if left_valid:
                stack.append(node.left)
        return res
