# problem description: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) <= 2: return len(nums)
        pre, curr = 1, 2
        while curr < len(nums):
            if nums[pre] == nums[curr] and nums[pre-1] == nums[curr]:
                curr += 1
            else:
                pre += 1
                nums[pre] = nums[curr]
                curr += 1
                
        return pre+1
