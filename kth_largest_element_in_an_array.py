import random

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        pi = self.partition(nums, 0, len(nums)-1)
        if pi+1 == k: return nums[pi]
        if pi+1 > k:
            return self.findKthLargest(nums[:pi+1], k)
        else:
            return self.findKthLargest(nums[pi+1:], k-pi-1)
    
    def partition(self, nums, left, right):
        pi = random.randint(left, right)
        pval = nums[pi]
        
        nums[pi], nums[right] = nums[right], nums[pi]
        
        res = 0
        for i in range(left, right):
            if nums[i] > pval:
                nums[res], nums[i] = nums[i], nums[res]
                res += 1
        
        nums[res], nums[right] = nums[right], nums[res]
        
        return res

print Solution().findKthLargest([3,2,1,5,6,4], 2)
