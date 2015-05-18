# problem description: https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        str = str.strip()
        if not str:
            return 0
        res, sign = 0, 1
        if str[0] == '-' or str[0] == '+':
            if str[0] == '-': sign = -1
            str = str[1:]
        i = 0
        while i < len(str):
            if str[i].isdigit():
                d = ord(str[i]) - ord('0')
                if res > 2**31 / 10 or (res == 2**31 / 10 and d > 7):
                    return 2**31 - 1 if sign == 1 else -2**31
                res *= 10
                res += d
            else:
                break
            i += 1
        return res * sign

def main():
    print Solution().myAtoi('-2147483647')

if __name__ == '__main__':
    main()
