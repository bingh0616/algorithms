# problem description: https://leetcode.com/problems/lru-cache/

class LRUCache:
    
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    # @param capacity, an integer
    def __init__(self, capacity):
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        self.mp = {}
        
    # put a node to head
    def put_to_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
        
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    # @return an integer
    def get(self, key):
        if key not in self.mp:
            return -1
        node = self.mp[key]
        self.remove_node(node)
        self.put_to_head(node)
        return node.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self.remove_node(node)
            self.put_to_head(node)
            return
            
        if self.size == self.capacity:
            last = self.tail.prev
            self.remove_node(last)
            self.mp.pop(last.key, None)
            self.size -= 1
        node = self.Node(key, value)
        self.mp[key] = node
        self.put_to_head(node)
        self.size += 1

def main():
    lc = LRUCache(1)
    lc.set(2,1)
    print lc.get(2)
    lc.set(3,2)
    print lc.get(2)
    

if __name__ == '__main__':
    main()
