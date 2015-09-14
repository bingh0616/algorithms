# problem description: https://leetcode.com/problems/h-index-ii/

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0: return 0
        h = min(citations[-1], 1)
        for i in reversed(xrange(len(citations)-1)):
            c = citations[i]
            h = max(h, min(c, len(citations)-i))
            if i-1 >= 0 and citations[i-1] <= h:
                break
        return h

# better O(log(n)) solution
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            m = (l+r)/2
            if citations[m] >= n-m:
                r = m-1
            else:
                l = m+1
        return n-l
