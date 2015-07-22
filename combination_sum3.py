# problem description: https://leetcode.com/problems/combination-sum-iii/

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        return self.helper(k, n, 1, range(1,10))
    
    def helper(self, k, n, start, A):
        if k == 0 or n == 0: return []
        if k == 1:
            if n >= start and n < 10:
                return [[n]]
        
        res = []
        for i in xrange(start, 10):
            for r in [[A[i-1]]+j for j in self.helper(k-1, n-A[i-1], i+1, A)]:
                res.append(r)
        return res
