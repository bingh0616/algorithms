# problem description: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) <= 1: return
        new_len = 0
        p = 1
        while p < len(nums):
            if nums[new_len] != nums[p]:
                new_len += 1
                nums[new_len] = nums[p]
            p += 1
            
        return new_len+1
