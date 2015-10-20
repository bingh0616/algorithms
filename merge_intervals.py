# problem description: https://leetcode.com/problems/merge-intervals/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if not intervals: return []
        res = []
        intervals = sorted(intervals, key=lambda it: it.start)
        s, e = intervals[0].start, intervals[0].end
        
        for i in xrange(1, len(intervals)):
            it = intervals[i]
            if e < it.start:
                res.append(Interval(s, e))
                s, e = it.start, it.end
            else:
                s, e = min(s, it.start), max(e, it.end)
        res.append(Interval(s,e))
        return res
