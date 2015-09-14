# problem description: https://leetcode.com/problems/different-ways-to-add-parentheses/

# my init AC solution, 164ms
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit(): return [int(input)]
        n = len(input)
        res = []
        for i in xrange(n):
            if input[i] not in '-+*': continue
            t = self.diffWaysToCompute(input[:i])
            s = self.diffWaysToCompute(input[i+1:])
            for e in t:
                for f in s:
                    res.append(eval(str(e)+input[i]+str(f)))
        
        return res

# clean and faster version of the above, 84ms

class Solution(object):
    def diffWaysToCompute(self, input):
        return [a+b if c == '+' else a-b if c == '-' else a*b
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]

# lots of repeat compute, can use DP to solve, cache the computed result, 52ms
class Solution(object):
    def __init__(self):
        self.cache = {}
    def diffWaysToCompute(self, input):
        if input in self.cache: return self.cache[input]
        res = [a+b if c == '+' else a-b if c == '-' else a*b
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]
        self.cache[input] = res
        return res
