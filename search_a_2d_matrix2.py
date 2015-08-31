# problem description: https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        # find the first row number that the start element > target
        left, right = 0, m-1
        while left < right:
            mid = (left+right) / 2
            if matrix[mid][0] <= target:
                left = mid + 1
            else:
                right = mid - 1
        end = left
        # find the last row number that the last element < target
        left, right = 0, m-1
        while left < right:
            mid = (left+right) / 2
            if matrix[mid][-1] < target:
                left = mid + 1
            else:
                right = mid - 1
        start = right
        
        # go through lines, do binary search on each row
        
        for l in xrange(start if start >= 0 else 0, end+1):
            a = matrix[l]
            left, right = 0, n-1
            while left <= right:
                mid = (left+right) / 2
                if a[mid] == target:
                    return True
                if a[mid] < target:
                    left = mid + 1
                if a[mid] > target:
                    right = mid-1
                    
                    
        return False
