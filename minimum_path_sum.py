# problem description: https://leetcode.com/problems/minimum-path-sum/

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        dp = [[0] * n for i in xrange(m)]
        dp[0][0] = grid[0][0]
        for i in xrange(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in xrange(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
            
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                
        return dp[m-1][n-1]
