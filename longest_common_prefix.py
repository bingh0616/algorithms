# problem description: https://leetcode.com/problems/longest-common-prefix/

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        first = strs[0]
        i = 0
        while i < len(first):
            c = first[i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    return first[:i]
            i += 1
            
        return first
