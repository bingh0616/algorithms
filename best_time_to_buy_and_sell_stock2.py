# problem description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        res = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += (prices[i]-prices[i-1])
        
        return res
