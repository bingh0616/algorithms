# problem description: https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        l, r = 0, 0
        sm = 0
        min_len = len(nums)+1
        while r < len(nums):
            sm += nums[r]
            r += 1
            while r < len(nums) and sm < s:
                sm += nums[r]
                r += 1
            while l < r and sm-nums[l] >= s:
                sm -= nums[l]
                l += 1
            if r-l < min_len and sm >= s:
                min_len = r-l

        return min_len if min_len <= len(nums) else 0

