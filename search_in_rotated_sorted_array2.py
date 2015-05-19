# problem description: https://leetcode.com/submissions/detail/28008755/

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) / 2
            if nums[mid] == target or nums[left] == target:
                return True
            if nums[left] < nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[right] > nums[mid]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                left += 1
        return False
