# problem description: https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if not nums: return 0
        max_so_far = nums[0]
        max_here, min_here = nums[0], nums[0]
        for val in nums[1:]:
            mm, mn = max_here, min_here
            max_here = max([mm * val, mn * val, val])
            min_here = min([mm * val, mn * val, val])
            max_so_far = max(max_here, max_so_far)
            
        return max_so_far
