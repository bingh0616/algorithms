# problem description: https://leetcode.com/problems/valid-anagram/

# one line code: O(nlog(n))
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

# O(n) solution use dict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        from collections import defaultdict
        mp = defaultdict(int)
        for i in s:
            mp[i] += 1
        
        for i in t:
            if i not in mp or mp[i] == 0:
                return False
            mp[i] -= 1
        return True
