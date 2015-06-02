# problem description: https://leetcode.com/problems/valid-palindrome/

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s = s.strip().lower()
        l, r = 0, len(s)-1
        while l < r:
            lr, rr = s[l].isalnum(), s[r].isalnum()
            if lr and rr:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            if not lr:
                l += 1
            if not rr:
                r -= 1
        return True
