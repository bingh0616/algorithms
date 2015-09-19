# problem description: https://leetcode.com/problems/4sum/

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        for i in xrange(n-3):
            # needed, or will not pass some test cases
            if target < nums[i]*4 or target > nums[-1]*4: break
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in xrange(i+1, n-2):
                if target-nums[i] < nums[j]*3 or target-nums[i] > nums[-1]*3: break
                if j > i+1 and nums[j] == nums[j-1]: continue
                l = j+1
                r = n-1
                while l < r:
                    sm = nums[i]+nums[j]+nums[l]+nums[r]
                    if sm == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]: l += 1
                        while l < r and nums[r] == nums[r+1]: r -= 1
                    elif sm < target:
                        l += 1
                        while l < r and nums[l] == nums[l-1]: l += 1
                    else:
                        r -= 1
                        while l < r and nums[r] == nums[r+1]: r -= 1
                        
        return res

# n sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results
    
    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return
    
        # solve 2-sum
        if N == 2:
            l,r = 0,len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):   # careful about range
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
