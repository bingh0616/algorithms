# problem description: https://leetcode.com/problems/sqrtx/

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x <= 1: return x
        l, r = 1, x
        while l < r:
            m = (l+r) / 2
            if m**2 == x:
                return m
            elif m**2 > x:
                r = m-1
            else:
                l = m+1
                
        return l-1 if l**2 > x else l

# newton's method
class Solution:
    def mySqrt(self, x):
        i = 1.0
        while abs(i**2-x) > 1e-6:
            i = (i+x/i)/2

        return int(i)

# 10.20.2015
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l < r-1:
            m = (l+r) / 2
            if m**2 == x:
                return m
            if m**2 > x:
                r = m-1
            else:
                l = m
        
        if l == r: return l if l**2 <=x else l-1
        return r if r**2 <= x else l
