# problem description: https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        res = 0
        while n > 0:
            res += (n/5)
            n /= 5
        return res
