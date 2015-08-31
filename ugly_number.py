# problem description: https://leetcode.com/submissions/detail/36899763/

class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        if num <= 0: return False
        factor = 2
        while num > 1 and factor <= 5:
            while num % factor == 0:
                if factor == 4:
                    return False
                num /= factor
            factor += 1
            
        return num <= 1
