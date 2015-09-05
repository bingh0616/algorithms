# problem description: https://leetcode.com/problems/contains-duplicate-iii/

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0: return False
        dc = {}
        for i in xrange(len(nums)):
            val = nums[i] + 2**31
            bucket = val / (t+1)
            if bucket in dc or (bucket-1 in dc and val-dc[bucket-1] <= t) \
                or (bucket+1 in dc and dc[bucket+1]-val <= t):
                    return True
                
            if len(dc) >= k:
                lb = (nums[i-k]+2**31) / (t+1)
                dc.pop(lb, None)
            dc[bucket] = val
            
        return False
