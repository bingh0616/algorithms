# problem description: https://leetcode.com/problems/count-and-say/

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0: return ''
        seq = '1'
        for i in xrange(2, n+1):
            tmp = ''
            cnt = 1
            for j in xrange(1, len(seq)+1):
                if j<len(seq) and seq[j] == seq[j-1]:
                    cnt += 1
                else:
                    tmp += str(cnt)
                    tmp += seq[j-1]
                    cnt = 1
                    
            seq = tmp
            
        return seq
