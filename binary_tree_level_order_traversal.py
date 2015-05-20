# problem description: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root: return []
        res = []
        lv_nodes = []
        q = collections.deque([root])
        curr_lv_cnt, next_lv_cnt = 1, 0
        while q:
            curr = q.popleft()
            if curr: lv_nodes.append(curr.val)
            curr_lv_cnt -= 1
            
            if curr:
                q.append(curr.left)
                q.append(curr.right)
                next_lv_cnt += 2
            if curr_lv_cnt == 0:
                if lv_nodes: res.append(lv_nodes)
                lv_nodes = []
                curr_lv_cnt = next_lv_cnt
                next_lv_cnt = 0
        return res
