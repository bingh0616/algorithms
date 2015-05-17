# problem description: https://leetcode.com/problems/word-break/

# recursion with memorization
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def __init__(self):
        self.cache = {}
    def wordBreak(self, s, wordDict):
        if s == '':
            return True
        if s in self.cache:
            return self.cache[s]
        for i in range(len(s)+1):
            if s[:i] in wordDict:
                if self.wordBreak(s[i:], wordDict):
                    self.cache[s] = True
                    return True
        self.cache[s] = False
        return False

# DP solution
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean

    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        
        for i in reversed(range(len(s))):
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict and dp[j]:
                    dp[i] = True
                    break
                
        return dp[0]


def main():
    print Solution().wordBreak('leetcode', set(['leet', 'cod']))

if __name__ == '__main__':
    main()
