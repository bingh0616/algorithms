# problem description: https://leetcode.com/problems/course-schedule-ii/

class Solution(object):
    class Node:
        def __init__(self, label):
            self.label = label
            self.incomings = []
            self.outgoings = []

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        nodes = [self.Node(i) for i in xrange(n)]
        curr_lb = [n-1]
        
        for e in prerequisites:
            nxt, pre = e
            nodes[pre].outgoings.append(nxt)
            nodes[nxt].incomings.append(pre)
            
        # dfs check if exist topological order (check cycle)
        total = [0]
        for i, node in enumerate(nodes):
            if not nodes[i].incomings:
                if not self.check(i, nodes, set(), total):
                    return []
                total[0] += 1
        if total[0] < n: return []
        
        visited = set()
        for i, node in enumerate(nodes):
            if not node.incomings:
                if i not in visited:
                    self.dfs(i, nodes, visited, curr_lb)
                
        res = [0] * n
        for i, node in enumerate(nodes):
            res[node.label] = i
        return res

    def dfs(self, start, nodes, visited, curr_lb):
        for i in nodes[start].outgoings:
            if i not in visited:
                visited.add(i)
                self.dfs(i, nodes, visited, curr_lb)
        nodes[start].label = curr_lb[0]
        curr_lb[0] -= 1
    
    def check(self, start, nodes, path, total):
        for i in nodes[start].outgoings:
            if i in path:
                return False
            path.add(i)
            if not self.check(i, nodes, path, total):
                return False
            path.discard(i)
            total[0] += 1
        return True
