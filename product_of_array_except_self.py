# problem description: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        left_fac, right_fac, i = 1, 1, 0
        n = len(nums)
        res = [1] * n
        while i<n:
            res[i] *= left_fac
            left_fac *= nums[i]
            i += 1
            res[n-i] *= right_fac
            right_fac *= nums[n-i]
        return res
