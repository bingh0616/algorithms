# problem description: https://leetcode.com/problems/next-permutation/

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        i = len(nums)-1
        while i>0:
            if nums[i] > nums[i-1]:
                j = len(nums)-1
                while j>=i:
                    if nums[j] > nums[i-1]:
                        break
                    j -= 1
                
                nums[i-1], nums[j] = nums[j], nums[i-1]
                nums[i:] = reversed(nums[i:])
                break
            i -= 1
            
        if i==0: nums.sort()
