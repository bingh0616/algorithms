# problem description: https://leetcode.com/problems/subsets-ii/ 

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        nums.sort()
        res = [[]]
        pre_cnt = 0
        
        for i, n in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                res = res + [r + [n] for r in res[-pre_cnt:]]
            else:
                tmp = len(res)
                res = res + [r + [n] for r in res]
                pre_cnt = len(res) - tmp
            
        return res

