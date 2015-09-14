# problem description: https://leetcode.com/problems/the-skyline-problem/

import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # head queue for right x and height
        n = len(buildings)
        res = []
        hr_q = []
        i = 0
        while i < n or hr_q:
            if not hr_q or (i<n and buildings[i][0] <= -hr_q[0][1]):
                x = buildings[i][0]
                while i<n and buildings[i][0] == x:
                    heapq.heappush(hr_q, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                x = -hr_q[0][1]
                while hr_q and -hr_q[0][1] <= x:
                    heapq.heappop(hr_q)
            
            h = len(hr_q) and -hr_q[0][0]
            if not res or res[-1][1] != h:
                res.append([x, h])
                
        return res

