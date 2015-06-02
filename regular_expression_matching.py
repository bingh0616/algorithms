# problem description: https://leetcode.com/problems/regular-expression-matching/

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def __init__(self):
        self.cache = {}
    def isMatch(self, s, p):
        if not p: return not s
        if (s,p) in self.cache: return self.cache[(s,p)]
        if len(p) > 1 and p[1] == '*':
            res = self.isMatch(s, p[2:])
            if s and (p[0] == s[0] or p[0] == '.'):
                res |= (self.isMatch(s[1:], p) or self.isMatch(s[1:], p[2:]))
            self.cache[(s,p)] = res
            return res
        else:
            if s and (p[0] == s[0] or p[0] == '.'):
                self.cache[(s,p)] = self.isMatch(s[1:], p[1:])
                return self.cache[(s,p)]
            return False
