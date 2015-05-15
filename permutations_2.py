# problem description: https://leetcode.com/problems/permutations-ii/

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        nums.sort()
        return self.permute(nums)
        
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            new_nums = nums[:i] + nums[i+1:]
            for pm in self.permute(new_nums):
                res.append([nums[i]] + pm)
                
        return res

def main():
    print Solution().permuteUnique([1, 1, 2])

if __name__ == '__main__':
    main()
