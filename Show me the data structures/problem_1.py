class DoubleNode: 
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class LRU_Cache:    
    def __init__(self, capacity):
        self.hashmap = dict()
        self.capacity = capacity
        self.head = DoubleNode(0,0)
        self.tail = DoubleNode(0,0)
        self.head.next = self.tail
        self.tail.previous = self.head
                  
    def get(self, key):
        if key not in self.hashmap:
            return -1
                
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._insert(node)
            return node.value
        
    def put(self, key, value):
        if key in self.hashmap:
            self._remove(self.hashmap[key])
        
        if key not in self.hashmap:
            node = DoubleNode(key, value)
            self._insert(node)
            self.hashmap[key] = node
            
        if len(self.hashmap) > self.capacity:
            node = self.head.next 
            self._remove(node)
            
            if node.key is None:
                del self.hashmap[node.key] 
                            
    def _remove(self, node): # cite: 1        
        if self.head is None or node is None:
            return 
        
        if self.head == node:
            self.head = node.next
            
        if node.next is not None:
            node.next.previous = node.previous
        
        if node.previous is not None:
            node.previous.next = node.next
            
    def _insert(self, node):
        node.next = self.head
        node.previous = None

        if self.head is not None:
            self.head.previous = node
        self.head = node


# Test Case 1 - Normal 
cache_one = LRU_Cache(5)
cache_one.put(1, 3)
cache_one.put(2, 4)   
print('test_1_get1', cache_one.get(1)) # returns 3
print('test_1_get2', cache_one.get(2)) # returns 4
print('test_1_get3', cache_one.get(3)) # return -1
cache_one.put(3, 5)
print('test_1_get2', cache_one.get(2)) # returns 4
cache_one.put(4, 5)
print('test_1_get1', cache_one.get(1)) # returns 3
print('test_1_get3', cache_one.get(3)) # returns 5
cache_one.put(3, 6)
print('test_1_get3', cache_one.get(3)) # returns 6

# Test Case 2 - Empty 
cache_two = LRU_Cache(0)
cache_two.put(1, 3)
cache_two.put(2, 4)  
cache_two.put(3, 5)  
print('test_2_get1', cache_two.get(1)) # returns 3
print('test_2_get2', cache_two.get(2)) # returns 4
print('test_2_get3', cache_two.get(3)) # return 5
cache_two.put(3, 5)
print('test_2_get2', cache_two.get(2)) # returns 4
cache_two.put(4, 5)
print('test_2_get1', cache_two.get(1)) # returns 3
print('test_2_get3', cache_two.get(3)) # returns 5
cache_two.put(3, 6)
print('test_2_get3', cache_two.get(3)) # returns 5

# Test Case 3 - Overflow 
cache_three = LRU_Cache(3)
cache_three.put(1, 3)
cache_three.put(2, 4)
print('test_3_get1', cache_three.get(1)) # returns 3
print('test_3_get2', cache_three.get(2)) # returns 4
print('test_3_get3', cache_three.get(3)) # returns -1
print('test_3_get3', cache_three.get(1)) # returns 3
print('test_3_get3', cache_three.get(2)) # returns 4
print('test_3_get3', cache_three.get(3)) # returns -1
print('test_3_get3', cache_three.get(1)) # returns 3


