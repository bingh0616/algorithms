# problem description: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if not digits: return []
        mp = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = ['']
        for d in digits:
            tmp = []
            for c in mp[d]:
                for r in res:
                    tmp.append(r+c)
            res = tmp
            
        return res
