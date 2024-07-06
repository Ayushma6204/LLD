from exception.storage_exception import StorageFullException 
from exception.notfound import NotFoundException
class HashMapStorage:
    def __init__(self, capacity):
        self.storage = {}
        self.capacity = capacity

    def is_storage_full(self):
        return len(self.storage) == self.capacity

    def add(self, key, value):
        if self.is_storage_full():
            raise StorageFullException("Capacity Full")

        self.storage[key] = value

    def remove(self, key):
        if key not in self.storage:
            raise NotFoundException(f"{key} doesn't exist in cache.")

        del self.storage[key]

    def get(self, key):
        if key not in self.storage:
            raise NotFoundException(f"{key} doesn't exist in cache.")

        return self.storage[key]