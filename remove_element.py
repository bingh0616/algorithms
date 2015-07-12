# problem description: https://leetcode.com/problems/remove-element/

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        l = len(nums)
        i = 0
        while i<l:
            if nums[i] == val:
                nums[i], nums[l-1] = nums[l-1], nums[i]
                i -= 1
                l -= 1
            i += 1
            
        return l
