# problem description: https://leetcode.com/problems/min-stack/

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.main_stk = []
        self.min_stk = []

    # @param x, an integer
    # @return nothing
    # time complexity: O(1)
    def push(self, x):
        self.main_stk.append(x)
        if (not self.min_stk) or x <= self.min_stk[-1]: self.min_stk.append(x)

    # @return nothing
    # time complexity: O(1)
    def pop(self):
        elem = self.main_stk.pop()
        if self.min_stk and elem == self.min_stk[-1]: self.min_stk.pop()

    # @return an integer
    # time complexity: O(1)
    def top(self):
        return self.main_stk[-1]

    # @return an integer
    # time complexity: O(1)
    def getMin(self):
        return self.min_stk[-1]
