# problem description: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = set()
        
        l, r, n = 0, 0, len(s)
        
        res = 0
        
        while r < n:
            if s[r] in st:
                while l < r and s[l] != s[r]:
                    st.discard(s[l])
                    l += 1
                st.discard(s[l])
                l += 1
            st.add(s[r])
            r += 1
            res = max(r-l, res)
            
        return res

