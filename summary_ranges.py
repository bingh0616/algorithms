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

# 11.9.2015
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        res = []
        left = 0
        i = 1
        while i < len(nums)+1:
            if i == len(nums) or nums[i]-nums[i-1] != 1:
                if left != i-1:
                    res.append('->'.join([str(nums[left]), str(nums[i-1])]))
                else:
                    res.append(str(nums[left]))
                left = i
            i += 1
                
        return res
