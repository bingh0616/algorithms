# problem description: https://leetcode.com/problems/anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dc = {}
        for s in strs:
            t = ''.join(sorted(s))
            if t not in dc: dc[t] = []
            dc[t].append(s)
        
        res = []
        for k in dc:
            res.append(sorted(dc[k]))
            
        return res

# with O(n) strSort, should be faster than above, but actually not
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dc = {}
        strs = sorted(strs)
        for s in strs:
            t = ''.join(self.strSort(s))
            if t not in dc: dc[t] = []
            dc[t].append(s)
        
        res = []
        for k in dc:
            res.append(dc[k])
            
        return res
    
    def strSort(self, s):
        cnt = [0] * 26
        for c in s:
            idx = ord(c)-ord('a')
            cnt[idx] += 1
        res = []
        for i in xrange(26):
            res += chr(i+ord('a')) * cnt[i]
        return ''.join(res)
