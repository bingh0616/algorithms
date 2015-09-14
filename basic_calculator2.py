# problem description: https://leetcode.com/problems/basic-calculator-ii/ 

# class Solution(object):
#     def calculate(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         s = ''.join([c for c in s if c != ' '])
#         return self.helper(s)
#         
#     def helper(self, s):
#         if len(s) == 0: return 0
#         if s.isdigit(): return int(s)
#         i = 0
#         while s[i] not in '+-/*': i += 1
#         if s[i] in '+-':
#             return (int(s[:i])+self.helper(s[i+1:])) if s[i] == '+' else (int(s[:i])-self.helper(s[i+1:]))
#         else:
#             j = i
#             i += 1
#             while i<len(s) and s[i] not in '+-/*': i += 1
#             curr = (int(s[:j])*int(s[j+1:i])) if s[j] == '*' else int((float(s[:j])/float(s[j+1:i])))
#             if i == len(s): return curr
#             return (curr+self.helper(s[i+1:])) if s[i] == '+' else (curr-self.helper(s[i+1:]))

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = '+'
        val = 0
        stk = []
        for i,c in enumerate(s):
            if c.isdigit():
                val = val*10+int(c)
            if c in '+-*/' or i == len(s)-1:
                if sign == '+':
                    stk.append(val)
                elif sign == '-':
                    stk.append(-val)
                elif sign == '*':
                    stk.append(stk.pop()*val)
                else:
                    stk.append(int(float(stk.pop())/val))
                sign = c
                val = 0
        
        res = 0
        for val in stk:
            res += val

        return res

print Solution().calculate(" 3 / 2 ")
