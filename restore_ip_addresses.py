# problem description: https://leetcode.com/problems/restore-ip-addresses/

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.helper(s, 4, [], res)
        return res
    
    def helper(self, s, n, solution, res):
        l = len(s)
        if l < n or l > 3*n: return
        if n == 0:
            res.append('.'.join(solution))
        else:
            for i in xrange(1, min(4, l+1)):
                if int(s[:i]) >= 0 and int(s[:i]) <= 255:
                    if i == 1 or s[0] != '0':
                        solution.append(s[:i])
                        self.helper(s[i:], n-1, solution, res)
                        solution.pop()
