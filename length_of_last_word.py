# problem description: https://leetcode.com/problems/length-of-last-word/

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        s = s.strip()
        i = len(s)-1
        while i >= 0 and s[i] != ' ': i -= 1
        return len(s)-i-1
