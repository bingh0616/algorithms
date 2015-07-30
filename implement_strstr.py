class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        t, s = haystack, needle
        p = [0] * len(s)
        for i in xrange(1, len(s)):
            j = p[i-1]
            while j>0 and s[i] != s[j]:
                j = p[j-1]
            j += 1 if s[i] == s[j] else 0
            p[i] = j
            
        i, j = 0, 0
        while True:
            if j == len(needle): return i
            if i+j >= len(haystack): break
            if needle[j] == haystack[i+j]:
                j += 1
            else:
                skip = max(j - p[j-1], 1)
                i += skip
                j = 0
                
        return -1

print Solution().strStr("mississippi", "issip")
