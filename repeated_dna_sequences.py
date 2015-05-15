# problem description: https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        res = set()
        start, end = 0, 10
        exist = set()
        
        while end <= len(s):
            if s[start:end] in exist:
                res.add(s[start:end])
            else:
                exist.add(s[start:end])
            start += 1
            end += 1
        return list(res)
