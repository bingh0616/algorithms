# problem description: https://leetcode.com/problems/maximal-square/

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        dp = [[0] * (m+1) for i in xrange(n+1)]
        res = 0
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == '0':
                    dp[i+1][j+1] = 0
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j])+1
                    res = max(dp[i+1][j+1], res)
                    
        return res**2

# space efficiency solution
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


