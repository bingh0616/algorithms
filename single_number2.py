# problem description: https://leetcode.com/problems/single-number-ii/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        one, two, three = 0, 0, 0
        for val in nums:
            two |= (one & val)
            one ^= val
            three = one & two
            # clean bits in one and two
            one &= ~three
            two &= ~three
        return one
