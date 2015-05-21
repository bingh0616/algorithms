# problem description: https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        res = ''
        while n > 0:
            r = (n-1)%26
            res += chr(r+ord('A'))
            n = (n-1)/26
            
        return res[::-1]
