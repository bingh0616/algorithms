# problem description: https://leetcode.com/problems/integer-to-english-words/

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return 'Zero'
        scale = 10**9
        dc = {10**9: 'Billion', 10**6: 'Million', 10**3: 'Thousand'}
        res = ''
        while scale > 0:
            if num / scale > 0:
                tmp = (self.helper(num / scale) + (' ' + dc[scale] if scale in dc else ''))
                res = res + ' ' + tmp if len(res) != 0 else tmp
            num %= scale
            scale /= 10**3
        return res
        
    def helper(self, num):
        dc = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten',
            11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 
            18:'Eighteen', 19: 'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy',
            80:'Eighty', 90:'Ninety', 100:'Hundred'}
            
        res = ''
        if num / 100 > 0:
            res += (dc[num/100] + ' ' + dc[100])
        num %= 100
        if num == 0: return res
        if num in dc:
            return res + ' ' + dc[num] if len(res) != 0 else dc[num]
        tmp = dc[num/10*10] + ' ' + dc[num%10]
        return res + ' ' + tmp if len(res) != 0 else tmp

