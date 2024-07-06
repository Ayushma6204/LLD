import unittest
from cache.cache_factory import CacheFactory

class TestCase(unittest.TestCase):
    def setUp(self):
        self.cache = CacheFactory().default_cache(3)
        print(self.cache)
    def test_put(self):
        self.cache.put(1,1)
        self.cache.put(2,2)
        self.cache.put(3,3)
        self.cache.put(4,4)
        m=self.cache.get(2)
        print(m)
        
        
    

if __name__=="__main__":
    unittest.main()