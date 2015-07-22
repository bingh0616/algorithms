# problem description: https://leetcode.com/problems/house-robber/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0: return 0
        pre_one, pre_two = nums[0], 0
        res = pre_one
        
        for i in xrange(1, len(nums)):
            n = nums[i]
            tmp = max(pre_one, pre_two+nums[i])
            res = max(tmp, pre_one)
            pre_two = pre_one
            pre_one = tmp
        
        return res
