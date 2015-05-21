# problem description: https://leetcode.com/problems/max-points-on-a-line/

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        if len(points) <= 2: return len(points)
        points = sorted(points, key=lambda p:(p.x, p.y))
        max_points = 2
        for i, p1 in enumerate(points):
            mp = {}
            same = 1
            for p2 in points[i+1:]:
                if p1.x == p2.x and p1.y == p2.y:
                    same += 1
                    continue
                if p1.x == p2.x:
                    key = (None, p1.x)
                else:
                    k = (float(p1.y)-p2.y) / (p1.x-p2.x)
                    b = p1.y - k*p1.x
                    key = (k, b)
                if key in mp:
                    mp[key] += 1
                else:
                    mp[key] = 1 + same
                max_points = max(max_points, mp[key])
            max_points = max(max_points, same)
        return max_points
