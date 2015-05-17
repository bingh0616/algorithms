# problem description: https://leetcode.com/problems/roman-to-integer/
class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        vals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i, r in enumerate(s):
            if i == 0 or vals[r] <= vals[s[i-1]]:
                res += vals[r]
            else:
                res += (vals[r] - 2 * vals[s[i-1]])
                
        return res
