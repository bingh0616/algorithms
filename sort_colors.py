# problem description: https://leetcode.com/problems/sort-colors/

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        r, w, b = 0, 0, 0
        for c in nums:
            if c == 0:
                nums[b] = 2
                nums[w] = 1
                nums[r] = 0
                r += 1
                w += 1
                b += 1
            elif c == 1:
                nums[b] = 2
                nums[w] = 1
                w += 1
                b += 1
            else:
                nums[b] = 2
                b += 1

def main():
    nums = [2,2,0,1,0]
    Solution().sortColors(nums)
    print nums

if __name__ == '__main__':
    main()
