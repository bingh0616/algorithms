# problem description: https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0: return False
        n = len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                if word[0] == board[i][j]:
                    if self.search(i, j, m, n, board, word, 0, set()):
                        return True
        
        return False
    def search(self, i, j, m, n, board, word, k, visited):
        if k == len(word)-1 and board[i][j] == word[k]: return True
        if board[i][j] != word[k]: return False
        res = False
        if i+1 < m and (i+1, j) not in visited:
            if self.search(i+1, j, m, n, board, word, k+1, visited | {(i,j)}):
                return True
        if i-1 >= 0 and (i-1, j) not in visited:
            if self.search(i-1, j, m, n, board, word, k+1, visited | {(i,j)}):
                return True
        if j+1 < n and (i, j+1) not in visited:
            if self.search(i, j+1, m, n, board, word, k+1, visited | {(i,j)}):
                return True
        if j-1 >= 0 and (i, j-1) not in visited:
            if self.search(i, j-1, m, n, board, word, k+1, visited | {(i,j)}):
                return True
        return False

# 10.26.2015
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0: return False
        n = len(board[0])
        
        for i in xrange(m):
            for j in xrange(n):
                if self.dfs(board, word, i, j, m, n, set()):
                    return True
        return False
    
    def dfs(self, board, word, i, j, m, n, visited):
        if not word: return True
        if word[0] != board[i][j]: return False
        word = word[1:]
        if not word: return True
        visited.add((i,j))
        if i+1 < m and (i+1,j) not in visited and self.dfs(board, word, i+1, j, m, n, visited):
            return True
        if i-1 >= 0 and (i-1,j) not in visited and self.dfs(board, word, i-1, j, m, n, visited):
            return True
        if j+1 < n and (i,j+1) not in visited and self.dfs(board, word, i, j+1, m, n, visited):
            return True
        if j-1 >= 0 and (i,j-1) not in visited and self.dfs(board, word, i, j-1, m, n, visited):
            return True
        visited.discard((i,j))
        return False
