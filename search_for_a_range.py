# problem description: https://leetcode.com/problems/search-for-a-range/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = -1, -1
        # find start
        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)/2
            if nums[m] >= target:
                r = m
            else:
                l = m+1
                
        if l == r and nums[l] == target:
            start = l
        if start == -1: return [-1,-1]
        
        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)/2
            if nums[m] < target:
                l = m+1
            elif nums[m] == target:
                if l == m:
                    end = l if nums[l] != nums[r] else r
                    break
                l = m
            else:
                r = m-1
        if l == r and nums[r] == target:
            end = r
        return [start, end]
