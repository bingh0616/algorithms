# problem description: https://leetcode.com/problems/happy-number/

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        exist = set([n])
        while True:
            new_num = 0
            while n > 0:
                d = n%10
                new_num += d**2
                n /= 10
            if new_num == 1:
                return True
            if new_num in exist:
                break
            n = new_num
            exist.add(new_num)
            
        return False
