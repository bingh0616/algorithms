class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        n -= 1
        if n <= 1: return 0
        is_prime = [True] * n
        is_prime[0] = False
        for i in xrange(2, n+1):
            if i**2 > n: break
            if is_prime[i-1]:
                j = i ** 2
                while j <= n:
                    is_prime[j-1] = False
                    j += i
        cnt = 0
        for i in xrange(n):
            if is_prime[i]: cnt += 1
        
        return cnt

# the above method is faster
class Solution2:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        n -= 1
        if n <= 1: return 0
        is_prime = [True] * n
        is_prime[0] = False
        for i in xrange(2, n+1):
            if i**2 > n: break
            if is_prime[i-1]:
                j = i
                while i*j <= n:
                    is_prime[i*j-1] = False
                    j += 1
        cnt = 0
        for i in xrange(n):
            if is_prime[i]: cnt += 1
        
        return cnt

print Solution().countPrimes(1500000)
