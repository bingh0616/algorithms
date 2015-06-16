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
