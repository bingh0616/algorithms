# problem description: https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        level = n/2
        for lv in xrange(level):
            for i in xrange(lv, n-lv-1):
                # store top
                tmp = matrix[lv][i]
                # left to top
                matrix[lv][i] = matrix[n-1-i][lv]
                # bottom to left
                matrix[n-1-i][lv] = matrix[n-lv-1][n-1-i]
                # right to bottom
                matrix[n-lv-1][n-1-i] = matrix[i][n-lv-1]
                # top to right
                matrix[i][n-lv-1] = tmp
