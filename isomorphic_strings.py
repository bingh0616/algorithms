# problem description: https://leetcode.com/problems/isomorphic-strings/

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        i = 0
        mp = {}
        used = set()
        while i<len(s):
            if s[i] not in mp:
                if t[i] in used: return False
                mp[s[i]] = t[i]
                used.add(t[i])
            elif mp[s[i]] != t[i]:
                return False
            i += 1
            
        return True
