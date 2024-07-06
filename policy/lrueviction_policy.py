from collections import OrderedDict
from alogirthm import DoublyLinkedList
class LRUEvictionPolicy:
    def __init__(self):
        self.dll = DoublyLinkedList()
        self.mapper = {}

    def key_accessed(self, key):
        if key in self.mapper:
            node = self.mapper[key]
            self.dll.detach_node(node)
            self.dll.add_node_at_last(node)
        else:
            node = self.dll.add_node_at_last(key)
            self.mapper[key] = node

    def evict_key(self):
        node = self.dll.get_first_node()
        if node:
            self.dll.detach_node(node)
            del self.mapper[node.key]
            return node.key
        return None