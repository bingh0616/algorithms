# problem description: https://leetcode.com/problems/multiply-strings/

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                res[i+j] += (int(num1[i]) * int(num2[j])) % 10
                res[i+j+1] += (int(num1[i]) * int(num2[j])) / 10
                
        for i in xrange(len(res)):
            if res[i] >= 10:
                res[i+1] += res[i] / 10
                res[i] %= 10
                
        s = [str(r) for r in res]
        while s and s[-1] == '0': s = s[:-1]
        if len(s) == 0: return '0'
        return ''.join(reversed(s))
