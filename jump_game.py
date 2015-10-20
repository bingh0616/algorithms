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

# 10.10.2015
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i in xrange(len(nums)):
            if reach < i: return False
            reach = max(reach, nums[i]+i)
            if reach >= len(nums): break
        return True
