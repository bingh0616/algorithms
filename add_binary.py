# problem description: https://leetcode.com/problems/add-binary/

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        a = a[::-1]
        b = b[::-1]
        i = 0
        c = ''
        carry = 0
        while i<len(a) or i<len(b):
            aval = int(a[i]) if i<len(a) else 0
            bval = int(b[i]) if i<len(b) else 0
            res = (aval+bval+carry) % 2
            carry = (aval+bval+carry) / 2
            c += str(res)
            i += 1
        if carry != 0: c += str(carry)
            
        return c[::-1]
