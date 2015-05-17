# problem description: https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        res = 0
        for c in s:
            res = res*26 + (ord(c)-ord('A')+1)
        return res
