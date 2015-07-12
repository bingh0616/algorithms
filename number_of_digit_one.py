# problem description: https://leetcode.com/problems/number-of-digit-one/

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        res = 0
        m = 1
        while m<=n:
            res += (n/m+8) / 10 * m + (n/m%10 == 1) * (n%m+1)
            m *= 10

        return res
        
