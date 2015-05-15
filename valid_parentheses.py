# problem description: https://leetcode.com/problems/valid-parentheses/

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        pares = {'(':0, ')':1, '{':2, '}':3, '[':4, ']':5}
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif pares[stack[-1]] == pares[c]-1 and pares[c] % 2 == 1:
                stack.pop()
            else:
                stack.append(c)
        return not stack
