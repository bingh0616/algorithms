# problem description: https://leetcode.com/problems/ugly-number-ii/

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        dp = [0] * n
        dp[0] = 1
        p2, p3, p5 = 0, 0, 0
        for i in xrange(1, n):
            dp[i] = min([dp[p2]*2, dp[p3]*3, dp[p5]*5])
            if dp[i] == dp[p2]*2: p2 += 1
            if dp[i] == dp[p3]*3: p3 += 1
            if dp[i] == dp[p5]*5: p5 += 1
            
        
        return dp[n-1]
