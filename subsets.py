# problem description: https://leetcode.com/problems/subsets/

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        return self.helper(nums)
        
    def helper(self, nums):
        if not nums: return [[]]
        res = []
        for r in self.helper(nums[1:]):
            res.append(r)
            res.append([nums[0]]+r)
        return res
