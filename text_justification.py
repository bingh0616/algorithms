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

