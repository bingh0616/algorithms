# problem description: https://leetcode.com/problems/permutations-ii/

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.helper(sorted(nums))
    def helper(self, nums):
        if len(nums) == 0: return [[]]
        res = []
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            res += ([nums[i]]+ j for j in self.helper(nums[:i]+nums[i+1:]))
        return res

def main():
    print Solution().permuteUnique([1, 1, 2])

if __name__ == '__main__':
    main()
