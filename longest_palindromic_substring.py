# problem description: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        longest = 1
        left, right = 0, 0
        for i in range(len(s)-1):
            new_max = max(self.get_length(i, i, s), self.get_length(i, i+1, s) if s[i] == s[i+1] else 1)

            if new_max > longest:
                longest = new_max
                left, right = i-(new_max-1)/2, i+new_max/2

        return s[left:right+1]
        
    def get_length(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right-left-1

def main():
    print Solution().longestPalindrome('abb')

if __name__ == '__main__':
    main()
