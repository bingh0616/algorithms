# problem description: https://leetcode.com/problems/majority-element-ii/

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        a, b = 0, 0
        cnta, cntb = 0, 0
        res = []
        
        for n in nums:
            if cnta == 0 or a == n:
                cnta += 1
                a = n
            elif cntb == 0 or b == n:
                cntb += 1
                b = n
            else:
                cnta -= 1
                cntb -= 1
        
        cnta, cntb = 0, 0
        for n in nums:
            if n == a: cnta += 1
            if n == b: cntb += 1
            
        if cnta > len(nums)/3: res.append(a)
        if a != b and cntb > len(nums)/3: res.append(b)
        
        return res
