# problem description: https://leetcode.com/problems/dungeon-game/

class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        if m == 0: return 0
        n = len(dungeon[0])
        dp = [[0] * n for i in range(m)]
        dp[m-1][n-1] = 1-dungeon[m-1][n-1]
        if dp[m-1][n-1] <= 0: dp[m-1][n-1] = 1
        for i in reversed(range(m-1)):
            dp[i][n-1] = dp[i+1][n-1] - dungeon[i][n-1]
            if dp[i][n-1] <= 0: dp[i][n-1] = 1
            
        for i in reversed(range(n-1)):
            dp[m-1][i] = dp[m-1][i+1] - dungeon[m-1][i]
            if dp[m-1][i] <= 0: dp[m-1][i] = 1
            
        for i in reversed(range(m-1)):
            for j in reversed(range(n-1)):
                dp[i][j] = min(dp[i+1][j], dp[i][j+1])-dungeon[i][j]
                if dp[i][j] <= 0: dp[i][j] = 1
                
        return dp[0][0]
