# problem description: https://leetcode.com/problems/divide-two-integers/

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        sign = 1 if (dividend<0) == (divisor<0) else -1
        dd, dv = abs(dividend), abs(divisor)
        c = 1
        
        while dd > dv:
            dv <<= 1
            c <<= 1
        
        res = 0
        while c > 0:
            if dd >= dv:
                if sign == 1 and res+c >= 2**31-1: return 2**31-1
                if sign == -1 and res+c >= 2**31: return -2**31
                res += c
                dd -= dv
            dv >>= 1
            c >>= 1
        return sign * res
