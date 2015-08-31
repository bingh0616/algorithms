# problem description: https://leetcode.com/problems/single-number-iii/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st = set()
        for i in nums:
            if i in st:
                st.discard(i)
            else:
                st.add(i)
        return list(st)

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(lambda a,b: a^b, nums)
        
        # find the last set digit
        xor &= (-xor)
        
        res = [0, 0]
        for n in nums:
            if n & xor == 0:
                res[0] ^= n
            else:
                res[1] ^= n
                
        return res
