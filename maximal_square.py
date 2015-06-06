# problem description: https://leetcode.com/problems/maximal-square/

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        max_len = 0
        # actually do not need a m*n matrix, keep two column is enough
        dp = [[0] * n for i in xrange(m)]
        
        for i in xrange(m):
            dp[i][0] = int(matrix[i][0])
            max_len = max(dp[i][0], max_len)
        
        for i in xrange(n):
            dp[0][i] = int(matrix[0][i])
            max_len = max(dp[0][i], max_len)
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]]) + 1
                    max_len = max(dp[i][j], max_len)
                    
        return max_len ** 2

class Solution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        max_len = 0
        last_topleft = 0
        dp = [0] * (n+1)
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                tmp = dp[j]
                if matrix[i-1][j-1] == '0':
                    dp[j] = 0
                else:
                    dp[j] = min([dp[j], dp[j-1], last_topleft]) + 1
                    max_len = max(max_len, dp[j])
                last_topleft = tmp

        return max_len ** 2


