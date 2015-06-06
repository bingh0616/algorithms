# problem description: https://leetcode.com/problems/word-break-ii/

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        if not s: return []
        self.cache = {}
        res = self.helper(s, wordDict)
        for i in xrange(len(res)):
            res[i] = ' '.join(res[i])
        return res
        
    def helper(self, s, wordDict):
        if not s: return [[]]
        if s in self.cache: return self.cache[s]
        res = []
        for i in xrange(1, len(s)+1):
            if s[:i] in wordDict:
                sub_res = self.helper(s[i:], wordDict)
                if sub_res:
                    res += [[s[:i]] + r for r in sub_res]
                    
        self.cache[s] = res
        return res
