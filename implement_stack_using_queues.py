# problem description: https://leetcode.com/problems/implement-stack-using-queues/

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = collections.deque([])
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)
        for i in xrange(len(self.q)-1):
            self.q.append(self.q.popleft())
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0
