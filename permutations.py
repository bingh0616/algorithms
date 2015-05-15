# problem description: https://leetcode.com/problems/permutations/

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            for pm in self.permute(new_nums):
                res.append([nums[i]] + pm)
                
        return res

def main():
    print Solution().permute([1])

if __name__ == '__main__':
    main()
