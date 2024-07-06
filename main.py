from cache.cache_factory import CacheFactory

def setup():
    global cache
    cache = CacheFactory().default_cache(3)

def run():
    cache.put(1, 1)
    cache.put(2, 2)

    print(cache.get(1))  # Accessing 1 after inserting 2, making 2 the least recently used.
    cache.put(3, 3)
    print(cache.get(3))

    # Adding 4 should trigger eviction based on Least Recently Used (LRU) policy (evicting 2)
    cache.put(4, 4)

    try:
        cache.get(2)
    except Exception as e:
        print(f"Exception: {e}")  # This should print "Tried to access non-existing key."

if __name__ == "__main__":
    setup()
    run()
