# problem description: https://leetcode.com/problems/candy/

class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        candies = [1] * len(ratings)
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]: candies[i] = candies[i-1]+1
        
        for i in reversed(xrange(len(ratings)-1)):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]: candies[i] = candies[i+1]+1
            
        return sum(candies)
