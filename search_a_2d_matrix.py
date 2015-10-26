# problem description: https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False
        
        l, r = 0, m-1
        
        while l <= r:
            mid = (l+r) / 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                l = mid
                break
            elif matrix[mid][0] > target:
                r = mid-1
            else:
                l = mid+1
        
        row = l
        if row >= m: return False
        l, r = 0, n-1
        
        while l <= r:
            mid = (l+r) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid-1
            else:
                l = mid+1
        
        return False
