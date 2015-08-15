import collections

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    class MaxQueue:
        def __init__(self):
            self.q = collections.deque([])
            self.max_q = collections.deque([])
        def dequeue(self):
            if self.q.popleft() == self.max_q[0]:
                self.max_q.popleft()
        def enqueue(self, elem):
            self.q.append(elem)
            while self.max_q and elem > self.max_q[-1]:
                self.max_q.pop()
            self.max_q.append(elem)
        def get_max(self):
            return self.max_q[0]
            
    # will be O(n) time because totally enqueue will less than n although there is a while loop inside enqueue
    def maxSlidingWindow(self, nums, k):
        res = []
        if not nums: return res
        max_q = self.MaxQueue()
        i = 0
        j = i+k-1
        
        for m in xrange(i, j+1):
            max_q.enqueue(nums[m])
        
        while j<len(nums):
            res.append(max_q.get_max())
            max_q.dequeue()
            i += 1
            j += 1
            if j<len(nums): max_q.enqueue(nums[j])
            
        return res

print Solution().maxSlidingWindow([1,3,1,2,0,5], 3)
