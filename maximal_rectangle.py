# problem description: https://leetcode.com/problems/maximal-rectangle/

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        height = [0] * n
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == '1':
                    height[j] = height[j] + 1
                else:
                    height[j] = 0
            res = max(res, self.largestRectangleArea(height+[0]))
        return res
    
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # height.append(0)
        stk = []
        res = 0
        for i in xrange(len(height)):
            while stk and height[i] < height[stk[-1]]:
                h = height[stk.pop()]
                w = i-stk[-1]-1 if stk else i
                res = max(res, w*h)
            stk.append(i)
            
        return res
