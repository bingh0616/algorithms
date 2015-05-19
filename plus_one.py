# problem description: https://leetcode.com/problems/plus-one/

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        i = len(digits)-1
        while i>=0:
            if digits[i] != 9:
                digits[i] += 1
                break
            digits[i] = 0
            i -= 1
        if i < 0:
            return [1] + digits
        return digits
