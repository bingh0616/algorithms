class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        return self.helper(nums, 0, len(nums)-1)
        
    def helper(self, nums, left, right):
        if right-left < 0:
            return -1
        mid = (right+left) / 2
        pre = None if mid == 0 else nums[mid-1]
        next = None if mid == len(nums)-1 else nums[mid+1]
        if (nums[mid] > pre or pre is None) and (nums[mid] > next or next is None):
            return mid
        left_res = self.helper(nums, left, mid-1)
        if left_res != -1: return left_res
        right_res = self.helper(nums, mid+1, right)
        if right_res != -1: return right_res
        return -1

def main():
    print Solution().findPeakElement([1,2,3])

if __name__ == '__main__':
    main()
