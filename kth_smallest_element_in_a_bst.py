# problem description: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# too naive
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        self.helper(root, res)
        return res[k-1]
        
    def helper(self, root, res):
        if root is None: return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

# better in order traversal solution
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = [1]
        self.helper(root, res, k)
        return res[0]
        
    def helper(self, root, curr, k):
        if root is None: return False
        l = self.helper(root.left, curr, k)
        if l: return True
        if curr[0] == k:
            curr[0] = root.val
            return True
        curr[0] += 1
        return self.helper(root.right, curr, k)
