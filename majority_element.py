# problem description: https://leetcode.com/problems/majority-element/
'''
The algorithm for first phase that works in O(n) is known as Moore’s Voting Algorithm. Basic idea of the algorithm is if we cancel out each occurrence of an element e with all the other elements that are different from e then e will exist till end if it is a majority element.
http://www.geeksforgeeks.org/majority-element/
'''
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        maj, cnt = num[0], 1
        
        for a in num[1:]:
            if cnt == 0:
                cnt += 1
                maj = a
            elif maj == a:
                cnt += 1
            else:
                cnt -= 1
                
        return maj
