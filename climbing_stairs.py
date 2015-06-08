# problem description: https://leetcode.com/problems/climbing-stairs/

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n<=1: return 1
        pre, curr = 1, 1
        for i in xrange(2, n+1):
            tmp = pre + curr
            pre = curr
            curr = tmp
        
        return curr
