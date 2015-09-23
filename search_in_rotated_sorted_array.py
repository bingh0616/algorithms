# problem description: https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)/2
            if target == nums[m]: return m
            # use nums[m] < nums[r] instead of nums[m] > nums[r] to avoid when l+1 == r (m == l)
            if nums[m] < nums[r]:
                if target > nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            else:
                if target >= nums[l] and target < nums[m]:
                    r = m-1
                else:
                    l = m+1
                
        return -1

