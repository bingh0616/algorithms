# problem description: https://leetcode.com/problems/permutation-sequence/

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        return self.helper(range(1,n+1), n, k)
        
    def helper(self, A, n, k):
        if n == 1: return str(A[0])
        pre_cnt = math.factorial(n-1)
        first_elem = (k-1)/pre_cnt
        
        rest_elem = self.helper(A[:first_elem]+A[first_elem+1:], n-1, (k-1)%pre_cnt+1)
        
        return str(A[first_elem])+rest_elem

# iteration solution
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        A = [x+1 for x in range(n)]
        k -= 1
        res = ''
        
        for i in reversed(range(n)):
            fact = math.factorial(i)
            idx = k / fact
            res += str(A[idx])
            A[idx:] = A[idx+1:]
            k %= fact
            
        return res
