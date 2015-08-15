class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        max_val = 0
        for i in range(len(nums)):
            n = nums[i]
            curr = n
            lst = nums[i:] + nums[:i]
            curr += self.rob_nocircle(lst[2:-1])
            max_val = max(max_val, curr)
        return max_val
    
    def rob_nocircle(self, nums):
        if len(nums) == 0: return 0
        pre_one, pre_two = nums[0], 0
        res = pre_one
        
        for i in xrange(1, len(nums)):
            n = nums[i]
            tmp = max(pre_one, pre_two+nums[i])
            res = max(tmp, pre_one)
            pre_two = pre_one
            pre_one = tmp
        
        return res

# better solution, with O(n) time and O(1) space
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        # either first or last house is not robbed
        return max(self.rob_nocircle(nums[1:]), self.rob_nocircle(nums[:-1]))
    
    def rob_nocircle(self, nums):
        if len(nums) == 0: return 0
        pre_one, pre_two = nums[0], 0
        res = pre_one
        
        for i in xrange(1, len(nums)):
            n = nums[i]
            tmp = max(pre_one, pre_two+nums[i])
            res = max(tmp, pre_one)
            pre_two = pre_one
            pre_one = tmp
        
        return res
