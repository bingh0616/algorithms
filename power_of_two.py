# problem description: https://leetcode.com/problems/power-of-two/

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n != 0 and (n & (n-1) == 0)
