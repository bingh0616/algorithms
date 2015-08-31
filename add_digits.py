# problem description: https://leetcode.com/problems/add-digits/

class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        while num >= 10:
            tmp = 0
            while num > 0:
                tmp += (num % 10)
                num /= 10
            num = tmp
            
        return num

# digit root
# dr(num) = 1 + ((n-1) mod 9)
class Solution:
    def addDigits(self, num):
        return (1 + (num-1) % 9) if num > 0 else 0
