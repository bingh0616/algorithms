# problem description: https://leetcode.com/problems/wildcard-matching/

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        si, pi = 0, 0
        ss, ps = -1, -1
        
        while si < len(s):
            if pi < len(p) and (p[pi] == s[si] or p[pi] == '?'):
                pi += 1
                si += 1
            elif pi < len(p) and p[pi] == '*':
                ss = si
                ps = pi
                pi += 1
            elif ps != -1:
                si = ss+1
                ss = si
                pi = ps
            else:
                return False
            
        while pi < len(p) and p[pi] == '*':
            pi += 1
        return pi == len(p)
