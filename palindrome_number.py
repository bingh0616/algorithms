# problem description: https://leetcode.com/problems/palindrome-number/

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0: return False
        div = 10
        while x/div > 0:
            div *= 10
        div /= 10
        while x > 0 and x%10 == x/div:
            x %= div
            x /= 10
            div /= 100
            
        return x == 0
        
