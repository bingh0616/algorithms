# problem description: https://leetcode.com/problems/integer-to-roman/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        tps = [(1000,'M'), (900,'CM'),  (500,'D'), (400,'CD'), (100,'C'), (90,'XC'), (50,'L'), (40,'XL'), (10,'X'), (9,'IX'), (5,'V'), (4,'IV'), (1,'I')]

        res = ''
        i = 0
        while num > 0:
            res += tps[i][1] * (num / tps[i][0])
            num %= tps[i][0]
            i += 1
        
        return res
