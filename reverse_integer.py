# problem description: https://leetcode.com/problems/reverse-integer/

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        sign = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while x > 0:
            if res > 2**31/10 or (res == 2**31/10 and x%10 > (7 if sign == 1 else 8)): return 0
            res = res * 10 + (x % 10)
            x /= 10
        return res * sign
