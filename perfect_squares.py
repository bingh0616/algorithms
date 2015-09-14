# problem description: https://leetcode.com/problems/perfect-squares/

# my solution, recursion with memorization 472ms
class Solution(object):
    cache = {}
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.cache: return self.cache[n]
        if n == 0: return 0
        if int(math.sqrt(n))**2 == n: return 1
        i = int(math.sqrt(n))
        res = 2**31-1
        while i>0:
            tmp = self.numSquares(n-i**2)
            if tmp > 0:
                res = min(res, 1+tmp)
            i -= 1
        self.cache[n] = res
        return res

# better method, static DP, 176ms
class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

# number theory method, best, 64ms
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while a**2 <= n:
            b = math.sqrt(n-a**2)
            if a**2 + b**2 == n:
                return (1 if a != 0 else 0) + (1 if b != 0 else 0)
            a += 1
        return 3
