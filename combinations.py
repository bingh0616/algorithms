# problem description: https://leetcode.com/problems/combinations/

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        return self.helper(range(1, n+1), k)
                
    def helper(self, A, k):
        if k == 0:
            return [[]]
        res = []
        for i in range(len(A)):
            # res += [[A[i]]+j for j in self.helper(A[i+1:], k-1)]
            for r in self.helper(A[i+1:], k-1):
                res.append([A[i]] + r)
                
        return res
