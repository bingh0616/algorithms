# problem description: https://leetcode.com/problems/scramble-string/

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def __init__(self):
        self.cache = {}
    def isScramble(self, s1, s2):
        if s1 == s2: return True
        if sorted(s1) != sorted(s2): return False
        if (s1, s2) in self.cache: return self.cache[(s1,s2)]
        n = len(s1)
        for i in xrange(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.cache[(s1, s2)] = True
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                self.cache[(s1, s2)] = True
                return True
        self.cache[(s1, s2)] = False
            
        return False
