# problem description: https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.helper(candidates, 0, target, res, [])
        return res
        
    def helper(self, candidates, start, target, res, sol):
        if target == 0:
            res.append(sol[:])
        else:
            for i in xrange(start, len(candidates)):
                if i > 0 and candidates[i-1] == candidates[i]:
                    continue
                if target-candidates[i] < 0:
                    break
                sol.append(candidates[i])
                self.helper(candidates, i, target-candidates[i], res, sol)
                sol.pop()
