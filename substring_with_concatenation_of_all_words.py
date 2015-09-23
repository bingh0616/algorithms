# problem description: https://leetcode.com/problems/substring-with-concatenation-of-all-words/

# naive implementation: 790ms
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s: return []
        mp = {}
        for w in words:
            if w in mp:
                mp[w] += 1
            else:
                mp[w] = 1
        
        wl = len(words[0])
        n, l = len(s), len(words)
        res = []
        
        for i in xrange(0, n-wl*l+1):
            mp2 = mp.copy()
            j = i
            while j<i+wl*l:
                w = s[j:j+wl]
                if w in mp2 and mp2[w] > 0:
                    mp2[w] -= 1
                    if mp2[w] == 0: mp2.pop(w, None)
                else:
                    break
                j += wl
                if j == i+wl*l: res.append(i)
        
        return res

# better implementation: 336ms
class Solution(object):
    def findSubstring(self, S, L):
        n = len(L)
        w = len(L[0])
        t = n*w
    
        p = tuple(sorted([x for x in L]))
        q = [S[i:i+w]*(S[i:i+w] in L) for i in xrange(len(S)-w+1)]
        return [i for i in xrange(len(S)-t+1) if tuple(sorted(q[i:i+t:w]))==p]


# best solution: https://leetcode.com/discuss/22289/my-ac-c-code-o-n-complexity-26ms
