# problem description: https://leetcode.com/problems/valid-sudoku/

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        for i in xrange(9):
            if not self.isValid(board, i, 0, i, 8): return False
            if not self.isValid(board, 0, i, 8, i): return False
            
        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                if not self.isValid(board, i, j, i+2, j+2): return False
        return True
                
    def isValid(self, board, x1, y1, x2, y2):
        used = [False] * 9
        for i in xrange(x1, x2+1):
            for j in xrange(y1, y2+1):
                if board[i][j] == '.': continue
                if used[ord(board[i][j])-ord('1')]: return False
                used[ord(board[i][j])-ord('1')] = True
                
        return True

# same complexity, easier understood
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        r, c = [False] * 10, [False] * 10
        for i in xrange(9):
            r, c = [False] * 10, [False] * 10
            for j in xrange(9):
                relem = int(board[i][j]) if board[i][j] != '.' else 0
                celem = int(board[j][i]) if board[j][i] != '.' else 0
                if relem != 0 and r[relem]: return False
                if celem != 0 and c[celem]: return False
                r[relem] = True
                c[celem] = True
        
        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                r = [False] * 10
                for m in xrange(i, i+3):
                    for n in xrange(j, j+3):
                        elem = int(board[m][n]) if board[m][n] != '.' else 0
                        if elem != 0 and r[elem]: return False
                        r[elem] = True
                        
        return True
