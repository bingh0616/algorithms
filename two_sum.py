# problem description: https://leetcode.com/problems/two-sum/

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        tuples = [(nums[i], i+1) for i in range(len(nums))]
        tuples.sort()
        left, right = 0, len(tuples)-1
        while left < right:
            sum = tuples[left][0] + tuples[right][0]
            if sum == target:
                return sorted([tuples[left][1], tuples[right][1]])
            elif sum < target:
                left += 1
            else:
                right -= 1
        # this should never execute because we guarantee have exactly one solution
        return [0, 0]

