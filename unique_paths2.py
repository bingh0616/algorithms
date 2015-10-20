# problem description: https://leetcode.com/problems/unique-paths-ii/

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        ob = obstacleGrid
        m = len(ob)
        if m == 0: return 0
        n = len(ob[0])
        paths = [[0] * (n+1) for i in xrange(m+1)]
        paths[0][1] = 1
        
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if ob[i-1][j-1] == 1:
                    paths[i][j] = 0
                else:
                    paths[i][j] = paths[i-1][j]+paths[i][j-1]
                    
        return paths[m][n]
