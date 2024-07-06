from policy.lrueviction_policy import LRUEvictionPolicy 
from storage.hashmap_storage import HashMapStorage 
from cache_ import Cache
class CacheFactory:
    @staticmethod
    def default_cache(capacity):
        eviction_policy = LRUEvictionPolicy()
        storage = HashMapStorage(capacity)
        return Cache(eviction_policy, storage)