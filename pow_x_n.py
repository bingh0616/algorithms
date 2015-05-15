# problem description: https://leetcode.com/problems/powx-n/

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0: return 1.0
        x = x if n >= 0 else 1/x
        extra = 1 if abs(n) % 2 == 0 else x
        return self.myPow(x*x, abs(n)/2) * extra
