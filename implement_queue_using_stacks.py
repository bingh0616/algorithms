# problem description: https://leetcode.com/problems/implement-queue-using-stacks/

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        # s2 is the stack whose element is in queue order
        # we only push s1's element to s2 when s2 is empty (lazy)
        self.s2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s1.append(x)
            
    def _check(self):
        if len(self.s2) == 0:
            while self.s1:
                self.s2.append(self.s1.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        self._check()
        return self.s2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self._check()
        return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0 and len(self.s2) == 0
