# problem description: https://leetcode.com/problems/course-schedule/

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    class Node:
        def __init__(self, label):
            self.label = label
            self.incomings = []
            self.outgoings = []
    def canFinish(self, numCourses, prerequisites):
        # construct a graph first
        nodes = [self.Node(i) for i in range(numCourses)]
        for edge in prerequisites:
            pre, post = edge
            nodes[pre].outgoings.append(post)
            nodes[post].incomings.append(pre)
        
        visited = [0]
        for n in nodes:
            if not n.incomings:
                path = set()
                if not self.dfs(nodes, n.label, path, visited):
                    return False
                visited[0] += 1

        return visited[0] >= numCourses

    def dfs(self, nodes, start, path, visited):
        for n in nodes[start].outgoings:
            if n in path:
                return False
            path.add(n)
            res = self.dfs(nodes, n, path, visited)
            path.discard(n)
            visited[0] += 1
            if not res:
                return res
        return True

def main():
    print Solution().canFinish(2, [[1,0],[0,1]])

if __name__ == '__main__':
    main()
