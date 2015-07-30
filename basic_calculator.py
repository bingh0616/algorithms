# problem description: https://leetcode.com/problems/basic-calculator/

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s = '(' + s + ')'
        stk = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = 0
                while s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                stk.append(str(num))
                i -= 1
            elif c == '(' or c == '+' or c == '-':
                stk.append(c)
            elif c == ')':
                res = 0
                prev_num = 0
                while stk[-1] != '(':
                    curr = stk.pop()
                    if curr.isdigit() or len(curr) > 1:
                        prev_num = int(curr)
                        if stk[-1] == '(': res += int(prev_num)
                    elif curr == '+':
                        res += prev_num
                    else:
                        res -= prev_num
                stk.pop()
                stk.append(str(res))
            i += 1
        return int(stk[-1])
