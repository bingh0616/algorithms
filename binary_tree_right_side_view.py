# problem description: https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        q = collections.deque([])
        if root: q.append(root)
        res = []
        curr_cnt = 1
        next_cnt = 0
        
        while q:
            curr = q.popleft()
            if curr.left: q.append(curr.left); next_cnt += 1
            if curr.right: q.append(curr.right); next_cnt += 1
            curr_cnt -= 1
            if curr_cnt == 0:
                res.append(curr.val)
                curr_cnt = next_cnt
                next_cnt = 0
        
        return res
