# problem description: https://leetcode.com/problems/minimum-window-substring/

class Solution:
    # @return a string
    def minWindow(self, S, T):
        if len(S) < len(T): return ''
        
        already_find, need_find = {}, {}
        for c in T:
            already_find[c] = 0
            if c in need_find:
                need_find[c] += 1
            else:
                need_find[c] = 1
                
        left, i = 0, 0
        find = 0
        start, end = 0, -1
        
        while i<len(S):
            c = S[i]
            if c in need_find:
                already_find[c] += 1
                if already_find[c] <= need_find[c]:
                    find += 1
                    
            while find == len(T):
                if end == -1 or end-start > i-left:
                    end = i
                    start = left
                    
                if S[left] in need_find:
                    already_find[S[left]] -= 1
                    if already_find[S[left]] < need_find[S[left]]:
                        find -= 1
                    
                left += 1
            i += 1
                
        return S[start:end+1]
