# problem description: https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        height.append(0)
        stk = []
        res = 0
        
        for i in xrange(len(height)):
            while stk and height[i] < height[stk[-1]]:
                h = height[stk.pop()]
                w = i-stk[-1]-1 if stk else i
                res = max(res, w*h)
                
            stk.append(i)
            
        return res
