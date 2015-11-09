# problem description: https://leetcode.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0': return 0
        p, q = 1, 1
        for i in xrange(1, len(s)):
            tmp = 0
            if s[i-1] == '1' or (s[i-1] == '2' and (int(s[i]) >= 0 and int(s[i]) <= 6)):
                tmp += p
            if s[i] != '0':
                tmp += q
            p = q
            q = tmp
            
        return q
