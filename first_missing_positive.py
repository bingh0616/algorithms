# problem description: https://leetcode.com/problems/first-missing-positive/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0
        while i<n:
            a = nums[i]
            if a > 0 and a <= n and a != i+1:
                if nums[a-1] != a:
                    nums[a-1], nums[i] = nums[i], nums[a-1]
                    i -= 1
            i += 1
            
        for i in xrange(n):
            if nums[i] != i+1:
                return i+1
                
        return n+1
