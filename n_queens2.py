# problem description: https://leetcode.com/problems/n-queens-ii/

class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        self.res = 0
        self.nQueens([['.'] * n for i in range(n)], 0, n)
        return self.res
        
    # i is the line we are placing
    def nQueens(self, grid, i, n):
        if i == n:
            self.res += 1
            return
        for j in range(n):
            grid[i][j] = 'Q'
            if self.isValid(grid, i, j, n):
                self.nQueens(grid, i+1, n)
            grid[i][j] = '.'
            
            
    def isValid(self, grid, i, j, n):
        for k in range(i):
            if grid[k][j] == 'Q':
                return False
        for k in range(1, i+1):
            if i-k >= 0 and j-k >= 0:
                if grid[i-k][j-k] == 'Q':
                    return False
            if i-k >= 0 and j+k < n:
                if grid[i-k][j+k] == 'Q':
                    return False
        return True
