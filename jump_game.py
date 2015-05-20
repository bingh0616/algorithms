# problem description: https://leetcode.com/problems/jump-game/

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        reach = 0
        for i in range(len(nums)):
            if reach < i: return False
            reach = max(reach, i+nums[i])
        return reach >= len(nums)-1
