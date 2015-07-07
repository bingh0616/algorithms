# problem description: https://leetcode.com/problems/distinct-subsequences/

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        n, m = len(s), len(t)
        dp = [[0] * (m+1) for i in xrange(n+1)]
        
        for i in xrange(n+1):
            dp[i][m] = 1
            
        for i in reversed(xrange(n)):
            for j in reversed(xrange(m)):
                dp[i][j] = dp[i+1][j]
                if s[i] == t[j]: dp[i][j] += dp[i+1][j+1]
                
        return dp[0][0]
