# problem description: https://leetcode.com/problems/insert-interval/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        res = []
        for i in xrange(len(intervals)):
            it = intervals[i]
            if e < it.start:
                res.append(Interval(s,e))
                s, e = it.start, it.end
            elif s > it.end:
                res.append(it)
            else:
                s, e = min(s, it.start), max(e, it.end)
        res.append(Interval(s, e))
        return res
