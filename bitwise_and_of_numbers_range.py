# problem description: https://leetcode.com/problems/bitwise-and-of-numbers-range/

import math
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = 0
        if n == 0: return a
        # can directly use 32 as xrange value
        for i in xrange(int(math.log(n, 2))+1):
            b = 2**i
            if n-m <= b:
                if (m & (1 << i)) != 0 and (n & (1 << i)) != 0:
                    a |= (1 << i)
            
        return a

# faster and simpler solution
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while m<n: n &= (n-1)
        return n

# explanation:
#
# The key point: reduce n by removing the rightest '1' bit until n<=m;
# 
# (1)if n>m,suppose m = vvvzzz, n = xxx100; since m<n, m can be vvv011 or less than vvv011, in either case we have vvv011 & xxx100 = zzz000;
# 
# => so we will get same result for rangBitWiseAnd(vvvzzz,xxx100) and rangBitWiseAnd(vvvzzz,xxx000);
# 
# This is why the rightest '1' bit can be removed by : n = n & (n-1);
# 
# (2)when n==m, obviously n is the result.
# 
# (3)when n<m, suppose we reduce n from rangBitWiseAnd(vvvzzz,xxx100) to rangBitWiseAnd(vvvzzz,xxx000);
# 
# i) xxx100 > vvvzzz => xxx >= vvv;
# 
# ii) xxx000 < vvvzzz => xxx <= vvv;
# 
# => xxx == vvv;
# 
# => rangBitWiseAnd(vvvzzz,xxx000) == rangeBitWiseAnd(xxxzzz,xxx000);
# 
# =>result is xxx000, which is also n;
