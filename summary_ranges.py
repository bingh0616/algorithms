# problem description: https://leetcode.com/problems/summary-ranges/

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums: return []
        start = nums[0]
        res = []
        for i in xrange(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                continue
            if start != nums[i-1]:
                res.append('{0}->{1}'.format(start, nums[i-1]))
            else:
                res.append(str(nums[i-1]))
            start = nums[i]
            
        if start != nums[len(nums)-1]:
            res.append('{0}->{1}'.format(start, nums[len(nums)-1]))
        else:
            res.append(str(nums[len(nums)-1]))
        return res
