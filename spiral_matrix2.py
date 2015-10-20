# problem description: https://leetcode.com/problems/spiral-matrix-ii/

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        r, c = n, n
        
        matrix = [[0] * n for i in xrange(n)]
        i, j = 0, -1
        val = 1
        while val <= n*n:
            for k in xrange(c):
                j += 1
                matrix[i][j] = val
                val += 1
            r -= 1

            for k in xrange(r):
                i += 1
                matrix[i][j] = val
                val += 1
            c -= 1

            for k in xrange(c):
                j -= 1
                matrix[i][j] = val
                val += 1
            r -= 1

            for k in xrange(r):
                i -= 1
                matrix[i][j] = val
                val += 1
            c -= 1

        return matrix
