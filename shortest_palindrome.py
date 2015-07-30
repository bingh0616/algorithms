# problem description: https://leetcode.com/problems/shortest-palindrome/

class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        i, l = 1, 0
        rev_s = s[::-1]
        new_s = s + '#' + rev_s
        lps = [0] * len(new_s)

        while i<len(new_s):
            if new_s[i] == new_s[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1
        return rev_s[:len(s)-lps[len(new_s)-1]] + s

    # shorter version
    def shortestPalindrome2(self, s):
        rev_s = s[::-1]
        new_s = s + '#' + rev_s
        # stores longest prefix suffix table (same as KMP table)
        lps = [0] * len(new_s)

        for i in xrange(1, len(new_s)):
            j = lps[i-1];
            while j > 0 and new_s[i] != new_s[j]:
                # use example 'abcabcabd' to understand the following line
                j = lps[j-1]
            j += 1 if new_s[i] == new_s[j] else 0
            lps[i] = j

        return rev_s[:len(s)-lps[len(new_s)-1]] + s



def main():
    print Solution().shortestPalindrome('abcda')
    print Solution().shortestPalindrome('abcd')


if __name__ == '__main__':
    main()
