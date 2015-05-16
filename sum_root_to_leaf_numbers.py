# problem description: https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        return self.helper(root, 0)
    
    def helper(self, root, curr):
        if not root: return 0
        res = curr*10 + root.val
        if not root.left and not root.right: return res
        return self.helper(root.left, res) + self.helper(root.right, res)

def main():
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.right = TreeNode(9)
    root.left.right.left = TreeNode(9)
    root.left.right.right = TreeNode(5)
    print Solution().sumNumbers(root)

if __name__ == '__main__':
    main()
