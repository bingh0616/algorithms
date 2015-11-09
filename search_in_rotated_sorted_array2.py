# problem description: https://leetcode.com/submissions/detail/28008755/

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) / 2
            # adding nums[left] == target so we do not need to add a condition for right -= 1
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

# 10.27.2015
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r) / 2
            if target == nums[m] or target == nums[l] or target == nums[r]:
                return True
            if nums[r] < nums[m]:
                # left half ordered
                if target < nums[m] and target > nums[r]:
                    r = m-1
                else:
                    l = m+1
            elif nums[r] > nums[m]:
                if target > nums[m] and target < nums[r]:
                    l = m+1
                else:
                    r = m-1
            else:
                l += 1
        return nums[l] == target 
