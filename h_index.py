# problem description: https://leetcode.com/problems/h-index/

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0: return 0
        citations = sorted(citations, reverse=True)
        h = min(citations[0], 1)
        for i in xrange(1, len(citations)):
            c = citations[i]
            h = max(h, min(c, i+1))
            if i+1 < len(citations) and citations[i+1] <= h:
                break
        return h

# other person's O(n) solution
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        a = [0] * (l+1)
        
        for i in xrange(l):
            if citations[i] > l:
                a[l] += 1
            else:
                a[citations[i]] += 1
        
        ret = 0
        for i in reversed(xrange(l+1)):
            ret += a[i]
            if ret >= i:
                return i
        
        return 0
