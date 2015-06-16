# problem description: https://leetcode.com/problems/jump-game-ii/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        step = -1
        curr_reach = -1
        max_reach = 0
        for i in xrange(len(nums)):
            a = nums[i]
            if i > curr_reach:
                step += 1
                curr_reach = max_reach
                if curr_reach >= len(nums)-1: break
            max_reach = max(max_reach, i+a)
            if max_reach == i and i != len(nums)-1: return -1
                
        return step
