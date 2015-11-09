# problem description: https://leetcode.com/problems/interleaving-string/

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def __init__(self):
        self.cache = {}
    def isInterleave(self, s1, s2, s3):
        if (s1, s2, s3) in self.cache:
            return self.cache[(s1, s2, s3)]
        if s1 == '':
            self.cache[(s1, s2, s3)] = (s2 == s3)
            return s2 == s3
        if s2 == '':
            self.cache[(s1, s2, s3)] = (s1 == s3)
            return s1 == s3
        if len(s1) + len(s2) != len(s3):
            return False
        res1, res2 = False, False
        if s1[0] == s3[0]:
            res1 = self.isInterleave(s1[1:], s2, s3[1:])
        if s2[0] == s3[0]:
            res2 = self.isInterleave(s1, s2[1:], s3[1:])
        self.cache[(s1, s2, s3)] = res1 or res2
        return res1 or res2

# 11.8.2015
class Solution(object):
    cache = {}
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3): return False
        if (s1, s2, s3) in self.cache:
            return self.cache[(s1, s2, s3)]
        if s1 == '': return s2 == s3
        if s2 == '': return s1 == s3
        res1, res2 = False, False
        if s1[0] == s3[0]:
            res1 = self.isInterleave(s1[1:], s2, s3[1:])
        if s2[0] == s3[0]:
            res2 = self.isInterleave(s1, s2[1:], s3[1:])
        self.cache[(s1, s2, s3)] = res1 or res2
        return res1 or res2
