# problem description: https://leetcode.com/problems/clone-graph/

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        self.cache = {}
        return self.helper(node)
    
    def helper(self, node):
        if not node: return node
        if node in self.cache: return self.cache[node]
        new_node = UndirectedGraphNode(node.label)
        self.cache[node] = new_node
        for n in node.neighbors:
            new_node.neighbors.append(self.helper(n))
        
        return new_node
