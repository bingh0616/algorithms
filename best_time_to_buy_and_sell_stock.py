# problem description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        min_p = 2 ** 31-1
        res = 0
        for i in xrange(len(prices)):
            res = max(res, prices[i]-min_p)
            if min_p > prices[i]:
                min_p = prices[i]
            
        return res
