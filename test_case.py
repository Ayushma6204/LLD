import unittest
from lru_factory import CacheFactory

class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache=CacheFactory().create_lru_cache(3)
    def test_eviction(self):
        self.cache.putValue(1,1)
        self.cache.putValue(2,2)
        self.cache.putValue(3,3)

        # self.assertEqual(self.cache.getValue(1),1) 
        self.cache.putValue(4,4)
        self.cache.putValue(5,5)
        print(len(self.cache.cache))
        self.assertEqual(self.cache.getValue(2),-1)
        # 1 should be evicted
        # self.assertEqual(cache.get(2), -1)  # 2 should be evicted
        # self.assertEqual(cache.get(3), 3)

if __name__ == "__main__":
    unittest.main()
