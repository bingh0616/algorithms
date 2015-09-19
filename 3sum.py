# problem description: https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in xrange(len(nums)-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            l = i+1
            r = len(nums)-1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
                elif sm < 0:
                    l += 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
        
        return res
