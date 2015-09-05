# problem description: https://leetcode.com/problems/contains-duplicate-ii/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums = [(nums[i], i) for i in xrange(len(nums))]
        nums.sort()
        
        for i in xrange(len(nums)-1):
            val, idx = nums[i]
            if val == nums[i+1][0] and abs(idx-nums[i+1][1]) <= k:
                return True
        
        return False
