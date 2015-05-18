# problem description: https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        mp = {}
        max_cons = 0
        for val in nums:
            if val not in mp:
                cons = 1
                if val-1 in mp: cons += mp[val-1]
                if val+1 in mp: cons += mp[val+1]
                if val-1 in mp: mp[val-mp[val-1]] = cons
                if val+1 in mp: mp[mp[val+1]+val] = cons
                mp[val] = cons
                max_cons = max(max_cons, cons)
        return max_cons
