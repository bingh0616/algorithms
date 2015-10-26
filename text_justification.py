# problem description: https://leetcode.com/problems/text-justification/

class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        l = maxWidth
        n = len(words)
        wl = 0
        wc = 0
        curr_words = []
        res = []
        i = 0

        while i<n:
            if l - (wl + len(words[i])) >= wc:
                wl += len(words[i])
                wc += 1
                curr_words.append(words[i])
                i += 1
            else:
                sps = (l-wl) / (wc-1) if wc > 1 else (l-wl)
                extra = (l-wl) % (wc-1) if wc > 1 else 0
                print curr_words, sps, extra
                line = ''
                for w in curr_words:
                    line += w
                    line += ' ' * sps
                    if extra > 0:
                        line += ' '
                        extra -= 1
                if wc != 1: line = line.strip()
                res.append(line)
                curr_words = []
                wl = 0
                wc = 0
                
        line = ''
        for w in curr_words:
            line += w
            line += ' '
        line = line.strip()
        line += ' ' * (l-len(line))
        res.append(line)
        return res


# 10.20.2015
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        L = maxWidth
        start = 0
        i = 0
        n = len(words)
        curr_len = 0
        word_cnt = 0
        res = []
        while i < n:
            w = words[i]
            if curr_len + len(w) + word_cnt  > L:
                spaces = (L-curr_len) / (word_cnt-1) if word_cnt != 1 else 0
                extra = L-(curr_len+spaces*(word_cnt-1))
                s = ''
                for j in xrange(start, i):
                    s += words[j]
                    if j != i-1:
                        s += (' ' * spaces)
                    if extra > 0: s += ' '
                    extra -= 1
                if extra > 0: s += (' ' * extra)
                curr_len = 0
                word_cnt = 0
                res.append(s)
                start = i
            else:
                curr_len += len(w)
                word_cnt += 1
                i += 1
        res.append(' '.join(words[n-word_cnt:]) + ' '* (L-curr_len-(word_cnt-1)))
                
        return res
