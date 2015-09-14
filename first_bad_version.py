# problem description: https://leetcode.com/problems/first-bad-version/

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        l, r = 1, n
        while l < r:
            m = (l+r) / 2
            if isBadVersion(m):
                r = m
            else:
                l = m+1
        return l
