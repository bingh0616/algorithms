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

# using kSum
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.kSum(nums, len(nums), 3, 0)
    
    def kSum(self, nums, n, k, target):
        # assum k is less than n
        if k == 2:
            return self.twoSum(nums, target)
        res = []
        for i in xrange(n-k+1):
            if i > 0 and nums[i] == nums[i-1]: continue
            pre = self.kSum(nums[i+1:], n-i-1, k-1, target-nums[i])
            res += [[nums[i]]+a for a in pre]
        
        return res
        
    def twoSum(self, nums, target):
        l, r = 0, len(nums)-1
        res = []
        while l < r:
            if nums[l]+nums[r] == target:
                res.append([nums[l], nums[r]])
                lp = nums[l]
                rp = nums[r]
                while l < r and nums[l] == lp:
                    l += 1
                while l < r and nums[r] == rp:
                    r -= 1
            elif nums[l]+nums[r] < target:
                lp = nums[l]
                while l < r and nums[l] == lp:
                    l += 1
            else:
                rp = nums[r]
                while l < r and nums[r] == rp:
                    r -= 1
        return res
