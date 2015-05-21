# problem description: https://leetcode.com/problems/valid-number/

class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        s = s.strip()
        is_num = False
        i = 0
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            i += 1
        while i < len(s) and s[i].isdigit():
            i += 1
            is_num = True
        if i < len(s) and s[i] == '.':
            i += 1
        while i < len(s) and s[i].isdigit():
            i += 1
            is_num = True
        if i < len(s) and s[i] == 'e' and is_num:
            is_num = False
            i += 1
            if i < len(s) and (s[i] == '+' or s[i] == '-'):
                i += 1
            while i < len(s) and s[i].isdigit():
                i += 1
                is_num = True
        return i == len(s) and is_num
        
    
def main():
    print Solution().isNumber('111')

if __name__ == '__main__':
    main()
