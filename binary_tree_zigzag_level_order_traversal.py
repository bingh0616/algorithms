# problem description: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = self.levelOrder(root)
        for i in xrange(1, len(res), 2):
            res[i] = res[i][::-1]
        return res
    
    def levelOrder(self, root):
        if root is None: return []
        q = collections.deque([root])
        
        res = []
        lv = []
        curr_cnt = 1
        next_cnt = 0
        
        while q:
            curr = q.popleft()
            if curr:
                lv.append(curr.val)
                q.append(curr.left)
                q.append(curr.right)
                next_cnt += 2
            curr_cnt -= 1
            if curr_cnt == 0:
                if lv: res.append(lv)
                lv = []
                curr_cnt = next_cnt
                next_cnt = 0
        return res
