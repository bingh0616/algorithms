# problem description: https://leetcode.com/problems/number-of-islands/

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        visited = set()
        res = 0
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    res += 1
                    self.dfs(grid, i, j, visited, m, n)
                    
        return res
    
    def dfs(self, grid, i, j, visited, m, n):
        visited.add((i,j))
        
        if i-1 >= 0 and grid[i-1][j] == '1' and (i-1, j) not in visited: self.dfs(grid, i-1, j, visited, m, n)
        if i+1 < m and grid[i+1][j] == '1' and (i+1, j) not in visited: self.dfs(grid, i+1, j, visited, m, n)
        if j-1 >= 0 and grid[i][j-1] == '1' and (i, j-1) not in visited: self.dfs(grid, i, j-1, visited, m, n)
        if j+1 < n and grid[i][j+1] == '1' and (i, j+1) not in visited: self.dfs(grid, i, j+1, visited, m, n)
        
