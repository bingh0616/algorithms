# problem description: https://leetcode.com/problems/roman-to-integer/
class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        dt = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res = 0
        
        for i in xrange(len(s)):
            res += int(dt[s[i]])
            if i > 0 and dt[s[i]] > dt[s[i-1]]:
                res -= (2*dt[s[i-1]])
                
        return res
