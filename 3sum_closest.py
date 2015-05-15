# problem description: https://leetcode.com/problems/3sum-closest/

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = None
        for i, val in enumerate(nums):
            left, right = i+1, len(nums)-1
            while left < right:
                sum = val+nums[left]+nums[right]
                
                if closest is None or abs(sum-target) < abs(closest-target):
                    closest = sum
                if sum == target:
                    return target
                elif sum > target:
                    right -= 1
                else:
                    left += 1
                
        return closest

def main():
    print Solution().threeSumClosest([0,2,1,-3], 1)

if __name__ == '__main__':
    main()
