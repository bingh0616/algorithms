# problem description: https://leetcode.com/problems/trapping-rain-water/

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        n = len(height)
        left_max = [0] * n
        for i in xrange(1, n):
            left_max[i] = max(left_max[i-1], height[i-1])
            
        right_max = [0] * n
        res = 0
        for i in reversed(xrange(n-1)):
            right_max[i] = max(right_max[i+1], height[i+1])
            res += max((min(left_max[i], right_max[i]) - height[i]), 0)
            
        return res
