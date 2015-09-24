# problem description: https://leetcode.com/problems/edit-distance/

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2+1) for i in xrange(n1+1)]
        for i in xrange(n1+1):
            dp[i][n2] = n1-i

        for i in xrange(n2+1):
            dp[n1][i] = n2-i
        
        for i in reversed(xrange(n1)):
            for j in reversed(xrange(n2)):
                dp[i][j] = min(dp[i+1][j], dp[i][j+1])+1
                if word1[i] != word2[j]:
                    dp[i][j] = min(dp[i+1][j+1]+1, dp[i][j])
                else:
                    dp[i][j] = min(dp[i+1][j+1], dp[i][j])
                    
        return dp[0][0]
