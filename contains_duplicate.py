# problem description: https://leetcode.com/problems/contains-duplicate/

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)
