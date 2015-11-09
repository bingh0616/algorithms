# problem description: https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

def main():
    print Solution().numTrees(3)

if __name__ == '__main__':
    main()

# 11.06.2015
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return n
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in xrange(2, n+1):
            for j in xrange(i):
                dp[i] += (dp[j]*dp[i-1-j])
        return dp[n]
