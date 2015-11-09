# problem description: https://leetcode.com/problems/gray-code/

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in xrange(n):
            for r in reversed(res):
                res.append(r+2**i)
            
        return res
