# problem description: https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        if not nums: return 0
        nums += [2**31-1]
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)/2
            if nums[m] < target:
                l = m+1
            else:
                r = m
                
        return l
