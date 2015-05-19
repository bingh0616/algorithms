# Find distance between two nodes in binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def two_nodes_distance(self, root, n1, n2):
        n1d = self.node_height(root, n1)
        if n1d == -1: return -1
        n2d = self.node_height(root, n2)
        if n2d == -1: return -1
        ac = self.lowest_common_ancestor(root, n1, n2)
        return  n1d + n2d - 2 * self.node_height(root, ac)

    def node_height(self, root, node):
        if not root or not node:
            return -1
        if root == node:
            return 0
        l = self.node_height(root.left, node)
        if l != -1:
            return l+1
        r = self.node_height(root.right, node)
        if r != -1:
            return r+1
        return -1

    def lowest_common_ancestor(self, root, n1, n2):
        if root is None or root == n1 or root == n2:
            return root
        l = self.lowest_common_ancestor(root.left, n1, n2)
        r = self.lowest_common_ancestor(root.right, n1, n2)
        if l and r:
            return root
        return l if l else r

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)
root.left.left.right = TreeNode(7)

print 'distance:', Solution().two_nodes_distance(root, root.left.left, root.left.right)

