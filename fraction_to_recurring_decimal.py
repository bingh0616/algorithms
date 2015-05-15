# problem description: https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        sign = 1 if numerator/denominator >= 0 else -1
        n, d = abs(numerator), abs(denominator)
        res = str(n / d)
        if sign == -1: res = '-' + res
        r = n % d
        if r == 0: return res
        res += '.'
        # record the remainder and its location
        mp = {}
        while r > 0:
            if r in mp:
                res = res[:mp[r]] + '(' + res[mp[r]:] + ')'
                break
            mp[r] = len(res)
            r *= 10
            res += str(r/d)
            r %= d
        return res

def main():
    print Solution().fractionToDecimal(1, 333)

if __name__ == '__main__':
    main()
