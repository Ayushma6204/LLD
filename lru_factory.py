from lru_cache import LRU
class CacheFactory:
    @staticmethod
    def create_lru_cache(capacity):
        return LRU(capacity)
