from collections.abc import Iterable
class DoublyLinkedListNode:
    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

    def get_prev(self):
        return self.prev

    def set_prev(self, prev_node):
        self.prev = prev_node

    def get_element(self):
        return self.element

    def set_element(self, element):
        self.element = element


class DoublyLinkedList:
    def __init__(self):
        self.dummy_head = DoublyLinkedListNode(None)
        self.dummy_tail = DoublyLinkedListNode(None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def detach_node(self, node):
        if node is not None:
            node.prev.next = node.next
            node.next.prev = node.prev

    def add_node_at_last(self, node):
        node=DoublyLinkedListNode(node)
        tail_prev = self.dummy_tail.prev
        tail_prev.next = node
        node.next = self.dummy_tail
        self.dummy_tail.prev = node
        node.prev = tail_prev

    def add_element_at_last(self, element):
        new_node = DoublyLinkedListNode(element)
        self.add_node_at_last(new_node)
        return new_node

    def is_item_present(self):
        return self.dummy_head.next != self.dummy_tail

    def get_first_node(self):
        if not self.is_item_present():
            return None
        return self.dummy_head.next

    def get_last_node(self):
        if not self.is_item_present():
            return None
        return self.dummy_tail.prev
