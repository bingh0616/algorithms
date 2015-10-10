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

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step, max_reach, reach = 0, 0, 0
        for i in xrange(len(nums)):
            if i > reach:
                step += 1
                reach = max_reach
            max_reach = max(max_reach, i+nums[i])
        return step
