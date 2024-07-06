from alogorithm import DLL 
from alogorithm import Node
class LRU:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}
        self.dll=DLL()
    
    def getValue(self,key):
        if key in self.cache:
            node=self.cache[key]
            self.dll.move_node_to_front(node)
            return node.val
        return -1
            
    def putValue(self,key,value):
        if key not in self.cache:
            if len(self.cache)==self.capacity:
                removed_node=self.dll.remove_last_node()
                if removed_node:
                    del self.cache[removed_node.key]
            node=Node(key,value)
            self.cache[key]=node 
            self.dll.add_node_at_front(node)
        else:
            node=self.cache[key]
            self.dll.add_node_at_front(node)
        print("Ayushma")
        print(len(self.cache))
        print(self.cache)
        print(self.dll.head.next)