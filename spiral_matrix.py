# problem description: https://leetcode.com/problems/spiral-matrix/

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        res = []
        i, j = 0, -1
        while True:
            for k in xrange(n):
                j += 1
                res.append(matrix[i][j])
            m -= 1
            if m == 0: break
            
            for k in xrange(m):
                i += 1
                res.append(matrix[i][j])
            n -= 1
            if n == 0: break
        
            for k in xrange(n):
                j -= 1
                res.append(matrix[i][j])
            m -= 1
            if m == 0: break
            
            for k in xrange(m):
                i -= 1
                res.append(matrix[i][j])
            n -= 1
            if n == 0: break
        
        return res
