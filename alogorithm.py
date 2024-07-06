class Node:
    def __init__(self,key=None,val=None):
        self.key=key
        self.val=val
        self.next=None 
        self.prev=None

class DLL:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail 
        self.tail.prev=self.head 
    
    def add_node_at_front(self,node):
        next1=self.head.next
        self.head.next=node 
        node.prev=self.head 
        node.next=next1 
        next1.prev=node 
    
    def remove_node(self,node):
        next_1=node.next 
        prev_1=node.prev 
        prev_1.next=next_1 
        next_1.prev=prev_1 
    
    def move_node_to_front(self,node):
        self.remove_node(node)
        self.add_node_at_front(node)
    
    def remove_last_node(self):
        if self.tail.prev != self.head:
            node=self.tail.prev 
            self.remove_node(node)
            return node
        return None 
    
    