# problem description: https://leetcode.com/problems/sudoku-solver/

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def process(self, board):
        self.rows = [[False] * 9 for i in xrange(9)]
        self.cols = [[False] * 9 for i in xrange(9)]
        self.sm = [[False] * 9 for i in xrange(9)]
        
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.': continue
                self.setExist(board, i, j, True)

    def setExist(self, board, i, j, bl):
        num = int(board[i][j])
        self.rows[i][num-1] = bl
        self.cols[j][num-1] = bl
        idx = (i/3) * 3 + j/3
        self.sm[idx][num-1] = bl

        
    def solveSudoku(self, board):
        self.process(board)
        self.helper(board)
        
    def helper(self, board):
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    for k in xrange(1, 10):
                        board[i][j] = str(k)
                        if self.isValid(board, i, j):
                            if self.helper(board): return True
                            self.setExist(board, i, j, False)

                    board[i][j] = '.'
                    return False
        return True
        
    
    def isValid(self, board, r, c):
        num = int(board[r][c])
        idx = (r/3) * 3 + c/3
        res = not self.rows[r][num-1] and not self.cols[c][num-1] and not self.sm[idx][num-1]
        if res: self.setExist(board, r, c, True)
        return res
