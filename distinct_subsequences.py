# problem description: https://leetcode.com/problems/distinct-subsequences/

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        dp = [[0] * (len(t)+1) for i in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][len(t)] = 1
        for i in reversed(range(len(s))):
            for j in reversed(range(len(t))):
                dp[i][j] = dp[i+1][j]
                if s[i] == t[j]: dp[i][j] += dp[i+1][j+1]
                    
        return dp[0][0]

def main():
    print Solution().numDistinct('rabbbit', 'rabbit')

if __name__ == '__main__':
    main()
