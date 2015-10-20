# problem description: https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums))
        self.reverse(nums, 0, k)
        self.reverse(nums, k, len(nums))
        
    def reverse(self, nums, s, e):
        for i in xrange(s, (s+e)/2):
            nums[i], nums[e+s-i-1] = nums[e+s-i-1], nums[i]
