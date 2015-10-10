# problem description: https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -2**31
        curr_sum = 0
        for val in nums:
            curr_sum += val
            curr_sum = max(curr_sum, val)
            max_sum = max(curr_sum, max_sum)
            
        return max_sum
