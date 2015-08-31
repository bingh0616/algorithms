# problem description: https://leetcode.com/problems/missing-number/

# my solution
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        nums += [-1]
        i = 0
        while i<n:
            idx = nums[i]
            if nums[i] != i:
                nums[i], nums[idx] = nums[idx], nums[i]
                if nums[i] != -1: i -= 1
            i += 1
        
        for i in xrange(n+1):
            if nums[i] == -1:
                return i
                
        # should never happen
        return -1

# better solution: added all up and use ideal sum subtract the added sum to calculate the missing one
class Solution(object):
    def missingNumber(self, nums):
        # or use sum = n * (n+1) / 2 to calculate ideal sum
        return sum(xrange(len(nums)+1))-sum(nums)

# another solution: XOR for all vals and its index. For example, [3,1,0] will XOR with [1,2,3] (ignore 0 because no effect), the result will be 2
class Solution(object):
    def missingNumber(self, nums):
        missing = 0
        for i in xrange(len(nums)):
            missing ^= (nums[i] ^ (i+1))
        return missing
