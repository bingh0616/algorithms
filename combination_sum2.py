# problem description: https://leetcode.com/problems/combination-sum-ii/

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(sorted(candidates), target, res, [], 0)
        return res
    
    def helper(self, candidates, target, res, sol, start):
        if target == 0:
            res.append(sol[:])
        else:
            for i in xrange(start, len(candidates)):
                if target - candidates[i] < 0:
                    break
                else:
                    if i > start and candidates[i] == candidates[i-1]: continue
                    sol.append(candidates[i])
                    self.helper(candidates, target-candidates[i], res, sol, i+1)
                    sol.pop()
