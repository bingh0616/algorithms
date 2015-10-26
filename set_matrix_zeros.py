# problem description: https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0: return
        n = len(matrix[0])
        first_row_zero, first_col_zero = False, False
        
        for j in xrange(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
            
        for i in xrange(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in xrange(1,m):
            for j in xrange(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if first_row_zero:
            for j in xrange(n):
                matrix[0][j] = 0
        
        if first_col_zero:
            for i in xrange(m):
                matrix[i][0] = 0
