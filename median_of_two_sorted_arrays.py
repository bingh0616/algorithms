# problem description: https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1) + len(nums2)
        if n % 2 == 0:
            return (self.kth(nums1, nums2, n/2) + self.kth(nums1, nums2, n/2+1)) / 2.0
        else:
            return self.kth(nums1, nums2, n/2+1)
    
    def kth(self, a, b, k):
        la, lb = len(a), len(b)
        if la > lb: return self.kth(b, a, k)
        if la == 0: return b[k-1]
        if k == 1: return min(a[0], b[0])
        pa = min(k/2, la)
        pb = k-pa
        if a[pa-1] > b[pb-1]:
            return self.kth(a, b[pb:], k-pb)
        else:
            return self.kth(a[pa:], b, k-pa)
