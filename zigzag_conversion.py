# problem description: https://leetcode.com/problems/zigzag-conversion/

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        buffer = [''] * numRows
        i = 0
        while i<len(s):
            for idx in range(numRows):
                if i<len(s): buffer[idx] += s[i]
                i += 1
                
            for idx in range(numRows-2, 0, -1):
                if i<len(s): buffer[idx] += s[i]
                i += 1
        
        return reduce(lambda a,b:a+b, buffer)
