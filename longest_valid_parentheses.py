# problem description: https://leetcode.com/problems/longest-valid-parentheses/

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = []
        res = 0
        for i in xrange(len(s)):
            c = s[i]
            if stk and s[stk[-1]] == '(' and c == ')':
                stk.pop()
                prev = stk[-1] if stk else -1
                res = max(res, i-prev)
            else:
                stk.append(i)
                
        return res
